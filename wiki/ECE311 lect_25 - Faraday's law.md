---
type: lecture
area: em
source-ref: "ECE 311 lect_25, slides pp. 1-9"
tags: [electromagnetics, pde]
course: ece311
lecture: lect_25
---
# ECE311 lect_25 - Faraday's law

**Summary**: Time-varying magnetic flux induces an EMF; the static equations are incomplete; transformers and alternators.

**Course**: ECE 311 (Electromagnetics I, Purdue, Spring 2024, Prof. D. S. Elliott) · **Lecture date**: Mar 6 (per the schedule) · **File**: `Electromagnetics/Lectures Slides/lect_25.pdf` (9 slides)

---

## Topics
- Summary of the static equations and constitutive relations
- Faraday's law and EMF
- Moving magnets, transformers, alternators

## Key results
The static set (p. 1): $\nabla\cdot D=\rho_v$, $\nabla\times E=0$, $\nabla\cdot B=0$, $\nabla\times H=J_v$, with $D=\varepsilon E$, $B=\mu H$, and charge conservation $\nabla\cdot J_v=-\partial\rho_v/\partial t$.
EMF induced by a changing flux:
$$\mathcal E=-\frac{d\Phi_M}{dt}$$
Reversing a magnet reverses $\mathcal E$; approach and retreat give opposite signs; a stationary magnet gives zero (p. 1).

## Examples
> [!example] Static equations not complete
> $\nabla\times E=0$ cannot hold when $B$ changes, motivating $\nabla\times E=-\partial B/\partial t$.

**Sources**: `Electromagnetics/Lectures Slides/lect_25.pdf`; lecture order from `Electromagnetics/ECE311_Spring2024_Schedule.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Faraday's law]]
- [[Maxwell's equations]]
- [[Electrostatics]]
- [[Magnetostatics]]
- [[ECE311 lect_24 - Magnetic forces and torques]]
- [[ECE311 lect_27 - Displacement current and Maxwell's equations]]
