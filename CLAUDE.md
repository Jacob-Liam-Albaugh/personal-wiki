# LLM Wiki — Papers library

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

The existing topic folders **are** the raw layer. They are not moved into a `raw/` folder
(they sit in iCloud, two contain their own git repos, and other tools point at them).

```
<topic folders>/               -- source documents (immutable -- never modify, rename or move)
  PSL Reading Group/           -- lab reading group, files named YY.MM.DD - <title>.pdf
  Bayesian/ DSL/ IFT/ ML/ Operators/ Physics Informed Architectures/ Stochastic Methods/
  Symmetries/ Guassian Processes/ Generative ML/ LLMs/ Transforms/ Math/ Linear Optimization/
  Digital Signal Processing/   -- ECE 438 course notes (+ ECE 301 review)
  ECE 27000/                   -- ECE 270 digital systems, weekly lecture notes
  Electromagnetics/            -- ECE 311 lecture slides
  _text books/                 -- textbooks; has its own git repo (git-lfs) -- read only
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

The same paper often sits in several topic folders (e.g. Welling-Teh SGLD is in `Bayesian/`,
`IFT/` and `Stochastic Methods/`), and some entries are ~1 KB Finder aliases, not PDFs. A paper
gets **one** source page. Its `source-ref` names the real PDF; `sources.md` lists every other
path as a duplicate or alias of it. A paper's presence in several folders is useful signal:
record those folders in its `areas` list.

## Areas

Every content page has one primary `area` and may list more in `areas`. Area slugs:

| Slug | Covers | Main folders |
|---|---|---|
| `bayesian` | Bayesian inference, VI, inverse problems, MCMC | `Bayesian/` |
| `ift` | information field theory, SG-MCMC used for IFT | `IFT/` |
| `dsl` | polynomial functors, applied category theory, Bilionis Poly DSL | `DSL/` |
| `ml` | deep-learning foundations: optimizers, init, architectures, spectral bias | `ML/`, `LLMs/` |
| `operators` | operator learning: DeepONet, FNO, LNO, neural operators | `Operators/` |
| `physics-informed` | PINNs, HNN/LNN, neural ODEs, SINDy, NIF | `Physics Informed Architectures/` |
| `stochastic` | Brownian motion, Karhunen-Loève, polynomial chaos, SDEs, score models, diffusion | `Stochastic Methods/`, `Generative ML/`, `Diffusion/` |
| `symmetry` | equivariance and invariance in networks | `Symmetries/` |
| `gp` | Gaussian processes and kernel methods | `Guassian Processes/` |
| `math` | convexity, linear optimization, transforms | `Math/`, `Linear Optimization/`, `Transforms/` |
| `dsp` | ECE 438 DSP and image processing | `Digital Signal Processing/` |
| `digital` | ECE 270 digital systems | `ECE 27000/` |
| `em` | ECE 311 electromagnetics | `Electromagnetics/` |
| `me697` | ME 697 course book (`advanced-scientific-machine-learning/book/`) | course repo |

A new folder gets a new slug, recorded here before it is used.

## Ingest workflow

When the user adds a source or asks you to ingest one:

1. Read the full source document (PDFs via PyMuPDF; handwritten or scanned notes visually).
2. Discuss key takeaways with the user before writing anything. When the user has asked
   for a batch ingest, write the pages and put the takeaways in the log entry and the
   end-of-turn summary instead.
3. Create a source page in `wiki/` (type `paper`, or `lecture` for course notes).
4. Create or update definition / theorem / method / concept pages for each major idea.
   Prefer updating an existing page over creating a near-duplicate.
5. Add `[[wiki-links]]` both ways: source page → concept pages, concept page → every source
   page that uses it.
6. Update `wiki/meta/index.md`, `wiki/meta/sources.md` (status → ingested), and for reading
   group papers `wiki/meta/reading-group.md`.
7. Append an entry to `wiki/meta/log.md` with the date, sources, and pages touched.
8. Run `python3 tools/authors.py && python3 tools/refs.py --n 2` from the repo root. The first
   builds `wiki/authors/` and links each paper's `authors`. The second rewrites each paper's
   `%% refs:start %%` block (Cites / Cited by in this wiki) and `wiki/meta/wanted-papers.md`,
   which lists works outside the wiki cited by at least n wiki sources. Tell the user about new wanted entries.
9. Rebuild the graphify graph with `uv tool run --from graphifyy python -I tools/graph.py .`.
   It writes the untracked `graphify-out/`. Query it with `graphify query "..."`, `graphify path "A" "B"`
   or `graphify explain "X"`.

A single source may touch 10-15 wiki pages. That is normal.

**Ingest order.** Reading-group papers and lab (Bilionis) papers first, then the other
research folders, then course notes. Textbooks and the ME 697 repo are **reference-only**: they
are ingested chapter by chapter only when the user asks, or cited from a concept page to give
another place to look. Long books (Seven Sketches, Poly, Polynomial Functors, BDA3, GPML) are
ingested one chapter per source page (`spivak-niu-poly-ch1.md`, ...).

## Page types and templates

- `paper` — one research paper (or one book chapter)
- `lecture` — one lecture / topic file from course notes
- `definition` — a defined object (Gaussian process, neural operator, polynomial functor, ...)
- `theorem` — a named theorem, proposition, or lemma worth a standalone page
- `method` — an algorithm or model (SGLD, DeepONet, PINN, Adam, SINDy, ...)
- `concept` — broader narrative pages: comparisons, families of methods, area overviews

### Frontmatter (required on every content page)

```yaml
---
type: paper | lecture | definition | theorem | method | concept
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
file: "Bayesian/Welling, Teh - Baysian Learning via Stochastic Gradient Langevin Dynamics.pdf"
```

The body line `**Authors**: Max Welling, Yee Whye Teh · ...` must give full names in PDF order;
`tools/authors.py` reads it. Never edit the `%% refs %%` block by hand.

Author pages (`type: author`) live in `wiki/authors/`, one per person, and are generated.
Graph view colours them with the group `path:authors`; add `-path:authors` to the graph
search to hide them, the same way tags are toggled.

Lecture pages add `course:` (`ece438`, `ece270`, `ece311`, `me697`) and `lecture:` (the
file's own label, e.g. `DSP.3.E`, `L22`, `lect_14`, `week 07 10_03`).

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

### Lecture pages

Course-note pages follow the paper template with sections "Topics", "Key results",
"Examples", in place of Problem/Method/Results. Homework and exam-review problems are folded
into the relevant definition/method page as `> [!example]` callouts, cited to their file.

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
  `_text books/` and `advanced-scientific-machine-learning/` are never touched.
- Page names are short, readable titles, scannable in graph view. Concepts use the common
  name or acronym (`SGLD.md`, `ELBO.md`, `Classifier-free guidance.md`). Paper pages are
  `<short name> (<Firstauthor> <year>).md` (e.g. `SGLD (Welling 2011).md`); lecture pages are
  `<COURSE> <lecture> - <topic>.md` (e.g. `ECE438 DSP.3.E - FFT.md`); book chapters are
  `<Book short> ch<N> - <topic>.md` (e.g. `Seven Sketches ch1 - Generative effects.md`). No `: / # | ^ [ ] ?`.
- Write in clear, plain language.
- When uncertain how to categorize something, ask the user.
