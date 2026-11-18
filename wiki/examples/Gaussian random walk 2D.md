---
type: example
area: me697
areas: [me697]
source-ref: "ASML (ME 697)"
tags: [uq]
data-origin: [synthetic]
tasks: [stochastic simulation]
uses: 1
---

# Gaussian random walk 2D

**Summary**: 1 use in ASML (ME 697). Data: synthetic. Tasks: stochastic simulation.

**Covered in**: ASML (ME 697)
**Sources**: `text_books/advanced-scientific-machine-learning/book/ml-software/functional_programming/04_random.ipynb`.
**Last updated**: 2026-11-18

---

## 2D Gaussian random walk

`text_books/advanced-scientific-machine-learning/book/ml-software/functional_programming/04_random.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: sampling / simulation
- **Technique**: jax.random key splitting + lax.scan
- **Data**: 100,000 steps of x_{t+1}=x_t+sigma\*z, z~N(0,I_2), sigma=0.1, generated with split PRNG keys
- **Data origin**: synthetic
- **Forward model**: Gaussian random walk in 2D via lax.scan in JAX
- **Data dimension**: 100000 x 2
- **Ground truth**: none
- **Libraries**: JAX
- **Notes**: Primarily a PRNG/functional-randomness demo; marginal as a test problem.

## Related pages
- [[Examples catalogue]]
- [[Markov chain Monte Carlo]]
