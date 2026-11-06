---
type: lecture
area: em
source-ref: "ECE 311 lect_3, slides pp. 1-10"
tags: [electromagnetics, pde]
course: ece311
lecture: lect_3
---
# ECE311 lect_3 - Gradient divergence curl

**Summary**: Gradient, divergence and curl in rectangular, cylindrical and spherical coordinates, with two identities that underlie the potentials introduced later.

**Course**: ECE 311 (Electromagnetics I, Purdue, Spring 2024, Prof. D. S. Elliott) · **Lecture date**: Jan 12 (per the schedule) · **File**: `Electromagnetics/Lectures Slides/lect_3.pdf` (10 slides)

---

## Topics
- Gradient (slope, direction of steepest change)
- Divergence (outflow per unit volume, scalar)
- Curl (rotation, axis direction)
- Identities $\nabla\times\nabla f=0$ and $\nabla\cdot\nabla\times A=0$

## Key results
Rectangular forms (p. 1):
$$\nabla f=a_x\frac{\partial f}{\partial x}+a_y\frac{\partial f}{\partial y}+a_z\frac{\partial f}{\partial z}$$
$$\nabla\cdot D=\frac{\partial D_x}{\partial x}+\frac{\partial D_y}{\partial y}+\frac{\partial D_z}{\partial z}$$
Cylindrical divergence (p. 4): $\nabla\cdot A=\frac1\rho\frac{\partial(\rho A_\rho)}{\partial\rho}+\frac1\rho\frac{\partial A_\varphi}{\partial\varphi}+\frac{\partial A_z}{\partial z}$.
The point-charge field $E\propto a_R/R^2$ has $\nabla\cdot E=0$ except at $R=0$ (p. 5); this exception is resolved in [[ECE311 lect_5 - Gauss' law and divergence theorem]].

## Examples
> [!example] Curl of rotating fields (pp. 7-8)
> $A=-y\,a_x+x\,a_y$ has $\nabla\times A=2a_z$ (rotation). $B=a_\varphi$ has $\nabla\times B=a_z/\rho$. $C=a_R/R^2$ has zero curl.

> [!example] Divergence in cylindrical coordinates (p. 4)
> $F=a_\rho\cos\varphi+a_z(\rho^2+z^2)$ gives $\nabla\cdot F=2\cos\varphi+2z$ - wait: slide result is $2\cos\varphi+2z$ after the $1/\rho$ factor cancels.

**Sources**: `Electromagnetics/Lectures Slides/lect_3.pdf`; lecture order from `Electromagnetics/ECE311_Spring2024_Schedule.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Vector calculus for EM]]
- [[Electric potential]]
- [[Magnetic vector potential]]
- [[Maxwell's equations]]
- [[ECE311 lect_2 - Coordinate systems]]
- [[ECE311 lect_4 - Coulomb's law]]
