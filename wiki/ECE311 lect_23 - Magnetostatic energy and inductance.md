---
type: lecture
area: em
source-ref: "ECE 311 lect_23, slides pp. 1-8"
tags: [electromagnetics]
course: ece311
lecture: lect_23
---
# ECE311 lect_23 - Magnetostatic energy and inductance

**Summary**: Energy and energy density stored in a magnetic field, and inductance computed from stored energy or flux linkage for common geometries.

**Course**: ECE 311 (Electromagnetics I, Purdue, Spring 2024, Prof. D. S. Elliott) · **Lecture date**: Mar 1 (per the schedule) · **File**: `Electromagnetics/Lectures Slides/lect_23.pdf` (8 slides)

---

## Topics
- Work to establish a current distribution
- Flux linkage of current filaments
- Inductance of standard configurations

## Key results
Circuit analogy (p. 1): $W_m=\tfrac12LI^2$. In field terms the energy density is $w_m=\tfrac12H\cdot B$ (quoted in lect_34).
Flux linkage of one filament (p. 2): $\Phi_k=\int B\cdot ds_k=\oint A\cdot d\ell_k$.
Wiki note: $L$ follows from $W_m=\tfrac12LI^2$ or $L=\Phi/I$.

## Examples
> [!example] Inductance from flux
> Solenoid (Ex. 23-1, PDF p. 5): $W_m'=\tfrac12\mu n^2I^2s$, so $L'=\mu n^2s$ (agrees with Ex. 22-2). Toroid, rectangular section of thickness $h$ (Ex. 23-2, PDF p. 5): $H_\varphi=NI/2\pi\rho$, giving $L=\dfrac{\mu N^2h}{2\pi}\ln\dfrac ba$. Coax is Ex. 23-3 (PDF p. 6), not read here.

**Sources**: `Electromagnetics/Lectures Slides/lect_23.pdf`; lecture order from `Electromagnetics/ECE311_Spring2024_Schedule.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Inductance]]
- [[Electrostatic energy]]
- [[Faraday's law]]
- [[ECE311 lect_22 - Magnetic boundary conditions and inductance]]
- [[ECE311 lect_24 - Magnetic forces and torques]]
