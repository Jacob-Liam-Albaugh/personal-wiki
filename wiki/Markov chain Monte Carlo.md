---
type: method
area: bayesian
areas: [bayesian, me697]
source-ref: "ME 697 book, inverse/sampling 01-02"
tags: [mcmc, sampling, bayesian, inverse-problems]
---

# Markov chain Monte Carlo

> [!algorithm] Random-walk Metropolis-Hastings
> Given the current state $x$:
> 1. Propose $x'\sim q(x'|x)$, here a Gaussian centred on $x$.
> 2. Accept with probability
> $$\alpha=\min\Big(1,\frac{p(x')\,q(x|x')}{p(x)\,q(x'|x)}\Big).$$
> 3. Otherwise stay at $x$.
>
> (source: `inverse/sampling/02_mcmc_blackjax.ipynb`; this page writes the standard acceptance ratio, **[unverified]** against the notebook text)

**Intuition**: Build a Markov chain whose long-run distribution is the posterior, using only unnormalized densities, so the evidence $p(y)$ is never needed. The samples approximate expectations; their quality depends on how fast the chain forgets its start and moves across the target.

## Diagnostics (source: sampling/02)
- **Burn-in**: discard the initial transient (100 of 400 steps in the notebook).
- **Thinning**: keep every $k$-th sample (4 in the notebook) to cut autocorrelation and storage.
- **Split R-hat**: compares within-chain and between-chain variance across several chains; values near 1 indicate mixing.
- **ESS**: effective sample size, the number of independent samples the correlated chain is worth.
- **Trace plots**: made with arviz.

Wiki note: sampling/02 says to change the `alpha` parameter, but the proposal's parameter is `sigma`.

Wiki note: the notebook calls $\hat V$ "an estimate of the variance between chains". It is the pooled estimate of the marginal variance that combines within-chain and between-chain parts.

## Variants in this course
- Random-walk MH on a banana density with `blackjax.rmh` (Wang et al., arXiv 1706.01435, §5.1.3).
- [[Hamiltonian Monte Carlo]]: gradient-guided proposals.
- [[NUTS]]: HMC with adaptive path length and warmup.
- [[SGLD]] and [[SG-MCMC]]: stochastic-gradient versions for large data, with [[Metropolis-Hastings correction]] discussed on its own page.

## Where it appears
- [[Hierarchical Bayesian model]] and [[Identifiability]] use [[NUTS]].
- Reference text: Gelman et al., *Bayesian Data Analysis* ch. 11, and ME 539 Lecture 27 (cited by the book, not read).

**Covered in**: ASML book inverse/sampling (ME 697 4.2); homework 6
**Sources**: `text_books/advanced-scientific-machine-learning/book/inverse/sampling/01_mcmc_basics.md`, `02_mcmc_blackjax.ipynb`, `text_books/advanced-scientific-machine-learning/book/inverse/sampling/intro.md`, `03_hmc_blackjax.ipynb`, `04_nuts_blackjax.ipynb`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Bayesian inverse problems]] · [[Langevin dynamics]] · [[Variational inference]] · [[Laplace approximation]]
- [[Particle MCMC]] · [[Riemannian manifold HMC]] · [[JAX random keys]]

> [!example] Homework 6, problem 1 (source: homework/06_homework.ipynb)
> Show detailed balance implies stationarity, and that the Metropolis-Hastings kernel satisfies detailed balance.

> [!example] Homework 6, problem 3: pharmacokinetics
> Two-compartment IV bolus acetaminophen model: log posterior, prior predictive, MAP, MCMC.

