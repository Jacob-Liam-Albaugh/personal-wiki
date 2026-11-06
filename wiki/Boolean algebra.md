---
type: concept
area: digital
areas: [digital]
source-ref: "ECE 270 lectures 08_22, 08_31, 09_07 (Wakerly ch. 3)"
tags: [digital-logic]
---

# Boolean algebra

**Summary**: The two-valued algebra of AND, OR and NOT used to describe and simplify logic circuits, called switching algebra in ECE 270.

## Operators and notation
- Inverter $Y = X'$ (Verilog `!` or `~`), AND $X \cdot Y$ (`&`), OR $X + Y$ (`|`). (source: 08_31.pdf, p. 5-6)
- A bit is 0 or 1; 0 is low or false, 1 is high or true. (source: 08_22.pdf, p. 21-22)
- Implication: if not Q then not P is correct (contrapositive); if not P then not Q is wrong. (source: 08_31.pdf, p. 7)

## Theorems
Each theorem has a dual: swap + with $\cdot$ and 0 with 1. Tables 3-1 to 3-3 list them; the slides say to know the content, not the numbering. (source: 08_31.pdf, p. 8-13)

$$X + X' = 1$$
$$X \cdot Y + X \cdot Y' = X$$
$$X + X \cdot Y = X$$
$$X \cdot Y + X' \cdot Z + Y \cdot Z = X \cdot Y + X' \cdot Z$$

- DeMorgan: $(X_1 \cdots X_n)' = X_1' + \dots + X_n'$ and the dual form. It gives two symbols per gate (see [[Logic gate]]). (source: 08_31.pdf, p. 11, 14-15)
- Shannon expansion: $F = X_1 F(1,\dots) + X_1' F(0,\dots)$. The slide calls it "not obvious". (source: 08_31.pdf, p. 11)

## Forms of a function
- Literal, product term, sum of products, sum term, product of sums, normal term. See [[Minterms and maxterms]] for the canonical sum and product. (source: 08_31.pdf, p. 16-21)
- Ways to specify one function: circuit, truth table, sum of minterms, product of maxterms, $\Sigma$ list, $\Pi$ list, Verilog. (source: 08_31.pdf, p. 21)

## Simplification
- Combining theorem on adjacent terms drives [[Karnaugh map]] minimization. (source: 09_07.pdf, p. 21-23)
- Minimization goals: fewer first-level gates, fewer inputs to them, fewer inputs to the second-level gate. (source: 09_07.pdf, p. 19)
- Adding the consensus term removes a static hazard; see [[Hazards]]. (source: 09_12.pdf, p. 5)

## Where it appears
- [[ECE270 week 02 08_31 - Boolean algebra and canonical forms]] states the theorems and canonical forms.
- [[ECE270 week 03 09_07 - Circuit analysis and Karnaugh maps]] uses them to analyze and simplify circuits.
- [[ECE270 week 04 09_14 - Verilog modules and combinational design]] maps the operators to Verilog.

Wiki note: the slides call it switching algebra; it is the two-element Boolean algebra.

**Sources**: `ECE 27000/week 01/08_22.pdf`, `ECE 27000/week 02/08_31.pdf`, `ECE 27000/week 03/09_07.pdf`, `ECE 27000/week 04/09_12.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Logic gate]]
- [[Minterms and maxterms]]
- [[Karnaugh map]]
- [[NAND and NOR universality]]
- [[Hazards]]
- [[Verilog]]
- [[ECE270 week 02 08_31 - Boolean algebra and canonical forms]]
- [[ECE270 week 03 09_07 - Circuit analysis and Karnaugh maps]]
