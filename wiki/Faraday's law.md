---
type: concept
area: em
source-ref: "ECE 311 slides, lect_25, lect_27"
tags: [electromagnetics, pde]
---

# Faraday's law

**Summary**: A time-varying magnetic flux induces an EMF; the static equations are incomplete without it.

## Law
$$\mathcal E=-\frac{d\Phi_M}{dt}$$
Reversing a magnet reverses $\mathcal E$; approach and retreat give opposite signs; a stationary magnet gives zero (lect_25, p. 1). Differential form (wiki note): $\nabla\times E=-\partial B/\partial t$. The static equation $\nabla\times E=0$ cannot hold when $B$ changes, which motivates the extension ([[Maxwell's equations]]). Transformer EMF comes from $\partial B/\partial t$, motional EMF from $u\times B$; applications are transformers, generators and alternators.

## Generators and moving circuits (lect_27)
Rotating loop in uniform $B_0$: $v(t)=-d\Phi_M/dt$, with $\Phi_M=adB_0\cos\omega t$ gives $v=ad\omega B_0\sin\omega t$ (p. 1).

> [!example] Sliding bar (lect_27, Ex. 27-1, p. 1)
> $u=20\,a_y$ m/s, $B=4\cos(10^3t-y)\,a_z$ mWb/m$^2$, rail spacing $x_0=60$ cm; the EMF has a transformer term (from $\partial B/\partial t$) and a motional term (from $u\times B$).

**Covered in**: ECE 311 lect_25, lect_27 (Electromagnetics/Lectures Slides/lect_25.pdf, Electromagnetics/Lectures Slides/lect_27.pdf)
**Sources**: ECE 311 lecture slides (Spring 2024, Prof. D. S. Elliott): `Electromagnetics/Lectures Slides/lect_25.pdf`, `Electromagnetics/Lectures Slides/lect_27.pdf`; lecture order from `Electromagnetics/ECE311_Spring2024_Schedule.pdf`. Statements marked Wiki note are standard physics not read in the slides.
**Last updated**: 2026-11-06

---

## Related pages
- [[Maxwell's equations]]
- [[Inductance]]
- [[Magnetostatics]]
