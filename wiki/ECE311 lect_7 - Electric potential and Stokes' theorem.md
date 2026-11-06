---
type: lecture
area: em
source-ref: "ECE 311 lect_7, slides pp. 1-8"
tags: [electromagnetics]
course: ece311
lecture: lect_7
---
# ECE311 lect_7 - Electric potential and Stokes' theorem

**Summary**: Because curl E = 0 the work to move a charge is path independent, so a scalar potential V with E = -grad V exists; Stokes' theorem is verified and V of a point charge is derived.

**Course**: ECE 311 (Electromagnetics I, Purdue, Spring 2024, Prof. D. S. Elliott) · **Lecture date**: Jan 24 (per the schedule) · **File**: `Electromagnetics/Lectures Slides/lect_7.pdf` (8 slides)

---

## Topics
- Vector path integrals
- Stokes' theorem
- Potential difference and its inverse $E=-
abla V$
- Potential of a point charge

## Key results
Work against the field and potential (pp. 1, 4):
$$W=-q\int_a^bE\cdot d\ell,\qquad V_B-V_A=-\int_A^BE\cdot d\ell$$
Path independence follows from Stokes' theorem $\int_s(\nabla\times A)\cdot ds=\oint_cA\cdot d\ell$ and $\nabla\times E=0$ (p. 4).
Inversion: $E=-\nabla V$ (p. 7); so $W=q(V_b-V_a)$ and 1 J moves 1 C through 1 V.
Point charge with reference at infinity (p. 8):
$$V(R)=\frac{q}{4\pi\varepsilon_0R}$$

## Examples
> [!example] Path dependence (pp. 2-3)
> For a non-conservative $F=x^2a_\varphi+xz\,a_z$ the line integral from $(b,0,0)$ to $(b,0,h)$ is $bh^2/2$ on the straight path but $\pi b^3$ on the spiral path.

> [!example] Stokes check (pp. 5-6)
> $A=-y\,a_x+x\,a_y$ on a rectangle: $\oint A\cdot d\ell=2x_0y_0=\int(\nabla\times A)\cdot ds$.

> [!example] Potential of 1.0 nC at 1 m (p. 8)
> $V=9.0$ V.

**Sources**: `Electromagnetics/Lectures Slides/lect_7.pdf`; lecture order from `Electromagnetics/ECE311_Spring2024_Schedule.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Electric potential]]
- [[Electrostatics]]
- [[Vector calculus for EM]]
- [[Magnetic vector potential]]
- [[ECE311 lect_6 - Applications of Gauss' law]]
- [[ECE311 lect_8 - Electric potential and dipole]]
