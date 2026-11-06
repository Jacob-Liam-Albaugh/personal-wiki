---
type: lecture
area: em
source-ref: "ECE 311 lect_6, slides pp. 1-7"
tags: [electromagnetics]
course: ece311
lecture: lect_6
---
# ECE311 lect_6 - Applications of Gauss' law

**Summary**: Using Gauss' law with symmetric Gaussian surfaces to get E for a sphere, infinite line, cylinder and infinite plane; conductors and shielding.

**Course**: ECE 311 (Electromagnetics I, Purdue, Spring 2024, Prof. D. S. Elliott) · **Lecture date**: Jan 22 (per the schedule) · **File**: `Electromagnetics/Lectures Slides/lect_6.pdf` (7 slides)

---

## Topics
- Procedure: check symmetry, choose Gaussian surface, use symmetry to simplify $E$, evaluate the flux
- Point/sphere, line, sheet charge fields
- Faraday cage and coaxial cable shielding

## Key results
Three dimensionalities of source (p. 5):
$$E_R=\frac{Q}{4\pi\varepsilon_0R^2}\ \text{(point)},\quad E_\rho=\frac{\rho_\ell}{2\pi\varepsilon_0\rho}\ \text{(line)}$$
$$E_z=\frac{\rho_s}{2\varepsilon_0}\ \text{(sheet)}$$
The field falls as $R^{-2}$, $\rho^{-1}$, $z^{0}$ as the source becomes uniform in 0, 1, 2 dimensions.
Long cylinder, radius $a$, uniform $\rho_v$: $E_\rho=\rho_v\rho/2\varepsilon_0$ for $\rho<a$ and $\rho_va^2/2\varepsilon_0\rho$ for $\rho>a$ (pp. 2-3).
Excess charge on a conductor sits on its surface; $E=0$ inside, so a closed conducting shell shields its interior (p. 6).

## Examples
> [!example] Coaxial cable shield (pp. 6-7)
> Inner conductor radius $a$ with $\rho_s$: the outer shield (radius $b$) must carry $\rho_s'=-\rho_sa/b$ for no field outside, i.e. $\rho_\ell'=-\rho_\ell$. The charge sits on the shield's inner surface.

**Sources**: `Electromagnetics/Lectures Slides/lect_6.pdf`; lecture order from `Electromagnetics/ECE311_Spring2024_Schedule.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Gauss's law]]
- [[Electrostatics]]
- [[Dielectric polarization]]
- [[ECE311 lect_5 - Gauss' law and divergence theorem]]
- [[ECE311 lect_7 - Electric potential and Stokes' theorem]]
