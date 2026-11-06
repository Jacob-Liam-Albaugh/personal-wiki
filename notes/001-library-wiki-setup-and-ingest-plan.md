# 001 — Library wiki: setup decisions and ingest plan

2026-11-06

## Decisions
- **No `raw/` move.** The topic folders (Bayesian/, IFT/, Operators/, …) are the raw layer and stay where they are. Pages cite paths relative to the Papers folder.
- **Areas** are slugs taken from those folders and the courses: bayesian, ift, dsl, ml, operators, physics-informed, stochastic, symmetry, gp, math, dsp, digital, em, me697.
- **Duplicates.** Each paper gets one page. The canonical copy is the published version; preprints and extra copies are listed against it in `wiki/meta/sources.md`.
- **Reference-only sources:** `_text books/` and the ME 697 repository. They are ingested one chapter per page, and only on request.
- **Git** tracks only `wiki/`, `notes/`, `CLAUDE.md` and `.gitignore`. It runs on the local `main` branch with no remote.

## Done (batch 1)
- 10 papers ingested: the reading group, the lab IFT papers, the Poly DSL paper, and SG-MCMC.
- 48 wiki pages written, and every link resolves except 3 planned pages.

## Done (batch 2)
- 9 Bayesian/ papers ingested: lab VI, Margossian-Blei, three Kingma papers, SDE-BNN, Fortuin priors, Zhu-Zabaras.
- 13 concept pages added, for 70 pages in all.

## Done (batch 3)
- 4 Operators/ papers and 2 generative papers (score SDE, Group Equivariant GANs) ingested.
- 17 concept pages added and diffusion-models rewritten as a hub. Sub-topics live as sections on hub pages.

## Done (batch 4)
- 5 Diffusion/ papers ingested: DDPM, DDIM, classifier-free guidance, CLIP (with its supplement), and the Nakkiran tutorial. The Song and Wang copies in Diffusion/ are duplicates.
- 8 concept pages added: DDPM, DDIM, noise prediction, noise schedule, classifier guidance, classifier-free guidance, contrastive learning, zero-shot transfer. Updated Diffusion models, Flow matching, Score matching (Tweedie's formula) and ELBO (the diffusion bound).
- **Renamed every page to a readable title** (e.g. `SGLD (Welling 2011)`, `ELBO`), with all links rewritten. Every page now carries topic tags, and graph view colours nodes by them. The naming and tag rules are in CLAUDE.md.

## Done (batch 5)
- ME 697 book part 1 (`ml-software/`): 4 lecture pages and 11 concept pages (JAX transformations, autodiff, optimizers, initialization). New topic tags `optimization` and `software`.

## Done (batches 6 onward)
- Everything else is ingested: the remaining papers, ME 697 parts 2-6, ECE 438/311/270, *Poly*, *Seven Sketches*, and the BT and BJS chapters. Only `_text books/` reference items are left out. Per-batch detail is in `wiki/meta/log.md`.
- Added `tools/`:
  - `authors.py` builds the author pages and graph links.
  - `refs.py` builds the in-wiki citation links and `wiki/meta/wanted-papers.md` (threshold n=2).
  - `test_tools.py` is the self-check.
- Ingest routine: write the pages, then run `python3 tools/authors.py` and `python3 tools/refs.py --n 2`. Download the wanted papers at the top of the list next.

## Open checks against the PDFs
- Alberts & Bilionis 2023, eq. 22: the SGLD noise convention.
- The PIFT Ex. 2 and Ex. 4 noise values.
- Cyclical SG-MCMC Thm 2: the exponents.
- Low-precision SGLD Thm 3: the A/(αm) grouping.
- The DeepONet Thm 3 κ(m,V) rate.
- Zhu & Zabaras: the SVGD equation form and the figure page cites.
- Fortuin: the NTK recursion.
- LNO Fig. 3 values (read by eye) and the GRU comparison.
- Operator review eq. 5.12 exponent, p. 27.
- Kovachki 2022 table page cites.
