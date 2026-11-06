---
type: lecture
area: em
source-ref: "ECE 311 lect_29, slides pp. 1-9"
tags: [electromagnetics, pde]
course: ece311
lecture: lect_29
---
# ECE311 lect_29 - Wave equation and plane waves

**Summary**: Source-free Maxwell's equations give the vector wave equation; uniform plane waves in lossless media and their properties.

**Course**: ECE 311 (Electromagnetics I, Purdue, Spring 2024, Prof. D. S. Elliott) · **Lecture date**: Mar 22 (per the schedule) · **File**: `Electromagnetics/Lectures Slides/lect_29.pdf` (9 slides)

---

## Topics
- Maxwell's equations in a linear source-free medium
- Derivation of the wave equations for $E$ and $H$
- Uniform plane wave, propagation constant $k$, wavelength
- Phase velocity

## Key results
Linear source-free medium (slides, PDF p. 2):
$$\nabla\times E=-\mu\,\partial H/\partial t,\qquad \nabla\times H=\varepsilon\,\partial E/\partial t$$
$$\nabla\cdot E=0,\qquad \nabla\cdot H=0$$
Taking the curl and using $\nabla\times\nabla\times H=\nabla(\nabla\cdot H)-\nabla^2H$ gives the wave equations (pp. 3-5):
$$\nabla^2E-\varepsilon\mu\,\partial^2E/\partial t^2=0$$
$$\nabla^2H-\varepsilon\mu\,\partial^2H/\partial t^2=0$$
Uniform plane wave $E(z,t)=E_0\cos(\omega t-kz)$ with constant $E_0$ (p. 6) solves it if (p. 9):
$$k=\omega\sqrt{\varepsilon\mu}$$
Wavenumber and phase velocity (pp. 7, 10-11):
$$k=2\pi/\lambda,\qquad u_p=\omega/k=1/\sqrt{\varepsilon\mu}$$
$$f=u_p/\lambda,\qquad c=1/\sqrt{\varepsilon_0\mu_0}=2.998\times10^8\ \mathrm{m/s}$$
$u_p$ depends only on the material (not on $\omega$ except through $\varepsilon(\omega),\mu(\omega)$); group velocity is not covered. $E_0\sin(\omega t+kz)$ travels in $-z$ (p. 14).

## Examples
> [!example] i-Clicker (PDF p. 7)
> Wavelength of a 300 MHz wave in vacuum: $\lambda=u_p/f=c/f\approx1$ m (arithmetic, wiki note).

**Sources**: `Electromagnetics/Lectures Slides/lect_29.pdf`; lecture order from `Electromagnetics/ECE311_Spring2024_Schedule.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Electromagnetic wave]]
- [[Maxwell's equations]]
- [[ECE311 lect_30 - Plane waves]]
- [[ECE311 lect_28 - Potentials and time-harmonic fields]]
