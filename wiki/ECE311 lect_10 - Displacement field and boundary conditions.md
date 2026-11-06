---
type: lecture
area: em
source-ref: "ECE 311 lect_10, slides pp. 1-8"
tags: [electromagnetics]
course: ece311
lecture: lect_10
---
# ECE311 lect_10 - Displacement field and boundary conditions

**Summary**: Polarization charge enters Gauss' law, leading to the displacement field D; boundary conditions for E and D at material interfaces; simple dielectrics.

**Course**: ECE 311 (Electromagnetics I, Purdue, Spring 2024, Prof. D. S. Elliott) · **Lecture date**: Jan 31 (per the schedule) · **File**: `Electromagnetics/Lectures Slides/lect_10.pdf` (8 slides)

---

## Topics
- Effective (bound) charge density $\rho_{v,eff}=-\nabla\cdot P$
- Displacement field D and general Gauss' law
- Boundary conditions for E and D
- Simple (linear, isotropic, homogeneous) media, susceptibility and permittivity

## Key results
Definition and generalised Gauss' law (p. 2), valid in all media:
$$D=\varepsilon_0E+P,\qquad \nabla\cdot D=\rho_v$$
$$\oint_sD\cdot ds=Q_{enc}\ \text{(free charge)}$$
Boundary conditions at an interface (p. 3):
$$E_{1t}=E_{2t},\qquad D_{2n}-D_{1n}=\rho_s$$
Linear media: $P=\varepsilon_0\chi_eE$, hence $D=\varepsilon E$ with $\varepsilon=\varepsilon_0(1+\chi_e)$ and $\varepsilon_r=1+\chi_e$ (p. 3).

## Examples
> [!example] Meaning of E, D, P (p. 2)
> $E$ is the total field (force $F=qE$); $P$ is dipole moment density; $D/\varepsilon_0$ is the field of the free charge only in limited cases.

**Sources**: `Electromagnetics/Lectures Slides/lect_10.pdf`; lecture order from `Electromagnetics/ECE311_Spring2024_Schedule.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Dielectric polarization]]
- [[Gauss's law]]
- [[Maxwell's equations]]
- [[Capacitance]]
- [[ECE311 lect_9 - Materials and conductor boundary conditions]]
- [[ECE311 lect_11 - Electrostatic energy and forces]]
