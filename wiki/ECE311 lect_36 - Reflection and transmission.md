---
type: lecture
area: em
source-ref: "ECE 311 lect_36, slides pp. 1-11"
tags: [electromagnetics]
course: ece311
lecture: lect_36
---
# ECE311 lect_36 - Reflection and transmission

**Summary**: Normal incidence of a plane wave on an interface between two media: reflection and transmission coefficients.

**Course**: ECE 311 (Electromagnetics I, Purdue, Spring 2024, Prof. D. S. Elliott) · **Lecture date**: Apr 8 (per the schedule) · **File**: `Electromagnetics/Lectures Slides/lect_36.pdf` (11 slides)

---

## Topics
- Boundary conditions at the interface
- Reflection and transmission coefficients
- Good and perfect conductors

## Key results
Normal incidence, $E_i=a_yE_{i0}e^{-j\beta_1z}$, reflected wave back in medium 1, transmitted wave (possibly lossy, $\kappa_t=\beta_2-j\alpha_2$) in medium 2 (slide numbers in brackets, PDF pp. 2-4).
Boundary conditions at $z=0$ ($J_s=0$ except for a perfect conductor) [5]:
$$E_{i0}+E_{r0}=E_{t0}$$
$$\frac{E_{i0}}{\eta_1}-\frac{E_{r0}}{\eta_1}=\frac{E_{t0}}{\eta_2}$$
Coefficients [5-6]:
$$\Gamma=\frac{E_{r0}}{E_{i0}}=\frac{\eta_2-\eta_1}{\eta_2+\eta_1}$$
$$\tau=\frac{E_{t0}}{E_{i0}}=1+\Gamma=\frac{2\eta_2}{\eta_2+\eta_1}$$
Complex $\eta$ for lossy media and good conductors, $\eta=\sqrt{\pi f\mu/\sigma}\,(1+j)$ [7]. Reflected plus transmitted power balance: $\mathcal P_t-\mathcal P_r=\mathcal P_i$ [13]. Perfect conductor: $\Gamma=-1$, $\tau=0$, $J_s=a_y2E_{i0}/\eta_0$ [16].

## Examples
> [!example] Example 36-1 (PDF pp. 4-5)
> Window glass $\varepsilon_2=2.25\varepsilon_0$: $\eta_2=\eta_0/1.5$, so $\Gamma=-0.2$ at the first surface and $+0.2$ at the second; $|\Gamma|^2=0.04$ in each case.

> [!example] Example 36-2 (PDF pp. 6, 8)
> Aluminum ($\sigma=3.5\times10^7$ S/m) at $6\times10^{14}$ Hz: $\eta_2=8.2(1+j)\ \Omega$, $\Gamma=-0.956+j0.044$, $|\Gamma|^2=0.92$, so 92 percent of the power is reflected; $\tau\approx0.044(1+j)$.

**Sources**: `Electromagnetics/Lectures Slides/lect_36.pdf`; lecture order from `Electromagnetics/ECE311_Spring2024_Schedule.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Reflection and transmission of waves]]
- [[Electromagnetic wave]]
- [[Transmission line]]
- [[ECE311 lect_35 - Power absorption]]
- [[ECE311 lect_37 - Standing waves]]
