---
type: example
area: me539
areas: [me539]
source-ref: "Intro SciML (ME 539)"
tags: [sampling, mcmc, bayesian, inverse-problems, ml, vi]
data-origin: [real]
tasks: [sampling, inverse problem and calibration, regression, variational inference]
uses: 2
---

# Challenger O-ring

**Summary**: 2 uses in Intro SciML (ME 539). Data: real. Tasks: sampling, inverse problem and calibration, regression, variational inference.

**Covered in**: Intro SciML (ME 539)
**Sources**: `text_books/Machine Learning & Statistics/intro-to-scientific-machine-learning/notebooks/27 - Sampling Methods/hands-on-27.4.ipynb` and the notebooks listed below.
**Last updated**: 2026-11-18

---

## Challenger O-ring failure, logistic regression with NUTS

`text_books/Machine Learning & Statistics/intro-to-scientific-machine-learning/notebooks/27 - Sampling Methods/hands-on-27.4.ipynb`

- **Source**: Intro SciML (ME 539), lecture, complete
- **Problem**: Bayesian logistic regression
- **Technique**: NumPyro NUTS 1000+1000
- **Data**: Date,Temperature,Damage Incident; 25 rows, 1 NA, 23 usable, 7 damage incidents, 53-81 F
- **Data origin**: real
- **Data file**: data/challenger_data.csv
- **Forward model**: p=1/(1+exp(beta\*T+alpha)), alpha,beta~N(0,10^2), Bernoulli
- **Unknown dimension**: 2
- **Data dimension**: 23
- **Ground truth**: none
- **What makes it hard**: tiny data, extrapolation to 31 F
- **Libraries**: numpyro, jax
- **Notes**: HW5 reference in notebook

## Challenger O-ring with variational inference

`text_books/Machine Learning & Statistics/intro-to-scientific-machine-learning/notebooks/28 - Variational Inference/hands-on-28.ipynb`

- **Source**: Intro SciML (ME 539), lecture, complete
- **Problem**: Bayesian logistic regression
- **Technique**: pyro SVI, AutoDiagonalNormal, 40000 iterations
- **Data**: same as 27.4
- **Data origin**: real
- **Data file**: data/challenger_data.csv
- **Forward model**: p=sigmoid(alpha+beta\*T)
- **Unknown dimension**: 2
- **Data dimension**: 23
- **Ground truth**: compare with NUTS
- **What makes it hard**: mean-field underestimates correlation
- **Libraries**: pyro, torch
- **Notes**: text says N(0,10^2) prior but code uses Normal(0,100); sign convention opposite to 27.4

## Related pages
- [[Examples catalogue]]
- [[NUTS]] · [[Variational inference]]
