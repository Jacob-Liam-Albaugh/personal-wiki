---
type: method
area: stochastic
areas: [stochastic, bayesian, me697]
source-ref: "ME 697 book, sinverse/fs/02_filter.ipynb and 03_smoother.ipynb (dax package)"
tags: [inverse-problems, bayesian, sampling, uq]
---

# Particle filter

A sequential Monte Carlo method for filtering in a [[Stochastic state-space model]] when the state law is not Gaussian. The book uses the bootstrap filter and bootstrap smoother of the `dax` package (`BootstrapFilter`, `BootstrapSmoother`).

> [!algorithm] Bootstrap particle filter
> Keep $N$ particles $x_{t-1}^{(i)}$. For each step $t$:
> 1. Propagate: $x_t^{(i)}\sim p_\theta(x_t\mid x_{t-1}^{(i)},u_t)$.
> 2. Weight: $w^{(i)}\propto p_\theta(y_t\mid x_t^{(i)})$.
> 3. Resample particles in proportion to $w^{(i)}$.

The weighted particle set approximates $p(x_t\mid y_{1:t})$. The average weight at each step multiplies into an unbiased estimate $\hat Z$ of the likelihood $p_\theta(y_{1:T})$ **[unverified here: standard SMC fact, used by [[Particle MCMC]]]**.

## Smoother
The bootstrap smoother keeps whole trajectories and conditions on all data, giving $p(x_t\mid y_{1:T})$. The book uses 1000 trajectories (source: 03_smoother.ipynb).

## In the book
> [!example] Duffing oscillator
> 10,000 particles on $t\in[0,40]$, first 200 steps as training data. The credible band narrows as data arrive. Forecasting from the final filtered state loses the true state after a while (source: 02_filter.ipynb).
> The smoother beats the filter, most for the hidden velocity at early times, and more so with larger observation noise (source: 03_smoother.ipynb).

## Notes
- Generic limits: weight degeneracy in high dimensions, cost grows with $N$ **[unverified]**.
- The smoother is the E-step workhorse of [[Expectation-maximization]].
- In the linear-Gaussian case the [[Kalman filter]] is exact and cheaper.

**Covered in**: ASML book sinverse/fs (ME 697 6.2)
**Sources**: `courses/ME 697/advanced-scientific-machine-learning/book/sinverse/fs/02_filter.ipynb`, `03_smoother.ipynb`, `01_reading.md` (heading "Particle Filters" only), `courses/ME 697/advanced-scientific-machine-learning/book/sinverse/fs/intro.md`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Stochastic state-space model]] · [[Kalman filter]] · [[Expectation-maximization]] · [[Particle MCMC]]
- [[Markov chain Monte Carlo]] · [[Euler-Maruyama method]]
