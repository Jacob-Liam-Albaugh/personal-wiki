---
type: lecture
area: em
source-ref: "ECE 311 lect_12, slides pp. 1-9"
tags: [electromagnetics, pde]
course: ece311
lecture: lect_12
---
# ECE311 lect_12 - Poisson and Laplace equations

**Summary**: Combining Gauss' law with E = -grad V gives Poisson's equation, Laplace's equation in charge-free regions; 1-D solutions with boundary conditions; and the start of capacitance.

**Course**: ECE 311 (Electromagnetics I, Purdue, Spring 2024, Prof. D. S. Elliott) · **Lecture date**: Feb 5 (per the schedule) · **File**: `Electromagnetics/Lectures Slides/lect_12.pdf` (9 slides)

---

## Topics
- Poisson and Laplace equations in three coordinate systems
- Properties of solutions of Laplace's equation
- 1-D solutions between parallel plates, including two dielectrics
- Capacitance as $Q/V$

## Key results
For homogeneous media (p. 2):
$$\nabla^2V=-\rho_v/\varepsilon$$
$$\nabla^2V=0\quad(\rho_v=0)$$
Properties of $V$ with $\nabla^2V=0$ (p. 3): no local maxima or minima; $V$ inside a closed surface lies between its min and max on the surface; the value at a sphere's centre equals the surface average.
Parallel plates: $V(y)=Ay+B$, with $V(0)=0,\ V(d)=V_0$ giving $V=V_0y/d$ (p. 3).

## Examples
> [!example] Two charge-free dielectric layers (p. 4)
> $V$ is piecewise linear, with constants fixed by $V(0)=0$, $V(d_1+d_2)=V_0$ and continuity of $V$ and $D_n$ at the interface.

**Sources**: `Electromagnetics/Lectures Slides/lect_12.pdf`; lecture order from `Electromagnetics/ECE311_Spring2024_Schedule.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Poisson and Laplace equations]]
- [[Capacitance]]
- [[Electrostatics]]
- [[PINN]]
- [[ECE311 lect_11 - Electrostatic energy and forces]]
- [[ECE311 lect_14 - Capacitance and method of images]]
