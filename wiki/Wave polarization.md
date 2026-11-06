---
type: concept
area: em
source-ref: "ECE 311 slides, lect_33"
tags: [electromagnetics, signals]
---

# Wave polarization

**Summary**: Locus of E over time: linear, circular and elliptical, from the relative amplitude and phase of orthogonal E components; polarizers and wave plates.

## Cases
Polarization is the orientation of $E$. Phase difference $\delta$ between orthogonal components: $0$ or $\pi$ linear; $\pm\pi/2$ with equal amplitude circular; otherwise elliptical (wiki note).

Linear (lect_33, pp. 3-4):
$$E=a_xE_0e^{-jkz}\ (\text{horizontal}),\qquad E=a_yE_0e^{-jkz}\ (\text{vertical})$$
$$E=\tfrac1{\sqrt2}(a_x\pm a_y)E_0e^{-jkz}\quad(\pm45^\circ)$$
Circular (a 90 degree phase shift between components, p. 10):
$$E_R=\tfrac1{\sqrt2}(a_x-ja_y)E_0e^{-jkz},\qquad E_L=\tfrac1{\sqrt2}(a_x+ja_y)E_0e^{-jkz}$$

## Polarizers and wave plates
A polarizer transmits one component; for incident polarization at angle $\theta$ the transmitted amplitude is $E_0\cos\theta$ (Malus' law, Ex. 33-1, p. 8). A wave plate of thickness $d$ with different $\varepsilon$ for $x$ and $y$ gives phase difference (p. 11)
$$\varphi_x-\varphi_y=\omega\sqrt{\varepsilon_x\mu}\,d-\omega\sqrt{\varepsilon_y\mu}\,d=\pm\pi/2$$
for a $\lambda/4$ retarder.

> [!example] Examples 33-2 to 33-4 (lect_33, PDF pp. 6-7)
> Right circular light through a $\lambda/4$ retarder with vertical fast axis becomes linear at $+45^\circ$; with horizontal fast axis, linear at $-45^\circ$. Reflection off a screen is rejected by a polarizer plus $\lambda/4$ retarder at $45^\circ$ because the returning wave is orthogonal to the transmission axis.

**Covered in**: ECE 311 lect_33 (Electromagnetics/Lectures Slides/lect_33.pdf)
**Sources**: ECE 311 lecture slides (Spring 2024, Prof. D. S. Elliott): `Electromagnetics/Lectures Slides/lect_33.pdf`; lecture order from `Electromagnetics/ECE311_Spring2024_Schedule.pdf`. Statements marked Wiki note are standard physics not read in the slides.
**Last updated**: 2026-11-06

---

## Related pages
- [[Electromagnetic wave]]
