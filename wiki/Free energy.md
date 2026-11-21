---
type: concept
area: ift
areas: [ift, bayesian, stochastic]
source-ref: "Eastman, Introduction to Statistical Mechanics, ch. 2, 4, 5, 6"
tags: [ift, mechanics, bayesian]
---

# Free energy

**Summary**: Thermodynamic potentials are minus log probabilities of macrostates: p ∝ exp(−Φ/kT). The stable state minimises the potential, and the Helmholtz free energy is the maximum extractable work. In inference the same quantity is −log evidence, which variational inference bounds.

## Enßlin's Gibbs free energy (ch. 11-12)
In IFT the free energy of the tempered posterior is $F=-T\ln Z$ with $Z$ the evidence, and the Legendre transform to the Gibbs free energy $G=U-TS_B$ over a Gaussian ansatz is the objective of [[Gibbs free energy]]; at $T=1$ it equals $D_{\rm KL}$ of the ansatz from the posterior up to the constant $-\ln P(d)$. See also [[Free theory (IFT)]] and [[Interacting information field theory]] (generating functional, $\ln Z$ as sum of connected diagrams).

(source: Ensslin - Information Theory & Information Field Theory.pdf, pp. 133-137; p. = PDF page)

**Covered in**: Eastman statmech ch. 2 (The statistical description of physical systems), ch. 4 (Interpretation), ch. 5 (Thermodynamics), ch. 6 (Phase transitions); Enßlin IT & IFT ch. 11-12 (pp. 129-138)
**Sources**: Eastman, *Introduction to Statistical Mechanics*, github.com/peastman/statmech @cdf566e, `source/statisticaldescription.rst`, `source/interpretation.rst`, `source/thermodynamics.rst`, `source/phasetransitions.rst`, `text_books/Machine Learning & Statistics/Ensslin - Information Theory & Information Field Theory.pdf`.
**Last updated**: 2026-11-21

---

## The potentials (ch. 2)
Summing the [[Boltzmann distribution]] over the microstates of a macrostate gives p = exp(−Φ/kT)/Z with
```
H   = E + PV          enthalpy
A   = E - TS          Helmholtz
G   = E + PV - TS     Gibbs
Φ_G = E - μN - TS     grand potential
```
Which one applies depends on what the system exchanges with its bath.

## What a potential means (ch. 4)
- It measures probability: lower Φ, more likely macrostate.
- It mixes bath and system quantities. Written carefully,
  ```
  G_A = E_A + P_B V_A - T_B S_A
  ```
  T and P belong to the bath; E, V, S belong to the system.
- If the macrostate is a distribution rather than a fixed value, use averages: G = ⟨E⟩ + P⟨V⟩ − T⟨S⟩.
- Equilibrium minimises Φ. Setting ∂G/∂V_A = 0 gives −∂E_A/∂V_A = P_B − P_A: the system's own pressure matches the bath's.

## Maximum work (ch. 5)
Extracting work while in contact with a bath at T, the most you can get is
```
W_max = E - T(S - S_0)
```
the Helmholtz free energy: energy minus the part that must be dumped as heat to keep total entropy from falling.

## Phases (ch. 6)
The stable phase is the one with lowest free energy; a [[Phase transition]] happens where two phases' free energies cross. Local minima are metastable phases.

## IFT and variational inference
Wiki note, standard identifications **[unverified]** (not in Eastman):
- With kT = 1 and energy H = −log p(d, φ), the free energy is F = −log Z = −log p(d).
- For any q(φ):
  ```
  F_q = E_q[H] - S[q]
      = -ELBO(q)
      = F + KL(q || p(φ|d))
  ```
  so F_q ≥ F, with equality at the true posterior. Minimising variational free energy is the Gibbs variational principle, the inference version of "equilibrium minimises Φ".
- Restricting q to a product gives [[Mean-field theory]] / mean-field VI.
- The free energy as a function of hyperparameters is the negative log marginal likelihood used for evidence-based tuning (cf. [[Nested SGLD]]).

## Related pages
- [[Partition function]] · [[Statistical entropy]] · [[Variational inference]] · [[ELBO]] · [[KL divergence]]
- [[Information field theory]] · [[Laplace approximation]]
- [[Gibbs free energy]] · [[Free theory (IFT)]] · [[Interacting information field theory]]
