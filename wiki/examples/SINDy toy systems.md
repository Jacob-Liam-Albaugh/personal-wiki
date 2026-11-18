---
type: example
area: me697
areas: [me697]
source-ref: "ASML (ME 697)"
tags: [inverse-problems]
data-origin: [simulated]
tasks: [system identification]
uses: 3
---

# SINDy toy systems

**Summary**: 3 uses in ASML (ME 697). Data: simulated. Tasks: system identification.

**Covered in**: ASML (ME 697)
**Sources**: `text_books/advanced-scientific-machine-learning/book/inverse/data/02_sindy_1.ipynb` and the notebooks listed below.
**Last updated**: 2026-11-18

---

## SINDy: 2D linear oscillator

`text_books/advanced-scientific-machine-learning/book/inverse/data/02_sindy_1.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: System identification
- **Technique**: LassoCV (n_alphas 10000, eps 1e-5) on degree-5 polynomial library; learned model re-simulated
- **Data**: Noise-free, 10000 points on t in [0,25], x0=(2,0); exact derivatives
- **Data origin**: simulated
- **Forward model**: x1'=-0.1x1+2x2, x2'=-2x1-0.1x2; scipy odeint
- **Unknown dimension**: 2 x 21 coefficients
- **Data dimension**: 10000x2
- **Ground truth**: true coefficients known; near-perfect recovery stated
- **Libraries**: numpy, scipy, sklearn
- **References**: Brunton et al. 2016 (PNAS) and its Appendix
- **Notes**: Reproduces Fig 2 left column of Appendix.

## SINDy: 2D cubic system

`text_books/advanced-scientific-machine-learning/book/inverse/data/02_sindy_1.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: System identification
- **Technique**: LassoCV degree-5 polynomial library
- **Data**: Noise-free, 10000 points t in [0,25], x0=(2,0)
- **Data origin**: simulated
- **Forward model**: x1'=-0.1x1^3+2x2^3, x2'=-2x1^3-0.1x2^3
- **Unknown dimension**: 2 x 21
- **Data dimension**: 10000x2
- **Ground truth**: true coefficients known
- **Libraries**: numpy, scipy, sklearn
- **References**: Brunton et al. 2016 (PNAS) and its Appendix
- **Notes**: Reproduces Fig 2 right column.

## SINDy: 3D linear system

`text_books/advanced-scientific-machine-learning/book/inverse/data/02_sindy_1.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: System identification
- **Technique**: LassoCV degree-5 polynomial library (3 variables)
- **Data**: Noise-free, 2000 points t in [0,50], x0=(2,0,1)
- **Data origin**: simulated
- **Forward model**: x1'=-0.1x1-2x2, x2'=2x1-0.1x2, x3'=-0.3x3
- **Unknown dimension**: 3 x 56
- **Data dimension**: 2000x3
- **Ground truth**: true coefficients known
- **Libraries**: numpy, scipy, sklearn
- **References**: Brunton et al. 2016 (PNAS) and its Appendix
- **Notes**: Reproduces Fig 3.

## Related pages
- [[Examples catalogue]]
- [[SINDy]] · [[LASSO]]
