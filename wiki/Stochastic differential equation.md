---
type: concept
area: stochastic
areas: [stochastic, me697]
source-ref: "ME 697 book, sinverse/intro and sinverse/sodes"
tags: [sampling, uq, inverse-problems, pde]
---

# Stochastic differential equation

An SDE adds random forcing to an ODE (source: sinverse/sodes/intro.md: "SDEs model random external excitations"):

$$
dX_t = a(X_t,t)\,dt + b(X_t,t)\,dW_t.
$$

Here $W$ is a [[Wiener process]] ([[Brownian motion]]), $a$ is the drift and $b$ the diffusion coefficient.

## Where they appear in the book
| SDE | Page | Closed form used |
|---|---|---|
| $dX=\mu X\,dt+\sigma X\,dW$ | [[Geometric Brownian motion]] | Itô log transform, lognormal law |
| $dX=-\lambda(X-\mu)dt+\sigma\,dW$ | [[Ornstein-Uhlenbeck process]] | mean and variance of $X_t$ |
| Duffing oscillator with noise | [[Stochastic state-space model]] | none, particle methods |

## Tools
- Simulation: [[Euler-Maruyama method]].
- Brownian paths from random walks (Donsker) and bridges via the [[Karhunen-Loève expansion]] (source: 02_bm.ipynb).
- Density evolution: [[Fokker-Planck equation]].
- Gradient drift with unit noise: [[Langevin dynamics]], used for sampling in [[SGLD]].

## Inverse problems for SDEs
Observed through noise, an SDE becomes a state-space model. Filtering and smoothing recover the state ([[Particle filter]]), calibration recovers parameters ([[Expectation-maximization]], [[Particle MCMC]]).

**Wiki note**: the book does not define the Itô integral or Itô's lemma beyond using the log transform for GBM. For a full treatment see the stochastic-methods pages linked from [[Brownian motion]].

**Covered in**: ASML book sinverse/sodes (ME 697 6.1)
**Sources**: `text_books/advanced-scientific-machine-learning/book/sinverse/intro.md`, `sinverse/sodes/intro.md`, `02_bm.ipynb`, `03_stochastic_exponential_growth.ipynb`, `04_ornstein_uhlenbeck.ipynb`, `sinverse/sodes/01_reading.md`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Euler-Maruyama method]] · [[Geometric Brownian motion]] · [[Ornstein-Uhlenbeck process]]
- [[Stochastic state-space model]] · [[Wiener process]] · [[Fokker-Planck equation]] · [[Langevin dynamics]]
