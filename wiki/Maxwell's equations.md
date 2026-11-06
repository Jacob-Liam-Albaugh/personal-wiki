---
type: concept
area: em
source-ref: "ECE 311 slides, lect_1, lect_25, lect_27, lect_28"
tags: [electromagnetics, pde]
---

# Maxwell's equations

**Summary**: The four field equations of classical electromagnetism, built up in ECE 311 from the static laws plus Faraday induction and displacement current.

## Overview
The opening lecture's thumbnail sketch of EM (lect_1, p. 3): charges exert forces and produce $E$ (Gauss' law); currents produce $B$ (Ampere's law); charge is conserved; changing $B$ gives $E$ (Faraday); changing $E$ gives $B$ (Ampere with displacement current); coupled $E$ and $B$ describe propagating waves that carry power and information.

## Static set (lect_25, p. 1)
$$\nabla\cdot D=\rho_v,\qquad \nabla\times E=0$$
$$\nabla\cdot B=0,\qquad \nabla\times H=J_v$$
Constitutive relations: $D=\varepsilon E$, $B=\mu H$. Charge conservation: $\nabla\cdot J_v=-\partial\rho_v/\partial t$.

## What time variation adds
- Faraday: $\nabla\times E=-\partial B/\partial t$ (EMF $=-d\Phi_M/dt$), see [[Faraday's law]].
- Displacement current completes the set (lect_27; wiki note, standard form):
$$\nabla\times H=J_v+\frac{\partial D}{\partial t}$$

## Consequences
- Source-free combination gives the wave equation, see [[Electromagnetic wave]].
- Potentials: $B=\nabla\times A$ and $E=-\nabla V-\partial A/\partial t$ (lect_28), see [[Magnetic vector potential]], [[Electric potential]].
- Boundary conditions from the static case still hold for time-varying fields (lect_28, p. 1).
- Phasor form: fields $\propto e^{j\omega t}$ turn $\partial/\partial t$ into $j\omega$; the link to Fourier analysis is in [[Fourier transform]] (wiki note). Phasors are used throughout the wave lectures ([[Electromagnetic wave]]).
- Energy flow: [[Poynting theorem]].
- A good conductor is one with $\sigma/\omega\varepsilon\gg1$ ([[Electromagnetic wave]]).

**Covered in**: ECE 311 lect_1, lect_25, lect_27, lect_28 (courses/ECE 311/Lectures Slides/lect_1.pdf, courses/ECE 311/Lectures Slides/lect_25.pdf, courses/ECE 311/Lectures Slides/lect_27.pdf, courses/ECE 311/Lectures Slides/lect_28.pdf)
**Sources**: ECE 311 lecture slides (Spring 2024, Prof. D. S. Elliott): `courses/ECE 311/Lectures Slides/lect_1.pdf`, `courses/ECE 311/Lectures Slides/lect_25.pdf`, `courses/ECE 311/Lectures Slides/lect_27.pdf`, `courses/ECE 311/Lectures Slides/lect_28.pdf`; lecture order from `courses/ECE 311/ECE311_Spring2024_Schedule.pdf`. Statements marked Wiki note are standard physics not read in the slides.
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
- [[Fourier transform]]
