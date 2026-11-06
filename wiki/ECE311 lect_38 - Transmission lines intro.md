---
type: lecture
area: em
source-ref: "ECE 311 lect_38, slides pp. 1-10"
tags: [electromagnetics]
course: ece311
lecture: lect_38
---
# ECE311 lect_38 - Transmission lines intro

**Summary**: Why circuit theory fails at short wavelengths, the distributed model of a line, and the telegrapher equations.

**Course**: ECE 311 (Electromagnetics I, Purdue, Spring 2024, Prof. D. S. Elliott) · **Lecture date**: Apr 12 (per the schedule) · **File**: `Electromagnetics/Lectures Slides/lect_38.pdf` (10 slides)

---

## Topics
- Boundary conditions at perfect conductors
- Parallel-plate line: fields, charge and current
- Circuit variables V and I, L' and C'
- Wave equations, beta and phase velocity
- Characteristic impedance Z0
- Coax, twin lead, microstrip formulas

## Key results
Starting point: UPW solutions between the conductors, treated as perfect conductors with a lossless dielectric. Boundary conditions: $E_{tan}=0$, $B_n=0$, $D_n=\rho_s$, $H_{tan}=J_s$ (PDF p. 3, [5]).
Parallel-plate line, fields $e^{-j\beta z}$ (PDF pp. 4-5, [8-10]):
$$\mathbf E=a_yE_0e^{-j\beta z}$$
$$\mathbf H=-a_x\tfrac{E_0}{\eta}e^{-j\beta z}$$
$$\rho_s=-\varepsilon E_0e^{-j\beta z}$$
$$\mathbf J_s=-a_z\tfrac{E_0}{\eta}e^{-j\beta z}$$
Charge conservation $\partial J_{s,z}/\partial z+\partial\rho_s/\partial t=0$ is checked on [9]. $E_y,H_x,\rho_s,J_s$ share the $e^{-j\beta z}$ dependence and propagate as a unit [10].
Circuit variables (PDF p. 5, [13-14]):
$$V=-E_yd,\qquad I=H_xw$$
$$\frac{dV}{dz}=-j\omega L'I,\qquad L'=\frac{\mu d}{w}$$
$$\frac{dI}{dz}=-j\omega C'V,\qquad C'=\frac{\varepsilon w}{d}$$
$$\frac{d^2V}{dz^2}+\omega^2L'C'V=0$$
Ladder model (KVL, KCL on $L'\Delta z$, $C'\Delta z$) gives the same pair [15]. Solutions $V=V_0e^{-j\beta z}$, $I=I_0e^{-j\beta z}$ (PDF pp. 6-7, [16-18]):
$$\beta=\omega\sqrt{L'C'}=\omega\sqrt{\varepsilon\mu}=\tfrac{2\pi}{\lambda}$$
$$u_p=\frac{\omega}{\beta}=\frac{1}{\sqrt{\varepsilon\mu}}$$
$$Z_0=\frac{V_0}{I_0}=\sqrt{\frac{L'}{C'}}=\eta\frac dw\ \text{(parallel plate)}$$
$R_0=\mathrm{Re}(Z_0)$ is not equated to losses; $Z_0$ is defined by $V_0/I_0$ even for perfect conductors [17].
Common lines (PDF p. 2, [3-4], [5]):
$$\text{coax: }C'=\frac{2\pi\varepsilon}{\ln(b/a)},\quad L'\simeq\frac{\mu}{2\pi}\ln\frac ba$$
$$\text{twin lead: }C'=\frac{\pi\varepsilon_0}{\cosh^{-1}(d/2a)},\quad L'\simeq\frac{\mu_0}{\pi}\cosh^{-1}\frac{d}{2a}$$
Microstrip has no simple formula; use numerics or tables [4].

## Examples
> [!example] i-Clicker (PDF p. 7, [17])
> Coax with $C'=109$ pF/m and $L'=0.285\ \mu$H/m: $Z_0=\sqrt{L'/C'}\approx51\ \Omega$ (answer b).

**Sources**: `Electromagnetics/Lectures Slides/lect_38.pdf`; lecture order from `Electromagnetics/ECE311_Spring2024_Schedule.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Transmission line]]
- [[Capacitance]]
- [[Inductance]]
- [[ECE311 lect_37 - Standing waves]]
- [[ECE311 lect_39 - Transmission line losses]]
