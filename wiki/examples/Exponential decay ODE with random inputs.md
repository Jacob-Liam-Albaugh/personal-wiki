---
type: example
area: me697
areas: [me697]
source-ref: "ASML (ME 697)"
tags: [uq]
data-origin: [analytic]
tasks: [uncertainty propagation]
uses: 3
---

# Exponential decay ODE with random inputs

**Summary**: 3 uses in ASML (ME 697). Data: analytic. Tasks: uncertainty propagation.

**Covered in**: ASML (ME 697)
**Sources**: `text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/up/polynomial_chaos/05_pc_ode_1d.ipynb` and the notebooks listed below.
**Last updated**: 2026-11-18

---

## Linear ODE with uniform decay rate

`text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/up/polynomial_chaos/05_pc_ode_1d.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: uncertainty propagation
- **Technique**: PC Galerkin projection (Legendre degree 5), coefficient ODE solved with Diffrax Tsit5 on t in [0,10], 2000 save points; MC with 10,000 samples via closed form
- **Data origin**: analytic
- **Forward model**: dx/dt=-(0.5+0.1\*Xi)x, x0=1, Xi~U[-1,1]; closed form exp(-(0.5+0.1 xi)t)
- **Unknown dimension**: 1 random input
- **Data dimension**: 2000 time points
- **Ground truth**: analytic solution and MC
- **Libraries**: JAX, Diffrax, orthojax

## Exponential decay Fokker-Planck

`text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/up/sensitivity_analysis/05_fokker_planck.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: uncertainty propagation
- **Technique**: exact Fokker-Planck solution vs MC (10,000 samples), mu0=2, sigma0=0.2, lambda=2, t in [0,1]
- **Data origin**: analytic
- **Forward model**: x'=-lambda x, x0~N(mu0,sigma0^2); p_t=lambda d/dx[x p]; closed-form Gaussian with mu_t=mu0 exp(-lambda t)
- **Unknown dimension**: 1
- **Ground truth**: analytic PDF
- **Libraries**: JAX, NumPy
- **Notes**: Bug: the quoted sigma_t^2 has an extra mu0^2/(2 lambda)(1-exp(-2 lambda t)) term that does not belong to deterministic decay (true variance is sigma0^2 exp(-2 lambda t)).

## Exponential decay with uniform inputs (LHS vs MC)

`text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/up/sensitivity_analysis/06_lhs.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: uncertainty propagation
- **Technique**: Latin hypercube vs uniform MC for mean and variance; RSE of variance vs number of samples; 10,000 LHS samples; 100 repeated experiments of 25 samples
- **Data origin**: analytic
- **Forward model**: y'=-a y, y(0)=y0, a=0.1 x1, y0=8+2 x2, x~U(0,1)^2; solved with scipy odeint, t in [0,50], 200 steps; y=(8+2x2) exp(-0.1 x1 t)
- **Unknown dimension**: 2
- **Data dimension**: 200 time points
- **Ground truth**: analytic mean 90(1-exp(-0.1t))/t and variance 2440(1-exp(-0.2t))/(6t)-mean^2
- **Libraries**: SciPy (qmc, odeint), NumPy
- **Notes**: LHS converges faster than MC. Note the percentile uses 2.75 rather than 2.5 (typo).

## Related pages
- [[Examples catalogue]]
- [[Latin hypercube sampling]] · [[Sensitivity analysis]] · [[Fokker-Planck equation]]
