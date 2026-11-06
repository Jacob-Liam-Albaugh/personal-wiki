---
type: concept
area: digital
areas: [digital]
source-ref: "ECE 270 lecture 08_24 (Wakerly ch. 14)"
tags: [digital-logic]
---

# MOSFET

**Summary**: The metal-oxide-semiconductor field-effect transistor, used in logic as a voltage-controlled switch; NMOS and PMOS together form CMOS.

## Behavior
- A MOS transistor is a voltage-controlled resistance. Raising $V_{gs}$ lowers $R_{ds}$ in an NMOS; the opposite holds in a PMOS. (source: 08_24.pdf, p. 9-12)
- The gate looks like a capacitor, so no steady current flows into it. (source: 08_24.pdf, p. 9)
- Physical structure of NMOS and PMOS is on slide 24. (source: 08_24.pdf, p. 24)

## Why CMOS
- CMOS replaced bipolar transistors because it uses less energy. (source: 08_24.pdf, p. 9)
- Complementary pairs mean one transistor is off in each steady state; see [[CMOS logic]].

## As a switch model
- Each gate is drawn as a transistor circuit, a switch model, a function table of which transistors are on, and a logic symbol. (source: 08_24.pdf, p. 13-39)
- In the output model of lecture 08_29 the on transistor is a resistor of about 100-200 $\Omega$. (source: 08_29.pdf, p. 7-12)

## Handling
- Gate oxides are damaged by electrostatic discharge, $Q = CV$; wrist straps and shielding bags protect them. (source: 08_29.pdf, p. 19-20)

## Where it appears
[[ECE270 week 01 08_24 - Transistors and CMOS gates]], [[ECE270 week 02 08_29 - CMOS electrical behavior]].

**Sources**: `ECE 27000/week 01/08_24.pdf`, `ECE 27000/week 02/08_29.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[CMOS logic]]
- [[Logic gate]]
- [[Static timing and propagation delay]]
- [[ECE270 week 01 08_24 - Transistors and CMOS gates]]
