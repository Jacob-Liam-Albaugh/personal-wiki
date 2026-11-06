---
type: concept
area: em
source-ref: "ECE 311 slides, lect_19, lect_20, lect_28"
tags: [electromagnetics, pde]
---

# Magnetic vector potential

**Summary**: A with B equal to curl A, its calculation for currents, the magnetic dipole, and its role in time-varying fields.

## Definition (lect_19)
Because $\nabla\cdot B=0$ a vector potential exists (p. 3):
$$B=\nabla\times A$$
as $\nabla\times E=0$ implies $V$ exists for $E=-\nabla V$ ([[Electric potential]]). That $\nabla\cdot\nabla\times A=0$ follows from the divergence and Stokes theorems ([[Vector calculus for EM]]). Flux: $\int B\cdot ds=\oint A\cdot d\ell$. Compare $E=-\nabla V$ with $V=-\int E\cdot d\ell$.

Wiki note: from the Biot-Savart law $A(r)=\dfrac{\mu_0}{4\pi}\int\dfrac{J_v(r')}{|r-r'|}dv'$ (standard form).

## Magnetic dipole (lect_20)
Far field of a current loop of radius $b$, $R\gg b$ (p. 3):
$$A=\frac{\mu_0\,m\times a_R}{4\pi R^2},\qquad m=IS\,a_z$$
The field has the same form as the electric dipole field ([[Electric potential]]).

> [!example] Dipole potential derivation (lect_20, pp. 1-2)
> Choose $\varphi=\pi/2$ by symmetry, expand $|r-r'|^{-1}\approx R^{-1}(1+\frac{b}{R}\sin\theta\sin\varphi')$ and integrate around the loop.

Magnetized material is modelled by equivalent currents ([[Magnetic materials]]).

## Time-varying fields (lect_28)
$B=\nabla\times A$ still holds because $\nabla\cdot B=0$. Faraday's law gives (p. 1)
$$E=-\nabla V-\frac{\partial A}{\partial t}$$

**Covered in**: ECE 311 lect_19, lect_20, lect_28 (courses/ECE 311/Lectures Slides/lect_19.pdf, courses/ECE 311/Lectures Slides/lect_20.pdf, courses/ECE 311/Lectures Slides/lect_28.pdf)
**Sources**: ECE 311 lecture slides (Spring 2024, Prof. D. S. Elliott): `courses/ECE 311/Lectures Slides/lect_19.pdf`, `courses/ECE 311/Lectures Slides/lect_20.pdf`, `courses/ECE 311/Lectures Slides/lect_28.pdf`; lecture order from `courses/ECE 311/ECE311_Spring2024_Schedule.pdf`. Statements marked Wiki note are standard physics not read in the slides.
**Last updated**: 2026-11-06

---

## Related pages
- [[Magnetostatics]]
- [[Electric potential]]
- [[Maxwell's equations]]
- [[Magnetic materials]]
