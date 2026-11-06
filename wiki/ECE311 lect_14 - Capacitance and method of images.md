---
type: lecture
area: em
source-ref: "ECE 311 lect_14, slides pp. 1-10"
tags: [electromagnetics, pde]
course: ece311
lecture: lect_14
---
# ECE311 lect_14 - Capacitance and method of images

**Summary**: More capacitance calculations (two dielectrics, isolated sphere) and the method of images for a charge near a conductor.

**Course**: ECE 311 (Electromagnetics I, Purdue, Spring 2024, Prof. D. S. Elliott) · **Lecture date**: Feb 9 (per the schedule) · **File**: `Electromagnetics/Lectures Slides/lect_14.pdf` (10 slides)

---

## Topics
- Capacitance of parallel plates with two dielectric layers
- Isolated spherical conductor
- Method of images

## Key results
Capacitance (p. 2): $C=Q/V$ with $Q=\rho_sA$.
Two dielectrics in series: $D_1=D_2=\rho_s$, $V=E_1d_1+E_2d_2$, so
$$\frac1C=\frac{d_1}{\varepsilon_1A}+\frac{d_2}{\varepsilon_2A}$$
Isolated sphere of radius $R_0$ in a medium of permittivity $\varepsilon$ (p. 3): $C=4\pi\varepsilon R_0$.

## Examples
> [!example] Which fields match across the interface? (p. 3)
> $D_1=D_2$ (normal $D$ continuous when no free surface charge), while $E_1\ne E_2$ unless $\varepsilon_1=\varepsilon_2$.

**Sources**: `Electromagnetics/Lectures Slides/lect_14.pdf`; lecture order from `Electromagnetics/ECE311_Spring2024_Schedule.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Capacitance]]
- [[Poisson and Laplace equations]]
- [[Dielectric polarization]]
- [[ECE311 lect_12 - Poisson and Laplace equations]]
- [[ECE311 lect_15 - Current density and Ohm's law]]
