---
type: concept
area: em
source-ref: "ECE 311 slides, lect_29, lect_30, lect_31, lect_32, lect_33, lect_34, lect_35, lect_36, lect_37"
tags: [electromagnetics, pde, signals]
---

# Electromagnetic wave

**Summary**: Self-sustaining E and H fields that propagate; the wave equation, uniform plane waves in lossless and lossy media, skin depth, and the EM spectrum.

## Wave equation (lect_29)
Linear source-free medium (PDF p. 2):
$$\nabla\times E=-\mu\,\partial H/\partial t,\qquad \nabla\times H=\varepsilon\,\partial E/\partial t$$
$$\nabla\cdot E=0,\qquad \nabla\cdot H=0$$
Taking the curl and using $\nabla\times\nabla\times H=\nabla(\nabla\cdot H)-\nabla^2H$ gives (pp. 3-5):
$$\nabla^2E-\varepsilon\mu\,\partial^2E/\partial t^2=0$$
$$\nabla^2H-\varepsilon\mu\,\partial^2H/\partial t^2=0$$
Uniform plane wave $E(z,t)=E_0\cos(\omega t-kz)$ with constant $E_0$ (p. 6) solves it if (p. 9) $k=\omega\sqrt{\varepsilon\mu}$. Wavenumber and phase velocity (pp. 7, 10-11):
$$k=2\pi/\lambda,\qquad u_p=\omega/k=1/\sqrt{\varepsilon\mu}$$
$$f=u_p/\lambda,\qquad c=1/\sqrt{\varepsilon_0\mu_0}=2.998\times10^8\ \mathrm{m/s}$$
$u_p$ depends only on the material (not on $\omega$ except through $\varepsilon(\omega),\mu(\omega)$); group velocity is not covered. $E_0\sin(\omega t+kz)$ travels in $-z$ (p. 14).

> [!example] i-Clicker (lect_29, PDF p. 7)
> Wavelength of a 300 MHz wave in vacuum: $\lambda=c/f\approx1$ m (wiki arithmetic).

## Plane waves (lect_30)
Phasor plane wave $E=E_0e^{j(\omega t-kz)}$ (slides use $k$, not $\beta$).
- $\nabla\cdot E=0$ forces $E_z=0$: $E$ is transverse to the propagation direction.
- Faraday's law gives $H=\dfrac{1}{\omega\mu}\nabla\times E$, so $E$ and $H$ are in phase.
$$|E|/|H|=\sqrt{\mu/\varepsilon}\equiv\eta\quad(\text{intrinsic impedance})$$
$$\eta_0=\sqrt{\mu_0/\varepsilon_0}=120\pi\ \Omega\approx377\ \Omega$$
- $E\cdot H=0$ and $E\times H$ points along propagation.

Arbitrary direction (pp. 8-13): $E=E_0e^{j(\omega t-k\cdot r)}$ with propagation vector $k$, $|k|=\omega\sqrt{\varepsilon\mu}=2\pi/\lambda$, derived by $\nabla\to-jk$ on $e^{-jk\cdot r}$ (pp. 9-11):
$$k\cdot E=0,\qquad k\cdot H=0$$
$$H=\tfrac1\eta\,\hat k\times E,\qquad E=-\eta\,\hat k\times H$$
$$u_p=\omega/k=1/\sqrt{\varepsilon\mu}$$

> [!example] Example 30-1 (lect_30, PDF p. 6)
> Lossless non-magnetic medium, $\varepsilon_r=4$, $k=(3a_x+4a_y-\sqrt{11}a_z)$ m$^{-1}$: $|k|=6$ m$^{-1}$, $\omega=ck/\sqrt{\varepsilon_r}=9\times10^8$ s$^{-1}$, $f=143$ MHz. i-Clicker: $E=10$ V/m in vacuum gives $|H|=E/\eta_0$ (about 26.5 mA/m, arithmetic).

## Lossy media (lect_31)
$E(z)=E_0e^{-j\kappa z}$ with complex wavenumber (PDF pp. 2-7):
$$\kappa=\beta-j\alpha,\qquad \gamma=\alpha+j\beta=j\kappa$$
$\alpha$ is the attenuation constant and $\beta$ the phase constant. Loss enters through $\sigma$ and $\varepsilon=\varepsilon'-j\varepsilon''$; Ampere and Faraday give the general result
$$\kappa=\omega\sqrt{\varepsilon\mu}\sqrt{1-\frac{j\sigma}{\omega\varepsilon}}$$
Still $E\perp\kappa$ and $H\perp\kappa$.

Lossy dielectric ($\sigma=0$, $\varepsilon''\ll\varepsilon'$):
$$\alpha\simeq\frac{\omega\varepsilon''}{2}\sqrt{\mu/\varepsilon'}$$
$$\beta\simeq\omega\sqrt{\varepsilon'\mu}\left[1+\tfrac18(\varepsilon''/\varepsilon')^2\right]$$
$$\eta\simeq\sqrt{\mu/\varepsilon'}\left(1+\tfrac{j\varepsilon''}{2\varepsilon'}\right)$$
$H$ lags $E$ by $\tan^{-1}(\varepsilon''/2\varepsilon')$; $u_p\simeq\frac{1}{\sqrt{\varepsilon'\mu}}\left[1-\frac{\varepsilon''}{8\varepsilon'}\right]$.

Good conductor ($\sigma/\omega\varepsilon\gg1$):
$$\alpha=\beta=\sqrt{\pi f\mu\sigma}$$
$$\delta\equiv\alpha^{-1}=(\pi f\mu\sigma)^{-1/2}\quad(\text{skin depth})$$
$$\eta=\sqrt{\pi f\mu/\sigma}\,(1+j),\qquad u_p=\sqrt{2\omega/\mu\sigma}$$
$H$ lags $E$ by $45^\circ$.

> [!example] Examples 31-1 and 31-2 (lect_31, PDF pp. 4-5)
> 100 MHz, $\varepsilon_r=3.0-j0.1$, non-magnetic: $\beta=3.6$ m$^{-1}$, $\alpha=0.061$ m$^{-1}$; $H$ lags $E$ by 0.017 rad (0.95 degrees); $u_p=1.7\times10^8$ m/s.

> [!example] Example 31-3 (lect_31, PDF p. 6)
> Copper at 100 MHz: $\alpha=\beta=1.51\times10^5$ m$^{-1}$, $\delta=6.6\ \mu$m, $\lambda=41.5\ \mu$m (3 m in air); $\eta=0.0026(1+j)\ \Omega$.

## EM spectrum (lect_32)
$c=f\lambda$. Bands run from radio and microwaves through infrared, visible, ultraviolet, X-ray to gamma rays; low-frequency wave effects are covered by the same [[Maxwell's equations]]. Circuit theory fails when the line length is comparable to $\lambda$, which motivates [[Transmission line]] models.

## Topics
- [[Wave polarization]].
- Power flow and absorption: [[Poynting theorem]].
- Interfaces and standing waves: [[Reflection and transmission of waves]].
- Guided version: [[Transmission line]].

**Covered in**: ECE 311 lect_29, lect_30, lect_31, lect_32, lect_33, lect_34, lect_35, lect_36, lect_37 (Electromagnetics/Lectures Slides/lect_29.pdf, Electromagnetics/Lectures Slides/lect_30.pdf, Electromagnetics/Lectures Slides/lect_31.pdf, Electromagnetics/Lectures Slides/lect_32.pdf, Electromagnetics/Lectures Slides/lect_33.pdf, Electromagnetics/Lectures Slides/lect_34.pdf, Electromagnetics/Lectures Slides/lect_35.pdf, Electromagnetics/Lectures Slides/lect_36.pdf, Electromagnetics/Lectures Slides/lect_37.pdf)
**Sources**: ECE 311 lecture slides (Spring 2024, Prof. D. S. Elliott): `Electromagnetics/Lectures Slides/lect_29.pdf`, `Electromagnetics/Lectures Slides/lect_30.pdf`, `Electromagnetics/Lectures Slides/lect_31.pdf`, `Electromagnetics/Lectures Slides/lect_32.pdf`, `Electromagnetics/Lectures Slides/lect_33.pdf`, `Electromagnetics/Lectures Slides/lect_34.pdf`, `Electromagnetics/Lectures Slides/lect_35.pdf`, `Electromagnetics/Lectures Slides/lect_36.pdf`, `Electromagnetics/Lectures Slides/lect_37.pdf`; lecture order from `Electromagnetics/ECE311_Spring2024_Schedule.pdf`. Statements marked Wiki note are standard physics not read in the slides.
**Last updated**: 2026-11-06

---

## Related pages
- [[Maxwell's equations]]
- [[Wave polarization]]
- [[Poynting theorem]]
- [[Reflection and transmission of waves]]
- [[Transmission line]]
- [[Impedance matching]]
- [[Fourier transform]]
