---
type: definition
area: bayesian
tags: [bayesian]
---

# Bayesian model averaging

> [!definition] Posterior predictive from samples
> $$p(y|x,D)\approx\frac1S\sum_{s=1}^Sp(y|x,\theta_s),\qquad \theta_s\sim p(\theta|D).$$

Welling & Teh weight samples by step size instead (see [[SGLD]]).

## Where it appears
- [[Cyclical SG-MCMC (Zhang 2020)]] — ensemble across cycles.
- [[Low-precision SGLD (Zhang 2022)]] — test-time prediction (p. 7).

**Sources**: `IFT/Ruqi Zhang - Cyclical Stochastic Gradient MCMC.pdf`, `IFT/Ruqi Zhang - Low Precision Stochastic Gradient Langevin Dynamics.pdf`.
**Last updated**: 2026-11-06

---
## Related pages
- [[Bayesian neural networks]]
- [[Cyclical SG-MCMC]]
- [[SG-MCMC]]
