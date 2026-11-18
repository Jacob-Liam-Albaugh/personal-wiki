---
type: example
area: me697
areas: [me697]
source-ref: "ASML (ME 697)"
tags: [bayesian, inverse-problems]
data-origin: [analytic]
tasks: [inverse problem and calibration]
uses: 1
---

# Gamma density (Laplace)

**Summary**: 1 use in ASML (ME 697). Data: analytic. Tasks: inverse problem and calibration.

**Covered in**: ASML (ME 697)
**Sources**: `text_books/advanced-scientific-machine-learning/book/inverse/basics/04_laplace_approximation_gen.ipynb`.
**Last updated**: 2026-11-18

---

## Gamma density Laplace approximation

`text_books/advanced-scientific-machine-learning/book/inverse/basics/04_laplace_approximation_gen.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: Posterior approximation (1D toy)
- **Technique**: Laplace approximation: Adam (lr 0.01) for mode + autodiff second derivative; multi-D formula derived in markdown only
- **Data origin**: analytic
- **Forward model**: Gamma(alpha=10) log-density; mode = alpha-1 = 9; curvature via jax grad(grad)
- **Unknown dimension**: 1
- **Ground truth**: analytic Gamma density and mode 9
- **Libraries**: jax, optax, jax.scipy.stats
- **Notes**: Bug: find_minimum status always overwritten to 'maximum iterations reached'.

## Related pages
- [[Examples catalogue]]
- [[Laplace approximation]] · [[Adam]]
