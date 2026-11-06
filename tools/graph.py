"""Build graphify-out/ (graph.json, graph.html, GRAPH_REPORT.md) from wiki links, with no LLM.

Usage: uv tool run --from graphifyy python -I tools/graph.py .
"""
import json, re, sys, collections
from pathlib import Path
from graphify.build import build_from_json
from graphify.cluster import cluster, score_all
from graphify.analyze import god_nodes, surprising_connections, suggest_questions
from graphify.report import generate
from graphify.export import to_json, to_html
from graphify.detect import detect

R = Path(sys.argv[1]).resolve(); W = R / "wiki"; O = R / "graphify-out"; O.mkdir(exist_ok=True)
pages = {p.stem: p for p in W.rglob("*.md")
         if ".obsidian" not in p.parts and "meta" not in p.parts and not re.match(r"\d{4}-\d{2}-\d{2}|Untitled", p.stem)}
nid = lambda s: re.sub(r"[^a-z0-9]+", "_", s.lower()).strip("_")
tags, nodes, edges = {}, [], []
for name, p in pages.items():
    s = p.read_text()
    t = re.search(r"^tags:\s*\[(.*?)\]", s, re.M)
    tags[nid(name)] = [x.strip() for x in t.group(1).split(",") if x.strip()] if t else []
    ft = "paper" if re.search(r"^type:\s*paper", s, re.M) else "document"
    nodes.append(dict(id=nid(name), label=name, file_type=ft, source_file=str(p), source_location=None,
                      source_url=None, captured_at=None, author=None, contributor=None))
    refs = re.search(r"%% refs:start %%(.*?)%% refs:end %%", s, re.S)
    cited = set(re.findall(r"\[\[([^\]|#]+)", refs.group(1))) if refs else set()
    for tgt in dict.fromkeys(l.strip() for l in re.findall(r"\[\[([^\]|#^]+)", s)):
        if tgt in pages and tgt != name:
            rel = "cites" if tgt in cited else "authored_by" if pages[tgt].parent.name == "authors" else "references"
            edges.append(dict(source=nid(name), target=nid(tgt), relation=rel, confidence="EXTRACTED",
                              confidence_score=1.0, source_file=str(p), source_location=None, weight=1.0))
ext = dict(nodes=nodes, edges=edges, hyperedges=[], input_tokens=0, output_tokens=0)
G = build_from_json(ext, root=str(R), directed=False)
comms = cluster(G)
coh = score_all(G, comms)
labels = {}
for cid, members in comms.items():
    c = collections.Counter(t for m in members for t in tags.get(m, []))
    top = [t for t, _ in c.most_common(2)]
    labels[cid] = " + ".join(top) if top else G.nodes[members[0]].get("label", f"Community {cid}")
gods = god_nodes(G); sur = surprising_connections(G, comms)
qs = suggest_questions(G, comms, labels)
to_json(G, comms, str(O / "graph.json"), force=True)
det = detect(W, cache_root=R)
(O / "GRAPH_REPORT.md").write_text(generate(G, comms, coh, labels, gods, sur, det,
    {"input": 0, "output": 0}, str(R), suggested_questions=qs))
to_html(G, comms, str(O / "graph.html"), community_labels=labels)
print(f"{G.number_of_nodes()} nodes, {G.number_of_edges()} edges, {len(comms)} communities")
print(collections.Counter(e["relation"] for e in edges))
