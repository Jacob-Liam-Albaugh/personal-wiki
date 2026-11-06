---
type: lecture
area: em
source-ref: "ECE 311 lect_43, slides pp. 1-7"
tags: [electromagnetics]
course: ece311
lecture: lect_43
---
# ECE311 lect_43 - Impedance matching

**Summary**: Matching a load to a line: quarter-wave transformer and stub matching.

**Course**: ECE 311 (Electromagnetics I, Purdue, Spring 2024, Prof. D. S. Elliott) · **Lecture date**: Apr 24 (per the schedule) · **File**: `Electromagnetics/Lectures Slides/lect_43.pdf` (7 slides)

---

## Topics
- Why match impedance
- Quarter-wave transformer
- Shorted stub matching: idea and admittances
- Stub design conditions G1 = G0 and B1 cancellation

## Key results
Matching reduces or removes reflections and standing-wave maxima and minima, optimises power to the load, lowers frequency dependence, protects the source, and makes $Z_{in}=Z_0$ (PDF p. 2, [3]). Slide numbers in brackets.
Quarter-wave transformer, line of impedance $R_{02}$ and $\ell=\lambda/4$ (PDF pp. 2-3, [4-5]):
$$Z_{in}=R_{02}\frac{Z_L+jR_{02}\tan\beta\ell}{R_{02}+jZ_L\tan\beta\ell}$$
$$\beta\ell=\tfrac\pi2:\quad Z_{in}=\frac{R_{02}^2}{Z_L}$$
$$Z_{in}=R_0\ \Rightarrow\ R_{02}=\sqrt{Z_LR_0}$$
Most useful for microstrip, where trace width sets $R_{02}$; limited bandwidth because $\ell=\lambda/4$ is needed [5].
Shorted or open stub in parallel at $\ell_1$ from the load (PDF pp. 3-4, [6-8]): reflections from the load and from the stub end cancel at the branch point. Work in admittances, $Y_0=1/Z_0$:
$$Y_{in}=Y_1+Y_{st}=\frac1{R_0}=G_0$$
$$Y_{st}=-jG_0\cot\beta\ell_{st}\ \text{(shorted stub)}$$
Matching conditions [8-9]:
$$G_1=G_0,\qquad B_1-G_0\cot\beta\ell_{st}=0$$
Choose $\ell_1$ so $G_1=G_0$, then $\ell_{st}$ to cancel $B_1$ [9].

## Examples
> [!example] Example 43-1 (PDF pp. 4-6, [9-12])
> Match $Z_L=(25+j75)\ \Omega$ to a 50 ohm line, $G_0=20$ mS. $G_1=G_0$ gives $\tan^2\beta\ell_1+6\tan\beta\ell_1+4=0$, so $\tan\beta\ell_1=-3\pm\sqrt5=-0.7639$ or $-5.236$. Then $\beta\ell_1=142.62^\circ$ or $100.81^\circ$, $\ell_1=0.396\lambda$ or $0.280\lambda$. For $\beta\ell_1=142.62^\circ$, $B_1=-2.236G_0$, so $\cot\beta\ell_{st}=-2.236$. The PDF ends here (slide 12); the stub length and the second solution are not worked on the slides.

**Sources**: `Electromagnetics/Lectures Slides/lect_43.pdf`; lecture order from `Electromagnetics/ECE311_Spring2024_Schedule.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Impedance matching]]
- [[Transmission line]]
- [[ECE311 lect_42 - SWR and lines as circuit elements]]
- [[ECE311 lect_44 - Pulses on transmission lines]]
