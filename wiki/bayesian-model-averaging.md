---
type: definition
area: bayesian
---

# Bayesian model averaging

> [!definition] Posterior predictive from samples
> $$p(y|x,D)\approx\frac1S\sum_{s=1}^Sp(y|x,\theta_s),\qquad \theta_s\sim p(\theta|D).$$

Welling & Teh weight samples by step size instead (see [[stochastic-gradient-langevin-dynamics]]).

## Where it appears
- [[zhang-2020-cyclical-sg-mcmc]] — ensemble across cycles.
- [[zhang-2022-low-precision-sgld]] — test-time prediction (p. 7).

**Sources**: `IFT/Ruqi Zhang - Cyclical Stochastic Gradient MCMC.pdf`, `IFT/Ruqi Zhang - Low Precision Stochastic Gradient Langevin Dynamics.pdf`.
**Last updated**: 2026-11-06
