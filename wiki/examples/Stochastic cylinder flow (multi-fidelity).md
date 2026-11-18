---
type: example
area: me697
areas: [me697]
source-ref: "ASML (ME 697)"
tags: [uq, ml]
data-origin: [simulated]
tasks: [surrogate modelling]
uses: 1
---

# Stochastic cylinder flow (multi-fidelity)

**Summary**: 1 use in ASML (ME 697). Data: simulated. Tasks: surrogate modelling.

**Covered in**: ASML (ME 697)
**Sources**: `text_books/advanced-scientific-machine-learning/book/up/mf/02_mf_gps.ipynb`.
**Last updated**: 2026-11-18

---

## Stochastic flow past a cylinder, base pressure superquantile (multi-fidelity)

`text_books/advanced-scientific-machine-learning/book/up/mf/02_mf_gps.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: surrogate modelling (multi-fidelity)
- **Technique**: same input-warped MF GP as the synthetic example; ground_truth.csv used as test set
- **Data**: Superquantile risk R_0.6 of base pressure coefficient C_BP from stochastic incompressible flow past a cylinder; inputs x1 in [0,0.5], x2 in [0,0.1]; y in about [-0.81,-0.43].
- **Data origin**: simulated
- **Data file**: data/mf_cylinder_flow/high_fidelity_data.csv (8 rows), low_fidelity_data.csv (99 rows), ground_truth.csv (357 rows = 21 x 17 grid); columns x1, x2, y
- **Forward model**: Incompressible Navier-Stokes past cylinder with random inflow U = 1 + s1 sin(pi y/9) + s2 [xi1 sin(pi y/9) + xi2 cos(pi y/9)]; solver outputs are precomputed (not in notebook).
- **Unknown dimension**: 2 inputs
- **Data dimension**: 8 HF + 99 LF training; 357 test
- **Ground truth**: 357-point grid ground_truth.csv
- **What makes it hard**: very few HF samples
- **Libraries**: jax, tinygp, optax, pandas
- **References**: Perdikaris et al. 2015
- **Notes**: Notebook concludes MF GP is best.

## Related pages
- [[Examples catalogue]]
- [[Multi-fidelity Gaussian process]] · [[Gaussian process]] · [[Surrogate model]] · [[Navier-Stokes equations]]
