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

## Queue (about 178 files), in this order
1. Bayesian/ — the remaining papers.
2. Operators/ — FNO, Neural Operators, LNO, Stuart.
3. Physics Informed Architectures/.
4. Stochastic Methods/ — the four Karhunen-Loève papers. These will fill out [[karhunen-loeve-expansion]].
5. ML/, Guassian Processes/, Symmetries/, LLMs/.
6. Math/, Transforms/, Linear Optimization/. The BJS book and MIT ch. 1-5 have an old OCR layer with garbled math. Read the equations from page images; re-OCR will not help.
7. Course notes: ECE 438 (DSP), ECE 270, ECE 311 (EM).
8. Books, chapter by chapter: Spivak-Niu *Poly*, *Seven Sketches*. These will fill the planned poly-composition-product and dirichlet-product pages.

## Open checks against the PDFs
- Alberts & Bilionis 2023, eq. 22: the SGLD noise convention.
- The PIFT Ex. 2 and Ex. 4 noise values.
- Cyclical SG-MCMC Thm 2: the exponents.
- Low-precision SGLD Thm 3: the A/(αm) grouping.
- The DeepONet Thm 3 κ(m,V) rate.
- Zhu & Zabaras: the SVGD equation form and the figure page cites.
- Fortuin: the NTK recursion.
