---
type: concept
area: em
source-ref: "ECE 311 slides, lect_20, lect_21, lect_22"
tags: [electromagnetics]
---

# Magnetic materials

**Summary**: Magnetization and equivalent currents, the field H, material types, and magnetic boundary conditions.

## Magnetization
Magnetized material is modelled by equivalent currents from the magnetization $M$ (dipole moment density, from the loop dipole of [[Magnetic vector potential]]):
$$J_{v,eff}=\nabla\times M$$

## The field H (lect_21)
Equivalent currents modify Ampere's law and define $H$; valid in all media for static fields (p. 1):
$$H=\frac{B}{\mu_0}-M\ \ (\mathrm{A/m}),\qquad \nabla\times H=J_v$$
Linear media: $B=\mu H$. A displacement-current term must still be added for time-varying fields ([[Maxwell's equations]]). $B$ is the total field, $M$ the magnetic dipole moment density, and $H$ is sourced by free currents only: the magnetic mirror of $E$, $P$, $D$ ([[Dielectric polarization]]). Types: diamagnetic, paramagnetic, ferromagnetic.

## Boundary conditions (lect_22)
$$B_{1n}=B_{2n},\qquad a_{n2}\times(H_1-H_2)=J_s$$
With no surface current and linear media, $\mu_1H_{1n}=\mu_2H_{2n}$ and $H_{1t}=H_{2t}$, so the angles of field lines on the two sides are related by the permeabilities. True surface currents appear only on perfect conductors; for dielectrics and imperfect conductors $H_t$ is continuous.

> [!example] Refraction of $B$ (lect_22, p. 1)
> The slides derive the relation between $\theta_1$ and $\theta_2$ from the two boundary conditions.

**Covered in**: ECE 311 lect_20, lect_21, lect_22 (courses/ECE 311/Lectures Slides/lect_20.pdf, courses/ECE 311/Lectures Slides/lect_21.pdf, courses/ECE 311/Lectures Slides/lect_22.pdf)
**Sources**: ECE 311 lecture slides (Spring 2024, Prof. D. S. Elliott): `courses/ECE 311/Lectures Slides/lect_20.pdf`, `courses/ECE 311/Lectures Slides/lect_21.pdf`, `courses/ECE 311/Lectures Slides/lect_22.pdf`; lecture order from `courses/ECE 311/ECE311_Spring2024_Schedule.pdf`. Statements marked Wiki note are standard physics not read in the slides.
**Last updated**: 2026-11-06

---

## Related pages
- [[Magnetostatics]]
- [[Ampere's law]]
- [[Inductance]]
- [[Magnetic vector potential]]
