---
type: example
area: me697
areas: [me697]
source-ref: "ASML (ME 697)"
tags: [uq, ml]
data-origin: [synthetic]
tasks: [surrogate modelling]
uses: 1
---

# Multi-fidelity 2D synthetic function

**Summary**: 1 use in ASML (ME 697). Data: synthetic. Tasks: surrogate modelling.

**Covered in**: ASML (ME 697)
**Sources**: `text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/up/mf/02_mf_gps.ipynb`.
**Last updated**: 2026-11-18

---

## Multi-fidelity 2D synthetic function (Perdikaris)

`text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/up/mf/02_mf_gps.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: surrogate modelling (multi-fidelity)
- **Technique**: LF GP, then HF GP on lifted input (x/ell, m_l(x)/ell_aug) with RBF kernel via tinygp Transform (input warping); Adam lr 1e-3, 5000 iterations; compared with HF-only GP by RMSE and parity plots
- **Data**: 50 low-fidelity and 8 high-fidelity Latin-hypercube points in [0,1]^2; 100 uniform test points; fixed noise 1e-3.
- **Data origin**: synthetic
- **Data file**: none (generated in notebook)
- **Forward model**: f_h = 0.5 sin(2.5 x1 + (2/3) x2)^2 + (2/3) exp(-x1 (x2-0.5)^2) cos(4 x1 + x2)^2; f_l = 2.5 f_h + (1/3)(sin(x1+x2) + 0.5 exp(-x1) sin(x1+7 x2)). Pure NumPy/JAX functions.
- **Unknown dimension**: 2 inputs
- **Data dimension**: 50 LF + 8 HF observations
- **Ground truth**: analytic f_h on 100 test points
- **What makes it hard**: nonlinear LF-HF relation, very few HF points
- **Libraries**: jax, tinygp, optax
- **References**: Perdikaris et al. 2015
- **Notes**: Markdown text says 1.5 f_h but code uses 2.5 f_h (discrepancy).

## Related pages
- [[Examples catalogue]]
- [[Multi-fidelity Gaussian process]] · [[Gaussian process]] · [[Surrogate model]] · [[Adam]]
