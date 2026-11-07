"""Sort PDFs dropped in inbox/ into papers/<topic>/ and queue them for ingest.

Usage: python3 tools/inbox.py [--dry-run]
A PDF goes to the folder most of its citing wiki pages come from (via the wanted-papers list),
else to the folder of the wiki papers it cites. Unplaced PDFs stay in inbox/.
"""
import json, re, sys
from collections import Counter
from pathlib import Path

import fitz

from refs import R, WANTED, CACHE, entries_for, fold, load_pages, matches, words

INBOX = R / "inbox"
QUEUE = INBOX / "to-ingest.txt"
BAD_TITLE = re.compile(r"^(untitled|microsoft word|document\d*|arxiv|paper)\b|\.(dvi|tex|docx?|pdf)$", re.I)


def topic_of(file):
    parts = Path(file).parts
    return parts[1] if len(parts) > 2 and parts[0] == "papers" else None


def big_title(page):
    lines = [l for b in page.get_text("dict")["blocks"] for l in b.get("lines", [])
             if l["dir"] == (1, 0) and l["bbox"][1] < page.rect.height * 0.6
             and "".join(s["text"] for s in l["spans"]).strip() and "arxiv" not in str(l).lower()]
    if not lines:
        return ""
    top = max(s["size"] for l in lines for s in l["spans"] if s["text"].strip())
    return " ".join("".join(s["text"] for s in l["spans"]).strip()
                    for l in lines if any(s["size"] >= top - 0.5 and s["text"].strip() for s in l["spans"]))


def surnames(author_field):
    names = [n.strip() for n in re.split(r";|,| and |&", author_field or "") if n.strip()]
    out = [n.split()[-1] for n in names if not re.search(r"\d|@", n) and len(n.split()) >= 2]
    return out


def ref_surnames(entry):
    body = re.sub(r"^\[?\d{1,3}[.\]]\s*", "", entry)
    m = re.match(r"(.+?(?<!\b[A-Z])\.)\s", body)
    pieces = [x.strip(" .") for x in re.split(r",|\band\b|&", m.group(1) if m else "") if x.strip(" .")]
    initials = [x for x in pieces if re.fullmatch(r"(?:[A-Z]\.?\s*-?)+", x)]
    names = [x for x in pieces if x not in initials and not re.search(r"\d|et al", x)]
    sur = [n.split()[0] if initials else n.split()[-1] for n in names if 0 < len(n.split()) <= 4]
    return [x for x in sur if not re.fullmatch(r"[A-Z]\.?", x)]


def clean(s):
    s = re.sub(r"[:/#|^\[\]?\\*\"<>]", " ", s)
    return re.sub(r"\s+", " ", s).strip(" .")


def filename(sur, title):
    who = ", ".join(sur) if 0 < len(sur) <= 4 else f"{sur[0]} et al" if sur else "Unknown"
    return clean(f"{who} - {title[:120]}") + ".pdf"


def best_wanted(title, text, wanted):
    tw, head = words(title), fold(text[:4000])
    best, score = None, 0.8
    for c in wanted:
        if len(tw) < 2 or not re.search(rf"\b{re.escape(c['sur'])}\b", head):
            continue
        s = len(c["ws"] & tw) / len(tw)
        if s >= score:
            best, score = c, s
    return best


def existing(title, known):
    tw = words(title)
    return next((f for f, ws in known if len(tw) >= 2 and len(tw & ws) / max(len(tw), len(ws)) >= 0.8), None)


def known_titles(pages):
    out = [(pg["file"], words(pg.get("title") or "")) for pg in pages.values()]
    out += [(str(f.relative_to(R)), words(f.stem.split(" - ", 1)[-1])) for f in (R / "papers").rglob("*.pdf")]
    return out


def place(pdf, wanted, pages, cache, known):
    d = fitz.open(pdf)
    text = "\n".join(p.get_text() for p in list(d)[:2])
    meta = d.metadata or {}
    title = meta.get("title") or ""
    if len(title) < 10 or BAD_TITLE.search(title.strip()):
        title = big_title(d[0]) or pdf.stem
    if dupe := existing(title, known):
        return None, None, f"DUPE of {dupe}"
    sur = surnames(meta.get("author"))
    votes, why = Counter(), ""
    c = best_wanted(title, text, wanted)
    if c:
        votes.update(t for b in c["by"] if b in pages and (t := topic_of(pages[b]["file"])))
        why = f"wanted, cited by {len(c['by'])}"
        sur = sur or ref_surnames(c["text"])
    if not votes:
        ents, _ = entries_for(pdf, cache)
        titles = {n: cache.get(str(R / pg["file"]), {}).get("title", "") for n, pg in pages.items()}
        cited = {n for e in ents for n, pg in pages.items() if matches(e, pg, titles[n])}
        votes.update(t for n in cited if (t := topic_of(pages[n]["file"])))
        why = f"cites {len(cited)} wiki papers"
    topic = votes.most_common(1)[0][0] if votes else None
    return topic, filename(sur, clean(title)), why


def main(dry):
    INBOX.mkdir(exist_ok=True)
    pdfs = sorted(INBOX.glob("*.pdf"))
    if not pdfs:
        print(f"no PDFs in {INBOX.relative_to(R)}/")
        return
    wanted = json.loads(WANTED.read_text()) if WANTED.exists() else []
    for c in wanted:
        c["ws"] = words(re.sub(r"^\[?\d{1,3}[.\]]\s*", "", c["text"]))
    pages = load_pages()
    cache = json.loads(CACHE.read_text()) if CACHE.exists() else {}
    known, moved = known_titles(pages), []
    for pdf in pdfs:
        topic, name, why = place(pdf, wanted, pages, cache, known)
        if why.startswith("DUPE"):
            print(f"DUPE  {pdf.name}  ({why[5:]})")
            continue
        if not topic:
            print(f"KEEP  {pdf.name}  (no topic found; {why})")
            continue
        dest = R / "papers" / topic / name
        if dest.exists():
            print(f"DUPE  {pdf.name}  ->  {dest.relative_to(R)} already exists")
            continue
        print(f"MOVE  {pdf.name}  ->  {dest.relative_to(R)}  ({why})")
        if not dry:
            pdf.rename(dest)
            moved.append(str(dest.relative_to(R)))
    if moved:
        with QUEUE.open("a") as f:
            f.write("\n".join(moved) + "\n")
        print(f"{len(moved)} queued in {QUEUE.relative_to(R)}")


if __name__ == "__main__":
    main("--dry-run" in sys.argv)
