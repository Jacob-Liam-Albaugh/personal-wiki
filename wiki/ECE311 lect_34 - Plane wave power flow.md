---
type: lecture
area: em
source-ref: "ECE 311 lect_34, slides pp. 1-8"
tags: [electromagnetics]
course: ece311
lecture: lect_34
---
# ECE311 lect_34 - Plane wave power flow

**Summary**: Poynting theorem: energy conservation in EM fields, Poynting vector and average power of a plane wave.

**Course**: ECE 311 (Electromagnetics I, Purdue, Spring 2024, Prof. D. S. Elliott) · **Lecture date**: Apr 3 (per the schedule) · **File**: `Electromagnetics/Lectures Slides/lect_34.pdf` (8 slides)

---

## Topics
- Derivation of the Poynting theorem
- Poynting vector, power density
- Time-averaged power density
- Poynting theorem with phasors

## Key results
Start from $\nabla\cdot(E\times H)=H\cdot(\nabla\times E)-E\cdot(\nabla\times H)$ with Faraday and Ampere, in linear isotropic media (slide numbers in brackets, PDF pp. 2-4):
$$E\cdot J_v=\sigma E^2,\qquad \partial w_m/\partial t=\mu H\cdot\partial H/\partial t,\ \ \partial w_e/\partial t=\varepsilon E\cdot\partial E/\partial t$$
Poynting theorem [4]:
$$\oint_s(E\times H)\cdot ds=-\frac{dW_m}{dt}-\frac{dW_e}{dt}-\int_v\sigma E^2dv$$
Poynting vector, with $\mathcal P\parallel k$ in simple media [5]:
$$\mathcal P=E\times H\ \ (\mathrm{W/m^2}),\qquad |\mathcal P|=EH=E^2/\eta$$
Time average for $E=E_0\cos(\omega t-kz)$ [9]:
$$\overline{\mathcal P}=E_0^2/2\eta$$
Lossy wave $E_0e^{-j\beta z}e^{-\alpha z}$: $\overline{\mathcal P}=\frac{E_0^2}{2\eta}e^{-2\alpha z}$ [13]. Phasor form uses $\nabla\times E=-j\omega\mu H$ and $\nabla\times H=J_v+j\omega\varepsilon E$ (PDF p. 7).

## Examples
> [!example] Example 34-1 (PDF p. 3)
> Parallel-plate line (width $w$, spacing $d$): $E_y=-V/d$, $H_x=i/w$, so $\mathcal P=Vi/(wd)\,a_z$ and $P=Vi$: the power is carried by the fields between the conductors.

> [!example] Examples 34-2 to 34-5 (PDF pp. 4-7)
> 10 V/m at 100 MHz in air: $0.265\cos^2(\omega t-kz)$ W/m$^2$. Sunlight at $1.3$ kW/m$^2$: total power $1.7\times10^{17}$ W (170 PW) and $E\approx990$ V/m. 10 W laser, 1 mm radius: $3.2\times10^6$ W/m$^2$ and $E_0=4.9\times10^4$ V/m. With $\alpha=0.1$ m$^{-1}$ power halves after $z=\ln2/2\alpha=3.5$ m.

**Sources**: `Electromagnetics/Lectures Slides/lect_34.pdf`; lecture order from `Electromagnetics/ECE311_Spring2024_Schedule.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Poynting theorem]]
- [[Electromagnetic wave]]
- [[Electrostatic energy]]
- [[ECE311 lect_33 - Polarization]]
- [[ECE311 lect_35 - Power absorption]]
