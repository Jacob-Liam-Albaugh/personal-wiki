---
type: definition
area: stochastic
areas: [stochastic, ift]
source-ref: "Eastman, Introduction to Statistical Mechanics, ch. 2, 6, 8"
tags: [mechanics, sampling, mcmc]
---

# Ergodicity

> [!definition] Time average equals ensemble average
> A system is ergodic if the long-time average of a quantity along one trajectory equals its average over the equilibrium ensemble.
> (source: Eastman, *Introduction to Statistical Mechanics*, github.com/peastman/statmech @cdf566e, `source/statisticaldescription.rst`)

**Intuition**: one long movie of a single system shows you every typical state in the right proportions, so you can replace the impossible ensemble sum by watching one copy.

## Why it matters (ch. 2)
Statistical mechanics computes ensemble averages, but experiments measure time averages. Ergodicity, together with the equal a priori postulate, is what licenses the swap.

## When it fails
- **Broken symmetry** ([[Ising model]], ch. 6): below T_C a magnet stays in one of two equally likely magnetisations, so the time average of M is ±M_0 while the ensemble average is 0.
- **Metastable phases** ([[Phase transition]], ch. 6): local free-energy minima trap the dynamics.
- **Isolated deterministic systems** ([[Liouville's theorem]], ch. 8): fine-grained density never spreads; coarse-graining and contact with a bath restore effective ergodicity.

## MCMC
Wiki note **[unverified]**: an MCMC estimate (1/n) Σ f(θ_k) is a time average; it converges to the posterior expectation because the chain is built to be ergodic for the target. Poor mixing between posterior modes is practical ergodicity breaking, the same as a metastable phase. See [[Markov chain Monte Carlo]], [[Langevin dynamics]].

## Where it appears
- [[Markov chain Monte Carlo]], [[Hamiltonian Monte Carlo]], [[SGLD]].
- [[Boltzmann distribution]].

**Covered in**: Eastman statmech ch. 2 (The statistical description of physical systems), ch. 6 (Phase transitions), ch. 8 (Phase space)
**Sources**: Eastman, *Introduction to Statistical Mechanics*, github.com/peastman/statmech @cdf566e, `source/statisticaldescription.rst`, `source/phasetransitions.rst`, `source/phasespace.rst`.
**Last updated**: 2026-11-21

---

## Related pages
- [[Statistical entropy]] · [[Phase transition]] · [[Liouville's theorem]]
