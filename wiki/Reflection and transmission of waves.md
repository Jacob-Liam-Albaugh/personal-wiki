---
type: concept
area: em
source-ref: "ECE 311 slides, lect_36, lect_37"
tags: [electromagnetics, pde]
---

# Reflection and transmission of waves

**Summary**: Normal incidence of a plane wave on an interface, reflection and transmission coefficients, and the standing waves and SWR they produce.

## Normal incidence (lect_36)
$E_i=a_yE_{i0}e^{-j\beta_1z}$, reflected wave back in medium 1, transmitted wave (possibly lossy, $\kappa_t=\beta_2-j\alpha_2$) in medium 2 (PDF pp. 2-4). Boundary conditions at $z=0$ ($J_s=0$ except for a perfect conductor):
$$E_{i0}+E_{r0}=E_{t0}$$
$$\frac{E_{i0}}{\eta_1}-\frac{E_{r0}}{\eta_1}=\frac{E_{t0}}{\eta_2}$$
Coefficients:
$$\Gamma=\frac{E_{r0}}{E_{i0}}=\frac{\eta_2-\eta_1}{\eta_2+\eta_1}$$
$$\tau=\frac{E_{t0}}{E_{i0}}=1+\Gamma=\frac{2\eta_2}{\eta_2+\eta_1}$$
Complex $\eta$ for lossy media and good conductors, $\eta=\sqrt{\pi f\mu/\sigma}\,(1+j)$ ([[Electromagnetic wave]]). Power balance: $\mathcal P_t-\mathcal P_r=\mathcal P_i$ (slide 13). Perfect conductor: $\Gamma=-1$, $\tau=0$, $J_s=a_y2E_{i0}/\eta_0$.

> [!example] Example 36-1 (lect_36, PDF pp. 4-5)
> Window glass $\varepsilon_2=2.25\varepsilon_0$: $\eta_2=\eta_0/1.5$, so $\Gamma=-0.2$ at the first surface and $+0.2$ at the second; $|\Gamma|^2=0.04$ in each case.

> [!example] Example 36-2 (lect_36, PDF pp. 6, 8)
> Aluminum ($\sigma=3.5\times10^7$ S/m) at $6\times10^{14}$ Hz: $\eta_2=8.2(1+j)\ \Omega$, $\Gamma=-0.956+j0.044$, $|\Gamma|^2=0.92$, so 92 percent of the power is reflected; $\tau\approx0.044(1+j)$.

## Standing waves (lect_37)
Perfect reflector, $E_{r0}=-E_{i0}$ (PDF pp. 2-4):
$$E_1(z,t)=a_y\,2E_{i0}\sin\omega t\,\sin\beta_1z$$
$$H_1(z,t)=-a_x\tfrac{2E_{i0}}{\eta_1}\cos\omega t\,\cos\beta_1z$$
Nodes (minima) and anti-nodes (maxima) are fixed in space; nodes of $E$ coincide with anti-nodes of $H$, and $E$, $H$ are $\pi/2$ out of phase in time. The average power of the two counter-propagating waves cancels: $\mathcal P_i+\mathcal P_r=0$.

Partial reflection, $|\Gamma|<1$:
$$E_{max}=E_{i0}(1+|\Gamma|),\qquad E_{min}=E_{i0}(1-|\Gamma|)$$
$$S=\frac{E_{max}}{E_{min}}=\frac{1+|\Gamma|}{1-|\Gamma|},\qquad |\Gamma|=\frac{S-1}{S+1}$$
Spacing between nodes (or between anti-nodes) is $\Delta z=\lambda/2$. The phase of $\Gamma$ follows from the first minimum $z_{min}<0$: $\theta_\Gamma=\pi(2n+1)-4\pi z_{min}/\lambda$.

> [!example] Example 37-1 (lect_37, PDF p. 7)
> Pattern with $E_{max}=1.5|E_i|$ and $E_{min}=0.5|E_i|$: $S=3$, $|\Gamma|=0.5$; a minimum at the surface makes $\Gamma$ real and negative, so $\Gamma=-0.5$.

Same algebra on a [[Transmission line]].

**Covered in**: ECE 311 lect_36, lect_37 (Electromagnetics/Lectures Slides/lect_36.pdf, Electromagnetics/Lectures Slides/lect_37.pdf)
**Sources**: ECE 311 lecture slides (Spring 2024, Prof. D. S. Elliott): `Electromagnetics/Lectures Slides/lect_36.pdf`, `Electromagnetics/Lectures Slides/lect_37.pdf`; lecture order from `Electromagnetics/ECE311_Spring2024_Schedule.pdf`. Statements marked Wiki note are standard physics not read in the slides.
**Last updated**: 2026-11-06

---

## Related pages
- [[Electromagnetic wave]]
- [[Impedance matching]]
- [[Transmission line]]
