---
type: lecture
area: em
source-ref: "ECE 311 lect_11, slides pp. 1-8"
tags: [electromagnetics]
course: ece311
lecture: lect_11
---
# ECE311 lect_11 - Electrostatic energy and forces

**Summary**: Energy stored when assembling charges, its expression in terms of the fields, energy density, and forces by virtual displacement.

**Course**: ECE 311 (Electromagnetics I, Purdue, Spring 2024, Prof. D. S. Elliott) · **Lecture date**: Feb 2 (per the schedule) · **File**: `Electromagnetics/Lectures Slides/lect_11.pdf` (8 slides)

---

## Topics
- Work to assemble point charges
- Energy of a continuous distribution
- Energy in terms of D and E; energy density
- Force from virtual displacement

## Key results
For a continuous distribution (p. 2):
$$W_e=\tfrac12\int_v\rho_vV\,dv$$
Using $\rho_v=\nabla\cdot D$ and $E=-\nabla V$ (p. 3):
$$W_e=\tfrac12\int_vD\cdot E\,dv,\qquad w_e=\tfrac12D\cdot E$$
Energy density later gives the energy carried by EM waves (p. 3).

## Examples
> [!example] Uniformly charged sphere (pp. 2-4)
> $E_R$ inside and outside is found with Gauss' law, then $V(R)$, then $W_e$; the slide result (PDF p. 4, checked) is $W_e=\dfrac{4\pi\rho_v^2a^5}{15\varepsilon_0}$.

> [!example] Coaxial conductors at potential $V_0$ (p. 4)
> Gauss' law for $D_\rho$, then integrate $w_e$ over the volume.

**Sources**: `Electromagnetics/Lectures Slides/lect_11.pdf`; lecture order from `Electromagnetics/ECE311_Spring2024_Schedule.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Electrostatic energy]]
- [[Capacitance]]
- [[Electrostatics]]
- [[Poynting theorem]]
- [[ECE311 lect_10 - Displacement field and boundary conditions]]
- [[ECE311 lect_12 - Poisson and Laplace equations]]
