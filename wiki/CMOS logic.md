---
type: concept
area: digital
areas: [digital]
source-ref: "ECE 270 lectures 08_24, 08_29 (Wakerly ch. 14)"
tags: [digital-logic]
---

# CMOS logic

**Summary**: Logic built from complementary pairs of NMOS and PMOS transistors; the pull-up and pull-down networks are duals, so gates are inverting.

## Gates
- Inverter: PMOS to $V_{DD}$ and NMOS to ground, both gates on the input. Low in turns the PMOS on, so the output is high; high in does the reverse. (source: 08_24.pdf, p. 13-15)
- NAND: NMOS in series, PMOS in parallel; output low only when both inputs are high. NOR is the dual. (source: 08_24.pdf, p. 25-33)
- AND is NAND plus inverter; AND-OR-INVERT and OR-AND-INVERT are single compound gates (Figs. 14-16 to 14-19). (source: 08_24.pdf)
- Fan-in notes: NOR about 4, NAND about 6; NMOS is faster than PMOS, so NAND beats NOR. (source: 08_24.pdf, p. 33)

## Logic levels
- Typical 5.0 V CMOS: logic 0 up to 1.5 V, invalid 1.5 to 3.5 V, logic 1 above 3.5 V. HC series uses $0.3\,V_{CC}$ and $0.7\,V_{CC}$. (source: 08_24.pdf, p. 22-23; 08_29.pdf, p. 4-6)
- Lower supply voltage cuts power and heat. (source: 08_24.pdf, p. 23)

## Electrical behavior
- An output is a resistor to $V_{CC}$ or to ground; the other is over 1 M$\Omega$. (source: 08_29.pdf, p. 7-12)
- Load capacitance sets rise and fall times:
$$i = e^{-t/(RC)}$$
(normalized, source: 08_29.pdf, p. 21).
- Both transistors conduct for inputs in the invalid range, wasting current. (source: 08_29.pdf, p. 15-17)

## Other uses
- A 2-input multiplexer bit can be built from transmission gates (Fig. 8-20, Fig. 6-27). (source: 11_07.pdf, p. 8; 09_21.pdf, p. 14-20)

## Where it appears
[[ECE270 week 01 08_24 - Transistors and CMOS gates]], [[ECE270 week 02 08_29 - CMOS electrical behavior]].

**Sources**: `ECE 27000/week 01/08_24.pdf`, `ECE 27000/week 02/08_29.pdf`, `ECE 27000/week 09/09_21.pdf`, `ECE 27000/week 12/11_07.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[MOSFET]]
- [[Logic gate]]
- [[Static timing and propagation delay]]
- [[NAND and NOR universality]]
- [[ECE270 week 01 08_24 - Transistors and CMOS gates]]
- [[ECE270 week 02 08_29 - CMOS electrical behavior]]
