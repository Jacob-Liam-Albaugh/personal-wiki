---
type: lecture
area: em
source-ref: "ECE 311 lect_42, slides pp. 1-10"
tags: [electromagnetics]
course: ece311
lecture: lect_42
---
# ECE311 lect_42 - SWR and lines as circuit elements

**Summary**: Standing wave ratio on a line and short or open stubs used as inductors and capacitors.

**Course**: ECE 311 (Electromagnetics I, Purdue, Spring 2024, Prof. D. S. Elliott) · **Lecture date**: Apr 22 (per the schedule) · **File**: `Electromagnetics/Lectures Slides/lect_42.pdf` (10 slides)

---

## Topics
- Standing waves on a lossless line
- Standing wave ratio S
- Finding Gamma from the pattern
- Line as a circuit element: Zin and Vin
- Power transfer along the line

## Key results
Standing waves, lossless line, $V_0^-=\Gamma V_0^+$ (PDF p. 2, [3]; slide numbers in brackets):
$$v(z,t)=V_0^+\cos(\omega t-\beta z)+\Gamma V_0^+\cos(\omega t+\beta z)$$
$$V_{max}=V_0^+(1+|\Gamma|),\qquad V_{min}=V_0^+(1-|\Gamma|)$$
Standing wave ratio (PDF p. 2, [4]):
$$S=\frac{|V_{max}|}{|V_{min}|}=\frac{1+|\Gamma|}{1-|\Gamma|},\qquad |\Gamma|=\frac{S-1}{S+1}$$
For $\Gamma=\pm1$, $S\to\infty$; for $\Gamma=0$, $S\to1$. For $\Gamma=-1$, $V_{max}=2V_0^+$, $V_{min}=0$ [4]. Plots for $\Gamma=\pm0.1,\pm0.5,\pm1$ are on [4]; the $\Gamma=+1/3$ voltage and current patterns are on PDF p. 4 [7].
$$S=\frac{I_{max}}{I_{min}}\ \text{(also, [6])}$$
Locating the phase of $\Gamma$ (PDF p. 8, [16]):
$$|V|\ \text{max at}\ z_{max}:\ 2\beta z_{max}+\theta_\Gamma=2n\pi$$
$$\theta_\Gamma=2n\pi-\frac{4\pi z_{max}}{\lambda}$$
Line as a circuit element (PDF pp. 5-6, [10-12]): replace the line by $Z_{in}$ at the source end, $V_{in}=V_g\,Z_{in}/(Z_g+Z_{in})$. Quarter-wave line: $\beta\ell=\pi/2$ and $Z_{in}=R_0^2/Z_L$ [11]. Half-wave: $Z_{in}=Z_L$ [8].
Power check: $P_g-P_{R_g}=P_L$ with $P_g=\tfrac12V_gI_{in}^*$ [14].

## Examples
> [!example] Example 42-1 (PDF pp. 3-4)
> $Z_0=50$, $Z_L=100\ \Omega$, $V_L=2$ V. $\Gamma=1/3$; $V_0^+=1.5$ V, $V_0^-=0.5$ V; $V_{max}=2$ V, $V_{min}=1$ V, $S=2$; $I_{max}=40$ mA, $I_{min}=20$ mA, $S=2$. $V_{max}$ is at $z=0$ since $\Gamma$ is real and positive. Input impedance for $\ell=\lambda/4$: $25\ \Omega$; $\lambda/2$: $100\ \Omega$; $3\lambda/8$: $(40+30j)\ \Omega$ (PDF pp. 4-5, [8-9]).

> [!example] Example 42-2 (PDF pp. 5-7, [10-14])
> $V_g=16$ V, $Z_g=15\ \Omega$, $Z_0=50\ \Omega$, $Z_L=100\ \Omega$, $\ell=3\lambda/4$. $Z_{in}=R_0^2/Z_L=25\ \Omega$, so $V_{in}=16\cdot25/40=10$ V. $\Gamma=1/3$, $V_0^+=j15$ V, $V_0^-=j5$ V, $V_L=j20$ V. $I_L=j200$ mA, $P_L=\tfrac12|I_L|^2R_L=2$ W. $I_{in}=400$ mA; $P_g=3.2$ W, $P_{R_g}=1.2$ W, difference $2.0$ W matches $P_L$.

> [!example] Example 42-3 (PDF pp. 8-9, [15-18])
> $R_0=50\ \Omega$, $S=1.5$, first voltage maximum at $z=-\lambda/16$. $|\Gamma|=0.2$; $\theta_\Gamma=\pi/4$ so $\Gamma=0.2e^{j\pi/4}$. $Z_L=Z_0(1+\Gamma)/(1-\Gamma)=(63.4+j18.7)\ \Omega$.

**Sources**: `Electromagnetics/Lectures Slides/lect_42.pdf`; lecture order from `Electromagnetics/ECE311_Spring2024_Schedule.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Transmission line]]
- [[Impedance matching]]
- [[ECE311 lect_41 - Finite-length lines and input impedance]]
- [[ECE311 lect_43 - Impedance matching]]
