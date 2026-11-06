---
type: concept
area: em
source-ref: "ECE 311 slides, lect_34, lect_35"
tags: [electromagnetics, pde]
---

# Poynting theorem

**Summary**: Conservation of electromagnetic energy, the Poynting vector, average power of a plane wave, and power absorption in lossy media.

## Derivation and statement (lect_34)
Start from $\nabla\cdot(E\times H)=H\cdot(\nabla\times E)-E\cdot(\nabla\times H)$ with Faraday and Ampere, in linear isotropic media (PDF pp. 2-4):
$$E\cdot J_v=\sigma E^2,\qquad \partial w_m/\partial t=\mu H\cdot\partial H/\partial t,\ \ \partial w_e/\partial t=\varepsilon E\cdot\partial E/\partial t$$
Poynting theorem:
$$\oint_s(E\times H)\cdot ds=-\frac{dW_m}{dt}-\frac{dW_e}{dt}-\int_v\sigma E^2dv$$
Energy densities $w_e=\tfrac12E\cdot D$ ([[Electrostatic energy]]), $w_m=\tfrac12H\cdot B$; loss $E\cdot J$ ([[Ohm's law and current density]]).

## Poynting vector
$$\mathcal P=E\times H\ \ (\mathrm{W/m^2}),\qquad |\mathcal P|=EH=E^2/\eta$$
with $\mathcal P\parallel k$ in simple media. Time average for $E=E_0\cos(\omega t-kz)$:
$$\overline{\mathcal P}=E_0^2/2\eta$$
Lossy wave $E_0e^{-j\beta z}e^{-\alpha z}$: $\overline{\mathcal P}=\frac{E_0^2}{2\eta}e^{-2\alpha z}$. Phasor form uses $\nabla\times E=-j\omega\mu H$ and $\nabla\times H=J_v+j\omega\varepsilon E$; time-harmonic average $\overline{\mathcal P}=\tfrac12\mathrm{Re}(E\times H^*)$ (wiki note).

> [!example] Example 34-1 (lect_34, PDF p. 3)
> Parallel-plate line (width $w$, spacing $d$): $E_y=-V/d$, $H_x=i/w$, so $\mathcal P=Vi/(wd)\,a_z$ and $P=Vi$: the power is carried by the fields between the conductors.

> [!example] Examples 34-2 to 34-5 (lect_34, PDF pp. 4-7)
> 10 V/m at 100 MHz in air: $0.265\cos^2(\omega t-kz)$ W/m$^2$. Sunlight at $1.3$ kW/m$^2$: total power $1.7\times10^{17}$ W (170 PW) and $E\approx990$ V/m. 10 W laser, 1 mm radius: $3.2\times10^6$ W/m$^2$ and $E_0=4.9\times10^4$ V/m. With $\alpha=0.1$ m$^{-1}$ power halves after $z=\ln2/2\alpha=3.5$ m.

## Power absorption (lect_35)
Plane wave through an absorbing medium $(\varepsilon'-j\varepsilon'',\sigma)$ (PDF pp. 2-4): phasor fields $E_x=E_0e^{-\alpha z}e^{-j\beta z}$ with $\eta=\omega\mu/\kappa$ and $|\eta|=E_0/H_0$. Power through a slab of area $\Delta s$ and thickness $\Delta z$, from the Poynting vector:
$$\oint\mathcal P\cdot ds=-\frac{\beta E_0^2}{2\omega\mu}\left(1-e^{-2\alpha\Delta z}\right)\Delta s$$
Right side of the Poynting theorem: absorbed power density
$$P_v^{abs}=\tfrac12(\sigma+\omega\varepsilon'')E_0^2$$
Consistency of the two sides requires
$$\frac{\sigma+\omega\varepsilon''}{2\alpha}=\frac{\beta}{\omega\mu}$$
which follows from $-\mathrm{Im}(\kappa^2)=\omega\mu(\omega\varepsilon''+\sigma)=2\alpha\beta$. Power density decays as $e^{-2\alpha z}$.

> [!example] Examples 35-1 and 35-2 (lect_35, PDF pp. 5-6)
> 1 GHz, $\varepsilon_r=2.5-j0.5$: $\beta=33.3$ m$^{-1}$, $\alpha=3.31$ m$^{-1}$, $\lambda=0.189$ m, 90 percent of power absorbed at $z=\ln10/2\alpha=0.348$ m. With $E_0=10$ V/m the absorbed power per unit area is 0.189 W/m$^2$.

> [!example] Example 35-3 (lect_35, PDF pp. 6-7)
> Saltwater, 500 MHz, $\sigma=4.8$ S/m, $\varepsilon_r=80$: $\beta=122$ m$^{-1}$, $\alpha=78$ m$^{-1}$, $\lambda=0.052$ m, power halves at $z=0.0044$ m. Example 35-4 (PDF p. 7) revisits the parallel-plate line with finite conductor conductivity; not read in detail (see [[Transmission line]] for the loss model).

**Covered in**: ECE 311 lect_34, lect_35 (courses/ECE 311/Lectures Slides/lect_34.pdf, courses/ECE 311/Lectures Slides/lect_35.pdf)
**Sources**: ECE 311 lecture slides (Spring 2024, Prof. D. S. Elliott): `courses/ECE 311/Lectures Slides/lect_34.pdf`, `courses/ECE 311/Lectures Slides/lect_35.pdf`; lecture order from `courses/ECE 311/ECE311_Spring2024_Schedule.pdf`. Statements marked Wiki note are standard physics not read in the slides.
**Last updated**: 2026-11-06

---

## Related pages
- [[Electromagnetic wave]]
- [[Electrostatic energy]]
- [[Ohm's law and current density]]
- [[Transmission line]]
