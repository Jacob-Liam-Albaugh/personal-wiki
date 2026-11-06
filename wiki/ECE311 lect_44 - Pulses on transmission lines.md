---
type: lecture
area: em
source-ref: "ECE 311 lect_44, slides pp. 1-8"
tags: [electromagnetics]
course: ece311
lecture: lect_44
---
# ECE311 lect_44 - Pulses on transmission lines

**Summary**: Transient pulses bouncing between a source and a mismatched load.

**Course**: ECE 311 (Electromagnetics I, Purdue, Spring 2024, Prof. D. S. Elliott) · **Lecture date**: Apr 26 (per the schedule) · **File**: `Electromagnetics/Lectures Slides/lect_44.pdf` (8 slides)

---

## Topics
- Reflection at source and load
- Bounce diagram

## Key results
Reflection coefficients at the two ends:
$$\Gamma_L=\frac{R_L-R_0}{R_L+R_0},\qquad \Gamma_S=\frac{R_g-R_0}{R_g+R_0}$$
Example 44-1 (PDF pp. 3-5, checked): $R_0=50$, $R_g=100$, $R_L=25$ give $\Gamma_L=-1/3$ and $\Gamma_g=+1/3$, with $V_1^+=V_g/3$. Successive pulses: $V_1^-=-V_1^+/3$, $V_2^+=-V_1^+/9$, $V_2^-=+V_1^+/27$, $V_3^+=+V_1^+/81$.
Long pulses accumulate: $V(\infty)=\dfrac{V_1^+(1+\Gamma_L)}{1-\Gamma_g\Gamma_L}=V_g\dfrac{R_L}{R_g+R_L}$ (PDF p. 5).

## Examples
> [!example] Example 44-1
> Pulse launched with a voltage divider $R_0/(R_0+R_g)$ then repeatedly reflected.

**Sources**: `Electromagnetics/Lectures Slides/lect_44.pdf`; lecture order from `Electromagnetics/ECE311_Spring2024_Schedule.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Transmission line]]
- [[Reflection and transmission of waves]]
- [[ECE311 lect_43 - Impedance matching]]
