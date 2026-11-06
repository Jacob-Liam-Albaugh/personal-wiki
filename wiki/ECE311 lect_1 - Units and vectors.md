---
type: lecture
area: em
source-ref: "ECE 311 lect_1, slides pp. 1-8"
tags: [electromagnetics]
course: ece311
lecture: lect_1
---
# ECE311 lect_1 - Units and vectors

**Summary**: Opening lecture: SI units, charge and current densities, scalars and vectors, dot and cross products. The slides also give a one-slide sketch of how electromagnetics fits together.

**Course**: ECE 311 (Electromagnetics I, Purdue, Spring 2024, Prof. D. S. Elliott) · **Lecture date**: Jan 8 (per the schedule) · **File**: `Electromagnetics/Lectures Slides/lect_1.pdf` (8 slides)

---

## Topics
- Examples of EM devices (motors, antennas, MRI, x-ray, microwave ovens)
- SI base units used in the course: m, kg, s, A (not candela or kelvin)
- Charge, charge density ($\rho_v,\rho_s,\rho_\ell$), current, current density ($J_v, J_s$)
- Scalars and vectors; dot and cross products

## Key results
The slides' thumbnail sketch of EM (p. 3):
- charges exert forces and produce $E$ (Gauss' law); currents produce $B$ (Ampere's law)
- charge is conserved; changing $B$ gives $E$ (Faraday); changing $E$ gives $B$ (Ampere with displacement current)
- coupled $E$ and $B$ describe propagating waves that carry power and information

The ampere is defined by the force between two long parallel wires 1 m apart: $2\times10^{-7}$ N/m at 1 A (p. 4). The elementary charge is $e=1.602176634\times10^{-19}$ C (p. 5).

Densities are limits of ratios, e.g.:
$$\rho_v=\lim_{\Delta v\to0}\frac{\Delta q}{\Delta v}\ \ (\mathrm{C/m^3})$$
$$J_v=\lim_{\Delta s\to0}\frac{\Delta I}{\Delta s}\ \ (\mathrm{A/m^2})$$

Vector products (p. 7):
$$A\cdot B=|A||B|\cos\theta$$
$$|A\times B|=|A||B|\sin\theta$$
$A\times B$ is perpendicular to both $A$ and $B$ and $A\times B=-B\times A$ (p. 8).

## Examples
> [!example] Surface charge density of a capacitor plate (p. 5)
> A 0.5 uF capacitor charged to 1 V holds 0.5 uC on the positive plate; with plate area $10^{-2}$ m$^2$ and uniform charge, $\rho_s=0.5\times10^{-4}$ C/m$^2$.

> [!example] Dot and cross product (p. 7)
> For $A=(5,6,-3)$ and $B=(-1,2,3)$: $A\cdot B=-2$ and $A\times B=(24,-12,16)$, which is orthogonal to $A$ (dot product $120-72-48=0$).

**Sources**: `Electromagnetics/Lectures Slides/lect_1.pdf`; lecture order from `Electromagnetics/ECE311_Spring2024_Schedule.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Vector calculus for EM]]
- [[Electrostatics]]
- [[Maxwell's equations]]
- [[Ohm's law and current density]]
- [[ECE311 lect_2 - Coordinate systems]]
