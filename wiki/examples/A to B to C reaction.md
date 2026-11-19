---
type: example
area: me539
areas: [me539]
source-ref: "Intro SciML (ME 539)"
tags: [bayesian, inverse-problems]
data-origin: [simulated]
tasks: [inverse problem and calibration]
uses: 1
---

# A to B to C reaction

**Summary**: 1 use in Intro SciML (ME 539). Data: simulated. Tasks: inverse problem and calibration.

**Covered in**: Intro SciML (ME 539)
**Sources**: `text_books/Machine Learning & Statistics/intro-to-scientific-machine-learning/notebooks/homework/homework-08.ipynb`.
**Last updated**: 2026-11-18

---

## A->B->C reaction calibration under fixed budget

`text_books/Machine Learning & Statistics/intro-to-scientific-machine-learning/notebooks/homework/homework-08.ipynb`

- **Source**: Intro SciML (ME 539), homework, complete
- **Problem**: simulation calibration
- **Technique**: GP surrogate (Matern) with EI on log1p loss vs random search, 24 evaluations incl. 6 initial, 31x31 candidate grid
- **Data origin**: simulated
- **Forward model**: dA/dt=-k1 A, dB/dt=k1 A-k2 B, dC/dt=k2 B, (1,0,0); A,B observed at 10 times 0.5-5.0, sigma 0.025; true k=(0.7,0.35), bounds [0.1,1.5]
- **Unknown dimension**: 2
- **Data dimension**: 20 observations
- **Ground truth**: known true rates
- **What makes it hard**: cheap solver but budgeted
- **Libraries**: sklearn, scipy
- **Notes**: distinct from lecture catalysis.csv

## Related pages
- [[Examples catalogue]]
- [[Gaussian process]] · [[Surrogate model]] · [[Catalysis problem]]
