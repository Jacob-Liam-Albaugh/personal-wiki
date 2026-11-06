---
type: concept
area: digital
areas: [digital]
source-ref: "ECE 270 lectures 08_22, 08_24, 09_12, 09_14 (Wakerly ch. 3-5, 14)"
tags: [digital-logic]
---

# Logic gate

**Summary**: A physical circuit realizing a Boolean function of its inputs: AND, OR, NOT, NAND, NOR and XOR, each with a symbol, a truth table and a CMOS circuit.

## Basic gates
- Inverter, AND, OR, then NAND and NOR; a 3-input black box is specified by a truth table (Table 1-2). (source: 08_22.pdf, p. 22-27)
- XOR and XNOR appear in the full adder and parity examples; Verilog built-ins are `and nand or nor xor xnor buf not` plus tristate variants. (source: 09_14.pdf, p. 23)

## Symbols
- Fig. 4-3 gives the shapes (AND, OR, buffer, NAND, NOR, inverter, bubbles). A buffer strengthens a signal. (source: 09_12.pdf, p. 10-12)
- Fig. 4-4: generalized DeMorgan gives an equivalent second symbol for each gate; a NAND is an OR with inverted inputs. (source: 08_31.pdf, p. 14-15; 09_12.pdf, p. 12)

## Realization
- In CMOS the natural gates are inverting: inverter, NAND, NOR, AOI, OAI. AND and OR need an extra inverter stage, so they are slower and larger. See [[CMOS logic]]. (source: 08_24.pdf, p. 13-18, 33)
- Fan-in limits noted on a slide: about 4 for NOR and 6 for NAND; wider gates become trees. (source: 08_24.pdf, p. 33)
- Unused inputs are tied to a constant or another input, never left floating. (source: 08_29.pdf, p. 18; 09_12.pdf, p. 13)

## Two-level forms
- AND-OR becomes NAND-NAND; OR-AND becomes NOR-NOR. See [[NAND and NOR universality]]. (source: 09_07.pdf, p. 15-18)

## Delay
- Each gate has propagation delay $t_{pLH}$ and $t_{pHL}$; see [[Static timing and propagation delay]] and [[Timing diagram]]. (source: 08_29.pdf, p. 21-27)

## Where it appears
- [[ECE270 week 01 08_24 - Transistors and CMOS gates]] builds gates from transistors.
- [[ECE270 week 02 08_31 - Boolean algebra and canonical forms]] gives the algebra behind them.
- [[ECE270 week 04 09_14 - Verilog modules and combinational design]] instantiates them in structural Verilog.
- [[ECE270 week 11 10_31 - Binary arithmetic, codes and adders]] builds the full adder from XOR, AND and OR gates.

**Sources**: `ECE 27000/week 01/08_22.pdf`, `ECE 27000/week 01/08_24.pdf`, `ECE 27000/week 02/08_29.pdf`, `ECE 27000/week 04/09_12.pdf`, `ECE 27000/week 04/09_14.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Boolean algebra]]
- [[CMOS logic]]
- [[MOSFET]]
- [[NAND and NOR universality]]
- [[Verilog]]
- [[Adders and arithmetic circuits]]
- [[ECE270 week 01 08_24 - Transistors and CMOS gates]]
