---
type: concept
area: em
source-ref: "ECE 311 slides, lect_1, lect_2, lect_3"
tags: [electromagnetics, pde]
---

# Vector calculus for EM

**Summary**: SI units, charge and current densities, vector products, coordinate systems and the differential operators (gradient, divergence, curl) used throughout ECE 311.

## Units and densities
SI base units used in the course: m, kg, s, A (not candela or kelvin). The ampere is defined by the force between two long parallel wires 1 m apart: $2\times10^{-7}$ N/m at 1 A (p. 4 of lect_1); see [[Biot-Savart law and Lorentz force]]. The elementary charge is $e=1.602176634\times10^{-19}$ C (p. 5).

Charge densities are $\rho_v,\rho_s,\rho_\ell$ (volume, surface, line) and current densities $J_v,J_s$. They are limits of ratios, e.g.:
$$\rho_v=\lim_{\Delta v\to0}\frac{\Delta q}{\Delta v}\ \ (\mathrm{C/m^3})$$
$$J_v=\lim_{\Delta s\to0}\frac{\Delta I}{\Delta s}\ \ (\mathrm{A/m^2})$$

> [!example] Surface charge density of a capacitor plate (lect_1, p. 5)
> A 0.5 uF capacitor charged to 1 V holds 0.5 uC on the positive plate; with plate area $10^{-2}$ m$^2$ and uniform charge, $\rho_s=0.5\times10^{-4}$ C/m$^2$.

## Scalar and vector products
$$A\cdot B=|A||B|\cos\theta$$
$$|A\times B|=|A||B|\sin\theta$$
$A\times B$ is perpendicular to both $A$ and $B$, and $A\times B=-B\times A$ (pp. 7-8).

> [!example] Dot and cross product (lect_1, p. 7)
> For $A=(5,6,-3)$ and $B=(-1,2,3)$: $A\cdot B=-2$ and $A\times B=(24,-12,16)$, which is orthogonal to $A$ (dot product $120-72-48=0$).

## Coordinate systems (lect_2)
Cylindrical and spherical to rectangular (p. 2):
$$x=\rho\cos\varphi,\quad y=\rho\sin\varphi$$
$$x=R\sin\theta\cos\varphi,\quad y=R\sin\theta\sin\varphi$$
$$z=R\cos\theta$$
Volume elements (pp. 6-7):
$$dv=\rho\,d\rho\,d\varphi\,dz\quad\text{(cylindrical)}$$
$$dv=R^2\sin\theta\,dR\,d\theta\,d\varphi\quad\text{(spherical)}$$
The slides check that $a_R,a_\theta,a_\varphi$ are mutually orthogonal and right-handed, e.g. $a_R\times a_\theta=a_\varphi$ (pp. 5-6). The line, surface and volume elements $d\ell$, $ds$, $dv$ set up every EM integral.

> [!example] Two points on a sphere of radius 5 m (lect_2, pp. 3-4)
> With $P_1$ at $(\theta,\varphi)=(\pi/4,3\pi/4)$ and $P_2$ at $(\pi/2,\pi/4)$ the angle between the radius vectors is $\pi/2$, the chord is $5\sqrt2\approx7.07$ m and the arc is $7.85$ m.

> [!example] Area of a spherical patch (lect_2, p. 9)
> For radius $a$, $\pi/4<\theta<3\pi/4$, $0<\varphi<\pi/2$: $S=a^2\pi/\sqrt2$, which is $0.177$ of the sphere.

> [!example] Mass of a cylinder (lect_2, pp. 7-8)
> For $\rho_m=\rho_0\cos(\pi\rho/2a)e^{-z/h}$ the slides integrate with $dv=\rho\,d\rho\,d\varphi\,dz$ and get $M\approx0.92\,\rho_0a^2h$.

## Operators (lect_3)
- Gradient: slope and direction of steepest increase of a scalar.
- Divergence: net outflow per unit volume of a vector field (a scalar).
- Curl: rotation, with the axis as direction.

Rectangular forms (p. 1):
$$\nabla f=a_x\frac{\partial f}{\partial x}+a_y\frac{\partial f}{\partial y}+a_z\frac{\partial f}{\partial z}$$
$$\nabla\cdot D=\frac{\partial D_x}{\partial x}+\frac{\partial D_y}{\partial y}+\frac{\partial D_z}{\partial z}$$
Cylindrical divergence (p. 4): $\nabla\cdot A=\frac1\rho\frac{\partial(\rho A_\rho)}{\partial\rho}+\frac1\rho\frac{\partial A_\varphi}{\partial\varphi}+\frac{\partial A_z}{\partial z}$.

The point-charge field $E\propto a_R/R^2$ has $\nabla\cdot E=0$ except at $R=0$ (p. 5); the exception is resolved by [[Gauss's law]].

## Integral theorems
$$\oint_sF\cdot ds=\int_v\nabla\cdot F\,dv\quad\text{(divergence theorem)}$$
$$\oint_cF\cdot d\ell=\int_s(\nabla\times F)\cdot ds\quad\text{(Stokes' theorem)}$$
They turn integral laws into differential ones ([[Gauss's law]], [[Ampere's law]]).

Identities used: $\nabla\times\nabla V=0$ (so $E=-\nabla V$, see [[Electric potential]]) and $\nabla\cdot\nabla\times A=0$ (so $B=\nabla\times A$, see [[Magnetic vector potential]]).

> [!example] Curl of rotating fields (lect_3, pp. 7-8)
> $A=-y\,a_x+x\,a_y$ has $\nabla\times A=2a_z$ (rotation). $B=a_\varphi$ has $\nabla\times B=a_z/\rho$. $C=a_R/R^2$ has zero curl.

> [!example] Divergence in cylindrical coordinates (lect_3, p. 4)
> $F=a_\rho\cos\varphi+a_z(\rho^2+z^2)$ is quoted with $\nabla\cdot F=2\cos\varphi+2z$ after the $1/\rho$ factor cancels. **[unverified]**: for the field exactly as written the formula above gives $\cos\varphi/\rho+2z$, so the printed field probably carries a factor of $\rho$.

> [!example] Check of the divergence theorem (lect_5, pp. 6-7)
> $A=a_xx$ over a cube of side $a$: both sides equal $a^3$. Over a sphere of radius $a$: $\frac{4\pi}{3}a^3$.

> [!example] Stokes check (lect_7, pp. 5-6)
> $A=-y\,a_x+x\,a_y$ on a rectangle: $\oint A\cdot d\ell=2x_0y_0=\int(\nabla\times A)\cdot ds$.

**Covered in**: ECE 311 lect_1, lect_2, lect_3 (courses/ECE 311/Lectures Slides/lect_1.pdf, courses/ECE 311/Lectures Slides/lect_2.pdf, courses/ECE 311/Lectures Slides/lect_3.pdf)
**Sources**: ECE 311 lecture slides (Spring 2024, Prof. D. S. Elliott): `courses/ECE 311/Lectures Slides/lect_1.pdf`, `courses/ECE 311/Lectures Slides/lect_2.pdf`, `courses/ECE 311/Lectures Slides/lect_3.pdf`; lecture order from `courses/ECE 311/ECE311_Spring2024_Schedule.pdf`. Statements marked Wiki note are standard physics not read in the slides.
**Last updated**: 2026-11-06

---

## Related pages
- [[Electrostatics]]
- [[Magnetostatics]]
- [[Maxwell's equations]]
- [[Coulomb's law]]
