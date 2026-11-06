# Personal Wiki

A personal knowledge base of research papers, concepts, and study notes, maintained with Claude Code and organized as an Obsidian vault.

Topics include Bayesian inference, information field theory, scientific machine learning, neural operators, generative models, and applied category theory. Paper summaries connect to shared pages covering definitions, methods, and theorems. It also covers course notes (ME 697, ECE 438/311/270) and textbooks read chapter by chapter.

## Navigation

- [Wiki index](wiki/meta/index.md) — browse topics and papers.
- [Source inventory](wiki/meta/sources.md) — references and ingestion status.
- [Wanted papers](wiki/meta/wanted-papers.md) — outside papers cited by two or more wiki sources; candidates to add.
- [Reading group](wiki/meta/reading-group.md) — Predictive Science Lab sessions.
- [Project notes](notes/000-index.md) — workflow and planning.
- [CLAUDE.md](CLAUDE.md) — maintenance instructions and page conventions.

## Reading locally

Clone the repository and open `wiki/` as an Obsidian vault for linked navigation, equations, and callouts. The repository contains Markdown notes; the sources sit beside `wiki/` in `papers/`, `courses/` and `text_books/` and are not tracked.

## Authors, citations, and graph

- Each paper links to author pages in `wiki/authors/`. They appear in Obsidian's graph; hide them with `-path:authors`.
- Papers in the wiki that cite each other are linked in a "Cites / Cited by in this wiki" block.
- A graphify graph is built from the wiki's links into `graphify-out/` (untracked).

## Maintenance

Run after each ingest:

```bash
make
```

`make authors`, `make refs`, and `make graph` run the steps separately; `make test` checks the tools.

