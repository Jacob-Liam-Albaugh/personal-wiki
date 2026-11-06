---
type: method
area: stochastic
source-ref: "Zhang, Cooper, De Sa 2020, eqs. 3, 6; Welling & Teh 2011 §3"
tags: [sampling, mcmc]
---

# Metropolis-Hastings correction

> [!definition] MH acceptance
> $$\tau=\min\Big(1,\frac{\pi(y)\,q(y\to x)}{\pi(x)\,q(x\to y)}\Big).$$
> Removes discretization bias exactly, but needs the full-data energy $U$.

**How the SG-MCMC papers treat it**
- [[SGLD (Welling 2011)]]: rejection rate → 0 as $\epsilon\to0$, so it is dropped.
- [[Cyclical SG-MCMC (Zhang 2020)]]: not used; bias accepted.
- [[AMAGOLD (Zhang 2020)]]: one MH step per $T$ stochastic steps — see [[AMAGOLD]].

## Examples
- RMHMC accepts with a Hamiltonian-difference test after the generalized implicit leapfrog; reversibility needs fixed-point convergence of the implicit steps (source: Girolami 2011, eq. 16-18). Link [[RMHMC (Girolami 2011)]].

> [!example] Homework 6, problem 1 (source: homework/06_homework.ipynb)
> Prove the Metropolis-Hastings kernel satisfies detailed balance. [[Particle MCMC]] reuses the same acceptance rule with an estimated likelihood.

## Where it appears
- Random-walk Metropolis-Hastings with a Gaussian proposal run with `blackjax.rmh` on a banana density, with burn-in, thinning and split R-hat: [[Markov chain Monte Carlo]], [[ME697 4.2 - Sampling posteriors]]. (source: `inverse/sampling/02_mcmc_blackjax.ipynb`)
- The same accept/reject step ends each [[Hamiltonian Monte Carlo]] trajectory. **[unverified]** in the notebook text.

**Sources**: `IFT/Ruqi Zhang - AMAGOLD.pdf`, `IFT/Welling - Bayesian Learning via Stochastic Gradient Langevin Dynamics.pdf`.
**Last updated**: 2026-11-06

---
## Related pages
- [[Markov chain Monte Carlo]]
- [[Hamiltonian Monte Carlo]]
- [[AMAGOLD]]
- [[SGLD]]
