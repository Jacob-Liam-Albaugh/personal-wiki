---
type: lecture
area: em
source-ref: "ECE 311 lect_31, slides pp. 1-8"
tags: [electromagnetics]
course: ece311
lecture: lect_31
---
# ECE311 lect_31 - Plane waves in lossy media

**Summary**: Complex propagation constant gamma = alpha + j beta for conducting media; attenuation, good dielectrics and good conductors.

**Course**: ECE 311 (Electromagnetics I, Purdue, Spring 2024, Prof. D. S. Elliott) · **Lecture date**: Mar 27 (per the schedule) · **File**: `Electromagnetics/Lectures Slides/lect_31.pdf` (8 slides)

---

## Topics
- Complex propagation constant $\gamma=\alpha+j\beta$
- General $\kappa$ for a conducting, absorbing medium
- Lossy dielectric (weak absorption)
- Good conductor, skin depth

## Key results
Attenuation (slide numbers in brackets, PDF pp. 2-7). $E(z)=E_0e^{-j\kappa z}$ with complex wavenumber:
$$\kappa=\beta-j\alpha,\qquad \gamma=\alpha+j\beta=j\kappa$$
$\alpha$ is the attenuation constant and $\beta$ the phase constant [3]. Loss enters through $\sigma$ and $\varepsilon=\varepsilon'-j\varepsilon''$ [5]; Ampere and Faraday give the general result [6]:
$$\kappa=\omega\sqrt{\varepsilon\mu}\sqrt{1-\frac{j\sigma}{\omega\varepsilon}}$$
Still $E\perp\kappa$ and $H\perp\kappa$ [4].
Lossy dielectric ($\sigma=0$, $\varepsilon''\ll\varepsilon'$) [7, 9]:
$$\alpha\simeq\frac{\omega\varepsilon''}{2}\sqrt{\mu/\varepsilon'}$$
$$\beta\simeq\omega\sqrt{\varepsilon'\mu}\left[1+\tfrac18(\varepsilon''/\varepsilon')^2\right]$$
$$\eta\simeq\sqrt{\mu/\varepsilon'}\left(1+\tfrac{j\varepsilon''}{2\varepsilon'}\right)$$
$H$ lags $E$ by $\tan^{-1}(\varepsilon''/2\varepsilon')$; $u_p\simeq\frac{1}{\sqrt{\varepsilon'\mu}}\left[1-\frac{\varepsilon''}{8\varepsilon'}\right]$.
Good conductor ($\sigma/\omega\varepsilon\gg1$) [11-12]:
$$\alpha=\beta=\sqrt{\pi f\mu\sigma}$$
$$\delta\equiv\alpha^{-1}=(\pi f\mu\sigma)^{-1/2}\quad(\text{skin depth})$$
$$\eta=\sqrt{\pi f\mu/\sigma}\,(1+j),\qquad u_p=\sqrt{2\omega/\mu\sigma}$$
$H$ lags $E$ by $45^\circ$.

## Examples
> [!example] Example 31-1 and 31-2 (PDF pp. 4-5)
> 100 MHz, $\varepsilon_r=3.0-j0.1$, non-magnetic: $\beta=3.6$ m$^{-1}$, $\alpha=0.061$ m$^{-1}$; $H$ lags $E$ by 0.017 rad (0.95 degrees); $u_p=1.7\times10^8$ m/s.

> [!example] Example 31-3 (PDF p. 6)
> Copper at 100 MHz: $\alpha=\beta=1.51\times10^5$ m$^{-1}$, $\delta=6.6\ \mu$m, $\lambda=41.5\ \mu$m (3 m in air); $\eta=0.0026(1+j)\ \Omega$.

**Sources**: `Electromagnetics/Lectures Slides/lect_31.pdf`; lecture order from `Electromagnetics/ECE311_Spring2024_Schedule.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Electromagnetic wave]]
- [[Ohm's law and current density]]
- [[ECE311 lect_35 - Power absorption]]
- [[ECE311 lect_30 - Plane waves]]
- [[ECE311 lect_32 - EM spectrum]]
