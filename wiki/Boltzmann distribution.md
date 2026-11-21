---
type: definition
area: ift
areas: [ift, stochastic]
source-ref: "Eastman, Introduction to Statistical Mechanics, ch. 2 (statisticaldescription.rst)"
tags: [ift, mechanics, bayesian, sampling]
---

# Boltzmann distribution

> [!definition] Canonical (Maxwell-Boltzmann) distribution
> A system A in contact with a heat bath B at temperature T is in microstate s with
> ```
> p(s) = exp(-E(s)/kT) / Z
> Z = Σ_s exp(-E(s)/kT)
> β = 1/kT
> ```
> (source: Eastman, *Introduction to Statistical Mechanics*, github.com/peastman/statmech @cdf566e, `source/statisticaldescription.rst`)

**Intuition**: the bath has far more states than the system. Giving the system energy E costs the bath a factor exp(-βE) in available states, so high-energy states are exponentially rare.

## Derivation (ch. 2)
Equal a priori probabilities: in equilibrium every microstate of the isolated whole is equally likely. Write the total as A plus bath B:
```
E_T ≈ E_A + E_B
Ω_T = Ω_A Ω_B
log Ω_B(E_B) ≈ α + β E_B
⇒ p(s_A) ∝ Ω_B(E_T - E_A)
         ∝ exp(-β E_A)
β = ∂ log Ω_B / ∂E
```
Taylor-expanding log Ω, not Ω, is the key step: log Ω is smooth, Ω grows like a huge power of E ([[Statistical entropy]]).

## Other ensembles and potentials
Letting the bath also exchange volume or particles adds conjugate terms. Defining
```
P = kT ∂log Ω_B/∂V
μ = -kT ∂log Ω_B/∂N
```
the probability of a system state becomes p = exp(-Φ/kT)/Z with Φ the matching energy-like quantity:

| Ensemble | Exchanged | Φ for a microstate |
|---|---|---|
| microcanonical | nothing | (all states equal) |
| canonical | energy | E |
| isothermal-isobaric | energy, volume | E + PV |
| grand canonical | energy, particles | E − μN |

Summing over the microstates of a macrostate turns these into the [[Free energy]] potentials (A, G, Φ_G).

## IFT dictionary
Wiki note: any density can be written p(φ) = exp(−H[φ])/Z with H = −log p. That is a Boltzmann distribution at kT = 1 with "energy" H. IFT's information Hamiltonian ([[Information field theory]]) is exactly this energy, and the evidence is [[Partition function|Z]]. Tempered posteriors scale H by β ≠ 1. **[unverified]**: standard identification, not stated by Eastman.

## Quantum note
Eastman separates two kinds of probability: the ensemble probability of a wavefunction, and the Born-rule probability of a measurement outcome given the wavefunction (ch. 2).

## Where it appears
- [[Langevin dynamics]] and [[Hamiltonian Monte Carlo]] target exp(−U) as stationary law.
- [[Equipartition theorem]], [[Ising model]], [[Mean-field theory]] are all computed from it.
- [[Ising model (retina spikes)]]: a fitted Boltzmann distribution over spike patterns.

**Covered in**: Eastman statmech ch. 2 (The statistical description of physical systems); Enßlin IT & IFT ch. 3 §3.3 (pp. 55-57)
**Sources**: Eastman, *Introduction to Statistical Mechanics*, github.com/peastman/statmech @cdf566e, `source/statisticaldescription.rst`, `text_books/Machine Learning & Statistics/Ensslin - Information Theory & Information Field Theory.pdf`.
**Last updated**: 2026-11-21

## MaxEnt connection (Enßlin)
The [[Maximum entropy principle]] gives $P(s\mid I_B)=P(s\mid I_0)\,e^{\mu^\dagger f(s)}/\mathcal Z(\mu)$ for a message fixing $\langle f\rangle$ (source: Ensslin - Information Theory & Information Field Theory.pdf, §3.3.3, eqs. 131-135, pp. 55-57; PDF page): the Boltzmann form with the prior as reference measure and $\mu$ as inverse temperature-like multipliers.

---

## Related pages
- [[Partition function]] · [[Statistical entropy]] · [[Free energy]] · [[Ergodicity]]
- [[Energy functional]] · [[Information field theory]] · [[Markov chain Monte Carlo]]
- [[Maximum entropy principle]]
