---
type: theorem
area: stochastic
areas: [stochastic, ift]
source-ref: "Eastman, Introduction to Statistical Mechanics, ch. 8 (phasespace.rst)"
tags: [mechanics, sampling, mcmc]
---

# Liouville's theorem

> [!theorem] Hamiltonian flow preserves phase-space volume
> Under Hamilton's equations
> ```
> ẋ =  ∂H/∂p
> ṗ = -∂H/∂x
> ```
> a region of phase space keeps its volume, dV/dt = 0, so the density ρ(x, p) is constant along trajectories.
> (source: Eastman, *Introduction to Statistical Mechanics*, github.com/peastman/statmech @cdf566e, `source/phasespace.rst`)

**Intuition**: an ensemble in phase space flows like an incompressible fluid. It can stretch and fold, but never compress.

## Consequences (ch. 8)
- A harmonic-oscillator ensemble rotates rigidly in phase space.
- It justifies counting microstates with uniform cells in (x, p): a cell keeps its size under the dynamics, so equal cells stay equally weighted. Binning by energy instead would not be invariant (Boltzmann's choice).
- A quantum version exists.

## Approach to equilibrium
Liouville implies an isolated deterministic system cannot truly equilibrate: fine-grained ρ never spreads. It does so in practice because
1. real systems are never isolated (heat bath, diffusion), and
2. chaos stretches and folds a region into filaments finer than any cell, so the coarse-grained density equilibrates.
This is why entropy increase needs coarse-graining ([[Statistical entropy]]).

## Sampling link
Wiki note **[unverified]**: [[Hamiltonian Monte Carlo]] relies on this. The leapfrog integrator is symplectic, so it preserves volume exactly; the Metropolis acceptance then needs no Jacobian. The [[Fokker-Planck equation]] with no diffusion term is the Liouville (continuity) equation, and probability-flow ODEs in [[Diffusion models]] move density this way, though generally not volume-preserving.

## Where it appears
- [[Hamiltonian Monte Carlo]], [[Riemannian manifold HMC]].
- [[Ergodicity]].

**Covered in**: Eastman statmech ch. 8 (Phase space)
**Sources**: Eastman, *Introduction to Statistical Mechanics*, github.com/peastman/statmech @cdf566e, `source/phasespace.rst`.
**Last updated**: 2026-11-21

---

## Related pages
- [[Fokker-Planck equation]] · [[Markov chain Monte Carlo]]
