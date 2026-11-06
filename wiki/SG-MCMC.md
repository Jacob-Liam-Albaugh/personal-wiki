---
type: concept
area: stochastic
areas: [stochastic, bayesian]
tags: [sampling, mcmc, bayesian]
---

# Stochastic-gradient MCMC

**Summary**: MCMC that replaces the full-data gradient with a minibatch estimate
$\tilde U(\theta)=-\frac{|D|}{|\tilde D|}\sum_{x\in\tilde D}\log p(x|\theta)-\log p(\theta)$ (AMAGOLD p. 3). Cheap per step, biased unless the step goes to zero or an MH step is added.

**Sources**: `IFT/Welling - Bayesian Learning via Stochastic Gradient Langevin Dynamics.pdf`, `IFT/Ruqi Zhang - Cyclical Stochastic Gradient MCMC.pdf`, `IFT/Ruqi Zhang - AMAGOLD.pdf`, `IFT/Ruqi Zhang - Low Precision Stochastic Gradient Langevin Dynamics.pdf`.
**Last updated**: 2026-11-06

---

## Members in the wiki
| Method | Page | Key point |
|---|---|---|
| SGLD | [[SGLD]] | first-order; decreasing steps |
| SGHMC | [[SGHMC]] | momentum + friction |
| Cyclical SG-MCMC | [[Cyclical SG-MCMC]] | cosine step schedule for multimodality |
| AMAGOLD | [[AMAGOLD]] | amortized MH removes bias |
| Low-precision SGLD | [[Variance-corrected quantization]] | quantized weights and gradients |
| Nested SGLD (lab) | [[Nested SGLD]] | hyperparameters with partition-function term |

Not yet covered: SGNHT and Ma et al.'s complete recipe (2015), cited only.

## Related pages
- [[Langevin dynamics]] · [[Metropolis-Hastings correction]] · [[Bayesian model averaging]]
