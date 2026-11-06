---
type: lecture
area: em
source-ref: "ECE 311 lect_8, slides pp. 1-8"
tags: [electromagnetics]
course: ece311
lecture: lect_8
---
# ECE311 lect_8 - Electric potential and dipole

**Summary**: Potential of discrete and continuous charge distributions, E recovered from V, and the electric dipole.

**Course**: ECE 311 (Electromagnetics I, Purdue, Spring 2024, Prof. D. S. Elliott) · **Lecture date**: Jan 26 (per the schedule) · **File**: `Electromagnetics/Lectures Slides/lect_8.pdf` (8 slides)

---

## Topics
- Potential from several point charges and from line, surface, volume charge
- Finding E as $-\nabla V$ (V must be known as a function of position)
- Spherical shell potential
- Electric dipole

## Key results
Superposition for continuous charge (p. 3):
$$V(r)=\int_v\frac{\rho_v(r')}{4\pi\varepsilon_0|r-r'|}\,dv'$$
A potential known at one point cannot give $E$ because the derivative needs $V(r)$ near that point (p. 2).
Dipole potential (quoted on p. 4 of lect_9): $V=\dfrac{p\cdot a_R}{4\pi\varepsilon_0R^2}$.

## Examples
> [!example] Finite line charge (pp. 3-4)
> The potential is a $\int d\xi/\sqrt{x^2+\xi^2}$ integral, and replacing $x\to\rho$ gives it off the $x$-$z$ plane.

> [!example] Shell of charge $q$, radius $a$ (p. 5)
> Integrating the shell gives $V=q/4\pi\varepsilon_0R$ outside and constant $q/4\pi\varepsilon_0a$ inside (slide p. 6 of the PDF, checked: $E=0$ inside, $E=q/4\pi\varepsilon_0R^2$ outside).

**Sources**: `Electromagnetics/Lectures Slides/lect_8.pdf`; lecture order from `Electromagnetics/ECE311_Spring2024_Schedule.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Electric potential]]
- [[Electrostatics]]
- [[Dielectric polarization]]
- [[Magnetic materials]]
- [[ECE311 lect_7 - Electric potential and Stokes' theorem]]
- [[ECE311 lect_9 - Materials and conductor boundary conditions]]
