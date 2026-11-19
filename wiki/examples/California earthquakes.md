---
type: example
area: me539
areas: [me539]
source-ref: "Intro SciML (ME 539)"
tags: [bayesian, inverse-problems]
data-origin: [real]
tasks: [inverse problem and calibration]
uses: 1
---

# California earthquakes

**Summary**: 1 use in Intro SciML (ME 539). Data: real. Tasks: inverse problem and calibration.

**Covered in**: Intro SciML (ME 539)
**Sources**: `text_books/Machine Learning & Statistics/intro-to-scientific-machine-learning/notebooks/homework/homework-03.ipynb`.
**Last updated**: 2026-11-18

---

## Southern California and Baja M>=6.5 earthquake rate

`text_books/Machine Learning & Statistics/intro-to-scientific-machine-learning/notebooks/homework/homework-03.ipynb`

- **Source**: Intro SciML (ME 539), homework, complete
- **Problem**: Bayesian rate inference
- **Technique**: Gamma-Poisson conjugate, prior sensitivity, credible intervals, posterior predictive check, 10- and 20-yr probabilities
- **Data**: 18 events; time, latitude, longitude, depth, mag, place, id; lat 32-37, lon -122 to -114, 1900-2025
- **Data origin**: real
- **Data file**: data/homework/southern-california-baja-earthquakes-1900-2025.csv
- **Unknown dimension**: 1 (rate lambda)
- **Data dimension**: 126 annual counts
- **What makes it hard**: few events, prior-sensitive
- **Libraries**: pandas, scipy
- **References**: USGS ComCat doi 10.5066/F7MS3QZH; Love 2012; Rotondi 2013

## Related pages
- [[Examples catalogue]]
- [[Sensitivity analysis]] · [[Poisson and Laplace equations]]
