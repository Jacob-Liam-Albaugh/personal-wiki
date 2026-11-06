---
type: concept
area: em
source-ref: "ECE 311 slides, lect_15, lect_16, lect_25"
tags: [electromagnetics]
---

# Ohm's law and current density

**Summary**: Conduction and convection current, conductivity, the local Ohm's law, resistance from fields, Joule heating, and Kirchhoff's laws in field form.

## Current density
Forms of current include wires, semiconductors, ions and electrons in vacuum. Through a surface (lect_15, p. 2):
$$J_v=\rho_vu=qnu,\qquad I=\int_sJ_v\cdot ds$$
For ordinary conductors the drift velocity is proportional to $E$: $u=-\mu_eE$ (p. 3), so with $\sigma$ the conductivity
$$J_v=\sigma E$$
(local Ohm's law). Charge conservation: $\nabla\cdot J_v=-\partial\rho_v/\partial t$. Kirchhoff's laws appear in field form.

## Resistance
$R=V/I$ with fields from Gauss' law.

> [!example] Coax with lossy dielectric (lect_15, Example 15-2, pp. 5-6)
> Lossy material between coax conductors of length $L$ (radii $a<b$): $D_\rho=\rho_sa/\rho$, $V_0=(\rho_sa/\varepsilon)\ln(b/a)$, $I=2\pi\sigma\rho_saL/\varepsilon$ (checked on the slide images), giving
> $$R=\frac{\ln(b/a)}{2\pi\sigma L},\qquad RC=\varepsilon/\sigma\quad(C=2\pi\varepsilon L/\ln(b/a))$$

## Power dissipation (lect_16)
Each carrier gives energy $qE\cdot u$ to the lattice per unit time; summing over $n\,dv$ carriers (p. 2):
$$d\wp=E\cdot J_v\,dv,\qquad \wp=\int_vE\cdot J_v\,dv$$
For uniform fields $\wp=VI$. The same result later accounts for the loss of EM waves in absorbing media ([[Poynting theorem]]). Extra boundary conditions between lossy media are in [[Dielectric polarization]] and [[Magnetic materials]].

> [!example] Coax lossy dielectric (lect_16, Example 16-1, p. 2)
> With $D_\rho=\rho_sa/\rho$ and $E_\rho=D_\rho/\varepsilon$ (checked): $E\cdot J_v=\sigma(\rho_sa/\varepsilon\rho)^2$, with $I=2\pi\sigma LV_0/\ln(b/a)$ and $R=\ln(b/a)/2\pi\sigma L$; integrating over $dv=\rho\,d\rho\,d\varphi\,dz$ gives the total power.

**Covered in**: ECE 311 lect_15, lect_16, lect_25 (Electromagnetics/Lectures Slides/lect_15.pdf, Electromagnetics/Lectures Slides/lect_16.pdf, Electromagnetics/Lectures Slides/lect_25.pdf)
**Sources**: ECE 311 lecture slides (Spring 2024, Prof. D. S. Elliott): `Electromagnetics/Lectures Slides/lect_15.pdf`, `Electromagnetics/Lectures Slides/lect_16.pdf`, `Electromagnetics/Lectures Slides/lect_25.pdf`; lecture order from `Electromagnetics/ECE311_Spring2024_Schedule.pdf`. Statements marked Wiki note are standard physics not read in the slides.
**Last updated**: 2026-11-06

---

## Related pages
- [[Electrostatics]]
- [[Electromagnetic wave]]
- [[Poynting theorem]]
- [[Capacitance]]
