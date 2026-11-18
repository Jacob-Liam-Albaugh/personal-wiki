---
type: example
area: me697
areas: [me697]
source-ref: "ASML (ME 697)"
tags: [bayesian, inverse-problems]
data-origin: [real]
tasks: [inverse problem and calibration]
uses: 1
---

# PK two-compartment IV bolus

**Summary**: 1 use in ASML (ME 697). Data: real. Tasks: inverse problem and calibration.

**Covered in**: ASML (ME 697)
**Sources**: `text_books/advanced-scientific-machine-learning/book/homework/06_homework.ipynb`.
**Last updated**: 2026-11-18

---

## Two-compartment PK IV bolus calibration

`text_books/advanced-scientific-machine-learning/book/homework/06_homework.ipynb`

- **Source**: ASML (ME 697), homework, partial
- **Problem**: Bayesian inverse problem
- **Technique**: MAP via Adam, NUTS (blackjax, 3 chains x 1000), mean-field and full-rank Gaussian VI, numpyro cross-check, AUC 0-36 h
- **Data**: Acetaminophen IV bolus, 1 patient, 6 times (0.0833,0.25,0.5,0.75,8,12 h), concentrations 0.0126 to 0.00061 g/L, dose 0.65 g.
- **Data origin**: real
- **Data file**: data/pk/iv_bolus_data_single_patient.json
- **Forward model**: dc1/dt=-k12 c1+k21 c2; dc2/dt=k12 c1-(k21+kd)c2; analytic c1 in JAX.
- **Unknown dimension**: 4 (k12,k21,kd,V), sigma=0.001 known
- **Data dimension**: 6
- **Ground truth**: none
- **What makes it hard**: Sparse data, parameter non-identifiability
- **Libraries**: jax, numpyro, blackjax, arviz
- **Notes**: Priors Exp(0.1) x3, LogNormal(4,0.5). Problem 3. Problems 1-2 are proofs, skipped.

## Related pages
- [[Examples catalogue]]
- [[NUTS]] · [[Variational inference]] · [[Identifiability]] · [[Adam]]
