---
type: method
area: bayesian
areas: [bayesian, stochastic, me697]
source-ref: "ME 697 book, sinverse/cali/02_em_example.ipynb (01_em_theory.md is headings only)"
tags: [inverse-problems, bayesian, optimization]
---

# Expectation-maximization

An iterative maximum-likelihood method for models with latent variables. In the book the latent variable is the state path $x_{1:T}$ of a [[Stochastic state-space model]] and the unknown is the parameter vector $\theta$.

> [!algorithm] EM for state-space models (source: sinverse/cali/02_em_example.ipynb)
> E-step: with the current iterate $\theta^{(k)}$ form

$$
Q(\theta\mid\theta^{(k)}) = E_{p_{\theta^{(k)}}(x_{1:T}\mid y_{1:T})}\big[\log p_\theta(y_{1:T},x_{1:T})\big].
$$

> M-step:

$$
\theta^{(k+1)} = \arg\max_\theta\ Q(\theta\mid\theta^{(k)}).
$$

The expectation is estimated with a bootstrap smoother ([[Particle filter]]); the M-step is gradient ascent.

> [!example] Duffing oscillator
> Unknowns $\theta=[\alpha,\beta,\delta,\sigma]$ from $\alpha_0=\beta_0=\delta_0=0$, $\sigma_0=2$. Settings: 1000 particles, 100 EM iterations, 100 M-step iterations, learning rate $10^{-3}$, `BootstrapSmoother(1)`. Result: $\alpha=-0.91$ (true $-1$), $\beta=0.93$ (true $1$), $\delta=0.38$ (true $0.3$). The noise estimate is 0.15 against a "true" 0.01 in the notebook. Point estimate only, so no uncertainty (source: 02_em_example.ipynb).

## Notes
- Each EM step does not decrease the likelihood **[unverified: standard property, not stated in the source]**.
- Cheaper than [[Particle MCMC]], but gives a point estimate where PMCMC gives a posterior.
- The notebook's closing question is identifiability of the parameters, see [[Identifiability]].

**Wiki note**: the "true sigma" in the notebook is $\sigma_x=0.01$, but the quantity estimated appears to be the observation noise $s$ (true 0.1).

**Covered in**: ASML book sinverse/cali (ME 697 6.3)
**Sources**: `advanced-scientific-machine-learning/book/sinverse/cali/02_em_example.ipynb`, `01_em_theory.md`, `advanced-scientific-machine-learning/book/sinverse/cali/intro.md`, `03_pmcmc_theory.md`, `04_pmcmc_example.ipynb`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Particle MCMC]] · [[Particle filter]] · [[Stochastic state-space model]]
- [[Variational inference]] (the ELBO is a lower bound with the same structure) · [[Laplace approximation]] · [[Adam]]
