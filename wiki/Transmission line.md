---
type: concept
area: em
source-ref: "ECE 311 slides, lect_38, lect_39, lect_41, lect_42, lect_43, lect_44"
tags: [electromagnetics, pde, signals]
---
# Transmission line

**Summary**: Two-conductor guiding structure modelled with per-unit-length L, C, R, G; voltage and current waves, reflection, input impedance and matching.

## Model (lect_38)
Slides give per-unit-length $L'$ and $C'$ for coax, twin lead and parallel plate (e.g. $L'=\mu d/w$).
$$Z_0=\sqrt{L'/C'}\quad(\text{lossless, wiki note})$$

## Terminated line
$$\Gamma=\frac{V_0^-}{V_0^+}=\frac{Z_L-Z_0}{Z_L+Z_0}$$
Input impedance and SWR: lect_41, lect_42. Losses: $\gamma=\alpha+j\beta$ (lect_39).

## Matching and transients
- Quarter-wave: $R_{02}^2=Z_LR_0$; stubs in admittance: [[Impedance matching]].
- Pulses: reflection at both ends, $\Gamma_L$ and $\Gamma_S$ (lect_44).

## Wiki note
Same mathematics as normal-incidence plane waves: [[Reflection and transmission of waves]].

**Sources**: ECE 311 lecture slides (Spring 2024, Prof. D. S. Elliott), [[ECE311 lect_38 - Transmission lines intro]], [[ECE311 lect_39 - Transmission line losses]], [[ECE311 lect_41 - Finite-length lines and input impedance]], [[ECE311 lect_42 - SWR and lines as circuit elements]], [[ECE311 lect_43 - Impedance matching]], [[ECE311 lect_44 - Pulses on transmission lines]]. Statements marked Wiki note are standard physics not read in the slides.
**Last updated**: 2026-11-06

---

## Related pages
- [[Electromagnetic wave]]
- [[Capacitance]]
- [[Inductance]]
- [[Maxwell's equations]]
- [[ECE311 lect_38 - Transmission lines intro]]
- [[ECE311 lect_39 - Transmission line losses]]
- [[ECE311 lect_41 - Finite-length lines and input impedance]]
- [[ECE311 lect_42 - SWR and lines as circuit elements]]
- [[ECE311 lect_43 - Impedance matching]]
- [[ECE311 lect_44 - Pulses on transmission lines]]
