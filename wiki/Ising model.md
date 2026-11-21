---
type: definition
area: ift
areas: [ift, stochastic, bayesian]
source-ref: "Eastman, Introduction to Statistical Mechanics, ch. 6 (phasetransitions.rst)"
tags: [ift, mechanics, sampling]
---

# Ising model

> [!definition] Spins on a lattice
> Spins σ_i = ±1 on a d-dimensional lattice, each with 2d nearest neighbours:
> ```
> E = -H Σ_i σ_i - J Σ_<ij> σ_i σ_j
> M = ⟨σ⟩
> ```
> H is the external field, J the coupling, M the magnetisation.
> (source: Eastman, *Introduction to Statistical Mechanics*, github.com/peastman/statmech @cdf566e, `source/phasetransitions.rst`)

**Intuition**: each spin wants to line up with the field and with its neighbours; temperature scrambles them. The fight between those decides whether order appears.

## Regimes (ch. 6)
- **J > 0, H = 0**: ferromagnet. Up and down are symmetric, yet at low T the system picks one: spontaneous symmetry breaking. The time average differs from the ensemble average, so [[Ergodicity]] fails.
- **J < 0**: antiferromagnet. Neighbours anti-align; long-range order with M = 0.
- **J = 0**: independent spins. Energy is bounded above, so negative temperature is possible.
- Entropy of a configuration with m up spins is binomial ([[Statistical entropy]]).

## Non-interacting solution
With J = 0 each spin is separate:
```
Z_1 = exp(H/kT) + exp(-H/kT)
M   = tanh(H/kT)
```
The [[Mean-field theory]] reuses this formula with an effective field.

## As a probabilistic model
Wiki note: exp(Σ h_i s_i + Σ J_ij s_i s_j)/Z is the maximum-entropy model of binary data with fixed means and pairwise correlations, also called a Boltzmann machine or pairwise Markov random field **[unverified]** (standard, not in Eastman). Fitting h, J is an inverse problem with an intractable [[Partition function]]; sampling uses [[Markov chain Monte Carlo]].

## Where it appears
- [[Ising model (retina spikes)]]: planned example fitting this model to spike data.
- [[Phase transition]], [[Mean-field theory]].

**Examples**: [[Ising model (retina spikes)]]
**Covered in**: Eastman statmech ch. 6 (Phase transitions)
**Sources**: Eastman, *Introduction to Statistical Mechanics*, github.com/peastman/statmech @cdf566e, `source/phasetransitions.rst`.
**Last updated**: 2026-11-21

---

## Related pages
- [[Boltzmann distribution]] · [[Free energy]] · [[Ergodicity]]
