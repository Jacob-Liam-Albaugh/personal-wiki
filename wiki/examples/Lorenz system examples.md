---
type: example
area: me697
areas: [me697]
source-ref: "ASML (ME 697)"
tags: [uq, inverse-problems]
data-origin: [simulated, analytic, synthetic]
tasks: [uncertainty propagation, sensitivity analysis, system identification]
uses: 5
---

# Lorenz system examples

**Summary**: 5 uses in ASML (ME 697). Data: simulated, analytic, synthetic. Tasks: uncertainty propagation, sensitivity analysis, system identification.

**Covered in**: ASML (ME 697)
**Sources**: `text_books/advanced-scientific-machine-learning/book/up/sensitivity_analysis/04_example_lorenz.ipynb` and the notebooks listed below.
**Last updated**: 2026-11-18

---

## Lorenz system sensitivity to initial conditions

`text_books/advanced-scientific-machine-learning/book/up/sensitivity_analysis/04_example_lorenz.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: sensitivity analysis / uncertainty propagation
- **Technique**: local sensitivity via jacobian w.r.t. initial condition and einsum variance; MC with 1000 samples of u0~N(1,0.001^2)
- **Data origin**: simulated
- **Forward model**: x'=sigma(y-x), y'=x(rho-z)-y, z'=xy-beta z, sigma=10, beta=8/3, rho=28, u0=(1,1,1), t in [0,100], 10,000 points, Diffrax Tsit5
- **Unknown dimension**: 3 initial conditions
- **Data dimension**: 3 x 10000
- **Ground truth**: MC
- **What makes it hard**: chaos; Jacobian has NaNs late in time in float32
- **Libraries**: JAX, Diffrax
- **Notes**: Deliberately shows local sensitivity analysis fails: tiny blob spreads over the whole attractor.

## SINDy: Lorenz system

`text_books/advanced-scientific-machine-learning/book/inverse/data/03_sindy_2.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: System identification (chaotic)
- **Technique**: Sequentially thresholded least squares (alpha 0.025) on degree-5 polynomial library; LassoCV tried and abandoned (needs scaling, too slow, poor)
- **Data**: 100 time units, dt 0.001 (100000 points), x0=(-8,7,27), exact derivatives; second run adds N(0,eta^2) noise, eta=10, to the derivatives; prediction run to t=250
- **Data origin**: simulated
- **Forward model**: Lorenz: x'=sigma(y-x), y'=x(rho-z)-y, z'=xy-beta z; sigma=10, rho=28, beta=8/3; scipy odeint
- **Unknown dimension**: 3 x 56
- **Data dimension**: 100000x3
- **Ground truth**: true Lorenz coefficients known; coefficients recovered exactly in noise-free case
- **What makes it hard**: Chaos: trajectories diverge, attractor matches; derivative noise eta=10
- **Libraries**: numpy, scipy, sklearn, jax (vmap for derivatives)
- **References**: Brunton et al. 2016 (PNAS) and its Appendix (Fig 4, 5); Brunton and Kutz 2019 databook
- **Notes**: Noisy case: attractor still looks good.

## Lorenz system PCE

`text_books/advanced-scientific-machine-learning/book/homework/03_homework.ipynb`

- **Source**: ASML (ME 697), homework, partial
- **Problem**: uncertainty propagation
- **Technique**: Polynomial chaos expansion
- **Data origin**: analytic
- **Forward model**: Lorenz sigma=10, beta=8/3, rho=28; ICs x~N(0,0.1), y~N(5,0.1), z~N(20,0.1).
- **Unknown dimension**: 3
- **Ground truth**: Monte Carlo
- **What makes it hard**: Chaos makes PCE degrade with time
- **Libraries**: orthojax, jax
- **Notes**: Problem 4.

## Partially observed Lorenz system SINDy

`text_books/advanced-scientific-machine-learning/book/homework/07_homework.ipynb`

- **Source**: ASML (ME 697), homework, partial
- **Problem**: system identification
- **Technique**: SINDy on x only fails; Hankel matrix (ell=5, then 100) with SVD to 3 modes; degree-5 SINDy
- **Data origin**: simulated
- **Forward model**: Lorenz sigma=10, rho=28, beta=8/3, x0=(-8,7,27), dt=0.01.
- **Data dimension**: 2000 samples of x
- **Ground truth**: known Lorenz equations
- **What makes it hard**: Partial observability
- **Libraries**: scipy, pysindy
- **Notes**: Problem 1. Code: num_steps=int(20/dt)=2000 but ts=linspace(0,100,num_steps) (dt mismatch).

## Noisy Lorenz SINDy without derivatives

`text_books/advanced-scientific-machine-learning/book/homework/07_homework.ipynb`

- **Source**: ASML (ME 697), homework, partial
- **Problem**: system identification
- **Technique**: Numerical differentiation (derivative package) then SINDy
- **Data origin**: synthetic
- **Forward model**: Lorenz as above with N(0,0.01^2) noise.
- **Ground truth**: known Lorenz equations
- **What makes it hard**: Noise amplification
- **Libraries**: pysindy, derivative
- **Notes**: Problem 2.

## Related pages
- [[Examples catalogue]]
- [[SINDy]] · [[Polynomial chaos]] · [[Singular value decomposition]] · [[LASSO]] · [[Sensitivity analysis]] · [[Local sensitivity analysis of ODEs]]
