---
type: lecture
area: em
source-ref: "ECE 311 lect_5, slides pp. 1-10"
tags: [electromagnetics, pde]
course: ece311
lecture: lect_5
---
# ECE311 lect_5 - Gauss' law and divergence theorem

**Summary**: Shows that static fields in vacuum obey curl E = 0 and div E = rho/eps0, deriving Gauss' law from Coulomb's law with the divergence theorem.

**Course**: ECE 311 (Electromagnetics I, Purdue, Spring 2024, Prof. D. S. Elliott) · **Lecture date**: Jan 19 (per the schedule) · **File**: `Electromagnetics/Lectures Slides/lect_5.pdf` (10 slides)

---

## Topics
- Vector surface integrals (flux)
- Divergence theorem
- Integral and differential Gauss' law
- $\nabla\times E=0$ for static fields

## Key results
All electrostatic fields in vacuum obey (p. 1):
$$\nabla\times E=0,\qquad \nabla\cdot E=\rho_v/\varepsilon_0$$
Divergence theorem (p. 6): $\int_v\nabla\cdot A\,dv=\oint_s A\cdot ds$.
For a point charge at the centre of a sphere, $\oint_sE\cdot ds=Q/\varepsilon_0$, independent of surface shape or where inside the charge sits (p. 8). By superposition:
$$\oint_sE\cdot ds=\frac{Q_{enc}}{\varepsilon_0}$$
Curl-free: checked component by component for a point charge, then by superposition for any static charge set (p. 2).

## Examples
> [!example] Is $p=x\,a_R+z\,a_\varphi$ an electrostatic field? (p. 3)
> Its curl is nonzero, so no.

> [!example] 1-D uniform charge (p. 9)
> If $E$ points along $x$ and $\rho_v$ is uniform then $dE_x/dx=\rho_v/\varepsilon_0$, so $E_x=\rho_vx/\varepsilon_0+E_0$.

> [!example] Check of the divergence theorem (pp. 6-7)
> $A=a_xx$ over a cube of side $a$: both sides equal $a^3$. Over a sphere of radius $a$: $\frac{4\pi}{3}a^3$.

**Sources**: `Electromagnetics/Lectures Slides/lect_5.pdf`; lecture order from `Electromagnetics/ECE311_Spring2024_Schedule.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Gauss's law]]
- [[Vector calculus for EM]]
- [[Electrostatics]]
- [[Maxwell's equations]]
- [[Coulomb's law]]
- [[ECE311 lect_4 - Coulomb's law]]
- [[ECE311 lect_6 - Applications of Gauss' law]]
