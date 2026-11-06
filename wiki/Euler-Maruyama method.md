---
type: method
area: stochastic
areas: [stochastic, me697]
source-ref: "ME 697 book, sinverse/sodes (03, 04) and sinverse/fs (02_filter)"
tags: [sampling, uq, mcmc]
---

# Euler-Maruyama method

> [!algorithm] Euler-Maruyama (source: sinverse/sodes/03_stochastic_exponential_growth.ipynb)
> For $dX=a(X,t)\,dt+b(X,t)\,dW$ and step $\Delta t$:

$$
X_{k+1} = X_k + a(X_k,t_k)\,\Delta t + b(X_k,t_k)\,\sqrt{\Delta t}\;Z_k,
\qquad Z_k\sim N(0,I).
$$

The Gaussian increment replaces $dW$ because $W(t+\Delta t)-W(t)\sim N(0,\Delta t)$ ([[Wiener process]]).

## In the book
- [[Geometric Brownian motion]]: $a=\mu X$, $b=\sigma X$, run with `lax.scan` (source: 03_stochastic_exponential_growth.ipynb).
- [[Ornstein-Uhlenbeck process]]: $a=-\lambda(X-\mu)$, $b=\sigma$; 1000 paths with 95% bands (source: 04_ornstein_uhlenbeck.ipynb).
- Discretizing the Duffing SDE in the `dax` package (`EulerMaruyama`) yields the Gaussian transition $N(\cdot,\ \mathrm{diag}(\sigma_x^2,\sigma_v^2)\Delta t)$ of a [[Stochastic state-space model]] (source: sinverse/fs/02_filter.ipynb).

## Notes
- Same scheme as unadjusted [[Langevin dynamics]] and the update of [[SGLD]] when the drift is a gradient.
- Strong order 1/2, weak order 1. **[unverified: standard result, not in the source]**
- Larger steps can leave the state space (negative values for GBM).

**Sources**: `advanced-scientific-machine-learning/book/sinverse/sodes/03_stochastic_exponential_growth.ipynb`, `04_ornstein_uhlenbeck.ipynb`, `sinverse/fs/02_filter.ipynb`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Stochastic differential equation]] · [[Stochastic state-space model]] · [[Langevin dynamics]] · [[SGLD]] · [[Brownian motion]]
- [[ME697 6.1 - Stochastic differential equations]] · [[ME697 6.2 - Filtering and smoothing]]
