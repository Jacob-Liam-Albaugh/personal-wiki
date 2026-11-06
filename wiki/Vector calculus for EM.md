---
type: concept
area: em
source-ref: "ECE 311 slides, lect_1, lect_2, lect_3"
tags: [electromagnetics, pde]
---
# Vector calculus for EM

**Summary**: Coordinate systems and the differential operators used throughout ECE 311.

## Operators (lect_3)
- Gradient: direction of steepest increase of a scalar.
- Divergence: net outflow density of a vector field.
- Curl: circulation density.
$$\oint_sF\cdot ds=\int_v\nabla\cdot F\,dv$$
$$\oint_cF\cdot d\ell=\int_s\nabla\times F\cdot ds$$
Divergence theorem and Stokes' theorem turn integral laws into differential ones ([[Gauss's law]], [[Ampere's law]]).

## Coordinates (lect_2)
Cartesian, cylindrical, spherical, with unit vectors and line, surface and volume elements.

## Wiki note
Identities used: $\nabla\times\nabla V=0$ (so $E=-\nabla V$) and $\nabla\cdot\nabla\times A=0$ (so $B=\nabla\times A$).

**Sources**: ECE 311 lecture slides (Spring 2024, Prof. D. S. Elliott), [[ECE311 lect_1 - Units and vectors]], [[ECE311 lect_2 - Coordinate systems]], [[ECE311 lect_3 - Gradient divergence curl]]. Statements marked Wiki note are standard physics not read in the slides.
**Last updated**: 2026-11-06

---

## Related pages
- [[Electrostatics]]
- [[Magnetostatics]]
- [[Maxwell's equations]]
- [[ECE311 lect_1 - Units and vectors]]
- [[ECE311 lect_2 - Coordinate systems]]
- [[ECE311 lect_3 - Gradient divergence curl]]
