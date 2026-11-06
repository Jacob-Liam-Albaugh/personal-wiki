---
type: concept
area: em
source-ref: "ECE 311 slides, lect_25, lect_27, lect_28"
tags: [electromagnetics, pde]
---
# Maxwell's equations

**Summary**: The four field equations of classical electromagnetism, built up in ECE 311 from the static laws plus Faraday induction and displacement current.

## Static set (lect_25, p. 1)
$$\nabla\cdot D=\rho_v,\qquad \nabla\times E=0$$
$$\nabla\cdot B=0,\qquad \nabla\times H=J_v$$
Constitutive relations: $D=\varepsilon E$, $B=\mu H$. Charge conservation: $\nabla\cdot J_v=-\partial\rho_v/\partial t$.

## What time variation adds
- Faraday: $\nabla\times E=-\partial B/\partial t$ (EMF $=-d\Phi_M/dt$), see [[Faraday's law]].
- Displacement current: $\nabla\times H=J_v+\partial D/\partial t$ (lect_27).

## Consequences
- Source-free combination gives the wave equation, see [[Electromagnetic wave]].
- Potentials: $B=\nabla\times A$ and $E=-\nabla V-\partial A/\partial t$ (lect_28), see [[Magnetic vector potential]], [[Electric potential]].
- Boundary conditions from the static case still hold (lect_28).
- Phasor form for sinusoidal fields replaces $\partial/\partial t$ by $j\omega$.
- Energy flow: [[Poynting theorem]].

**Sources**: ECE 311 lecture slides (Spring 2024, Prof. D. S. Elliott), [[ECE311 lect_25 - Faraday's law]], [[ECE311 lect_27 - Displacement current and Maxwell's equations]], [[ECE311 lect_28 - Potentials and time-harmonic fields]]. Statements marked Wiki note are standard physics not read in the slides.
**Last updated**: 2026-11-06

---

## Related pages
- [[Electrostatics]]
- [[Magnetostatics]]
- [[Electromagnetic wave]]
- [[Gauss's law]]
- [[Ampere's law]]
- [[Faraday's law]]
- [[Vector calculus for EM]]
- [[Transmission line]]
- [[ECE311 lect_25 - Faraday's law]]
- [[ECE311 lect_27 - Displacement current and Maxwell's equations]]
- [[ECE311 lect_28 - Potentials and time-harmonic fields]]
