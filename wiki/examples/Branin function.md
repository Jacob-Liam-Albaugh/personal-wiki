---
type: example
area: me697
areas: [me697, me539]
source-ref: "ASML (ME 697); Intro SciML (ME 539)"
tags: [uq, ml, optimization, gp]
data-origin: [simulated, analytic]
tasks: [surrogate modelling, optimization, active learning, regression]
uses: 2
---

# Branin function

**Summary**: 2 uses in ASML (ME 697) and Intro SciML (ME 539). Data: simulated, analytic. Tasks: surrogate modelling, optimization, active learning, regression.

**Covered in**: ASML (ME 697), Intro SciML (ME 539)
**Sources**: `text_books/advanced-scientific-machine-learning/book/homework/04_homework.ipynb` and the notebooks listed below.
**Last updated**: 2026-11-18

---

## Branin surrogate of legacy C++ code

`text_books/advanced-scientific-machine-learning/book/homework/04_homework.ipynb`

- **Source**: ASML (ME 697), homework, partial
- **Problem**: surrogate modelling / active learning / optimization / multi-fidelity
- **Technique**: GP with SE kernel; Sobol n=10 train, 50 test; 190 random added points; active learning from 1000 candidates; expected improvement for 50 iterations; multi-fidelity GP with f_low and n_low=200
- **Data origin**: simulated
- **Forward model**: Branin function in legacy C++ code called via subprocess wrapper.
- **Unknown dimension**: 2
- **Ground truth**: held-out test set; Branin known
- **Libraries**: GP library (unclear), numpy
- **Notes**: Problem 1. Problem 2 (permutation group) is algebra, skipped.

## Branin function with ARD GP (2D, 3D, 4D variants)

`text_books/intro-to-scientific-machine-learning/notebooks/22 - Gaussian Process Regression Conditioning on Data/hands-on-22.4.ipynb`

- **Source**: Intro SciML (ME 539), lecture, complete
- **Problem**: regression / feature relevance
- **Technique**: GPyTorch ExactGP, SE kernel with ARD, marginal likelihood; isotropic vs ARD RMSE, parity plots
- **Data**: rescaled Branin on [0,1]^2; N=30 (2D), 3D adds 0.1\*x3, 4D adds dummy x4 with N=40; noise sd 0.01; uniform random inputs
- **Data origin**: analytic
- **Forward model**: f=(1/51.95)[(15x2-5.1(15x1)^2/(4pi^2)+75x1/pi-6)^2+(10-10/(8pi))cos(15x1)-44.81]
- **Unknown dimension**: hyperparameters (length scales per input)
- **Data dimension**: 2-4 inputs
- **Ground truth**: analytic function on held-out test set
- **What makes it hard**: ARD recovers weak x3 and irrelevant x4 (long length scales)
- **Libraries**: gpytorch, torch
- **References**: Branin benchmark

## Related pages
- [[Examples catalogue]]
- [[Sobol indices]] · [[Multi-fidelity Gaussian process]] · [[Active learning]] · [[Gaussian process]] · [[Surrogate model]]
