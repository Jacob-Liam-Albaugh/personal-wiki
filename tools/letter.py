"""Convert non-Letter PDFs in papers/ to US Letter in place, without rasterising.

Usage: python3 tools/letter.py [--dry-run] [paths...]   (no paths: every PDF under papers/)
Each page is embedded as a Form XObject scaled to fit and centred, so fonts, vector figures and
image streams are copied byte for byte. Links, bookmarks and metadata are carried over; named
links become direct page jumps. The original is copied to ../personal-wiki-backups/pre-letter/
first, and the file is left as it was if pages, visible characters, link targets or images differ.
Files with landscape or rotated pages (slides, scanned book spreads) are left alone.
"""
import hashlib, re, shutil, sys
from pathlib import Path

import fitz

R = Path(__file__).resolve().parent.parent
BACKUP = R.parent / "personal-wiki-backups" / "pre-letter"
W, H = 612, 792


def status(doc):
    dims = [sorted((p.rect.width, p.rect.height)) for p in doc]
    if all(abs(w - W) < 2 and abs(h - H) < 2 for w, h in dims):
        return "letter"
    if any(p.rotation or p.rect.width > p.rect.height for p in doc):
        return "landscape"
    return "convert"


def fit(r):
    s = min(W / r.width, H / r.height)
    return fitz.Matrix(s, s) * fitz.Matrix(1, 0, 0, 1, (W - r.width * s) / 2, (H - r.height * s) / 2)


def squash(name):
    try:
        name = name.encode("latin-1").decode("utf-8")  # undoes MuPDF reading UTF-8 names as Latin-1
    except UnicodeError:
        pass
    return re.sub(r"[\s\ufeff\u200b]", "", name)


def links(doc):
    names = None
    for p in doc:
        for ln in p.get_links():
            ln = {k: v for k, v in ln.items() if k != "id"}
            if ln["kind"] == fitz.LINK_LAUNCH and doc.xref_get_key(ln["xref"], "A/S")[1] == "/URI":
                ln.update(kind=fitz.LINK_URI, uri=doc.xref_get_key(ln["xref"], "A/URI")[1])
            if ln["kind"] in (fitz.LINK_GOTO, fitz.LINK_NAMED):
                page = ln.get("page", -1)
                if isinstance(page, str):
                    page = int(page) - 1 if page.isdigit() else -1
                if page < 0 and ln["kind"] == fitz.LINK_NAMED:
                    names = names or {squash(k): v for k, v in doc.resolve_names().items()}
                    hit = names.get(squash(ln.get("nameddest", "")), {})
                    page, ln["to"] = hit.get("page", -1), hit.get("to", ln.get("to"))
                if page >= 0:
                    ln.update(kind=fitz.LINK_GOTO, page=page)
            yield p.number, ln


def convert(src_path, out_path):
    src, out = fitz.open(src_path), fitz.open()
    mats = [fit(p.rect) for p in src]
    for p in src:
        out.new_page(width=W, height=H).show_pdf_page(fitz.Rect(0, 0, W, H), src, p.number)
    for n, ln in links(src):
        ln.pop("xref", None)
        ln["from"] = ln["from"] * mats[n]
        if ln["kind"] == fitz.LINK_GOTO:
            ln["to"] = fitz.Point(ln.get("to") or (0, 0)) * mats[ln["page"]]
        out[n].insert_link(ln)
    out.set_toc(src.get_toc(simple=False))
    out.set_metadata(src.metadata)
    out.save(out_path, garbage=3, deflate=True)


def visible(page):
    d = page.get_text("dict", flags=fitz.TEXTFLAGS_TEXT | fitz.TEXT_IGNORE_ACTUALTEXT)
    return "".join(s["text"] for b in d["blocks"] for ln in b.get("lines", []) for s in ln["spans"] if s["alpha"])


def fingerprint(doc):
    targets = [(n, ln.get("uri"), ln.get("page") if ln["kind"] == fitz.LINK_GOTO else -1) for n, ln in links(doc)]
    imgs = {hashlib.md5(doc.xref_stream_raw(x[0])).hexdigest() for p in doc for x in p.get_images(full=True)}
    chars = [sorted("".join(visible(p).split())) for p in doc]
    return len(doc), chars, targets, imgs, len(doc.get_toc())


def to_letter(pdf, dry=False):
    with fitz.open(pdf) as d:
        st = status(d)
    if st != "convert" or dry:
        return st
    bak = BACKUP / pdf.resolve().relative_to(R)
    bak.parent.mkdir(parents=True, exist_ok=True)
    if not bak.exists():
        shutil.copy2(pdf, bak)
    tmp = pdf.with_name(pdf.name + ".tmp")
    convert(bak, tmp)
    with fitz.open(bak) as a, fitz.open(tmp) as b:
        same = fingerprint(a) == fingerprint(b)
    if not same:
        tmp.unlink()
        return "FAILED check, left as is"
    tmp.replace(pdf)
    return "converted"


def main(args):
    dry = "--dry-run" in args
    paths = [Path(a) for a in args if a != "--dry-run"] or sorted((R / "papers").rglob("*.pdf"))
    landscape = 0
    for pdf in paths:
        try:
            st = to_letter(pdf, dry)
        except (fitz.FileDataError, RuntimeError):
            continue
        landscape += st == "landscape"
        if st not in ("letter", "landscape"):
            print(f"{st.upper() if st == 'convert' else st}  {pdf.resolve().relative_to(R)}")
    if landscape:
        print(f"{landscape} landscape or rotated PDFs left as is")


if __name__ == "__main__":
    main(sys.argv[1:])
