---
type: concept
area: em
source-ref: "ECE 311 slides, lect_11"
tags: [electromagnetics]
---

# Electrostatic energy

**Summary**: Energy stored in charge distributions and electric fields, the energy density, and forces from virtual displacement.

## Results
Work to assemble point charges leads, for a continuous distribution, to (p. 2)
$$W_e=\tfrac12\int_v\rho_vV\,dv$$
Using $\rho_v=\nabla\cdot D$ and $E=-\nabla V$ (p. 3):
$$W_e=\tfrac12\int_vD\cdot E\,dv,\qquad w_e=\tfrac12D\cdot E$$
The energy density later gives the energy carried by EM waves ([[Poynting theorem]]). Forces follow from the change of stored energy under a virtual displacement; at fixed charge $F=-\nabla W_e$ (wiki note). For a capacitor $W_e=\tfrac12CV^2$ ([[Capacitance]]). Magnetic counterpart: $w_m=\tfrac12H\cdot B$ ([[Inductance]]).

> [!example] Uniformly charged sphere (lect_11, pp. 2-4)
> $E_R$ inside and outside is found with Gauss' law, then $V(R)$, then $W_e$; the slide result (checked) is $W_e=\dfrac{4\pi\rho_v^2a^5}{15\varepsilon_0}$.

> [!example] Coaxial conductors at potential $V_0$ (lect_11, p. 4)
> Gauss' law for $D_\rho$, then integrate $w_e$ over the volume.

**Covered in**: ECE 311 lect_11 (Electromagnetics/Lectures Slides/lect_11.pdf)
**Sources**: ECE 311 lecture slides (Spring 2024, Prof. D. S. Elliott): `Electromagnetics/Lectures Slides/lect_11.pdf`; lecture order from `Electromagnetics/ECE311_Spring2024_Schedule.pdf`. Statements marked Wiki note are standard physics not read in the slides.
**Last updated**: 2026-11-06

---

## Related pages
- [[Electrostatics]]
- [[Capacitance]]
- [[Poynting theorem]]
- [[Gauss's law]]
- [[Inductance]]
