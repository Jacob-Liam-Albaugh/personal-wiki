---
type: concept
area: em
source-ref: "ECE 311 slides, lect_12, lect_14"
tags: [electromagnetics, pde]
---

# Poisson and Laplace equations

**Summary**: Boundary-value problems for the potential: Poisson's equation, Laplace's equation in charge-free regions, 1-D solutions, and the method of images.

## Equations
Combining Gauss' law with $E=-\nabla V$ for homogeneous media (lect_12, p. 2):
$$\nabla^2V=-\rho_v/\varepsilon$$
$$\nabla^2V=0\quad(\rho_v=0)$$
Written in rectangular, cylindrical and spherical coordinates ([[Vector calculus for EM]]). Solutions are unique given boundary conditions. Properties of $V$ with $\nabla^2V=0$ (p. 3): no local maxima or minima; $V$ inside a closed surface lies between its min and max on the surface; the value at a sphere's centre equals the surface average.

## 1-D solutions
Parallel plates: $V(y)=Ay+B$, with $V(0)=0,\ V(d)=V_0$ giving $V=V_0y/d$ (p. 3). Capacitance follows as $Q/V$ ([[Capacitance]]).

> [!example] Two charge-free dielectric layers (lect_12, p. 4)
> $V$ is piecewise linear, with constants fixed by $V(0)=0$, $V(d_1+d_2)=V_0$ and continuity of $V$ and $D_n$ at the interface.

## Method of images
A charge near a grounded conductor is replaced by an image charge so that the boundary condition ($V=$ const on the conductor) holds on its surface (lect_14).

## Wiki note
[[PINN]] training solves the same PDE with a network ansatz.

**Covered in**: ECE 311 lect_12, lect_14 (Electromagnetics/Lectures Slides/lect_12.pdf, Electromagnetics/Lectures Slides/lect_14.pdf)
**Sources**: ECE 311 lecture slides (Spring 2024, Prof. D. S. Elliott): `Electromagnetics/Lectures Slides/lect_12.pdf`, `Electromagnetics/Lectures Slides/lect_14.pdf`; lecture order from `Electromagnetics/ECE311_Spring2024_Schedule.pdf`. Statements marked Wiki note are standard physics not read in the slides.
**Last updated**: 2026-11-06

---

## Related pages
- [[Electrostatics]]
- [[Electric potential]]
- [[Capacitance]]
- [[PINN]]
