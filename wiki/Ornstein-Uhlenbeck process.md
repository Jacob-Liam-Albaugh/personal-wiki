---
type: definition
area: stochastic
areas: [stochastic, me697]
source-ref: "ME 697 book, sinverse/sodes/04_ornstein_uhlenbeck.ipynb"
tags: [sampling, uq, inverse-problems]
---

# Ornstein-Uhlenbeck process

> [!definition] Ornstein-Uhlenbeck (OU) process, Vasicek model (source: sinverse/sodes/04_ornstein_uhlenbeck.ipynb)
> A mean-reverting [[Stochastic differential equation]]:

$$
dX_t = -\lambda\,(X_t-\mu)\,dt + \sigma\,dW_t,
$$

with reversion rate $\lambda>0$, long-run mean $\mu$, noise level $\sigma$ and a [[Wiener process]] $W$.

## Moments
Given $X_0$ (source: 04_ornstein_uhlenbeck.ipynb):

$$
E[X_t] = X_0 e^{-\lambda t} + \mu\,(1-e^{-\lambda t}),
$$

$$
V[X_t] = \frac{\sigma^2}{2\lambda}\,(1-e^{-2\lambda t}).
$$

As $t\to\infty$ the law tends to the stationary $N(\mu,\ \sigma^2/(2\lambda))$.

## Fitting recipe in the book
- Set $x_0$ and $\mu$ empirically from the data.
- Fit $\lambda$ by mean-squared error between the data and $E[X_t]$, with [[Adam]], on time rescaled to $[0,1]$.
- Get $\sigma$ from the variance formula (stationary variance $\sigma^2/2\lambda$).
- Simulate with [[Euler-Maruyama method]]; the median of 1000 paths agrees with $E[X_t]$.

> [!example] Treasury yield
> FRED series DGS2 (2-year Treasury), recovery after the COVID shock from 2020-03-12; recovery start 2021-09-12 and "recovered" about 1000 days later. Result in rescaled time: $\lambda=5.226$, $\sigma=1.311$ (source: 04_ornstein_uhlenbeck.ipynb).

## Notes
- The OU process is the Gaussian-process SDE with exponential covariance; the discretized version is an AR(1) model. It is the simplest linear-Gaussian [[Stochastic state-space model]], so the [[Kalman filter]] is exact for it.
- The stationary density solves the [[Fokker-Planck equation]]. The same drift with a potential $U$, $dX=-\nabla U\,dt+\sqrt2\,dW$, is [[Langevin dynamics]].
- Contrast with [[Geometric Brownian motion]], whose noise scales with the state.
- [[Diesel PM as OU process (Bolt 2026)]]: state-dependent $\mu_t,\sigma_t$ driven by engine signals, fit by maximum likelihood on the exact Gaussian transition (time-varying moments as integrals against $e^{-\lambda(t-s)}$).

**Wiki note**: the notebook's `estimate_sigma` computes `sqrt((2*lam*var)/1 - exp(-2*lam*t))`; the intended formula is $\sqrt{2\lambda\,\mathrm{var}/(1-e^{-2\lambda t})}$. Also $\lambda$ is in rescaled time. The "AR(1)" and "exponential covariance" remarks are standard facts, not stated in the source **[unverified here]**.

**Covered in**: ASML book sinverse/sodes (ME 697 6.1)
**Sources**: `text_books/advanced-scientific-machine-learning/book/sinverse/sodes/04_ornstein_uhlenbeck.ipynb`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Stochastic differential equation]] · [[Geometric Brownian motion]] · [[Euler-Maruyama method]]
- [[Brownian motion]] · [[Wiener process]] · [[Langevin dynamics]] · [[Fokker-Planck equation]] · [[Gaussian process]]
- [[Diesel PM as OU process (Bolt 2026)]]
