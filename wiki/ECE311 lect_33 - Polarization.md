---
type: lecture
area: em
source-ref: "ECE 311 lect_33, slides pp. 1-8"
tags: [electromagnetics]
course: ece311
lecture: lect_33
---
# ECE311 lect_33 - Polarization

**Summary**: Polarization of a plane wave: linear, circular and elliptical, from the relative amplitude and phase of orthogonal E components.

**Course**: ECE 311 (Electromagnetics I, Purdue, Spring 2024, Prof. D. S. Elliott) · **Lecture date**: Apr 1 (per the schedule) · **File**: `Electromagnetics/Lectures Slides/lect_33.pdf` (8 slides)

---

## Topics
- Linear polarization and polarizers
- Circular polarization
- Wave plates, quarter-wave retarder

## Key results
Polarization is the orientation of $E$ (slide numbers in brackets, PDF pp. 2-7).
Linear [3-4]:
$$E=a_xE_0e^{-jkz}\ (\text{horizontal}),\qquad E=a_yE_0e^{-jkz}\ (\text{vertical})$$
$$E=\tfrac1{\sqrt2}(a_x\pm a_y)E_0e^{-jkz}\quad(\pm45^\circ)$$
Circular (a 90 degree phase shift between components) [10]:
$$E_R=\tfrac1{\sqrt2}(a_x-ja_y)E_0e^{-jkz},\qquad E_L=\tfrac1{\sqrt2}(a_x+ja_y)E_0e^{-jkz}$$
A polarizer transmits one component; for incident polarization at angle $\theta$ the transmitted amplitude is $E_0\cos\theta$ (Malus' law, Ex. 33-1) [8].
A wave plate of thickness $d$ with different $\varepsilon$ for $x$ and $y$ gives phase difference $\varphi_x-\varphi_y=\omega\sqrt{\varepsilon_x\mu}\,d-\omega\sqrt{\varepsilon_y\mu}\,d=\pm\pi/2$ for a $\lambda/4$ retarder [11].

## Examples
> [!example] Examples 33-2 to 33-4 (PDF pp. 6-7)
> Right circular light through a $\lambda/4$ retarder with vertical fast axis becomes linear at $+45^\circ$; with horizontal fast axis, linear at $-45^\circ$. Reflection off a screen is rejected by a polarizer plus $\lambda/4$ retarder at $45^\circ$ because the returning wave is orthogonal to the transmission axis.

**Sources**: `Electromagnetics/Lectures Slides/lect_33.pdf`; lecture order from `Electromagnetics/ECE311_Spring2024_Schedule.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Wave polarization]]
- [[Electromagnetic wave]]
- [[ECE311 lect_32 - EM spectrum]]
- [[ECE311 lect_34 - Plane wave power flow]]
