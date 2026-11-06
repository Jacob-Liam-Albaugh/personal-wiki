---
type: concept
area: digital
areas: [digital]
source-ref: "ECE 270 lectures 08_24, 08_31, 09_07 (Wakerly ch. 3, 14)"
tags: [digital-logic]
---

# NAND and NOR universality

**Summary**: NAND and NOR gates are the natural CMOS gates, and AND-OR and OR-AND circuits convert directly into NAND-NAND and NOR-NOR circuits.

## Conversion
- An AND-OR circuit with a pair of inverters on each wire between levels becomes NAND-NAND; OR-AND becomes NOR-NOR (Figs. 3-18 to 3-20). (source: 09_07.pdf, p. 15-18)
- DeMorgan gives the second symbol of each gate: NAND is OR of inverted inputs, NOR is AND of inverted inputs (Figs. 3-3, 3-4). (source: 08_31.pdf, p. 14-15)
- Fig. 3-21 shows moving inverters to avoid nonstandard gates; Fig. 3-14 shows $G = WXY + YZ$ as AND-OR, NAND-NAND and with 2-input gates. (source: 09_07.pdf, p. 11-13, 17)

## Why use them
- CMOS NAND and NOR are one stage; AND and OR need an extra inverter, so they are slower and larger. Slide note: people do not usually think in NAND or NOR. (source: 09_07.pdf, p. 17; 08_24.pdf, p. 33)
- NAND is faster than NOR because NMOS is faster than PMOS. (source: 08_24.pdf, p. 33)

## Wiki note on universality
Wiki note: the slides show the two-level conversions; the statement that NAND alone (or NOR alone) can build any gate follows from them plus DeMorgan and is not stated as a theorem on the slides **[unverified]**.

## Where it appears
[[ECE270 week 01 08_24 - Transistors and CMOS gates]], [[ECE270 week 02 08_31 - Boolean algebra and canonical forms]], [[ECE270 week 03 09_07 - Circuit analysis and Karnaugh maps]].

**Sources**: `ECE 27000/week 01/08_24.pdf`, `ECE 27000/week 02/08_31.pdf`, `ECE 27000/week 03/09_07.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Logic gate]]
- [[CMOS logic]]
- [[Boolean algebra]]
- [[Karnaugh map]]
- [[ECE270 week 03 09_07 - Circuit analysis and Karnaugh maps]]
