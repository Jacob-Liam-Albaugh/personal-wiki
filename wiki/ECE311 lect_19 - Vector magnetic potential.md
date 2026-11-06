---
type: lecture
area: em
source-ref: "ECE 311 lect_19, slides pp. 1-8"
tags: [electromagnetics, pde]
course: ece311
lecture: lect_19
---
# ECE311 lect_19 - Vector magnetic potential

**Summary**: Because div B = 0 there exists a vector potential A with B = curl A; calculation of A and B from currents.

**Course**: ECE 311 (Electromagnetics I, Purdue, Spring 2024, Prof. D. S. Elliott) · **Lecture date**: Feb 21 (per the schedule) · **File**: `Electromagnetics/Lectures Slides/lect_19.pdf` (8 slides)

---

## Topics
- Analogy to the scalar potential V
- Why $\nabla\cdot\nabla\times A=0$ (via divergence theorem and Stokes' theorem)
- Vector potential of a current distribution

## Key results
Definition (p. 2):
$$B=\nabla\times A$$
The converse also holds: $\nabla\cdot B=0$ implies such an $A$ exists (p. 3), as $\nabla\times E=0$ implies $V$ exists for $E=-\nabla V$.
Wiki note: from the Biot-Savart law $A(r)=\dfrac{\mu_0}{4\pi}\int\dfrac{J_v(r')}{|r-r'|}dv'$ (standard form, used in lect_20).

## Examples
> [!example] Potential vs vector potential
> $E=-\nabla V$ with $V=-\int E\cdot d\ell$; $B=\nabla\times A$ with flux $\int B\cdot ds=\oint A\cdot d\ell$.

**Sources**: `Electromagnetics/Lectures Slides/lect_19.pdf`; lecture order from `Electromagnetics/ECE311_Spring2024_Schedule.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Magnetic vector potential]]
- [[Electric potential]]
- [[Magnetostatics]]
- [[ECE311 lect_18 - Ampere's law]]
- [[ECE311 lect_20 - Magnetic dipole and materials]]
