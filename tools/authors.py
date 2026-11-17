"""Build wiki/authors/ pages from each page's **Authors** line and link them from frontmatter.

Usage: python3 tools/authors.py [--dry-run]
"""
import re, sys, unicodedata
from collections import defaultdict
from pathlib import Path

R = Path(__file__).resolve().parent.parent
W = R / "wiki"
A = W / "authors"
DATE = "2026-11-06"
ALIAS = {"Alex Alberts": "Alexander Alberts"}
SKIP = {"et al", "et al.", "others", "equal contribution", "not stated", "unattributed", "anonymous", "unknown"}


def fold(s):
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()


def split_names(line):
    line = re.sub(r"\([^)]*\)", "", line)
    parts = re.split(r",|;|\band\b|&", line)
    out = []
    for p in parts:
        p = re.sub(r"\s+et al\.?$", "", re.sub(r"\s+", " ", p).strip(" .*"))
        if p and fold(p) not in SKIP and not re.search(r"\d", p):
            out.append(p)
    return out


def key(name):
    toks = ALIAS.get(name, name).replace(".", ". ").split()
    sur = fold(toks[-1])
    first = fold(toks[0]).rstrip(".") if len(toks) > 1 else ""
    return sur, first


def firsts(names):
    out = defaultdict(set)
    for n in names:
        sur, first = key(n)
        if len(first) > 1:
            out[sur].add(first)
    return out


def norm(n, full):
    sur, first = key(n)
    if len(first) <= 1:
        match = [f for f in full[sur] if f.startswith(first)]
        if len(match) == 1:
            return sur, match[0]
    return sur, first


def pages():
    for p in sorted(W.glob("*.md")):
        s = p.read_text()
        m = re.match(r"---\n(.*?)\n---\n", s, re.S)
        if not m or not re.search(r"^authors:", m.group(1), re.M):
            continue
        body = re.search(r"^\*\*Authors?\*\*:\s*(.*?)(?:\s+·|$)", s, re.M)
        if body:
            names = split_names(body.group(1))
        else:
            fm = re.search(r"^authors:\s*\[(.*)\]", m.group(1), re.M).group(1)
            names = [n.strip(' "[]') for n in fm.split(",") if n.strip()]
        yield p, s, names


def resolve(entries):
    full = firsts(n for _, _, names in entries for n in names)
    canon, unresolved = {}, set()
    for _, _, names in entries:
        for n in names:
            k = norm(n, full)
            if not k[1]:
                unresolved.add(n)
            if len(n) > len(canon.get(k, "")):
                canon[k] = n
    return canon, unresolved, full


def page_name(n):
    return re.sub(r'[:/#|^\[\]?"]', "", n.replace("[[", "").replace("]]", "")).strip()


def main(dry):
    entries = list(pages())
    canon, unresolved, full = resolve(entries)
    papers = defaultdict(list)
    for p, s, names in entries:
        links = []
        for n in names:
            a = page_name(canon[norm(n, full)])
            if a not in links:
                links.append(a)
            papers[a].append(p.stem)
        fmline = "authors: [" + ", ".join(f'"[[{a}]]"' for a in links) + "]"
        new = re.sub(r"^authors:.*$", fmline, s, count=1, flags=re.M)
        if new != s and not dry:
            p.write_text(new)
    if not dry:
        A.mkdir(exist_ok=True)
    for a, ps in sorted(papers.items()):
        body = "\n".join(f"- [[{x}]]" for x in sorted(set(ps)))
        text = (f"---\ntype: author\ntags: []\n---\n\n# {a}\n\n"
                f"Pages in this wiki by {a}:\n\n{body}\n\n"
                f"**Last updated**: {DATE}\n")
        if not dry:
            (A / f"{a}.md").write_text(text)
    for old in A.glob("*.md"):
        if old.stem not in papers and not dry:
            old.unlink()
    print(f"{len(entries)} pages, {len(papers)} authors")
    for n in sorted(unresolved):
        print("surname only, ambiguous or no full name:", n)


if __name__ == "__main__":
    main("--dry-run" in sys.argv)
