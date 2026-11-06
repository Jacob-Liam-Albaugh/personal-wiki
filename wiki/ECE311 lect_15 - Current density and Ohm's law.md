---
type: lecture
area: em
source-ref: "ECE 311 lect_15, slides pp. 1-8"
tags: [electromagnetics]
course: ece311
lecture: lect_15
---
# ECE311 lect_15 - Current density and Ohm's law

**Summary**: Convection and conduction currents, the local form of Ohm's law J = sigma E, resistance of a conducting object, and Kirchhoff's laws in field form.

**Course**: ECE 311 (Electromagnetics I, Purdue, Spring 2024, Prof. D. S. Elliott) · **Lecture date**: Feb 12 (per the schedule) · **File**: `Electromagnetics/Lectures Slides/lect_15.pdf` (8 slides)

---

## Topics
- Forms of current (wires, semiconductors, ions, electrons in vacuum)
- Current density from carrier density and velocity
- Mobility and conductivity
- Resistance from field quantities, Kirchhoff's laws

## Key results
Current through a surface (p. 2):
$$J_v=\rho_vu=qnu,\qquad I=\int_sJ_v\cdot ds$$
For ordinary conductors the drift velocity is proportional to $E$: $u=-\mu_eE$ (p. 3), so $J_v=\sigma E$ with $\sigma$ the conductivity (local Ohm's law, schedule: Lect. 15 'Ohm's Law; Res; Kirchhoff's Laws').
Resistance by $R=V/I$ with fields from Gauss' law (Example 15-2, PDF pp. 5-6, checked on the slide images):
$$R=\frac{\ln(b/a)}{2\pi\sigma L}$$
$$RC=\varepsilon/\sigma\quad(C=2\pi\varepsilon L/\ln(b/a))$$

## Examples
> [!example] Coax with lossy dielectric (referenced in lect_16)
> Example 15-2: lossy material between coax conductors of length $L$ (radii $a<b$). $D_\rho=\rho_sa/\rho$, $V_0=(\rho_sa/\varepsilon)\ln(b/a)$, $I=2\pi\sigma\rho_saL/\varepsilon$, giving $R=\ln(b/a)/2\pi\sigma L$ (PDF pp. 5-6). Lect_16 reuses it for dissipated power.

**Sources**: `Electromagnetics/Lectures Slides/lect_15.pdf`; lecture order from `Electromagnetics/ECE311_Spring2024_Schedule.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Ohm's law and current density]]
- [[Maxwell's equations]]
- [[ECE311 lect_16 - Power dissipation and conducting boundaries]]
- [[ECE311 lect_14 - Capacitance and method of images]]
