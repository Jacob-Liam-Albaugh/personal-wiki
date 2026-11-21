---
type: concept
area: ift
areas: [ift, stochastic]
source-ref: "Eastman, Introduction to Statistical Mechanics, ch. 6 (phasetransitions.rst)"
tags: [ift, mechanics, sampling]
---

# Phase transition

**Summary**: A phase is a local minimum of free energy; a transition happens where the global minimum switches between phases. Symmetry change forces a transition, and metastable phases break ergodicity, a picture that maps onto multimodal posteriors.

**Covered in**: Eastman statmech ch. 6 (Phase transitions)
**Sources**: Eastman, *Introduction to Statistical Mechanics*, github.com/peastman/statmech @cdf566e, `source/phasetransitions.rst`.
**Last updated**: 2026-11-21

---

## Basics
- The stable phase minimises [[Free energy]]. Crossing a coexistence line, the system jumps between phases and absorbs or releases latent heat (the entropy difference times T).
- **Clausius-Clapeyron**: along a coexistence line in the (T, P) plane
  ```
  dP/dT = (S_1 - S_2) / (V_1 - V_2)
  ```
- **Triple point**: three phases coexist. **Critical point**: the line ends; the free-energy difference between the phases vanishes and they become indistinguishable.

## Symmetry (Landau)
Phases with different symmetry groups must be separated by a transition: you cannot gradually lose a symmetry. Liquid and gas share a symmetry, so a path around the critical point connects them; a crystal and a liquid do not.

## Metastability and ergodicity breaking
A local, non-global free-energy minimum is a metastable phase: the system can sit in it for a long time (supercooled water, diamond). Then the time average differs from the ensemble average ([[Ergodicity]] breaks). Spontaneous magnetisation in the [[Ising model]] is the same effect.

## Inference analogy
Wiki note **[unverified]**: a multimodal posterior is a system with several phases. A local sampler ([[Langevin dynamics]], [[Hamiltonian Monte Carlo]]) stuck in one mode is a metastable phase; mixing time explodes as barriers rise. Tempering (raising kT) to cross barriers is the sampling counterpart of heating through a transition (cf. [[Cyclical SG-MCMC (Zhang 2020)]]). Mean-field VI can pick one mode, as [[Mean-field theory]] picks one magnetisation.

## Related pages
- [[Mean-field theory]] · [[Ising model]] · [[Free energy]] · [[Ergodicity]]
