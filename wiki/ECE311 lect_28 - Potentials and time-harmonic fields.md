---
type: lecture
area: em
source-ref: "ECE 311 lect_28, slides pp. 1-8"
tags: [electromagnetics, pde, signals]
course: ece311
lecture: lect_28
---
# ECE311 lect_28 - Potentials and time-harmonic fields

**Summary**: Retaining A, redefining the scalar potential for time-varying fields, boundary conditions unchanged, and Maxwell's equations for sinusoidal fields with phasors.

**Course**: ECE 311 (Electromagnetics I, Purdue, Spring 2024, Prof. D. S. Elliott) · **Lecture date**: Mar 20 (per the schedule) · **File**: `Electromagnetics/Lectures Slides/lect_28.pdf` (8 slides)

---

## Topics
- Potentials for time-varying fields
- Boundary conditions (same as static)
- Phasor notation and time-harmonic Maxwell's equations

## Key results
$B=\nabla\times A$ still holds because $\nabla\cdot B=0$. Faraday's law gives (p. 1):
$$E=-\nabla V-\frac{\partial A}{\partial t}$$
Boundary conditions from the static case remain valid for time-varying fields (p. 1).
Phasors: fields $\propto e^{j\omega t}$ turn $\partial/\partial t$ into $j\omega$; the link to Fourier analysis is in [[Fourier transform]] (wiki note).

## Examples
> [!example] Time-harmonic notation
> The slides review phasors before the wave lectures; they are used throughout [[ECE311 lect_29 - Wave equation and plane waves]].

**Sources**: `Electromagnetics/Lectures Slides/lect_28.pdf`; lecture order from `Electromagnetics/ECE311_Spring2024_Schedule.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Maxwell's equations]]
- [[Magnetic vector potential]]
- [[Electric potential]]
- [[Fourier transform]]
- [[ECE311 lect_27 - Displacement current and Maxwell's equations]]
- [[ECE311 lect_29 - Wave equation and plane waves]]
