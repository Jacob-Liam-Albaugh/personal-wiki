---
type: lecture
area: em
source-ref: "ECE 311 lect_20, slides pp. 1-8"
tags: [electromagnetics]
course: ece311
lecture: lect_20
---
# ECE311 lect_20 - Magnetic dipole and materials

**Summary**: Vector potential and field of a small current loop (magnetic dipole), and magnetization as a model of magnetic materials.

**Course**: ECE 311 (Electromagnetics I, Purdue, Spring 2024, Prof. D. S. Elliott) · **Lecture date**: Feb 23 (per the schedule) · **File**: `Electromagnetics/Lectures Slides/lect_20.pdf` (8 slides)

---

## Topics
- Far field of a current loop of radius $b$
- Magnetic dipole moment
- Magnetization $M$ and equivalent currents

## Key results
For $R\gg b$ the loop's potential is (p. 3):
$$A=\frac{\mu_0\,m\times a_R}{4\pi R^2},\qquad m=IS\,a_z$$
Its field has the same form as the electric dipole field. Taylor expansion of $|r-r'|^{-1}$ is used (p. 2).
Magnetized material is modelled by equivalent currents, $J_{v,eff}=\nabla\times M$ (stated in lect_21, p. 1).

## Examples
> [!example] Dipole potential derivation (pp. 1-2)
> Choose $\varphi=\pi/2$ by symmetry, expand $|r-r'|^{-1}\approx R^{-1}(1+\frac{b}{R}\sin\theta\sin\varphi')$ and integrate around the loop.

**Sources**: `Electromagnetics/Lectures Slides/lect_20.pdf`; lecture order from `Electromagnetics/ECE311_Spring2024_Schedule.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Magnetic materials]]
- [[Magnetic vector potential]]
- [[Dielectric polarization]]
- [[ECE311 lect_19 - Vector magnetic potential]]
- [[ECE311 lect_21 - Magnetic field H and materials]]
