---
type: example
area: me539
areas: [me539]
source-ref: "Intro SciML (ME 539)"
tags: [optimization]
data-origin: [analytic, synthetic]
tasks: [optimization]
uses: 2
---

# Bayesian optimisation 1D test function

**Summary**: 2 uses in Intro SciML (ME 539). Data: analytic, synthetic. Tasks: optimization.

**Covered in**: Intro SciML (ME 539)
**Sources**: `text_books/intro-to-scientific-machine-learning/notebooks/23 - Bayesian Global Optimization/hands-on-23.1.ipynb` and the notebooks listed below.
**Last updated**: 2026-11-18

---

## 1D Bayesian optimisation test function, noise-free

`text_books/intro-to-scientific-machine-learning/notebooks/23 - Bayesian Global Optimization/hands-on-23.1.ipynb`

- **Source**: Intro SciML (ME 539), lecture, complete
- **Problem**: global optimisation
- **Technique**: max-mean (fails), upper interval psi=1.96, probability of improvement, expected improvement; 23.6 samples posterior for max and argmax (1000 samples)
- **Data**: 3 initial points seed 12345; fixed GP lengthscale 0.15, outputscale 4.0, noise 1e-4
- **Data origin**: analytic
- **Forward model**: f(x)=-4(1-sin(6x+8exp(6x-7))) maximised on [0,1]
- **Unknown dimension**: 1
- **Data dimension**: 1
- **Ground truth**: analytic maximum
- **What makes it hard**: multimodal, greedy acquisition gets trapped
- **Libraries**: gpytorch, torch
- **Notes**: Same function reused in hands-on-23.2 to 23.4 and 23.6.

## 1D Bayesian optimisation, noisy observations

`text_books/intro-to-scientific-machine-learning/notebooks/23 - Bayesian Global Optimization/hands-on-23.5.ipynb`

- **Source**: Intro SciML (ME 539), lecture, complete
- **Problem**: noisy global optimisation
- **Technique**: noisy MUI, PI, EI
- **Data**: g=f+0.4\*randn, seed 123456, n_init=4, 20 iterations
- **Data origin**: synthetic
- **Forward model**: same f as 23.1 with noise sd 0.4
- **Unknown dimension**: 1
- **Data dimension**: 1
- **Ground truth**: analytic f
- **What makes it hard**: noise masks improvement
- **Libraries**: gpytorch, torch

## Related pages
- [[Examples catalogue]]
- [[Gaussian process]]
