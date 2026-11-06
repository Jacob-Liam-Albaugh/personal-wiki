---
type: method
area: stochastic
source-ref: "Zhang, Cooper, De Sa 2020, eqs. 3, 6; Welling & Teh 2011 §3"
---

# Metropolis-Hastings correction

> [!definition] MH acceptance
> $$\tau=\min\Big(1,\frac{\pi(y)\,q(y\to x)}{\pi(x)\,q(x\to y)}\Big).$$
> Removes discretization bias exactly, but needs the full-data energy $U$.

**How the SG-MCMC papers treat it**
- [[welling-2011-sgld]]: rejection rate → 0 as $\epsilon\to0$, so it is dropped.
- [[zhang-2020-cyclical-sg-mcmc]]: not used; bias accepted.
- [[zhang-2020-amagold]]: one MH step per $T$ stochastic steps — see [[amagold]].

**Sources**: `IFT/Ruqi Zhang - AMAGOLD.pdf`, `IFT/Welling - Bayesian Learning via Stochastic Gradient Langevin Dynamics.pdf`.
**Last updated**: 2026-11-06
