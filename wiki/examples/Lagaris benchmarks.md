---
type: example
area: me539
areas: [me539]
source-ref: "Intro SciML (ME 539)"
tags: [physics-informed, pde]
data-origin: [analytic]
tasks: [physics-informed]
uses: 2
---

# Lagaris benchmarks

**Summary**: 2 uses in Intro SciML (ME 539). Data: analytic. Tasks: physics-informed.

**Covered in**: Intro SciML (ME 539)
**Sources**: `text_books/Machine Learning & Statistics/intro-to-scientific-machine-learning/notebooks/26 - Physics-informed Deep Neural Networks/hands-on-26.1.ipynb` and the notebooks listed below.
**Last updated**: 2026-11-18

---

## Lagaris 1998 ODE benchmarks via trial-solution neural nets

`text_books/Machine Learning & Statistics/intro-to-scientific-machine-learning/notebooks/26 - Physics-informed Deep Neural Networks/hands-on-26.1.ipynb`

- **Source**: Intro SciML (ME 539), lecture, complete
- **Problem**: forward ODE solve
- **Technique**: trial solution A+x\*N(x) satisfying ICs by construction; LBFGS and Adam; collocation 10-100 pts
- **Data origin**: analytic
- **Forward model**: Ex1 y'=exp(-x/5)cos x - y/5, y(0)=0, sol exp(-x/5)sin x on [0,2]; Lagaris P1 y(0)=1 sol exp(-t^2/2)/(1+t+t^3)+t^2 on [0,1]; P4 2D system y1'=cos t+y1^2+y2-(1+t^2+sin^2 t), y2'=2t-(1+t^2)sin t+y1 y2, y(0)=(0,1), y1=sin t
- **Unknown dimension**: net weights (hidden 10-50)
- **Ground truth**: closed-form solutions
- **What makes it hard**: easy to moderate
- **Libraries**: torch
- **References**: Lagaris, Likas, Fotiadis 1998

## Lagaris 2D Poisson PDE benchmarks (Problems 5 and 6)

`text_books/Machine Learning & Statistics/intro-to-scientific-machine-learning/notebooks/26 - Physics-informed Deep Neural Networks/hands-on-26.2.ipynb`

- **Source**: Intro SciML (ME 539), lecture, complete
- **Problem**: forward PDE solve
- **Technique**: Psi=A+x(1-x)y(1-y)N, net 2-10-1 sigmoid, 10x10 grid, LBFGS; P6 LBFGS hits local minima so SGD used
- **Data origin**: analytic
- **Forward model**: Laplace(Psi)=f on [0,1]^2 Dirichlet; P5 f=exp(-x)(x-2+y^3+6y), sol exp(-x)(x+y^3); P6 (a=3) sol exp(-(a x+y)/5)sin(a^2 x^2+y)
- **Unknown dimension**: net weights
- **Data dimension**: 2 inputs
- **Ground truth**: closed-form solutions
- **What makes it hard**: P6 oscillatory, local minima
- **Libraries**: torch

## Related pages
- [[Examples catalogue]]
- [[Poisson and Laplace equations]] · [[Adam]] · [[SGD]]
