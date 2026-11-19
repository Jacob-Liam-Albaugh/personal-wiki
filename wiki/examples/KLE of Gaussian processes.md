---
type: example
area: me697
areas: [me697]
source-ref: "ASML (ME 697)"
tags: [ml]
data-origin: [analytic]
tasks: [dimensionality reduction]
uses: 2
---

# KLE of Gaussian processes

**Summary**: 2 uses in ASML (ME 697). Data: analytic. Tasks: dimensionality reduction.

**Covered in**: ASML (ME 697)
**Sources**: `text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/hup/funcin/04_kle.ipynb` and the notebooks listed below.
**Last updated**: 2026-11-18

---

## Karhunen-Loeve expansion of Gaussian processes

`text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/hup/funcin/04_kle.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: dimensionality reduction (random field representation)
- **Technique**: Nystrom KLE (class KarhunenLoeveExpansion, build_kle). Experiments: SE kernel scale 0.1 with nq=5 (poor eigenfunctions); lengthscales [0.01,0.05,0.1,0.2,0.5] with nq=100, alpha 0.9; Exp kernel scale 0.1, nq=100, alpha 0.8 (samples look too smooth, notebook asks why); KLE of GP conditioned on 3 random observations; 2D SE kernel scale 0.1, nq=100, alpha 0.9
- **Data**: No data; samples of GPs on [0,1] (and 2D).
- **Data origin**: analytic
- **Forward model**: none
- **Unknown dimension**: truncation order
- **Ground truth**: analytic kernel
- **What makes it hard**: short lengthscales need many terms
- **Libraries**: jax, tinygp
- **References**: Betz, Papaioannou & Straub 2014

## Karhunen-Loeve expansion (older NumPy/SciPy version)

`text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/hup/funcin/_04_kle_original.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: dimensionality reduction (random field representation)
- **Technique**: same KLE by Nystrom in NumPy/SciPy
- **Data**: No data; samples of GPs on [0,1] (and 2D).
- **Data origin**: analytic
- **Forward model**: none
- **Unknown dimension**: truncation order
- **Ground truth**: analytic kernel
- **Libraries**: jax, tinygp
- **References**: Betz, Papaioannou & Straub 2014
- **Notes**: Older variant of 04_kle.ipynb (21 cells vs 30); only diffed, not read in full.

## Related pages
- [[Examples catalogue]]
- [[Karhunen-Loève expansion]] · [[Gaussian process]]
