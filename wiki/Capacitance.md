---
type: concept
area: em
source-ref: "ECE 311 slides, lect_12, lect_14, lect_15, lect_38"
tags: [electromagnetics]
---

# Capacitance

**Summary**: Charge-to-voltage ratio of a conductor pair and its calculation for plates, spheres and coax, including layered dielectrics.

## Definition
$$C=Q/V,\qquad Q=\rho_sA$$
Find $E$ from [[Gauss's law]] or by solving Laplace's equation ([[Poisson and Laplace equations]]), integrate to $V$, divide. Stored energy $\tfrac12CV^2$ ([[Electrostatic energy]]).

## Examples
Two dielectrics in series between parallel plates: $D_1=D_2=\rho_s$, $V=E_1d_1+E_2d_2$, so
$$\frac1C=\frac{d_1}{\varepsilon_1A}+\frac{d_2}{\varepsilon_2A}$$
Isolated sphere of radius $R_0$ in a medium of permittivity $\varepsilon$ (lect_14, p. 3):
$$C=4\pi\varepsilon R_0$$
Coax of length $L$ and radii $a<b$: $C=2\pi\varepsilon L/\ln(b/a)$, so $C'=2\pi\varepsilon/\ln(b/a)$ per unit length; with a lossy dielectric $RC=\varepsilon/\sigma$ ([[Ohm's law and current density]]).

> [!example] Which fields match across the interface? (lect_14, p. 3)
> $D_1=D_2$ (normal $D$ continuous when no free surface charge), while $E_1\ne E_2$ unless $\varepsilon_1=\varepsilon_2$.

## Transmission lines
Capacitance per unit length gives $C'$ of a [[Transmission line]]: $C'=\varepsilon w/d$ (parallel plate), $2\pi\varepsilon/\ln(b/a)$ (coax), $\pi\varepsilon_0/\cosh^{-1}(d/2a)$ (twin lead).

**Covered in**: ECE 311 lect_12, lect_14, lect_15, lect_38 (courses/ECE 311/Lectures Slides/lect_12.pdf, courses/ECE 311/Lectures Slides/lect_14.pdf, courses/ECE 311/Lectures Slides/lect_15.pdf, courses/ECE 311/Lectures Slides/lect_38.pdf)
**Sources**: ECE 311 lecture slides (Spring 2024, Prof. D. S. Elliott): `courses/ECE 311/Lectures Slides/lect_12.pdf`, `courses/ECE 311/Lectures Slides/lect_14.pdf`, `courses/ECE 311/Lectures Slides/lect_15.pdf`, `courses/ECE 311/Lectures Slides/lect_38.pdf`; lecture order from `courses/ECE 311/ECE311_Spring2024_Schedule.pdf`. Statements marked Wiki note are standard physics not read in the slides.
**Last updated**: 2026-11-06

---

## Related pages
- [[Electrostatics]]
- [[Inductance]]
- [[Poisson and Laplace equations]]
- [[Dielectric polarization]]
- [[Transmission line]]
