---
type: concept
area: em
source-ref: "ECE 311 slides, lect_7, lect_8"
tags: [electromagnetics]
---

# Electric potential

**Summary**: Scalar potential V, which exists because E is curl-free, its calculation for discrete and continuous charge, and the electric dipole.

## Definition
Work against the field and potential (lect_7, pp. 1, 4):
$$W=-q\int_a^bE\cdot d\ell,\qquad V_B-V_A=-\int_A^BE\cdot d\ell$$
Path independence follows from Stokes' theorem and $\nabla\times E=0$ ([[Vector calculus for EM]]). Inversion (p. 7):
$$E=-\nabla V$$
so $W=q(V_b-V_a)$ and 1 J moves 1 C through 1 V. Point charge with reference at infinity (p. 8):
$$V(R)=\frac{q}{4\pi\varepsilon_0R}$$

> [!example] Path dependence (lect_7, pp. 2-3)
> For a non-conservative $F=x^2a_\varphi+xz\,a_z$ the line integral from $(b,0,0)$ to $(b,0,h)$ is $bh^2/2$ on the straight path but $\pi b^3$ on the spiral path.

> [!example] Potential of 1.0 nC at 1 m (lect_7, p. 8)
> $V=9.0$ V.

## Continuous charge (lect_8)
Superposition (p. 3):
$$V(r)=\int_v\frac{\rho_v(r')}{4\pi\varepsilon_0|r-r'|}\,dv'$$
with line and surface charge replacing $\rho_v\,dv'$. Finding $E=-\nabla V$ needs $V$ as a function of position; a potential known at one point cannot give $E$ because the derivative needs $V$ near that point (p. 2).

> [!example] Finite line charge (lect_8, pp. 3-4)
> The potential is a $\int d\xi/\sqrt{x^2+\xi^2}$ integral, and replacing $x\to\rho$ gives it off the $x$-$z$ plane.

> [!example] Shell of charge $q$, radius $a$ (lect_8, p. 5)
> Integrating the shell gives $V=q/4\pi\varepsilon_0R$ outside and constant $q/4\pi\varepsilon_0a$ inside (checked: $E=0$ inside, $E=q/4\pi\varepsilon_0R^2$ outside).

## Dipole
Two opposite charges give the dipole potential (quoted on p. 4 of lect_9)
$$V=\frac{p\cdot a_R}{4\pi\varepsilon_0R^2}$$
Potential falls as $1/R^2$ and field as $1/R^3$ (wiki note on exponents). The dipole moment density $P=np$ of a material is in [[Dielectric polarization]]; the magnetic analogue is the loop dipole in [[Magnetic vector potential]].

## Analogue
Magnetic version: [[Magnetic vector potential]].

**Covered in**: ECE 311 lect_7, lect_8 (Electromagnetics/Lectures Slides/lect_7.pdf, Electromagnetics/Lectures Slides/lect_8.pdf)
**Sources**: ECE 311 lecture slides (Spring 2024, Prof. D. S. Elliott): `Electromagnetics/Lectures Slides/lect_7.pdf`, `Electromagnetics/Lectures Slides/lect_8.pdf`; lecture order from `Electromagnetics/ECE311_Spring2024_Schedule.pdf`. Statements marked Wiki note are standard physics not read in the slides.
**Last updated**: 2026-11-06

---

## Related pages
- [[Electrostatics]]
- [[Poisson and Laplace equations]]
- [[Vector calculus for EM]]
- [[Dielectric polarization]]
- [[Magnetic vector potential]]
