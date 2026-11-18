---
type: example
area: me697
areas: [me697]
source-ref: "ASML (ME 697)"
tags: [ml]
data-origin: [simulated]
tasks: [dimensionality reduction]
uses: 1
---

# Navier-Stokes POD (Wang-Perdikaris)

**Summary**: 1 use in ASML (ME 697). Data: simulated. Tasks: dimensionality reduction.

**Covered in**: ASML (ME 697)
**Sources**: `text_books/advanced-scientific-machine-learning/book/homework/05_homework.ipynb`.
**Last updated**: 2026-11-18

---

## Wang-Perdikaris 2D Navier-Stokes POD

`text_books/advanced-scientific-machine-learning/book/homework/05_homework.ipynb`

- **Source**: ASML (ME 697), homework, partial
- **Problem**: dimensionality reduction
- **Technique**: SVD/POD, energy plots, 4 modes capture 90 percent, modal coefficient decorrelation, reconstruction
- **Data**: Velocity magnitude snapshots of 2D Navier-Stokes flow, dict keys sol, t, x, y; about 200 snapshots (notebook divides by 200). Not in the repo.
- **Data origin**: simulated
- **Data file**: https://raw.githubusercontent.com/PredictiveIntelligenceLab/CausalPINNs/main/data/NS.npy
- **Forward model**: 2D Navier-Stokes (solver output).
- **Data dimension**: snapshots x flattened grid
- **Ground truth**: original snapshots
- **Libraries**: numpy, scipy
- **References**: Wang & Perdikaris arXiv 2203.07404
- **Notes**: Problem 2. Problem 1 (POD proofs) skipped.

## Related pages
- [[Examples catalogue]]
- [[PINN]] · [[Singular value decomposition]] · [[Proper orthogonal decomposition]] · [[Navier-Stokes equations]]
