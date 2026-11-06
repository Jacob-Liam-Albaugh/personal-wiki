---
type: concept
area: em
source-ref: "ECE 311 slides, lect_18"
tags: [electromagnetics, pde]
---

# Ampere's law

**Summary**: Divergence and curl of B for static fields, the integral law, and its use to find B for symmetric currents; modified by H in materials.

## Forms
No magnetic charges, and (static, vacuum, lect_18 pp. 1-2)
$$\nabla\cdot B=0,\qquad \nabla\times B=\mu_0J_v$$
$$\oint_cB\cdot d\ell=\mu_0I_{enc}$$
In materials, with equivalent currents included ([[Magnetic materials]]):
$$\nabla\times H=J_v$$
Needs the displacement-current term for time variation ([[Maxwell's equations]]).

## Applications
Symmetric currents (wire, sheet) give $B$ directly. Straight wire of radius $a$, uniform current $I$ (p. 2): $B_\varphi=\mu_0I/2\pi\rho$ outside and $\mu_0I\rho/2\pi a^2$ inside.

> [!example] Infinite current sheet (lect_18, Example 18-2, p. 3)
> A rectangular Amperian loop around a sheet of uniform surface current; the field is uniform on each side.

**Covered in**: ECE 311 lect_18 (Electromagnetics/Lectures Slides/lect_18.pdf)
**Sources**: ECE 311 lecture slides (Spring 2024, Prof. D. S. Elliott): `Electromagnetics/Lectures Slides/lect_18.pdf`; lecture order from `Electromagnetics/ECE311_Spring2024_Schedule.pdf`. Statements marked Wiki note are standard physics not read in the slides.
**Last updated**: 2026-11-06

---

## Related pages
- [[Magnetostatics]]
- [[Gauss's law]]
- [[Magnetic materials]]
- [[Biot-Savart law and Lorentz force]]
- [[Vector calculus for EM]]
