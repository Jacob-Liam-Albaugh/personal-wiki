---
type: definition
area: ift
areas: [ift, stochastic]
source-ref: "Eastman, Introduction to Statistical Mechanics, ch. 2, ch. 3, ch. 5 (statisticaldescription.rst, largenumbers.rst, thermodynamics.rst)"
tags: [ift, mechanics]
---

# Statistical entropy

> [!definition] Boltzmann entropy
> For a macrostate with Ω microstates (the density of states)
> ```
> S = k log Ω
> 1/T = ∂S/∂E
> ```
> (source: Eastman, *Introduction to Statistical Mechanics*, github.com/peastman/statmech @cdf566e, `source/statisticaldescription.rst`)

**Intuition**: entropy counts how many microscopic arrangements look the same from outside. Temperature measures how fast that count grows when you add energy.

## Density of states
- One free particle: Ω ∝ E. N particles: Ω ∝ E^((3N−1)/2), an astronomically steep function, which is why one works with log Ω (ch. 2).
- Macrostate probability in the canonical ensemble:
  ```
  p(E) = Ω_A(E) exp(-E/kT) / Z
       = exp(-(E - TS)/kT) / Z
  ```
  Energy wants to be low, entropy wants to be high; E − TS is the [[Free energy]] that balances them.

## Large numbers (ch. 3)
For N two-state units, Ω(m) = N!/(m!(N−m)!): mean N/2, variance N/4, relative width 1/√N. At N ≈ 10^26 the macrostate is sharp, so "most probable" and "certain" coincide. This is the [[Central limit theorem]] at work.

## Second law (ch. 5)
- Eastman's view: the second law is not provable from reversible microscopic dynamics (Loschmidt's objection to Boltzmann's H-theorem). Entropy increases because the universe started in a low-entropy state (the Big Bang), which fixes the arrow of time.
- Heat: dQ = T dS. Heat flows from hot to cold because that raises total entropy.
- Coarse-graining and chaos explain why isolated systems still appear to equilibrate: [[Liouville's theorem]].

## IFT note
Wiki note: Gibbs/Shannon entropy −Σ p log p reduces to k log Ω for a uniform distribution over Ω states **[unverified]** (standard, not in Eastman). In VI the entropy of q is the term that keeps q spread out, the analogue of −TS in a free energy.

## Where it appears
- [[Free energy]], [[Phase transition]], [[Ising model]] (binomial entropy of spins).
- [[KL divergence]], [[ELBO]]: entropy term of the variational distribution.

**Covered in**: Eastman statmech ch. 2 (The statistical description of physical systems), ch. 3 (Large numbers), ch. 5 (Thermodynamics)
**Sources**: Eastman, *Introduction to Statistical Mechanics*, github.com/peastman/statmech @cdf566e, `source/statisticaldescription.rst`, `source/largenumbers.rst`, `source/thermodynamics.rst`.
**Last updated**: 2026-11-21

---

## Related pages
- [[Boltzmann distribution]] · [[Partition function]] · [[Ergodicity]]
