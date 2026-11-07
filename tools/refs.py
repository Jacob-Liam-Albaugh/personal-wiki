"""Link wiki pages whose source PDFs cite each other, and list outside works cited by >= n sources.

Usage: python3 tools/refs.py [--n 4] [--dry-run]
Writes a Cites / Cited by block into each page and wiki/meta/wanted-papers.md.
"""
import json, re, sys, time, unicodedata, urllib.error, urllib.parse, urllib.request
from datetime import date
from collections import defaultdict
from pathlib import Path

import fitz

R = Path(__file__).resolve().parent.parent
W = R / "wiki"
CACHE = R / "tools" / ".cache" / "refs.json"
WANTED = CACHE.parent / "wanted.json"
LINKS = CACHE.parent / "links.json"
DATE = date.today().isoformat()
START, END = "%% refs:start %%", "%% refs:end %%"
STOP = set("""with from that this their into over under using via based between through
toward towards analysis approach method methods model models learning study note notes
paper journal proceedings conference international review letters physical arxiv preprint
press university vol volume pages springer elsevier ieee transactions advances neural
information processing systems""".split())
SOFTWARE = {
    "JAX": r"\bjax: compos|deepmind jax ecosystem",
    "PyTorch": r"pytorch: an imperative|automatic differentiation in pytorch",
    "PyTorch Geometric": r"with pytorch geometric",
    "QPyTorch": r"qpytorch: ",
    "TensorFlow": r"\btensorflow: (a system|large-scale)",
    "Theano": r"\btheano: ",
    "Caffe": r"\bcaffe: convolutional",
    "NumPy": r"numpy array: a structure|array programming with numpy",
    "SciPy": r"\bscipy 1\.0|\bscipy: ",
    "Matplotlib": r"\bmatplotlib: ",
    "pandas": r"pandas-dev/pandas",
    "scikit-learn": r"scikit-?learn: machine",
    "scikit-image": r"scikit-image: ",
    "SymPy": r"\bsympy: symbolic",
    "Jupyter": r"jupyter notebooks",
    "Julia": r"julia: a fresh",
    "Optim.jl": r"optim: a mathematical optimization package",
    "DeepXDE": r"deepxde: a deep learning library",
    "DeepONet code": r"deeponet https://doi\.org/10\.5281/zenodo",
    "SciANN": r"sciann: ",
    "GPy": r"\bgpy: ",
    "GPflow": r"gpflow: ",
    "Pyro": r"pyro: deep universal",
    "NumPyro": r"probabilistic programming in numpyro",
    "BNNpriors": r"bnnpriors",
    "PySR": r"pysr: fast",
    "PySINDy": r"pysindy: ",
    "dcgp": r"\bdcgp: ",
    "FEniCS": r"fenics project",
    "UQLab": r"uqlab, a framework",
    "k-Wave": r"k-wave: matlab toolbox",
    "NPEET": r"\(npeet\)",
    "OpenAI Gym": r"openai gym",
    "OpenCV": r"opencv library",
    "Detectron2": r"\bdetectron2\b",
    "ftfy": r"\bftfy\b",
    "WebPlotDigitizer": r"webplotdigitizer",
}


def fold(s):
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()


def words(s):
    return {w for w in re.findall(r"[a-z]{4,}", fold(s)) if w not in STOP}


def dehyphen(s):
    return re.sub(r"(\w)- (\w)", r"\1\2", s)


def software(entry):
    e = fold(dehyphen(entry))
    return next((name for name, pat in SOFTWARE.items() if re.search(pat, e)), None)


def ref_section(text):
    heads = list(re.finditer(r"^\s*(?:\d+\.?\s*)?(references|bibliography|literature cited)\s*$",
                             text, re.I | re.M))
    return text[heads[-1].end():] if heads else ""


def split_entries(sec):
    lines = [l.strip() for l in sec.splitlines() if l.strip()]
    for pat in (r"^\[\d+\]", r"^\d{1,3}\.\s"):
        if sum(bool(re.match(pat, l)) for l in lines) >= 5:
            out = []
            for l in lines:
                if re.match(pat, l) or not out:
                    out.append(l)
                else:
                    out[-1] += " " + l
            return out
    out = []
    starts = r"^[A-Z][A-Za-z'\-]+,?\s+(?:[A-Z]\.|[A-Z][a-z]+[ ,])"
    for l in lines:
        if not out or (re.match(starts, l) and re.search(r"[.\d)]$", out[-1])):
            out.append(l)
        else:
            out[-1] += " " + l
    return out


def entries_for(pdf, cache):
    st = str(pdf.stat().st_mtime)
    c = cache.get(str(pdf))
    if c and c["mtime"] == st:
        return c["entries"], c["title"]
    try:
        d = fitz.open(pdf)
        text = "\n".join(p.get_text() for p in d)
        title = d.metadata.get("title") or ""
    except Exception:
        text, title = "", ""
    ents = [e[:400] for e in split_entries(ref_section(text)) if len(e) > 25]
    cache[str(pdf)] = {"mtime": st, "entries": ents, "title": title}
    return ents, title


def crossref_doi(text):
    q = urllib.parse.urlencode({"query.bibliographic": text[:300], "rows": 1, "select": "DOI,title"})
    req = urllib.request.Request(f"https://api.crossref.org/works?{q}", headers={"User-Agent": "personal-wiki-refs/1.0"})
    for wait in (2, 10, None):
        try:
            items = json.load(urllib.request.urlopen(req, timeout=20))["message"]["items"]
            break
        except (urllib.error.URLError, TimeoutError):
            if wait is None:
                raise
            time.sleep(wait)
    if not items:
        return None
    item = items[0]
    tw = words(" ".join(item.get("title") or []))
    return item["DOI"] if len(tw) >= 2 and len(tw & words(text)) / len(tw) >= 0.8 else None


def link(text):
    if m := re.search(r"\b(10\.\d{4,9}/[^\s,;]+?)\.?(?:\s|$)", text):
        return f"[DOI](https://doi.org/{m.group(1)})"
    if doi := crossref_doi(text):
        return f"[DOI](https://doi.org/{doi})"
    if m := re.search(r"(?:arxiv[:\s.]*(?:abs/)?)(\d{4}\.\d{4,5})", text, re.I):
        return f"[arXiv](https://arxiv.org/abs/{m.group(1)})"
    return scholar(text)


def scholar(text):
    return f"[Scholar](https://scholar.google.com/scholar?q={urllib.parse.quote_plus(text[:200])})"


def links_for(texts):
    known = json.loads(LINKS.read_text()) if LINKS.exists() else {}
    out = dict(known)
    for t in texts:
        if t in out:
            continue
        try:
            out[t] = known[t] = link(t)
        except (urllib.error.URLError, TimeoutError):
            out[t] = scholar(t)
    LINKS.parent.mkdir(parents=True, exist_ok=True)
    LINKS.write_text(json.dumps(known))
    return out


def load_pages():
    pages = {}
    for p in sorted(W.glob("*.md")):
        s = p.read_text()
        fm = re.match(r"---\n(.*?)\n---\n", s, re.S)
        if not fm:
            continue
        f = re.search(r'^file:\s*"?([^"\n]+\.pdf)"?', fm.group(1), re.M)
        if not f or not (R / f.group(1)).exists():
            continue
        h1 = re.search(r"^# (.+)$", s, re.M)
        title = re.sub(r"\s*\([^)]*\d{4}[^)]*\)\s*$", "", h1.group(1)) if h1 else p.stem
        au = re.search(r"^authors:\s*\[(.*)\]", fm.group(1), re.M)
        first = re.sub(r'[\["\]]', "", au.group(1).split(",")[0]).split()[-1] if au and au.group(1).strip() else ""
        yr = re.search(r"^year:\s*(\d{4})", fm.group(1), re.M)
        pages[p.stem] = dict(path=p, text=s, file=f.group(1), title=title,
                             first=fold(first), year=yr.group(1) if yr else "")
    return pages


def matches(entry, pg, pdftitle):
    e = fold(entry)
    if not pg["first"] or not re.search(rf"\b{re.escape(pg['first'])}\b", e[:60]):
        return False
    ew = words(entry)
    for t in (pg["title"], pdftitle, Path(pg["file"]).stem.split(" - ")[-1]):
        tw = words(t)
        if len(tw) >= 2 and len(tw & ew) / len(tw) >= 0.7:
            return True
        if len(tw) < 2 and len(t) > 6 and fold(t) in e and pg["year"] in e:
            return True
    return False


def ref_key(entry):
    body = re.sub(r"^\[?\d{1,3}[.\]]\s*", "", entry)
    sur = re.match(r"\s*([A-Z][A-Za-z'\-]+)", body)
    yr = re.search(r"\b(19|20)\d{2}\b", body)
    return (fold(sur.group(1)) if sur else "", yr.group(0) if yr else "", words(body))


def main(n, dry):
    cache = json.loads(CACHE.read_text()) if CACHE.exists() else {}
    pages = load_pages()
    by_file = defaultdict(list)
    for name, pg in pages.items():
        by_file[pg["file"]].append(name)
    owner = {f: sorted(ns)[0] for f, ns in by_file.items()}
    titles, ents = {}, {}
    for f in by_file:
        ents[f], titles[f] = entries_for(R / f, cache)
    cites, cited_by = defaultdict(set), defaultdict(set)
    uses, sw_ref = defaultdict(set), {}
    clusters = []
    for f, es in ents.items():
        src = owner[f]
        for e in es:
            hit = [t for t, pg in pages.items() if pg["file"] != f and matches(e, pg, titles[pg["file"]])]
            hit = {owner[pages[t]["file"]] for t in hit}
            if hit:
                for t in hit:
                    cites[src].add(t)
                    cited_by[t].add(src)
                continue
            if sw := software(e):
                uses[src].add(sw)
                if sw not in sw_ref or ("github" in e) > ("github" in sw_ref[sw]):
                    sw_ref[sw] = e
                continue
            sur, yr, ws = ref_key(e)
            if not sur or not yr or len(ws) < 3:
                continue
            for c in clusters:
                if c["sur"] == sur and c["yr"] == yr and len(ws & c["ws"]) / len(ws | c["ws"]) >= 0.4:
                    c["by"].add(src)
                    break
            else:
                clusters.append(dict(sur=sur, yr=yr, ws=ws, text=e, by={src}))
    for name, pg in pages.items():
        s = re.sub(rf"\n*{re.escape(START)}.*?{re.escape(END)}\n*", "\n\n", pg["text"], flags=re.S)
        lines = []
        if cites[name]:
            lines.append("**Cites in this wiki**: " + ", ".join(f"[[{t}]]" for t in sorted(cites[name])))
        if cited_by[name]:
            lines.append("**Cited by in this wiki**: " + ", ".join(f"[[{t}]]" for t in sorted(cited_by[name])))
        if uses[name]:
            lines.append("**Software cited**: " + ", ".join(f"[[software#{t}|{t}]]" for t in sorted(uses[name])))
        if lines:
            block = f"{START}\n" + "\n".join(lines) + f"\n{END}\n\n"
            s = re.sub(r"^(\*\*Sources\*\*:)", lambda m: block + m.group(1), s, count=1, flags=re.M)
        if s != pg["text"] and not dry:
            pg["path"].write_text(s)
    wanted = sorted((c for c in clusters if len(c["by"]) >= n), key=lambda c: (-len(c["by"]), c["sur"]))
    url = links_for([c["text"] for c in wanted])
    rows = "\n".join(
        f"| {len(c['by'])} | {c['yr']} | {re.sub(r'[|\[\]]', ' ', c['text'])[:200]} | {url[c['text']]} | "
        + ", ".join(f"[[{b}]]" for b in sorted(c["by"])) + " |" for c in wanted)
    md = (f"---\ntype: meta\ntags: []\n---\n\n# Wanted papers\n\n"
          f"Works not in this wiki that are cited by at least {n} wiki sources. "
          f"Generated by `python3 tools/refs.py --n {n}`; rerun after each ingest.\n\n"
          f"Link is the publisher DOI where Crossref finds a confident title match, else arXiv, else a Scholar search.\n\n"
          f"| Cited by | Year | Reference as extracted | Link | Citing pages |\n"
          f"|---|---|---|---|---|\n{rows}\n\n**Last updated**: {DATE}\n")
    if not dry:
        (W / "meta" / "software.md").write_text(software_md(uses, sw_ref))
        CACHE.parent.mkdir(parents=True, exist_ok=True)
        (W / "meta" / "wanted-papers.md").write_text(md)
        WANTED.write_text(json.dumps([dict(sur=c["sur"], yr=c["yr"], text=c["text"], by=sorted(c["by"]))
                                      for c in wanted]))
        CACHE.write_text(json.dumps(cache))
    nlinks = sum(len(v) for v in cites.values())
    print(f"{len(pages)} pages with PDFs, {sum(map(len, ents.values()))} references, "
          f"{nlinks} in-wiki citation links, {len(wanted)} wanted (n={n}), {len(sw_ref)} software")


def software_md(uses, sw_ref):
    by = defaultdict(set)
    for page, sws in uses.items():
        for sw in sws:
            by[sw].add(page)
    url = links_for([e for e in sw_ref.values() if not re.search(r"github\.com", e)])
    out = []
    for sw in sorted(by, key=lambda t: (-len(by[t]), t.lower())):
        e = re.sub(r"^\s*\[?\d{1,3}[.\]]?\s+", "", re.sub(r"\s+", " ", sw_ref[sw]))
        gh = re.search(r"https?://\s*github\.com/\s*[\w.-]+(?:/\s*[\w.-]+)?", e)
        link = f"[GitHub]({re.sub(r'\s', '', gh.group(0)).rstrip('.')})" if gh else url[sw_ref[sw]]
        out.append(f"## {sw}\n\nCited by {len(by[sw])}: " + ", ".join(f"[[{b}]]" for b in sorted(by[sw]))
                   + f"\n\nReference: {re.sub(r'[|\[\]]', ' ', e)[:300]} {link}\n")
    return (f"---\ntype: meta\ntags: [software]\n---\n\n# Software\n\n"
            f"Software, libraries and code archives cited by wiki sources, kept off [[wanted-papers]]. "
            f"Each paper lists its own under **Software cited**. Generated by `python3 tools/refs.py`; "
            f"add a name to `SOFTWARE` in that file to track another.\n\n" + "\n".join(out)
            + f"\n**Last updated**: {DATE}\n")


if __name__ == "__main__":
    a = sys.argv
    main(int(a[a.index("--n") + 1]) if "--n" in a else 4, "--dry-run" in a)
