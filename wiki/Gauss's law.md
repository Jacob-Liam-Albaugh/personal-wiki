---
type: concept
area: em
source-ref: "ECE 311 slides, lect_5, lect_6"
tags: [electromagnetics, pde]
---

# Gauss's law

**Summary**: Flux of D through a closed surface equals enclosed free charge; derived from Coulomb's law with the divergence theorem, and the main tool for fields of symmetric charge.

## Forms
All electrostatic fields in vacuum obey (lect_5, p. 1)
$$\nabla\times E=0,\qquad \nabla\cdot E=\rho_v/\varepsilon_0$$
The curl-free property is checked component by component for a point charge, then by superposition for any static charge set (p. 2). Gauss' law follows from the divergence theorem $\int_v\nabla\cdot A\,dv=\oint_sA\cdot ds$ (p. 6): for a point charge at the centre of a sphere $\oint_sE\cdot ds=Q/\varepsilon_0$, independent of surface shape or where inside the charge sits (p. 8). By superposition:
$$\oint_sE\cdot ds=\frac{Q_{enc}}{\varepsilon_0}$$
In a material the general form uses the displacement field ([[Dielectric polarization]]):
$$\oint_sD\cdot ds=Q_{enc},\qquad \nabla\cdot D=\rho_v$$

> [!example] Is $p=x\,a_R+z\,a_\varphi$ an electrostatic field? (lect_5, p. 3)
> Its curl is nonzero, so no.

> [!example] 1-D uniform charge (lect_5, p. 9)
> If $E$ points along $x$ and $\rho_v$ is uniform then $dE_x/dx=\rho_v/\varepsilon_0$, so $E_x=\rho_vx/\varepsilon_0+E_0$.

## Applications (lect_6)
Procedure: check symmetry, choose a Gaussian surface where the field is constant or perpendicular to it, use symmetry to simplify $E$, evaluate the flux. Three dimensionalities of source (p. 5):
$$E_R=\frac{Q}{4\pi\varepsilon_0R^2}\ \text{(point)},\quad E_\rho=\frac{\rho_\ell}{2\pi\varepsilon_0\rho}\ \text{(line)}$$
$$E_z=\frac{\rho_s}{2\varepsilon_0}\ \text{(sheet)}$$
The field falls as $R^{-2}$, $\rho^{-1}$, $z^{0}$ as the source becomes uniform in 0, 1, 2 dimensions.

Long cylinder, radius $a$, uniform $\rho_v$: $E_\rho=\rho_v\rho/2\varepsilon_0$ for $\rho<a$ and $\rho_va^2/2\varepsilon_0\rho$ for $\rho>a$ (pp. 2-3).

Excess charge on a conductor sits on its surface; $E=0$ inside, so a closed conducting shell shields its interior, as in a Faraday cage (p. 6).

> [!example] Coaxial cable shield (lect_6, pp. 6-7)
> Inner conductor radius $a$ with $\rho_s$: the outer shield (radius $b$) must carry $\rho_s'=-\rho_sa/b$ for no field outside, i.e. $\rho_\ell'=-\rho_\ell$. The charge sits on the shield's inner surface.

**Covered in**: ECE 311 lect_5, lect_6 (Electromagnetics/Lectures Slides/lect_5.pdf, Electromagnetics/Lectures Slides/lect_6.pdf)
**Sources**: ECE 311 lecture slides (Spring 2024, Prof. D. S. Elliott): `Electromagnetics/Lectures Slides/lect_5.pdf`, `Electromagnetics/Lectures Slides/lect_6.pdf`; lecture order from `Electromagnetics/ECE311_Spring2024_Schedule.pdf`. Statements marked Wiki note are standard physics not read in the slides.
**Last updated**: 2026-11-06

---

## Related pages
- [[Electrostatics]]
- [[Coulomb's law]]
- [[Vector calculus for EM]]
- [[Maxwell's equations]]
- [[Ampere's law]]
- [[Dielectric polarization]]
