---
type: concept
area: em
source-ref: "ECE 311 slides, lect_22, lect_23, lect_38"
tags: [electromagnetics]
---

# Inductance

**Summary**: Flux linkage per current and stored magnetic energy, with inductance of standard geometries.

## Results
Work to establish a current distribution gives the circuit analogy $W_m=\tfrac12LI^2$ (lect_23, p. 1). In field terms the energy density is
$$w_m=\tfrac12H\cdot B$$
Flux linkage of one filament (p. 2): $\Phi_k=\int B\cdot ds_k=\oint A\cdot d\ell_k$ ([[Magnetic vector potential]]). Then
$$L=\Phi/I,\qquad W_m=\tfrac12LI^2$$
The electric counterpart is [[Electrostatic energy]].

> [!example] Inductance from flux (lect_23)
> Solenoid (Ex. 23-1, PDF p. 5): $W_m'=\tfrac12\mu n^2I^2s$, so $L'=\mu n^2s$ (agrees with Ex. 22-2). Toroid, rectangular section of thickness $h$ (Ex. 23-2, PDF p. 5): $H_\varphi=NI/2\pi\rho$, giving $L=\dfrac{\mu N^2h}{2\pi}\ln\dfrac ba$. Coax is Ex. 23-3 (PDF p. 6), not read here.

## Transmission lines
Per-unit-length $L'$ of coax, twin lead and parallel plates feeds [[Transmission line]] models: $L'=\mu d/w$ (parallel plate), $L'\simeq\frac{\mu}{2\pi}\ln\frac ba$ (coax), $L'\simeq\frac{\mu_0}{\pi}\cosh^{-1}\frac d{2a}$ (twin lead). With $C'$: $L'C'=\varepsilon\mu$.

**Covered in**: ECE 311 lect_22, lect_23, lect_38 (courses/ECE 311/Lectures Slides/lect_22.pdf, courses/ECE 311/Lectures Slides/lect_23.pdf, courses/ECE 311/Lectures Slides/lect_38.pdf)
**Sources**: ECE 311 lecture slides (Spring 2024, Prof. D. S. Elliott): `courses/ECE 311/Lectures Slides/lect_22.pdf`, `courses/ECE 311/Lectures Slides/lect_23.pdf`, `courses/ECE 311/Lectures Slides/lect_38.pdf`; lecture order from `courses/ECE 311/ECE311_Spring2024_Schedule.pdf`. Statements marked Wiki note are standard physics not read in the slides.
**Last updated**: 2026-11-06

---

## Related pages
- [[Magnetostatics]]
- [[Capacitance]]
- [[Faraday's law]]
- [[Electrostatic energy]]
- [[Magnetic materials]]
- [[Transmission line]]
