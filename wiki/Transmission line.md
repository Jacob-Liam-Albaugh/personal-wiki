---
type: concept
area: em
source-ref: "ECE 311 slides, lect_38, lect_39, lect_41, lect_42, lect_44"
tags: [electromagnetics, pde, signals]
---

# Transmission line

**Summary**: Two-conductor guiding structure modelled with per-unit-length L, C, R, G; voltage and current waves, losses, reflection, input impedance, SWR and pulses.

## Distributed model (lect_38)
Circuit theory fails when the line is comparable to $\lambda$. Start from uniform plane-wave solutions between perfect conductors with a lossless dielectric. Boundary conditions: $E_{tan}=0$, $B_n=0$, $D_n=\rho_s$, $H_{tan}=J_s$ (PDF p. 3). Parallel-plate line, fields $e^{-j\beta z}$ (PDF pp. 4-5):
$$\mathbf E=a_yE_0e^{-j\beta z},\qquad \mathbf H=-a_x\tfrac{E_0}{\eta}e^{-j\beta z}$$
$$\rho_s=-\varepsilon E_0e^{-j\beta z},\qquad \mathbf J_s=-a_z\tfrac{E_0}{\eta}e^{-j\beta z}$$
Charge conservation $\partial J_{s,z}/\partial z+\partial\rho_s/\partial t=0$ is checked; $E_y,H_x,\rho_s,J_s$ share the $e^{-j\beta z}$ dependence and propagate as a unit.

Circuit variables (PDF p. 5):
$$V=-E_yd,\qquad I=H_xw$$
$$\frac{dV}{dz}=-j\omega L'I,\qquad L'=\frac{\mu d}{w}$$
$$\frac{dI}{dz}=-j\omega C'V,\qquad C'=\frac{\varepsilon w}{d}$$
$$\frac{d^2V}{dz^2}+\omega^2L'C'V=0$$
A ladder model (KVL, KCL on $L'\Delta z$, $C'\Delta z$) gives the same pair (telegrapher equations). Solutions $V=V_0e^{-j\beta z}$, $I=I_0e^{-j\beta z}$ (PDF pp. 6-7):
$$\beta=\omega\sqrt{L'C'}=\omega\sqrt{\varepsilon\mu}=\tfrac{2\pi}{\lambda}$$
$$u_p=\frac{\omega}{\beta}=\frac{1}{\sqrt{\varepsilon\mu}}$$
$$Z_0=\frac{V_0}{I_0}=\sqrt{\frac{L'}{C'}}=\eta\frac dw\ \text{(parallel plate)}$$
$R_0=\mathrm{Re}(Z_0)$ is not equated to losses; $Z_0$ is defined by $V_0/I_0$ even for perfect conductors.

Common lines (PDF p. 2), see [[Capacitance]] and [[Inductance]]:
$$\text{coax: }C'=\frac{2\pi\varepsilon}{\ln(b/a)},\quad L'\simeq\frac{\mu}{2\pi}\ln\frac ba$$
$$\text{twin lead: }C'=\frac{\pi\varepsilon_0}{\cosh^{-1}(d/2a)},\quad L'\simeq\frac{\mu_0}{\pi}\cosh^{-1}\frac{d}{2a}$$
Microstrip has no simple formula; use numerics or tables.

> [!example] i-Clicker (lect_38, PDF p. 7)
> Coax with $C'=109$ pF/m and $L'=0.285\ \mu$H/m: $Z_0=\sqrt{L'/C'}\approx51\ \Omega$.

## Losses (lect_39)
Sources of loss: dielectric absorption or conduction ($\sigma_d$ should be zero but is not), and finite conductor conductivity (PDF p. 2). Dielectric loss, with $\varepsilon=\varepsilon'-j\varepsilon''$ (pp. 2-4):
$$P_v^{abs}=\tfrac12(\sigma_d+\omega\varepsilon'')E_0^2$$
$$G'=\frac{(\sigma_d+\omega\varepsilon'')w}{d}$$
$$P'_{abs}=\tfrac12(\sigma_d+\omega\varepsilon'')E_0^2\,wd$$
$$\alpha=\tfrac12(\sigma_d+\omega\varepsilon'')\eta_d$$
Conductor loss (pp. 4-6): surface impedance and surface resistance
$$Z_s=\eta_c=\sqrt{\pi f\mu/\sigma_c}\,(1+j)=R_s+jX_s$$
$$R_s=X_s=\sqrt{\pi f\mu/\sigma_c}=\frac{1}{\delta\sigma_c}$$
$R_s\propto1/\delta$, not the actual conductor thickness. The current $I=wE_z(0)/\eta_c$ is carried in a skin depth $\delta=1/\sqrt{\pi f\mu\sigma_c}$ ([[Electromagnetic wave]]).
$$P'_{abs}=\tfrac12R'I^2,\qquad R'=\frac{2R_s}{w},\qquad \alpha=\frac{R_s}{\eta_dd}$$
Parameter table (PDF p. 7), units F/m, H/m, $\Omega$/m, S/m:
$$\text{parallel plate: }C'=\tfrac{\varepsilon'w}{d},\ L'=\tfrac{\mu d}{w},\ R'=\tfrac{2R_s}{w},\ G'=\tfrac{(\sigma_d+\omega\varepsilon'')w}{d}$$
$$\text{two-wire: }R'=\tfrac{R_s}{\pi a},\ G'=\tfrac{\pi(\sigma_d+\omega\varepsilon'')}{\cosh^{-1}(d/2a)}$$
$$\text{coax: }R'=\tfrac{R_s}{2\pi}\left(\tfrac1a+\tfrac1b\right),\ G'=\tfrac{2\pi(\sigma_d+\omega\varepsilon'')}{\ln(b/a)}$$
Lossy ladder (pp. 8-9) adds $R'\Delta z$ in series and $G'\Delta z$ in shunt:
$$\frac{dV}{dz}=-(R'+j\omega L')I,\qquad \frac{dI}{dz}=-(G'+j\omega C')V$$
$$\gamma=\alpha+j\beta=\sqrt{(R'+j\omega L')(G'+j\omega C')}$$
$$Z_0=\frac{V_0}{I_0}=\sqrt{\frac{R'+j\omega L'}{G'+j\omega C'}}$$
$V=V_0e^{-\alpha z}e^{-j\beta z}$, with $\alpha=\mathrm{Re}(\gamma)$, $\beta=\mathrm{Im}(\gamma)$.

> [!example] Hotseat (lect_39, PDF p. 7)
> The slide asks which of $\sigma_c$ large or small and $(\sigma_d+\omega\varepsilon'')$ large or small minimises attenuation; the answer is not on the slide. Wiki note: from $\alpha=\tfrac12(\sigma_d+\omega\varepsilon'')\eta_d$ and $R_s\propto1/\sqrt{\sigma_c}$, large $\sigma_c$ and small $(\sigma_d+\omega\varepsilon'')$.

## Terminated line (lect_41)
Load at $z=0$, source at $z=-\ell$ (PDF pp. 2-3):
$$V(z)=V_0^+e^{-\gamma z}+V_0^-e^{+\gamma z}$$
$$I(z)=I_0^+e^{-\gamma z}+I_0^-e^{+\gamma z}$$
$$\frac{V_0^+}{I_0^+}=Z_0,\qquad \frac{V_0^-}{I_0^-}=-Z_0$$
At the load $V_L=V_0^++V_0^-$ and $I_LZ_0=V_0^+-V_0^-$. With $V_L=Z_LI_L$:
$$\Gamma\equiv\frac{V_0^-}{V_0^+}=\frac{Z_L-Z_0}{Z_L+Z_0}$$
Fields at any $z$ (PDF pp. 3-5):
$$V(z)=I_L[Z_L\cosh(-\gamma z)+Z_0\sinh(-\gamma z)]$$
$$I(z)=\frac{I_L}{Z_0}[Z_L\sinh(-\gamma z)+Z_0\cosh(-\gamma z)]$$
Lossless: replace by $\cos(-\beta z)$ and $j\sin(-\beta z)$. Input impedance $Z_{in}=V(-\ell)/I(-\ell)$:
$$Z_{in}=Z_0\frac{Z_L+Z_0\tanh\gamma\ell}{Z_0+Z_L\tanh\gamma\ell}$$
$$Z_{in}=R_0\frac{Z_L+jR_0\tan\beta\ell}{R_0+jZ_L\tan\beta\ell}\ \text{(lossless)}$$
Special loads (PDF p. 6):
$$Z_L=Z_0:\ \Gamma=0,\ Z_{in}=Z_0$$
$$Z_L=0:\ Z_{in}=jR_0\tan\beta\ell$$
$$Z_L\to\infty:\ Z_{in}=-jR_0\cot\beta\ell$$
A matched load gives $V(z)=I_LZ_0e^{-j\beta z}$, a pure travelling wave. The same algebra as plane-wave normal incidence: [[Reflection and transmission of waves]].

> [!example] i-Clicker (lect_41, PDF p. 3)
> 50 ohm coax, 2 m long, with a 25 ohm load: $\Gamma=(25-50)/(25+50)=-1/3$. The slide does not mark an answer, so this value is computed here.

## SWR and lines as circuit elements (lect_42)
Standing waves, lossless line, $V_0^-=\Gamma V_0^+$ (PDF p. 2):
$$v(z,t)=V_0^+\cos(\omega t-\beta z)+\Gamma V_0^+\cos(\omega t+\beta z)$$
$$V_{max}=V_0^+(1+|\Gamma|),\qquad V_{min}=V_0^+(1-|\Gamma|)$$
Standing wave ratio:
$$S=\frac{|V_{max}|}{|V_{min}|}=\frac{1+|\Gamma|}{1-|\Gamma|},\qquad |\Gamma|=\frac{S-1}{S+1}$$
Also $S=I_{max}/I_{min}$. For $\Gamma=\pm1$, $S\to\infty$; for $\Gamma=0$, $S\to1$. For $\Gamma=-1$, $V_{max}=2V_0^+$, $V_{min}=0$. Locating the phase of $\Gamma$ (PDF p. 8):
$$|V|\ \text{max at}\ z_{max}:\ 2\beta z_{max}+\theta_\Gamma=2n\pi$$
$$\theta_\Gamma=2n\pi-\frac{4\pi z_{max}}{\lambda}$$
Line as a circuit element (PDF pp. 5-6): replace the line by $Z_{in}$ at the source end, $V_{in}=V_g\,Z_{in}/(Z_g+Z_{in})$. Quarter-wave line: $\beta\ell=\pi/2$ and $Z_{in}=R_0^2/Z_L$. Half-wave: $Z_{in}=Z_L$. Power check: $P_g-P_{R_g}=P_L$ with $P_g=\tfrac12V_gI_{in}^*$.

> [!example] Example 42-1 (lect_42, PDF pp. 3-4)
> $Z_0=50$, $Z_L=100\ \Omega$, $V_L=2$ V. $\Gamma=1/3$; $V_0^+=1.5$ V, $V_0^-=0.5$ V; $V_{max}=2$ V, $V_{min}=1$ V, $S=2$; $I_{max}=40$ mA, $I_{min}=20$ mA, $S=2$. $V_{max}$ is at $z=0$ since $\Gamma$ is real and positive. Input impedance for $\ell=\lambda/4$: $25\ \Omega$; $\lambda/2$: $100\ \Omega$; $3\lambda/8$: $(40+30j)\ \Omega$.

> [!example] Example 42-2 (lect_42, PDF pp. 5-7)
> $V_g=16$ V, $Z_g=15\ \Omega$, $Z_0=50\ \Omega$, $Z_L=100\ \Omega$, $\ell=3\lambda/4$. $Z_{in}=R_0^2/Z_L=25\ \Omega$, so $V_{in}=16\cdot25/40=10$ V. $\Gamma=1/3$, $V_0^+=j15$ V, $V_0^-=j5$ V, $V_L=j20$ V. $I_L=j200$ mA, $P_L=\tfrac12|I_L|^2R_L=2$ W. $I_{in}=400$ mA; $P_g=3.2$ W, $P_{R_g}=1.2$ W, difference $2.0$ W matches $P_L$.

> [!example] Example 42-3 (lect_42, PDF pp. 8-9)
> $R_0=50\ \Omega$, $S=1.5$, first voltage maximum at $z=-\lambda/16$. $|\Gamma|=0.2$; $\theta_\Gamma=\pi/4$ so $\Gamma=0.2e^{j\pi/4}$. $Z_L=Z_0(1+\Gamma)/(1-\Gamma)=(63.4+j18.7)\ \Omega$.

## Matching
Quarter-wave sections and stubs: [[Impedance matching]].

## Pulses (lect_44)
Transient pulses bounce between a source and a mismatched load. Reflection coefficients at the two ends:
$$\Gamma_L=\frac{R_L-R_0}{R_L+R_0},\qquad \Gamma_S=\frac{R_g-R_0}{R_g+R_0}$$
The launched pulse is set by a voltage divider $R_0/(R_0+R_g)$ and then repeatedly reflected (bounce diagram). Long pulses accumulate (PDF p. 5):
$$V(\infty)=\frac{V_1^+(1+\Gamma_L)}{1-\Gamma_g\Gamma_L}=V_g\frac{R_L}{R_g+R_L}$$

> [!example] Example 44-1 (lect_44, PDF pp. 3-5, checked)
> $R_0=50$, $R_g=100$, $R_L=25$ give $\Gamma_L=-1/3$ and $\Gamma_g=+1/3$, with $V_1^+=V_g/3$. Successive pulses: $V_1^-=-V_1^+/3$, $V_2^+=-V_1^+/9$, $V_2^-=+V_1^+/27$, $V_3^+=+V_1^+/81$.

**Covered in**: ECE 311 lect_38, lect_39, lect_41, lect_42, lect_44 (courses/ECE 311/Lectures Slides/lect_38.pdf, courses/ECE 311/Lectures Slides/lect_39.pdf, courses/ECE 311/Lectures Slides/lect_41.pdf, courses/ECE 311/Lectures Slides/lect_42.pdf, courses/ECE 311/Lectures Slides/lect_44.pdf)
**Sources**: ECE 311 lecture slides (Spring 2024, Prof. D. S. Elliott): `courses/ECE 311/Lectures Slides/lect_38.pdf`, `courses/ECE 311/Lectures Slides/lect_39.pdf`, `courses/ECE 311/Lectures Slides/lect_41.pdf`, `courses/ECE 311/Lectures Slides/lect_42.pdf`, `courses/ECE 311/Lectures Slides/lect_44.pdf`; lecture order from `courses/ECE 311/ECE311_Spring2024_Schedule.pdf`. Statements marked Wiki note are standard physics not read in the slides.
**Last updated**: 2026-11-06

---

## Related pages
- [[Electromagnetic wave]]
- [[Capacitance]]
- [[Inductance]]
- [[Maxwell's equations]]
- [[Reflection and transmission of waves]]
- [[Impedance matching]]
