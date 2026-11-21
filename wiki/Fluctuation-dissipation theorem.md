---
type: theorem
area: stochastic
areas: [stochastic, ift]
source-ref: "Eastman, Introduction to Statistical Mechanics, ch. 7 (friction.rst)"
tags: [sampling, mechanics, ift]
---

# Fluctuation-dissipation theorem

> [!theorem] Friction fixes the noise
> For the Langevin equation m ẍ = −γẋ + R(t), with R short-correlated (time τ ≪ m/γ), equilibrium at temperature T requires
> ```
> 2 γ k T = ∫ ⟨R(0) R(s)⟩ ds
> ```
> integrated over all s.
> (source: Eastman, *Introduction to Statistical Mechanics*, github.com/peastman/statmech @cdf566e, `source/friction.rst`)

**Intuition**: the same molecular collisions both slow the particle down (friction γ) and kick it about (noise R). If they did not balance, the particle would heat up or cool down forever.

## Langevin equation (ch. 7)
Assumptions on the random force: ⟨R⟩ = 0; R independent of x; correlated only over a short time τ; stationary. By the [[Central limit theorem]], ∫R dt over many τ is Gaussian with width ∝ √t, so R behaves as white noise (a [[Wiener process]] increment).

## Derivation
Solving the linear ODE for the velocity:
```
ẋ(t) = ẋ(0) e^{-γt/m}
     + (1/m) ∫ e^{-γ(t-t')/m} R(t') dt'
```
Demand that ⟨m ẋ²⟩ stays at kT ([[Equipartition theorem]]). This gives
```
2γkT = ∫_0^∞ e^{-γs/m} ⟨R(0)R(s)⟩ ds   (×2, symmetric)
```
For τ ≪ m/γ the exponential is 1 wherever the correlation is non-zero, giving the result above with the integral over all s.

## Diffusion (Einstein 1905, Langevin 1908)
With equipartition, at long times
```
d⟨x²⟩/dt → 2kT/γ
⟨x²⟩ = (2kT/γ) t
```
so the diffusion coefficient is D = kT/γ ([[Brownian movement (Einstein 1905)]]).

## Sampling link
Wiki note **[unverified]**: overdamped Langevin dynamics dθ = −∇U dt + √2 dW is this theorem at kT = 1, γ = 1. The √2 is fixed by FDT so that exp(−U) is stationary ([[Langevin dynamics]]). In [[SGLD]] the minibatch gradient noise adds extra fluctuation without extra friction, which is why the injected noise must dominate (step size → 0) for the right stationary law. The [[Ornstein-Uhlenbeck process]] is the velocity process here with R white.

## Where it appears
- [[Langevin dynamics]], [[Ornstein-Uhlenbeck process]], [[Brownian motion]].
- [[Generalised Langevin equation]]: memory kernel version, where FDT ties the kernel to the noise correlation.

**Covered in**: Eastman statmech ch. 7 (Friction and dissipation)
**Sources**: Eastman, *Introduction to Statistical Mechanics*, github.com/peastman/statmech @cdf566e, `source/friction.rst`.
**Last updated**: 2026-11-21

---

## Related pages
- [[Stochastic differential equation]] · [[Fokker-Planck equation]] · [[Wiener process]]
