---
type: concept
area: em
source-ref: "ECE 311 slides, lect_17, lect_24"
tags: [electromagnetics]
---

# Biot-Savart law and Lorentz force

**Summary**: B from a current element, and the force on moving charges, current elements, parallel wires and coils.

## Magnetic effects and B
Oersted (1820) connected electricity and magnetism. The magnetic flux density $B$ is in $\mathrm{Wb/m^2}=$ T; $1\,\mathrm G=10^{-4}$ T (lect_17, p. 3). Applications of the force on a moving charge: velocity selector, Hall probe, cyclotron, aurora.

## Biot-Savart law (p. 3)
$$B(r)=\frac{\mu_0}{4\pi}\oint\frac{I\,d\ell'\times(r-r')}{|r-r'|^3}$$
Differential properties of $B$: $\nabla\cdot B=0$ and $\nabla\times B=\mu_0J_v$ ([[Ampere's law]]).

## Lorentz force
$$F=qu\times B,\qquad dF=I\,d\ell\times B$$
Parallel currents attract and antiparallel currents repel; this is the basis of the ampere definition ([[Vector calculus for EM]]). Force per unit length between wires 1 and 2 separated by $d$ (lect_24, p. 1):
$$F_m'=\frac{\mu_0I_1I_2}{2\pi d}$$
Torque on a motor coil follows from the force on its sides.

> [!example] Levitating a wire (lect_24, p. 1)
> Two parallel wires, 1 cm apart, carry equal and opposite current $I$. With 22 gauge copper (density $8.96\times10^3$ kg/m$^3$, area $3.26\times10^{-7}$ m$^2$) the weight per length is $F_g'=0.0286$ N/m; setting $F_m'=F_g'$ gives $I=\sqrt{2\pi dF_g'/\mu_0}=37.8$ A (PDF p. 2, text layer). The slide notes this is a huge current for 22 gauge wire; the dissipation is $P'=I^2/\sigma S=76$ W/m.

**Covered in**: ECE 311 lect_17, lect_24 (courses/ECE 311/Lectures Slides/lect_17.pdf, courses/ECE 311/Lectures Slides/lect_24.pdf)
**Sources**: ECE 311 lecture slides (Spring 2024, Prof. D. S. Elliott): `courses/ECE 311/Lectures Slides/lect_17.pdf`, `courses/ECE 311/Lectures Slides/lect_24.pdf`; lecture order from `courses/ECE 311/ECE311_Spring2024_Schedule.pdf`. Statements marked Wiki note are standard physics not read in the slides.
**Last updated**: 2026-11-06

---

## Related pages
- [[Magnetostatics]]
- [[Ampere's law]]
- [[Magnetic materials]]
- [[Inductance]]
