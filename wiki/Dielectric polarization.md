---
type: concept
area: em
source-ref: "ECE 311 slides, lect_9, lect_10"
tags: [electromagnetics]
---

# Dielectric polarization

**Summary**: Conductors and dielectrics in static fields, bound charge and the polarization P, the displacement field D, and interface conditions for E and D.

## Conductors (lect_9)
Conductors and insulators (dielectrics) are characterised by conductivity. In the static case the field inside a conductor is zero and the conductor is an equipotential, charge sits on the surface and $E$ is normal to it. At the surface (p. 2):
$$E_t=0,\qquad E_n=\rho_s/\varepsilon_0$$
derived from $\oint E\cdot d\ell=0$ on a thin rectangular loop and Gauss' law on a pillbox (pp. 2-3).

> [!example] Normal field at copper (lect_9, p. 3)
> $\rho_s=1.0$ nC/m$^2$ gives $E_n=\rho_s/\varepsilon_0\approx113$ V/m (wiki arithmetic).

## Polarization
In a dielectric, bound charges form dipoles; with $n$ dipoles per volume the polarization is $P=np$ (dipole moment density, p. 4). The potential of the medium is the sum of dipole potentials ([[Electric potential]]). The effective bound charge density is
$$\rho_{v,eff}=-\nabla\cdot P$$

## Displacement field (lect_10)
Definition and generalised Gauss' law, valid in all media (p. 2):
$$D=\varepsilon_0E+P,\qquad \nabla\cdot D=\rho_v$$
$$\oint_sD\cdot ds=Q_{enc}\ \text{(free charge)}$$
$E$ is the total field (force $F=qE$); $P$ is dipole moment density; $D/\varepsilon_0$ is the field of the free charge only in limited cases.

Simple (linear, isotropic, homogeneous) media: $P=\varepsilon_0\chi_eE$, hence $D=\varepsilon E$ with $\varepsilon=\varepsilon_0(1+\chi_e)$ and $\varepsilon_r=1+\chi_e$ (p. 3).

## Boundary conditions
At an interface (lect_10, p. 3):
$$E_{1t}=E_{2t},\qquad D_{2n}-D_{1n}=\rho_s$$
with $\rho_s$ free surface charge. Without free surface charge normal $D$ is continuous while $E$ is not unless $\varepsilon_1=\varepsilon_2$ (example in [[Capacitance]]).

## Analogue
Magnetic version: [[Magnetic materials]] with $M$, $H$.

**Covered in**: ECE 311 lect_9, lect_10 (Electromagnetics/Lectures Slides/lect_9.pdf, Electromagnetics/Lectures Slides/lect_10.pdf)
**Sources**: ECE 311 lecture slides (Spring 2024, Prof. D. S. Elliott): `Electromagnetics/Lectures Slides/lect_9.pdf`, `Electromagnetics/Lectures Slides/lect_10.pdf`; lecture order from `Electromagnetics/ECE311_Spring2024_Schedule.pdf`. Statements marked Wiki note are standard physics not read in the slides.
**Last updated**: 2026-11-06

---

## Related pages
- [[Electrostatics]]
- [[Gauss's law]]
- [[Capacitance]]
- [[Magnetic materials]]
