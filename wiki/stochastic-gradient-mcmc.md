---
type: concept
area: stochastic
areas: [stochastic, bayesian]
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
| SGLD | [[stochastic-gradient-langevin-dynamics]] | first-order; decreasing steps |
| SGHMC | [[stochastic-gradient-hmc]] | momentum + friction |
| Cyclical SG-MCMC | [[cyclical-sg-mcmc]] | cosine step schedule for multimodality |
| AMAGOLD | [[amagold]] | amortized MH removes bias |
| Low-precision SGLD | [[variance-corrected-quantization]] | quantized weights and gradients |
| Nested SGLD (lab) | [[nested-sgld]] | hyperparameters with partition-function term |

Not yet covered: SGNHT and Ma et al.'s complete recipe (2015), cited only.

## Related pages
- [[langevin-dynamics]] · [[metropolis-hastings-correction]] · [[bayesian-model-averaging]]
