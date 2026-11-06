---
type: lecture
area: em
source-ref: "ECE 311 lect_16, slides pp. 1-7"
tags: [electromagnetics]
course: ece311
lecture: lect_16
---
# ECE311 lect_16 - Power dissipation and conducting boundaries

**Summary**: Joule heating as E dot J, power dissipation in a conducting medium, and extra boundary conditions between lossy media.

**Course**: ECE 311 (Electromagnetics I, Purdue, Spring 2024, Prof. D. S. Elliott) · **Lecture date**: Feb 14 (per the schedule) · **File**: `Electromagnetics/Lectures Slides/lect_16.pdf` (7 slides)

---

## Topics
- Power lost to lattice collisions
- Power dissipation density
- Boundary conditions between two lossy media

## Key results
Each carrier gives energy $qE\cdot u$ to the lattice per unit time; summing over $n\,dv$ carriers (p. 2):
$$d\wp=E\cdot J_v\,dv,\qquad \wp=\int_vE\cdot J_v\,dv$$
For uniform fields $\wp=VI$. The same result later accounts for loss of EM waves in absorbing media.

## Examples
> [!example] Coax lossy dielectric (p. 2)
> With $D_\rho=\rho_sa/\rho$ and $E_\rho=D_\rho/\varepsilon$, Example 16-1 (PDF p. 2, checked) gives $E\cdot J_v=\sigma(\rho_sa/\varepsilon\rho)^2$, with $I=2\pi\sigma L V_0/\ln(b/a)$ and $R=\ln(b/a)/2\pi\sigma L$; integrating over $dv=\rho\,d\rho\,d\varphi\,dz$ gives the total power.

**Sources**: `Electromagnetics/Lectures Slides/lect_16.pdf`; lecture order from `Electromagnetics/ECE311_Spring2024_Schedule.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Ohm's law and current density]]
- [[Electrostatic energy]]
- [[Poynting theorem]]
- [[ECE311 lect_15 - Current density and Ohm's law]]
- [[ECE311 lect_17 - Magnetic fields and Biot-Savart law]]
