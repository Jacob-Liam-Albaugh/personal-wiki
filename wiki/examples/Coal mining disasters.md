---
type: example
area: me539
areas: [me539]
source-ref: "Intro SciML (ME 539)"
tags: [sampling, mcmc, bayesian, inverse-problems]
data-origin: [real]
tasks: [sampling, inverse problem and calibration]
uses: 1
---

# Coal mining disasters

**Summary**: 1 use in Intro SciML (ME 539). Data: real. Tasks: sampling, inverse problem and calibration.

**Covered in**: Intro SciML (ME 539)
**Sources**: `text_books/Machine Learning & Statistics/intro-to-scientific-machine-learning/notebooks/27 - Sampling Methods/hands-on-27.4.ipynb`.
**Last updated**: 2026-11-18

---

## Coal mining disasters change-point

`text_books/Machine Learning & Statistics/intro-to-scientific-machine-learning/notebooks/27 - Sampling Methods/hands-on-27.4.ipynb`

- **Source**: Intro SciML (ME 539), lecture, complete
- **Problem**: Bayesian change-point
- **Technique**: Pyro NUTS (very slow) then NumPyro NUTS 1000 warmup + 1000 samples
- **Data**: columns year,disasters; 111 rows, 1851-1961
- **Data origin**: real
- **Data file**: data/coal_mining_disasters.csv
- **Forward model**: tau~U(1851,1962); lambda1,lambda2~Exp(1); counts~Poisson(lambda before/after tau)
- **Unknown dimension**: 3
- **Data dimension**: 111 counts
- **Ground truth**: none
- **What makes it hard**: non-smooth likelihood in tau stresses HMC
- **Libraries**: numpyro, pyro, jax
- **References**: classic Jarrett 1979 dataset

## Related pages
- [[Examples catalogue]]
- [[Hamiltonian Monte Carlo]] · [[NUTS]] · [[Poisson and Laplace equations]]
