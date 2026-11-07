# LLM Wiki — personal library

A personal knowledge base maintained by Claude Code, built over this folder of papers,
course notes and textbooks. Based on Andrej Karpathy's LLM Wiki pattern.

## Purpose

This wiki is a structured, interlinked knowledge base over everything in this folder: research
papers (sorted by topic folder), the Predictive Science Lab (Bilionis, Purdue) reading group,
undergraduate course notes, textbooks, and the ME 697 Advanced Scientific Machine Learning
course repo.

The wiki ingests sources and organizes them into one summary page per source, plus
definition, theorem, method and concept pages that cut across sources, all cross-linked. A
concept such as "stochastic gradient Langevin dynamics" or "reparameterization trick" gets
**one** page that every paper using it links to; that cross-paper synthesis is the point.

Claude maintains the wiki. The human curates sources, asks questions, and guides the analysis.

Project-level write-ups (handoff notes, design decisions, ingest plans) live in
`notes/NNN-<description>.md`, indexed in `notes/000-index.md`. These are about the *project*,
not content; content goes in `wiki/`.

## Folder structure

`papers/`, `courses/` and `text_books/` are the raw layer. Wiki pages cite sources by paths
relative to this folder (`papers/IFT/...`).

```
papers/                        -- research papers, by topic (source documents; never modify)
  PSL Reading Group/           -- lab reading group, files named YY.MM.DD - <title>.pdf
  Bayesian/ DSL/ Diffusion/ Generative ML/ Guassian Processes/ IFT/ LLMs/ ML/ Math/ Operators/
  Physics Informed Architectures/ Stochastic Methods/ Symmetries/ Transforms/
courses/                       -- class material
  ECE 270/                     -- digital systems, weekly lecture notes
  ECE 311/                     -- electromagnetics lecture slides
  ECE 438/                     -- DSP course notes (+ ECE 301 review)
  ME 697/                      -- syllabus, videos, homework, data
text_books/                    -- textbooks; its own git repo (git-lfs) -- read only
  advanced-scientific-machine-learning/ -- ME 697 jupyter-book repo; its own git repo -- read only
wiki/                          -- markdown pages maintained by Claude (flat; Obsidian vault root)
wiki/meta/                     -- navigation / bookkeeping scaffolding (hidden from graph by path)
wiki/meta/index.md             -- table of contents for the whole wiki, one section per area
wiki/meta/log.md               -- append-only record of all operations
wiki/meta/sources.md           -- inventory of every source file and its ingest status
wiki/meta/reading-group.md     -- PSL reading group sessions by date → paper page
notes/                         -- project write-ups, numbered, indexed in notes/000-index.md
```

Substantive pages live directly in `wiki/`. Obsidian resolves `[[wiki-links]]` by filename
alone, so links work regardless of subfolder.

### Duplicates and aliases

The same paper often sits in several topic folders (e.g. Welling-Teh SGLD is in `papers/Bayesian/`,
`papers/IFT/` and `papers/Stochastic Methods/`), and some entries are ~1 KB Finder aliases, not PDFs. A paper
gets **one** source page. Its `source-ref` names the real PDF; `sources.md` lists every other
path as a duplicate or alias of it. A paper's presence in several folders is useful signal:
record those folders in its `areas` list.

## Areas

Every content page has one primary `area` and may list more in `areas`. Area slugs:

| Slug | Covers | Main folders |
|---|---|---|
| `bayesian` | Bayesian inference, VI, inverse problems, MCMC | `papers/Bayesian/` |
| `ift` | information field theory, SG-MCMC used for IFT | `papers/IFT/` |
| `dsl` | polynomial functors, applied category theory, Bilionis Poly DSL | `papers/DSL/` |
| `ml` | deep-learning foundations: optimizers, init, architectures, spectral bias | `papers/ML/`, `papers/LLMs/` |
| `operators` | operator learning: DeepONet, FNO, LNO, neural operators | `papers/Operators/` |
| `physics-informed` | PINNs, HNN/LNN, neural ODEs, SINDy, NIF | `papers/Physics Informed Architectures/` |
| `stochastic` | Brownian motion, Karhunen-Loève, polynomial chaos, SDEs, score models, diffusion | `papers/Stochastic Methods/`, `papers/Generative ML/`, `papers/Diffusion/` |
| `symmetry` | equivariance and invariance in networks | `papers/Symmetries/` |
| `gp` | Gaussian processes and kernel methods | `papers/Guassian Processes/` |
| `math` | convexity, linear optimization, transforms | `papers/Math/`, `text_books/Linear Optimization/`, `papers/Transforms/` |
| `dsp` | ECE 438 DSP and image processing | `courses/ECE 438/` |
| `digital` | ECE 270 digital systems | `courses/ECE 270/` |
| `em` | ECE 311 electromagnetics | `courses/ECE 311/` |
| `me697` | ME 697 course book (`text_books/advanced-scientific-machine-learning/book/`) | course repo |

A new folder gets a new slug, recorded here before it is used.

## Ingest workflow

When the user adds a source or asks you to ingest one:

0. If `inbox/` holds PDFs, run `make sort`, report any DUPE/KEEP lines, then ingest every path in
   `inbox/to-ingest.txt` and empty that file once they are ingested.

1. Read the full source document (PDFs via PyMuPDF; handwritten or scanned notes visually).
2. Discuss key takeaways with the user before writing anything. When the user has asked
   for a batch ingest, write the pages and put the takeaways in the log entry and the
   end-of-turn summary instead.
3. Create a source page in `wiki/` (type `paper`). Course notes (lectures, slides, homework)
   get no page of their own: fold them into topic pages (step 4); see "Course notes".
4. Create or update definition / theorem / method / concept pages for each major idea.
   Prefer updating an existing page over creating a near-duplicate.
5. Add `[[wiki-links]]` both ways: source page → concept pages, concept page → every source
   page that uses it.
6. Update `wiki/meta/index.md`, `wiki/meta/sources.md` (status → ingested), and for reading
   group papers `wiki/meta/reading-group.md`.
7. Append an entry to `wiki/meta/log.md` with the date, sources, and pages touched.
8. Run `make` from the repo root. `make authors` builds `wiki/authors/` and links each paper's
   `authors`. `make refs` rewrites each paper's `%% refs:start %%` block (Cites / Cited by in this
   wiki) and `wiki/meta/wanted-papers.md`, which lists works outside the wiki cited by at least
   n wiki sources (`make refs N=3` to change n). Tell the user about new wanted entries.
   Check that every paper just ingested has left `wanted-papers.md` (grep its title). One that
   remains means its page lacks a `file:` path or its title does not match the citations: fix the
   page and rerun `make refs`.
   `make graph` rebuilds the untracked `graphify-out/`; query it with `graphify query "..."`,
   `graphify path "A" "B"` or `graphify explain "X"`.

A single source may touch 10-15 wiki pages. That is normal.

**Ingest order.** Reading-group papers and lab (Bilionis) papers first, then the other
research folders, then course notes. Textbooks and the ME 697 repo are **reference-only**: they
are ingested only when the user asks, or cited from a concept page to give another place to
look. Book chapters are never pages of their own: their content folds into topic pages, the same
way as course notes (see Course notes).

## Page types and templates

- `paper` — one research paper (never a book or book chapter)
- `definition` — a defined object (Gaussian process, neural operator, polynomial functor, ...)
- `theorem` — a named theorem, proposition, or lemma worth a standalone page
- `method` — an algorithm or model (SGLD, DeepONet, PINN, Adam, SINDy, ...)
- `concept` — broader narrative pages: comparisons, families of methods, area overviews

### Frontmatter (required on every content page)

```yaml
---
type: paper | definition | theorem | method | concept
area: <slug>
areas: [<slug>, ...]          # optional, extra areas
source-ref: "<short pointer, e.g. 'Welling, Teh 2011, eq. 4' or 'Topic DSP.6, §3'>"
tags: [<topic>, ...]          # topic tags only, see below
status: lead                  # only on stubs not built from an ingested source
---
```

Paper pages add:

```yaml
authors: ["[[Max Welling]]", "[[Yee Whye Teh]]"]   # written by tools/authors.py
year: 2011
venue: "ICML"                 # if known from the PDF
file: "papers/Bayesian/Welling, Teh - Baysian Learning via Stochastic Gradient Langevin Dynamics.pdf"
```

The body line `**Authors**: Max Welling, Yee Whye Teh · ...` must give full names in PDF order;
`tools/authors.py` reads it. Never edit the `%% refs %%` block by hand.

Author pages (`type: author`) live in `wiki/authors/`, one per person, and are generated.
Graph view colours them with the group `path:authors`; add `-path:authors` to the graph
search to hide them, the same way tags are toggled.

Tags are topics only, never page type, provenance or status.

Topics (several per page; graph view colours by them, first match wins in this order):
`diffusion`, `generative`, `sampling`, `mcmc`, `vi`, `ift`, `bayesian`, `inverse-problems`,
`operators`, `physics-informed`, `category-theory`, `mechanics`, `symmetry`, `gp`, `pde`, `uq`, `optimization`, `software`, `signals`, `electromagnetics`, `digital-logic`, `ml`.
A new topic tag is recorded here before it is used.

### Meta pages (hidden from graph view)

Navigation/bookkeeping pages (`index.md`, `log.md`, `sources.md`, `reading-group.md`) live in
`wiki/meta/` and carry no tags. Graph view hides them with the filter `-path:meta`, and
`.obsidian/app.json` excludes the folder.

### Obsidian callouts

- `> [!definition] <name>` — formal definitions
- `> [!theorem] <name>` — theorem/proposition/lemma statements
- `> [!proof]` — proofs (full, or sketch with note)
- `> [!algorithm] <name>` — algorithm or update-rule statements on method pages
- `> [!example]` — worked examples, experiments, homework problems
- `> [!failure]` — counterexamples, failure modes, reported limitations
- `> [!question]` — open questions the user or Claude raised while reading

### Paper template

```markdown
# <Short title> (<First author> <year>)

**Summary**: <2-3 sentences: problem, idea, result>.

**Authors**: ... · **Year**: ... · **File**: `<path>`

---

## Problem
## Method
<key equations / algorithm in callouts; link every method/definition to its own page>
## Results
<what the experiments actually show; numbers where the paper gives them>
## Limitations
<as stated by the authors, then any the wiki adds, labelled as such>
## Connections
<how it relates to other ingested papers: builds on, competes with, is used by>

**Sources**: `<file>`.
**Last updated**: <YYYY-MM-DD>

---

## Related pages
- [[...]]
```

### Definition / theorem / method template

```markdown
# <Name>

> [!definition|theorem|algorithm] <Name>
> <formal statement / update rule>
>
> (source: `<file>`, <label>)

**Intuition**: <plain-English gloss, 2-5 sentences>

## <Proof / Basic consequences / Variants> as appropriate
## Examples
## Failure modes / non-examples
## Where it appears
<one line per source page that uses it, with how it uses it>

**Sources**: `<file1>`, `<file2>`.
**Last updated**: <YYYY-MM-DD>

---

## Related pages
- [[...]]
```

### Concept template

```markdown
# <Concept>

**Summary**: <1-2 sentences>.

**Sources**: <files>.
**Last updated**: <YYYY-MM-DD>

---

## <Sections as appropriate>

## Related pages
- [[...]]
```

### Course notes and textbooks

Organise by topic, never by class, book or chapter. Textbook chapters fold into topic pages the
same way, e.g. `**Covered in**: Bertsimas-Tsitsiklis ch. 2 (pp. 42-57); Bazaraa-Jarvis-Sherali
ch. 2`; when two books treat a topic, merge them on one page and note where they differ. Lecture notes, slides and book sections from a course
(ECE 270, ECE 311, ECE 438, ME 697) are merged into the definition / method / concept page
for their topic, with a plain-text line above `**Sources**:` naming where it was covered,
e.g. `**Covered in**: ECE 438 IP.6, L34-L36` or `**Covered in**: ASML book up/polynomial_chaos
(ME 697 2.2); homework 3`. ME 697 follows the Advanced Scientific Machine Learning book
(`text_books/advanced-scientific-machine-learning/book/`). Homework and exam-review problems go on the
topic page they exercise as `> [!example]` callouts, cited to their file.

### Notation

Papers disagree on notation (e.g. sign of the Fourier exponent, `β` vs `1/T`, operator
`G` vs `𝒢`). A definition/method page states its notation once, and when a paper differs it
says *"<paper> writes X; this page uses Y"*. Never silently rewrite a paper's statement into
other notation on its own source page.

## Sources and their roles

1. **The source itself** is primary for its own source page. The page reports what the paper
   claims, not what Claude believes; Claude's own assessments go in clearly labelled
   sentences ("Wiki note: ...").
2. **Cross-source pages** (definition/method/concept) cite every source they draw on. When two
   sources disagree, say so explicitly and state which version the page follows and why.
3. **Textbooks and the ME 697 book** are reference: use them to fill a proof a paper defers, to
   give another place to look, or to fix notation.
4. **Claude's background knowledge** may fill gaps only when labelled. A claim with no
   ingested source is marked **[unverified]**. A page created from a citation or from memory
   (no source read) carries `status: lead` and a one-line note saying so.

### Citation format

- Inline: `(source: <file name>)`; add the folder only when the file name is ambiguous.
- With location: `(source: <file>, §3.2)`, `(source: <file>, eq. 7)`, `(source: <file>, p. 12)`.
- External references not in this folder: author-year, plus whether it was read or cited from
  memory.

### Other vaults

The user keeps other wikis (e.g. the Probability course vault, the `ift-sde` wiki at
`~/dev/ift-sde/wiki/ift-sde-wiki/`). They are separate and read-only from here: refer to their
pages by name in code font, never wiki-link to them, never edit them. Report errors found
there to the user.

## Question answering

1. Read `wiki/meta/index.md` first to find relevant pages.
2. Read those pages and synthesize an answer.
3. Cite specific wiki pages in the response.
4. If the answer is not in the wiki, say so; check `sources.md` for an un-ingested source
   that would answer it and offer to ingest it.
5. If the answer is valuable, offer to save it as a new wiki page.

## Lint

When asked to lint or audit the wiki:

- Contradictions between pages
- Orphan pages (no inbound links)
- Concepts mentioned on several pages that lack their own page
- `status: lead` pages whose source is now in the folder and could be ingested
- `sources.md` drift: files on disk missing from the inventory, or inventory rows whose file is gone
- Frontmatter completeness and template conformance per `type`
- Report findings as a numbered list with suggested fixes

## Rules

- Never modify, rename or move anything outside `wiki/`, `notes/`, `CLAUDE.md` and `.gitignore`.
- Always update `wiki/meta/index.md` and `wiki/meta/log.md` after changes.
- Git tracks only `wiki/`, `notes/`, `CLAUDE.md`, `.gitignore`; commit after each ingest or
  batch of edits on `main`. Local only: no remotes, no pushes. The nested repos in
  `text_books/` (including `advanced-scientific-machine-learning/`) is never touched.
- Page names are short, readable titles, scannable in graph view. Concepts use the common
  name or acronym (`SGLD.md`, `ELBO.md`, `Classifier-free guidance.md`). Paper pages are
  `<short name> (<Firstauthor> <year>).md` (e.g. `SGLD (Welling 2011).md`). Never name a page
  after a course, lecture, book or chapter. No `: / # | ^ [ ] ?`.
- Write in clear, plain language.
- When uncertain how to categorize something, ask the user.
