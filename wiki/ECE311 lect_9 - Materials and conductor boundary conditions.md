---
type: lecture
area: em
source-ref: "ECE 311 lect_9, slides pp. 1-8"
tags: [electromagnetics]
course: ece311
lecture: lect_9
---
# ECE311 lect_9 - Materials and conductor boundary conditions

**Summary**: Conductors versus dielectrics in static fields, boundary conditions for E at a conductor, and polarization of dielectrics.

**Course**: ECE 311 (Electromagnetics I, Purdue, Spring 2024, Prof. D. S. Elliott) · **Lecture date**: Jan 29 (per the schedule) · **File**: `Electromagnetics/Lectures Slides/lect_9.pdf` (8 slides)

---

## Topics
- Conductors, insulators (dielectrics), characterised by conductivity
- Static field inside a conductor is zero; conductor is an equipotential
- Boundary conditions at a conductor surface
- Polarization vector $P$ of a dielectric

## Key results
At the surface of a conductor in the static case (p. 2):
$$E_t=0,\qquad E_n=\rho_s/\varepsilon_0$$
Derived from $\oint E\cdot d\ell=0$ on a thin rectangular loop and Gauss' law on a pillbox (pp. 2-3).
Dielectric: bound charges form dipoles; with $n$ dipoles per volume the polarization is $P=np$ (dipole moment density) (p. 4). The potential of the medium is the sum of dipole potentials.

## Examples
> [!example] Normal field at copper (p. 3)
> $\rho_s=1.0$ nC/m$^2$ gives $E_n=\rho_s/\varepsilon_0\approx113$ V/m (wiki arithmetic).

**Sources**: `Electromagnetics/Lectures Slides/lect_9.pdf`; lecture order from `Electromagnetics/ECE311_Spring2024_Schedule.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Dielectric polarization]]
- [[Electrostatics]]
- [[Gauss's law]]
- [[Capacitance]]
- [[ECE311 lect_8 - Electric potential and dipole]]
- [[ECE311 lect_10 - Displacement field and boundary conditions]]
