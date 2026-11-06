---
type: lecture
area: em
source-ref: "ECE 311 lect_30, slides pp. 1-9"
tags: [electromagnetics]
course: ece311
lecture: lect_30
---
# ECE311 lect_30 - Plane waves

**Summary**: Time-harmonic uniform plane waves: wavenumber, wavelength, phase velocity, intrinsic impedance.

**Course**: ECE 311 (Electromagnetics I, Purdue, Spring 2024, Prof. D. S. Elliott) · **Lecture date**: Mar 25 (per the schedule) · **File**: `Electromagnetics/Lectures Slides/lect_30.pdf` (9 slides)

---

## Topics
- Plane wave in $+z$: transverse E, field H and impedance
- Intrinsic impedance of vacuum
- Plane wave in an arbitrary direction, propagation vector
- Phase velocity again

## Key results
Phasor plane wave $E=E_0e^{j(\omega t-kz)}$ (slides use $k$, not $\beta$; PDF pp. 2-6, slide numbers in brackets).
- $\nabla\cdot E=0$ forces $E_z=0$: $E$ is transverse to the propagation direction [3].
- Faraday's law gives $H=\dfrac{1}{\omega\mu}\nabla\times E$, so $E$ and $H$ are in phase [4-5].
$$|E|/|H|=\sqrt{\mu/\varepsilon}\equiv\eta\quad(\text{intrinsic impedance})$$
$$\eta_0=\sqrt{\mu_0/\varepsilon_0}=120\pi\ \Omega\approx377\ \Omega$$
- $E\cdot H=0$ and $E\times H$ points along propagation [6-7].
Arbitrary direction (pp. 8-13): $E=E_0e^{j(\omega t-k\cdot r)}$ with propagation vector $k$, $|k|=\omega\sqrt{\varepsilon\mu}=2\pi/\lambda$.
$$k\cdot E=0,\qquad k\cdot H=0$$
$$H=\tfrac1\eta\,\hat k\times E,\qquad E=-\eta\,\hat k\times H$$
$$u_p=\omega/k=1/\sqrt{\varepsilon\mu}$$
Derived by $\nabla\to-jk$ on $e^{-jk\cdot r}$ (pp. 9-11).

## Examples
> [!example] Example 30-1 (PDF p. 6)
> Lossless non-magnetic medium, $\varepsilon_r=4$, $k=(3a_x+4a_y-\sqrt{11}a_z)$ m$^{-1}$: $|k|=6$ m$^{-1}$, $\omega=ck/\sqrt{\varepsilon_r}=9\times10^8$ s$^{-1}$, $f=143$ MHz.
> i-Clicker: $E=10$ V/m in vacuum gives $|H|=E/\eta_0$ (about 26.5 mA/m, arithmetic).

**Sources**: `Electromagnetics/Lectures Slides/lect_30.pdf`; lecture order from `Electromagnetics/ECE311_Spring2024_Schedule.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Electromagnetic wave]]
- [[ECE311 lect_29 - Wave equation and plane waves]]
- [[ECE311 lect_31 - Plane waves in lossy media]]
