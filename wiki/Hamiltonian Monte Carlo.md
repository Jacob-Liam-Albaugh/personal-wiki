---
type: method
area: bayesian
areas: [bayesian, me697]
source-ref: "ME 697 book, inverse/sampling 03"
tags: [mcmc, sampling, bayesian]
---

# Hamiltonian Monte Carlo

> [!algorithm] HMC
> Augment $x$ with momentum $p\sim\mathcal N(0,M)$ and simulate the Hamiltonian
> $$H(x,p)=-\log\pi(x)+\tfrac12p^TM^{-1}p$$
> with $L$ leapfrog steps of size $\epsilon$, then accept or reject the end point with a Metropolis step.
>
> (source: `inverse/sampling/03_hmc_blackjax.ipynb`; the equations are the standard form, **[unverified]** against the notebook text)

**Intuition**: Treat $-\log\pi$ as a potential energy and give the sampler momentum. The trajectory follows the gradient and travels far while keeping a high acceptance rate, so the chain moves much faster than a random walk. It costs a gradient per leapfrog step, which [[Automatic differentiation]] provides.

## Tuning parameters
- Step size $\epsilon$, number of leapfrog steps $L$, mass matrix $M$.
- Notebook setting: $\epsilon=0.1$, $L=20$, identity $M$ (source: sampling/03).
- Poor choices give low acceptance (step too large) or slow exploration (path too short). [[NUTS]] adapts $L$ and, with warmup, $\epsilon$ and $M$.

> [!example] Banana density
> A curved target with $b=1$ and $\rho=0.9$ (high curvature), five chains of 200 samples, burn-in 50, run with `blackjax.hmc`.

## Where it appears
- [[Markov chain Monte Carlo]].

## Related ideas
- [[SGHMC]] is the stochastic-gradient version with friction.
- [[Riemannian manifold HMC]] replaces the constant mass matrix by a position-dependent metric.
- [[Langevin dynamics]] is the overdamped, one-step limit.

**Covered in**: ASML book inverse/sampling (ME 697 4.2)
**Sources**: `text_books/advanced-scientific-machine-learning/book/inverse/sampling/03_hmc_blackjax.ipynb`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Markov chain Monte Carlo]] · [[NUTS]] · [[Metropolis-Hastings correction]] · [[SG-MCMC]] · [[Momentum]]
- [[Riemannian manifold HMC]] (non-separable Hamiltonian, generalized leapfrog).
