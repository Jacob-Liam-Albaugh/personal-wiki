---
type: lecture
area: em
source-ref: "ECE 311 lect_35, slides pp. 1-10"
tags: [electromagnetics]
course: ece311
lecture: lect_35
---
# ECE311 lect_35 - Power absorption

**Summary**: Power loss in a lossy medium as the wave decays, and the power delivered to a conductor.

**Course**: ECE 311 (Electromagnetics I, Purdue, Spring 2024, Prof. D. S. Elliott) · **Lecture date**: Apr 5 (per the schedule) · **File**: `Electromagnetics/Lectures Slides/lect_35.pdf` (10 slides)

---

## Topics
- Wave in an absorbing slab
- Power absorbed per unit volume
- Check against the Poynting theorem

## Key results
Plane wave through an absorbing medium $(\varepsilon'-j\varepsilon'',\sigma)$ (slide numbers in brackets, PDF pp. 2-4). Phasor fields $E_x=E_0e^{-\alpha z}e^{-j\beta z}$ with $\eta=\omega\mu/\kappa$ and $|\eta|=E_0/H_0$ [3].
Power through a slab of area $\Delta s$ and thickness $\Delta z$, from the Poynting vector [5]:
$$\oint\mathcal P\cdot ds=-\frac{\beta E_0^2}{2\omega\mu}\left(1-e^{-2\alpha\Delta z}\right)\Delta s$$
Right side of the Poynting theorem: absorbed power density [6]
$$P_v^{abs}=\tfrac12(\sigma+\omega\varepsilon'')E_0^2$$
Consistency of the two sides requires [7-8]:
$$\frac{\sigma+\omega\varepsilon''}{2\alpha}=\frac{\beta}{\omega\mu}$$
which follows from $-\mathrm{Im}(\kappa^2)=\omega\mu(\omega\varepsilon''+\sigma)=2\alpha\beta$. Power density decays as $e^{-2\alpha z}$.

## Examples
> [!example] Example 35-1 and 35-2 (PDF pp. 5-6)
> 1 GHz, $\varepsilon_r=2.5-j0.5$: $\beta=33.3$ m$^{-1}$, $\alpha=3.31$ m$^{-1}$, $\lambda=0.189$ m, 90 percent of power absorbed at $z=\ln10/2\alpha=0.348$ m. With $E_0=10$ V/m the absorbed power per unit area is 0.189 W/m$^2$ (pp. 5-6).

> [!example] Example 35-3 (PDF pp. 6-7)
> Saltwater, 500 MHz, $\sigma=4.8$ S/m, $\varepsilon_r=80$: $\beta=122$ m$^{-1}$, $\alpha=78$ m$^{-1}$, $\lambda=0.052$ m, power halves at $z=0.0044$ m.
> Example 35-4 (PDF p. 7) revisits the parallel-plate line with finite conductor conductivity; not read in detail.

**Sources**: `Electromagnetics/Lectures Slides/lect_35.pdf`; lecture order from `Electromagnetics/ECE311_Spring2024_Schedule.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Poynting theorem]]
- [[Electromagnetic wave]]
- [[Ohm's law and current density]]
- [[ECE311 lect_34 - Plane wave power flow]]
- [[ECE311 lect_36 - Reflection and transmission]]
