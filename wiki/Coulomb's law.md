---
type: concept
area: em
source-ref: "ECE 311 slides, lect_4"
tags: [electromagnetics]
---

# Coulomb's law

**Summary**: Force and field of point charges and of continuous charge distributions, with superposition.

## Statement
Force on $q_2$ at $r_2$ from $q_1$ at $r_1$ (p. 2), with $\varepsilon_0=8.854$ pF/m:
$$F_{12}=\frac{q_1q_2\,(r_2-r_1)}{4\pi\varepsilon_0|r_2-r_1|^3}$$
Field (p. 3): $E(r)=\dfrac{q_1(r-r')}{4\pi\varepsilon_0|r-r'|^3}$ and $F=qE$. Primed coordinates mark the source point, unprimed the field point.

## Continuous charge
Superposition gives (p. 6)
$$E(r)=\int_v\frac{\rho_v(r')\,(r-r')}{4\pi\varepsilon_0|r-r'|^3}\,dv'$$
with $\rho_s\,ds'$ or $\rho_\ell\,d\ell'$ in place of $\rho_v\,dv'$. Note $\rho_v(r')$ is a function of $r'$, not density times $r'$.

Charged spherical shell (pp. 7-9): $E=0$ inside a uniform shell and $E=Q/(4\pi\varepsilon_0R^2)$ outside, with $Q=4\pi a^2\rho_s$. Uniform sphere (Ex. 4-4): $E_R=\rho_vR/3\varepsilon_0$ inside, $\rho_va^3/3\varepsilon_0R^2$ outside.

> [!example] Field of an electron (p. 4)
> An electron at $r'=(2,0,0)$ nm gives, at $r=(1,1,0)$ nm, $E\approx5.09\times10^{8}(1,-1,0)$ V/m (checked on the slide image).

> [!example] Three charges, superposition (pp. 4-5)
> Fields of three charges at $(2,3,0)$ nm are added vectorially to give $\frac{e}{4\pi\varepsilon_0}(-0.3\,a_x+0.4\,a_y)\ \mathrm{nm^{-2}}$.

## Use
Direct integration is practical only for simple geometry; symmetry problems use [[Gauss's law]], others use [[Electric potential]].

**Covered in**: ECE 311 lect_4 (courses/ECE 311/Lectures Slides/lect_4.pdf)
**Sources**: ECE 311 lecture slides (Spring 2024, Prof. D. S. Elliott): `courses/ECE 311/Lectures Slides/lect_4.pdf`; lecture order from `courses/ECE 311/ECE311_Spring2024_Schedule.pdf`. Statements marked Wiki note are standard physics not read in the slides.
**Last updated**: 2026-11-06

---

## Related pages
- [[Electrostatics]]
- [[Gauss's law]]
- [[Electric potential]]
- [[Vector calculus for EM]]
