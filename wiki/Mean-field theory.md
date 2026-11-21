---
type: method
area: ift
areas: [ift, bayesian]
source-ref: "Eastman, Introduction to Statistical Mechanics, ch. 6 (phasetransitions.rst)"
tags: [ift, mechanics, bayesian]
---

# Mean-field theory

> [!definition] Self-consistent field approximation
> Replace each spin's neighbours by the global average M. For the [[Ising model]]:
> ```
> E ≈ -(H + 2dJM) Σ_i σ_i
> M = tanh((H + 2dJM)/kT)
> ```
> (source: Eastman, *Introduction to Statistical Mechanics*, github.com/peastman/statmech @cdf566e, `source/phasetransitions.rst`)

**Intuition**: an interacting problem becomes many independent ones, each feeling an average field that depends on the answer. Solve for the field self-consistently.

## Solutions and the critical point
- If 2dJ/kT ≤ 1 there is one solution; otherwise up to three. When several exist, take the one with lowest [[Free energy]].
- Critical temperature:
  ```
  T_C = 2dJ / k
  ```
  Below T_C the system is ferromagnetic (M ≠ 0 at H = 0); above, paramagnetic.

## How good is it?
Eastman (ch. 6): wrong in 1D (the exact model is ferromagnetic only at T = 0), qualitatively right in 2D, better in 3D. It improves as each site has more neighbours, because the average field fluctuates less.

## Link to variational inference
Wiki note **[unverified]** (standard, not in Eastman): mean-field theory is the Gibbs variational principle with a product trial distribution q(σ) = Π q_i(σ_i). Minimising the variational [[Free energy]] over the q_i gives exactly the tanh self-consistency equation. Mean-field VI in Bayesian inference ([[Variational inference]], e.g. [[Scalable VI for dynamical systems (Gorbach 2017)]]) is the same construction: coordinate updates are the self-consistency loop. Eastman's failure modes carry over: mean-field ignores correlations, so it underestimates posterior variance when variables are strongly coupled.

## Where it appears
- [[Ising model]], [[Phase transition]].
- [[Scalable VI for dynamical systems (Gorbach 2017)]]: closed-form mean-field updates.

**Covered in**: Eastman statmech ch. 6 (Phase transitions)
**Sources**: Eastman, *Introduction to Statistical Mechanics*, github.com/peastman/statmech @cdf566e, `source/phasetransitions.rst`.
**Last updated**: 2026-11-21

---

## Related pages
- [[Phase transition]] · [[Ising model]] · [[Variational inference]] · [[ELBO]]
- [[Information field theory]]
