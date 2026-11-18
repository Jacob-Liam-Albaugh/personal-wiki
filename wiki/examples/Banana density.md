---
type: example
area: me697
areas: [me697]
source-ref: "ASML (ME 697)"
tags: [sampling, mcmc]
data-origin: [analytic]
tasks: [sampling]
uses: 3
---

# Banana density

**Summary**: 3 uses in ASML (ME 697). Data: analytic. Tasks: sampling.

**Covered in**: ASML (ME 697)
**Sources**: `text_books/advanced-scientific-machine-learning/book/inverse/sampling/02_mcmc_blackjax.ipynb` and the notebooks listed below.
**Last updated**: 2026-11-18

---

## Banana density

`text_books/advanced-scientific-machine-learning/book/inverse/sampling/02_mcmc_blackjax.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: Sampling
- **Technique**: Rosenbluth-Metropolis-Hastings (blackjax.rmh), Gaussian RW proposal sigma=1, 5 chains x 400 steps, init spread 5.0, burn-in 100, thin 4; split R-hat, ESS, arviz traces
- **Data origin**: analytic
- **Forward model**: banana_logdensity(x,a=1.15,b=0.5,rho=0.5): u1=x1/a, u2=a\*(x2-b\*(u1^2+a^2)), (u1,u2)~N(0,[ [1,rho],[rho,1]])
- **Unknown dimension**: 2
- **Ground truth**: analytic density (no reference sampler)
- **What makes it hard**: Curved, correlated 2D density
- **Libraries**: jax, blackjax, arviz
- **References**: Wang et al., arXiv 1706.01435 sec 5.1.3

## Banana density, high curvature

`text_books/advanced-scientific-machine-learning/book/inverse/sampling/03_hmc_blackjax.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: Sampling
- **Technique**: HMC via blackjax: step 0.1, identity mass, 20 leapfrog steps, 5 chains x 200, init spread 2.0, burn-in 50, thin 1; R-hat and ESS
- **Data origin**: analytic
- **Forward model**: Same banana with a=1.15, b=1.0, rho=0.9
- **Unknown dimension**: 2
- **Ground truth**: analytic density
- **What makes it hard**: Strong curvature and correlation
- **Libraries**: jax, blackjax, arviz
- **References**: Wang et al., arXiv 1706.01435
- **Notes**: R-hat converges quickly, ESS high.

## Banana density, high curvature (NUTS)

`text_books/advanced-scientific-machine-learning/book/inverse/sampling/04_nuts_blackjax.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: Sampling
- **Technique**: NUTS with blackjax.window_adaptation, 4 chains, 500 warmup, 500 samples, init N(0,I), burn-in 50, thin 2; arviz summary
- **Data origin**: analytic
- **Forward model**: Same banana a=1.15,b=1.0,rho=0.9
- **Unknown dimension**: 2
- **Ground truth**: analytic density
- **What makes it hard**: Strong curvature
- **Libraries**: jax, blackjax, arviz
- **References**: Adapted from a blackjax change-of-variable tutorial; Wang et al. arXiv 1706.01435

## Related pages
- [[Examples catalogue]]
- [[Hamiltonian Monte Carlo]] · [[NUTS]] · [[Markov chain Monte Carlo]]
