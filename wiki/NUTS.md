---
type: method
area: bayesian
areas: [bayesian, me697]
source-ref: "ME 697 book, inverse/sampling 04"
tags: [mcmc, sampling, bayesian]
---

# NUTS

> [!algorithm] No-U-Turn Sampler
> [[Hamiltonian Monte Carlo]] in which the number of leapfrog steps is chosen on the fly. The trajectory is extended until it starts to turn back on itself (a "U-turn"), then a point is drawn from it.
>
> (source: `inverse/sampling/04_nuts_blackjax.ipynb`; the stopping rule is the standard description, **[unverified]** against the notebook text)

**Intuition**: HMC needs a path length that is long enough to explore but short enough not to retrace its steps. NUTS removes that choice. Combined with warmup adaptation it leaves almost no hand-tuning.

## In Blackjax (source: sampling/04)
- `window_adaptation` tunes the step size and mass matrix during warmup.
- Notebook run: 500 warmup steps, 500 samples, 4 chains, thinning 2.
- hbayes/02 adds tempering (annealing) with a cosine schedule during warmup and prunes poor chains; see [[Hierarchical Bayesian model]].

## Failure modes
- Non-identifiable models give long, random-walk-looking traces: the harmonic-oscillator example in [[Identifiability]].
- Wiki note: funnel-shaped posteriors in hierarchical models are the usual reason for non-centered parameterizations; hbayes/02 contains both, and hbayes/03 ("bad posterior geometry") is an empty stub. **[unverified]**

## Where it appears
- [[Markov chain Monte Carlo]]: banana target.
- [[Hierarchical Bayesian model]]: cars on a bumpy road.
- [[Identifiability]]: harmonic oscillator.

**Covered in**: ASML book inverse/sampling (ME 697 4.2); ASML book inverse/hbayes (ME 697 4.4); ASML book inverse/odes (ME 697 4.5)
**Sources**: `advanced-scientific-machine-learning/book/inverse/sampling/04_nuts_blackjax.ipynb`, `hbayes/02_hbayes_example.ipynb`, `odes/02_identifiability.ipynb`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Hamiltonian Monte Carlo]] · [[Markov chain Monte Carlo]] · [[Riemannian manifold HMC]] · [[Automatic differentiation]]
