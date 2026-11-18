---
type: example
area: me697
areas: [me697]
source-ref: "ASML (ME 697)"
tags: [uq]
data-origin: [analytic]
tasks: [stochastic simulation]
uses: 1
---

# Brownian motion, bridge and sheet

**Summary**: 1 use in ASML (ME 697). Data: analytic. Tasks: stochastic simulation.

**Covered in**: ASML (ME 697)
**Sources**: `text_books/advanced-scientific-machine-learning/book/sinverse/sodes/02_bm.ipynb`.
**Last updated**: 2026-11-18

---

## Brownian motion, bridge and sheet

`text_books/advanced-scientific-machine-learning/book/sinverse/sodes/02_bm.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: sampling
- **Technique**: Direct simulation and KL expansion; empirical variance checked against analytic
- **Data**: Simulated paths: n_steps 10000 (1000 for bridge and 2D sheet), 1000 samples; sheet via KL expansion with 100/1000 terms.
- **Data origin**: analytic
- **Forward model**: W(t) with Var=t; Brownian bridge Var=t(1-t); 2D Brownian sheet via Karhunen-Loeve expansion.
- **Ground truth**: Analytic variances t and t(1-t)
- **Libraries**: jax, numpy, matplotlib
- **Notes**: Pure process-sampling demo, usable as SDE/path-space test.

## Related pages
- [[Examples catalogue]]
- [[Karhunen-Loève expansion]] · [[Brownian motion]]
