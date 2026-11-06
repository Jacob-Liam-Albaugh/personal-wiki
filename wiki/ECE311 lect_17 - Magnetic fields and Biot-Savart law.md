---
type: lecture
area: em
source-ref: "ECE 311 lect_17, slides pp. 1-7"
tags: [electromagnetics]
course: ece311
lecture: lect_17
---
# ECE311 lect_17 - Magnetic fields and Biot-Savart law

**Summary**: Introduces magnetic effects (Oersted, forces between wires, Lorentz force), defines B, and gives the Biot-Savart law for B from a current.

**Course**: ECE 311 (Electromagnetics I, Purdue, Spring 2024, Prof. D. S. Elliott) · **Lecture date**: Feb 16 (per the schedule) · **File**: `Electromagnetics/Lectures Slides/lect_17.pdf` (7 slides)

---

## Topics
- Connection between electricity and magnetism (Oersted 1820)
- Force between current-carrying wires
- Force on a moving charge; applications (velocity selector, Hall probe, cyclotron, aurora)
- Magnetic flux density B (tesla) and the Biot-Savart law
- Differential laws of B

## Key results
Magnetic flux density $B$ in $\mathrm{Wb/m^2}=$ T; $1\,\mathrm G=10^{-4}$ T (p. 3). Force on a moving charge (p. 2): $F=qu\times B$, with $dF=I\,d\ell\times B$ on a current element (p. 3).
Biot-Savart law (p. 3):
$$B(r)=\frac{\mu_0}{4\pi}\oint\frac{I\,d\ell'\times(r-r')}{|r-r'|^3}$$
Differential properties of $B$ (stated in lect_18, p. 1): $\nabla\cdot B=0$ and $\nabla\times B=\mu_0J_v$.

## Examples
> [!example] Wires carry force on each other
> Parallel currents attract and antiparallel currents repel; this is the basis of the ampere definition used in [[ECE311 lect_1 - Units and vectors]].

**Sources**: `Electromagnetics/Lectures Slides/lect_17.pdf`; lecture order from `Electromagnetics/ECE311_Spring2024_Schedule.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Biot-Savart law and Lorentz force]]
- [[Magnetostatics]]
- [[Ampere's law]]
- [[ECE311 lect_16 - Power dissipation and conducting boundaries]]
- [[ECE311 lect_18 - Ampere's law]]
