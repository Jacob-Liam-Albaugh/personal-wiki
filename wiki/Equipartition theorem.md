---
type: theorem
area: ift
areas: [ift, stochastic]
source-ref: "Eastman, Introduction to Statistical Mechanics, ch. 4 (interpretation.rst)"
tags: [ift, mechanics]
---

# Equipartition theorem

> [!theorem] kT/2 per quadratic degree of freedom
> If the energy has a separable term E_1 = C x², then in the canonical ensemble
> ```
> ⟨E_1⟩ = -∂/∂β log ∫ exp(-βCx²) dx
>       = 1/(2β)
>       = kT/2
> ```
> independent of C.
> (source: Eastman, *Introduction to Statistical Mechanics*, github.com/peastman/statmech @cdf566e, `source/interpretation.rst`)

**Intuition**: a stiffer spring confines x more tightly but exactly in proportion, so the average energy it holds is the same. Only the temperature matters.

## Proof sketch
The Gaussian integral is √(π/(βC)); its log is −½ log β plus a constant, and −∂/∂β gives 1/(2β). This is the [[Partition function]] derivative identity on a single quadratic term.

## Where it appears
- [[Fluctuation-dissipation theorem]]: ⟨m v²⟩ = kT fixes the Langevin noise strength.
- [[Brownian motion]]: Einstein's diffusion coefficient D = kT/γ uses it.
- Wiki note **[unverified]**: in [[Hamiltonian Monte Carlo]] each momentum component of a unit-mass Gaussian kinetic energy has ⟨p²/2⟩ = ½ (kT = 1), a quick diagnostic of the momentum refresh.

**Covered in**: Eastman statmech ch. 4 (Interpretation)
**Sources**: Eastman, *Introduction to Statistical Mechanics*, github.com/peastman/statmech @cdf566e, `source/interpretation.rst`.
**Last updated**: 2026-11-21

---

## Related pages
- [[Boltzmann distribution]] · [[Langevin dynamics]] · [[Gaussian process]]
