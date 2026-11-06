---
type: lecture
area: em
source-ref: "ECE 311 lect_37, slides pp. 1-8"
tags: [electromagnetics]
course: ece311
lecture: lect_37
---
# ECE311 lect_37 - Standing waves

**Summary**: Superposition of incident and reflected waves forms standing waves; standing wave ratio.

**Course**: ECE 311 (Electromagnetics I, Purdue, Spring 2024, Prof. D. S. Elliott) · **Lecture date**: Apr 10 (per the schedule) · **File**: `Electromagnetics/Lectures Slides/lect_37.pdf` (8 slides)

---

## Topics
- Superposition of counter-propagating waves
- Standing wave pattern, nodes and anti-nodes
- Standing wave ratio
- Reading $\Gamma$ from the pattern

## Key results
Perfect reflector, $E_{r0}=-E_{i0}$ (slide numbers in brackets, PDF pp. 2-4):
$$E_1(z,t)=a_y\,2E_{i0}\sin\omega t\,\sin\beta_1z$$
$$H_1(z,t)=-a_x\tfrac{2E_{i0}}{\eta_1}\cos\omega t\,\cos\beta_1z$$
Nodes (minima) and anti-nodes (maxima) are fixed in space; nodes of $E$ coincide with anti-nodes of $H$, and $E$, $H$ are $\pi/2$ out of phase in time [6]. The average power of the two counter-propagating waves cancels: $\mathcal P_i+\mathcal P_r=0$ [7].
Partial reflection, $|\Gamma|<1$ [8-10]:
$$E_{max}=E_{i0}(1+|\Gamma|),\qquad E_{min}=E_{i0}(1-|\Gamma|)$$
$$S=\frac{E_{max}}{E_{min}}=\frac{1+|\Gamma|}{1-|\Gamma|},\qquad |\Gamma|=\frac{S-1}{S+1}$$
Spacing between nodes (or between anti-nodes) is $\Delta z=\lambda/2$ [13]. The phase of $\Gamma$ follows from the first minimum $z_{min}<0$: $\theta_\Gamma=\pi(2n+1)-4\pi z_{min}/\lambda$ [14].

## Examples
> [!example] Example 37-1 (PDF p. 7)
> Pattern with $E_{max}=1.5|E_i|$ and $E_{min}=0.5|E_i|$: $S=3$, $|\Gamma|=0.5$; a minimum at the surface makes $\Gamma$ real and negative, so $\Gamma=-0.5$.

**Sources**: `Electromagnetics/Lectures Slides/lect_37.pdf`; lecture order from `Electromagnetics/ECE311_Spring2024_Schedule.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Reflection and transmission of waves]]
- [[Transmission line]]
- [[ECE311 lect_36 - Reflection and transmission]]
- [[ECE311 lect_38 - Transmission lines intro]]
