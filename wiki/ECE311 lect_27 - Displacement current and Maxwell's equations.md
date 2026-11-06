---
type: lecture
area: em
source-ref: "ECE 311 lect_27, slides pp. 1-7"
tags: [electromagnetics, pde]
course: ece311
lecture: lect_27
---
# ECE311 lect_27 - Displacement current and Maxwell's equations

**Summary**: Faraday's law for moving circuits (generator, sliding bar), then displacement current completes Maxwell's equations; definition of a good conductor.

**Course**: ECE 311 (Electromagnetics I, Purdue, Spring 2024, Prof. D. S. Elliott) · **Lecture date**: Mar 18 (per the schedule) · **File**: `Electromagnetics/Lectures Slides/lect_27.pdf` (7 slides)

---

## Topics
- Generator with rotating loop
- Moving bar in a time-varying field
- Displacement current
- Maxwell's equations

## Key results
Rotating loop in uniform $B_0$: $v(t)=-d\Phi_M/dt$, with $\Phi_M=adB_0\cos\omega t$ gives $v=ad\omega B_0\sin\omega t$ (p. 1).
Completed set (wiki note, standard; see [[Maxwell's equations]]):
$$\nabla\times H=J_v+\frac{\partial D}{\partial t}$$

## Examples
> [!example] Sliding bar (Ex. 27-1, p. 1)
> $u=20\,a_y$ m/s, $B=4\cos(10^3t-y)\,a_z$ mWb/m$^2$, rail spacing $x_0=60$ cm; the EMF has a transformer term (from $\partial B/\partial t$) and a motional term (from $u\times B$).

**Sources**: `Electromagnetics/Lectures Slides/lect_27.pdf`; lecture order from `Electromagnetics/ECE311_Spring2024_Schedule.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Maxwell's equations]]
- [[Faraday's law]]
- [[Electromagnetic wave]]
- [[Ohm's law and current density]]
- [[ECE311 lect_25 - Faraday's law]]
- [[ECE311 lect_28 - Potentials and time-harmonic fields]]
