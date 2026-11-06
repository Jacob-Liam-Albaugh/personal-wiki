---
type: lecture
area: em
source-ref: "ECE 311 lect_2, slides pp. 1-10"
tags: [electromagnetics]
course: ece311
lecture: lect_2
---
# ECE311 lect_2 - Coordinate systems

**Summary**: Rectangular, cylindrical and spherical coordinates, their unit vectors, and the line, surface and volume elements used to set up EM integrals.

**Course**: ECE 311 (Electromagnetics I, Purdue, Spring 2024, Prof. D. S. Elliott) · **Lecture date**: Jan 10 (per the schedule) · **File**: `Electromagnetics/Lectures Slides/lect_2.pdf` (10 slides)

---

## Topics
- Coordinate transformations
- Unit vectors in the three systems and conversions between them
- Integration elements $d\ell$, $ds$, $dv$
- Integration examples (mass of a cylinder, area of a spherical patch, charge in a sphere)

## Key results
Cylindrical and spherical to rectangular (p. 2):
$$x=\rho\cos\varphi,\quad y=\rho\sin\varphi$$
$$x=R\sin\theta\cos\varphi,\quad y=R\sin\theta\sin\varphi$$
$$z=R\cos\theta$$
Volume elements (pp. 6-7):
$$dv=\rho\,d\rho\,d\varphi\,dz\quad\text{(cylindrical)}$$
$$dv=R^2\sin\theta\,dR\,d\theta\,d\varphi\quad\text{(spherical)}$$
The slides check that $a_R,a_\theta,a_\varphi$ are mutually orthogonal and right-handed, e.g. $a_R\times a_\theta=a_\varphi$ (pp. 5-6).

## Examples
> [!example] Two points on a sphere of radius 5 m (pp. 3-4)
> With $P_1$ at $(\theta,\varphi)=(\pi/4,3\pi/4)$ and $P_2$ at $(\pi/2,\pi/4)$ the angle between the radius vectors is $\pi/2$, the chord is $5\sqrt2\approx7.07$ m and the arc is $7.85$ m.

> [!example] Area of a spherical patch (p. 9)
> For radius $a$, $\pi/4<\theta<3\pi/4$, $0<\varphi<\pi/2$: $S=a^2\pi/\sqrt2$, which is $0.177$ of the sphere.

> [!example] Mass of a cylinder (pp. 7-8)
> For $\rho_m=\rho_0\cos(\pi\rho/2a)e^{-z/h}$ the slides integrate with $dv=\rho\,d\rho\,d\varphi\,dz$ and get $M\approx0.92\,\rho_0a^2h$.

**Sources**: `Electromagnetics/Lectures Slides/lect_2.pdf`; lecture order from `Electromagnetics/ECE311_Spring2024_Schedule.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Vector calculus for EM]]
- [[ECE311 lect_1 - Units and vectors]]
- [[Maxwell's equations]]
- [[ECE311 lect_3 - Gradient divergence curl]]
