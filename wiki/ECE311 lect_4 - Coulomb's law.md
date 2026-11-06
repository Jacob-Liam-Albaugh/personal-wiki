---
type: lecture
area: em
source-ref: "ECE 311 lect_4, slides pp. 1-10"
tags: [electromagnetics]
course: ece311
lecture: lect_4
---
# ECE311 lect_4 - Coulomb's law

**Summary**: Coulomb's force law between point charges, the electric field defined from it, superposition, and the field of continuous charge distributions (worked for a charged spherical shell).

**Course**: ECE 311 (Electromagnetics I, Purdue, Spring 2024, Prof. D. S. Elliott) · **Lecture date**: Jan 17 (per the schedule) · **File**: `Electromagnetics/Lectures Slides/lect_4.pdf` (10 slides)

---

## Topics
- Coulomb force and permittivity of free space
- Electric field of a point charge, superposition
- Continuous line, surface and volume charge integrals
- Primed/unprimed notation: primed = source point, unprimed = field point

## Key results
Force on $q_2$ at $r_2$ from $q_1$ at $r_1$ (p. 2), with $\varepsilon_0=8.854$ pF/m:
$$F_{12}=\frac{q_1q_2\,(r_2-r_1)}{4\pi\varepsilon_0|r_2-r_1|^3}$$
Field (p. 3): $E(r)=\dfrac{q_1(r-r')}{4\pi\varepsilon_0|r-r'|^3}$ and $F=qE$.
Continuous charge (p. 6):
$$E(r)=\int_v\frac{\rho_v(r')\,(r-r')}{4\pi\varepsilon_0|r-r'|^3}\,dv'$$
with $\rho_s\,ds'$ or $\rho_\ell\,d\ell'$ in place of $\rho_v\,dv'$. Note $\rho_v(r')$ is a function of $r'$, not density times $r'$ (p. 6).
Shell result (pp. 7-9): $E=0$ inside a uniform spherical shell and $E=Q/(4\pi\varepsilon_0R^2)$ outside, with $Q=4\pi a^2\rho_s$. Uniform sphere (Ex. 4-4): $E_R=\rho_vR/3\varepsilon_0$ inside, $\rho_va^3/3\varepsilon_0R^2$ outside.

## Examples
> [!example] Field of an electron (p. 4)
> An electron at $r'=(2,0,0)$ nm gives, at $r=(1,1,0)$ nm, $E\approx5.09\times10^{8}(1,-1,0)$ V/m (checked on the slide image, p. 4).

> [!example] Three charges, superposition (pp. 4-5)
> Fields of three charges at $(2,3,0)$ nm are added vectorially to give $\frac{e}{4\pi\varepsilon_0}(-0.3\,a_x+0.4\,a_y)\ \mathrm{nm^{-2}}$.

**Sources**: `Electromagnetics/Lectures Slides/lect_4.pdf`; lecture order from `Electromagnetics/ECE311_Spring2024_Schedule.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Coulomb's law]]
- [[Electrostatics]]
- [[Gauss's law]]
- [[ECE311 lect_6 - Applications of Gauss' law]]
- [[ECE311 lect_3 - Gradient divergence curl]]
- [[ECE311 lect_5 - Gauss' law and divergence theorem]]
