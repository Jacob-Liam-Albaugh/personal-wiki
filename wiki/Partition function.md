---
type: definition
area: ift
areas: [ift, bayesian, stochastic]
source-ref: "Eastman, Introduction to Statistical Mechanics, ch. 2 (statisticaldescription.rst), ch. 4 (interpretation.rst)"
tags: [ift, mechanics, bayesian]
---

# Partition function

> [!definition] Normaliser of the Boltzmann distribution
> ```
> Z = Σ_s exp(-β Φ(s))
> ```
> Derivatives of log Z give ensemble averages:
> ```
> -∂ log Z / ∂β    = ⟨Φ⟩
> -kT ∂ log Z / ∂x = ⟨∂Φ/∂x⟩
> ```
> (source: Eastman, *Introduction to Statistical Mechanics*, github.com/peastman/statmech @cdf566e, `source/statisticaldescription.rst`)

**Intuition**: Z looks like a mere normaliser, but as a function of its parameters it is a generating function: every average you want is a derivative of log Z.

## Generating averages
- Energy: −∂log Z/∂β = ⟨E⟩.
- Any parameter x the energy depends on (volume, field H, coupling J): −kT ∂log Z/∂x = ⟨∂E/∂x⟩. With x = V this gives the pressure; with x = H in the [[Ising model]] it gives the magnetisation.
- Second derivatives give variances: ∂²log Z/∂β² = Var(E) **[unverified]** (standard; Eastman states only the first derivatives).
- [[Equipartition theorem]] is this identity applied to a Gaussian integral.

## Free energy
For the canonical ensemble
```
A = -kT log Z
```
so log Z is minus the [[Free energy]] in units of kT **[unverified]**: standard identity; Eastman defines A = E − TS and relates it to macrostate probability rather than writing A = −kT log Z.

## IFT dictionary
Wiki note:
- Bayes: p(φ|d) = p(d|φ)p(φ)/p(d). With H[φ|d] = −log p(d,φ), the evidence is
  ```
  p(d) = ∫ Dφ exp(-H[φ|d]) = Z
  ```
- Model selection by evidence is comparing free energies, −log Z.
- IFT's generating functional Z[q] (source term q, [[Information field theory]]) is the field version: derivatives in q give moments, derivatives of log Z[q] give cumulants (connected correlation functions).
- Variational inference bounds −log Z from above by the variational free energy = −[[ELBO]].
All four are standard **[unverified]** identifications, not from Eastman.

## Where it appears
- [[Information field theory]]: "the normalizing integral is the partition function".
- [[Laplace approximation]]: a Gaussian estimate of Z around the mode.
- [[Variational inference]], [[ELBO]], [[KL divergence]]: bounds on log Z.

**Covered in**: Eastman statmech ch. 2 (The statistical description of physical systems), ch. 4 (Interpretation)
**Sources**: Eastman, *Introduction to Statistical Mechanics*, github.com/peastman/statmech @cdf566e, `source/statisticaldescription.rst`, `source/interpretation.rst`.
**Last updated**: 2026-11-21

---

## Related pages
- [[Boltzmann distribution]] · [[Free energy]] · [[Statistical entropy]]
- [[Operator calculus for free theory]] · [[Gaussian process]]
