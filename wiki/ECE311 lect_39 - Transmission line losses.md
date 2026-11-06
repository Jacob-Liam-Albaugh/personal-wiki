---
type: lecture
area: em
source-ref: "ECE 311 lect_39, slides pp. 1-10"
tags: [electromagnetics]
course: ece311
lecture: lect_39
---
# ECE311 lect_39 - Transmission line losses

**Summary**: Lossy transmission lines with R and G per unit length; complex propagation constant and Z0.

**Course**: ECE 311 (Electromagnetics I, Purdue, Spring 2024, Prof. D. S. Elliott) · **Lecture date**: Apr 15 (per the schedule) · **File**: `Electromagnetics/Lectures Slides/lect_39.pdf` (10 slides)

---

## Topics
- Sources of loss in a transmission line
- Dielectric loss: G' and attenuation
- Conductor loss: surface impedance, R' and attenuation
- R', L', C', G' for common geometries
- Lossy ladder model, gamma and Z0

## Key results
Loss sources: dielectric absorption or conduction ($\sigma_d$ should be zero but is not), and finite conductor conductivity (PDF p. 2, [4]). Slides are numbered in brackets.
Dielectric loss (PDF pp. 2-4, [5-7]), with $\varepsilon=\varepsilon'-j\varepsilon''$:
$$P_v^{abs}=\tfrac12(\sigma_d+\omega\varepsilon'')E_0^2$$
$$G'=\frac{(\sigma_d+\omega\varepsilon'')w}{d}$$
$$P'_{abs}=\tfrac12(\sigma_d+\omega\varepsilon'')E_0^2\,wd$$
$$\alpha=\tfrac12(\sigma_d+\omega\varepsilon'')\eta_d$$
Conductor loss (PDF pp. 4-6, [8-12]). Surface impedance and surface resistance:
$$Z_s=\eta_c=\sqrt{\pi f\mu/\sigma_c}\,(1+j)=R_s+jX_s$$
$$R_s=X_s=\sqrt{\pi f\mu/\sigma_c}=\frac{1}{\delta\sigma_c}$$
$R_s\propto1/\delta$, not the actual conductor thickness [9]. The current $I=wE_z(0)/\eta_c$ is carried in a skin depth $\delta=1/\sqrt{\pi f\mu\sigma_c}$ [8].
$$P'_{abs}=\tfrac12R'I^2,\qquad R'=\frac{2R_s}{w}$$
$$\alpha=\frac{R_s}{\eta_dd}$$
Parameter table (PDF p. 7, [13]), units F/m, H/m, $\Omega$/m, S/m:
$$\text{parallel plate: }C'=\tfrac{\varepsilon'w}{d},\ L'=\tfrac{\mu d}{w},\ R'=\tfrac{2R_s}{w},\ G'=\tfrac{(\sigma_d+\omega\varepsilon'')w}{d}$$
$$\text{two-wire: }R'=\tfrac{R_s}{\pi a},\ G'=\tfrac{\pi(\sigma_d+\omega\varepsilon'')}{\cosh^{-1}(d/2a)}$$
$$\text{coax: }R'=\tfrac{R_s}{2\pi}\left(\tfrac1a+\tfrac1b\right),\ G'=\tfrac{2\pi(\sigma_d+\omega\varepsilon'')}{\ln(b/a)}$$
Lossy ladder (PDF pp. 8-9, [15-16]) adds $R'\Delta z$ in series and $G'\Delta z$ in shunt:
$$\frac{dV}{dz}=-(R'+j\omega L')I,\qquad \frac{dI}{dz}=-(G'+j\omega C')V$$
$$\gamma=\alpha+j\beta=\sqrt{(R'+j\omega L')(G'+j\omega C')}$$
$$Z_0=\frac{V_0}{I_0}=\sqrt{\frac{R'+j\omega L'}{G'+j\omega C'}}$$
Slide [17-18]: $V=V_0e^{-\alpha z}e^{-j\beta z}$, and $\alpha=\mathrm{Re}(\gamma)$, $\beta=\mathrm{Im}(\gamma)$.

## Examples
> [!example] Hotseat (PDF p. 7, [14])
> Slide asks which of $\sigma_c$ large or small and $(\sigma_d+\omega\varepsilon'')$ large or small minimises attenuation; the answer is not on the slide. Wiki note: from $\alpha=\tfrac12(\sigma_d+\omega\varepsilon'')\eta_d$ and $R_s\propto1/\sqrt{\sigma_c}$, large $\sigma_c$ and small $(\sigma_d+\omega\varepsilon'')$.

**Sources**: `Electromagnetics/Lectures Slides/lect_39.pdf`; lecture order from `Electromagnetics/ECE311_Spring2024_Schedule.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Transmission line]]
- [[ECE311 lect_31 - Plane waves in lossy media]]
- [[ECE311 lect_38 - Transmission lines intro]]
- [[ECE311 lect_41 - Finite-length lines and input impedance]]
