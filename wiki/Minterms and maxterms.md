---
type: concept
area: digital
areas: [digital]
source-ref: "ECE 270 lectures 08_31, 09_07 (Wakerly ch. 3)"
tags: [digital-logic]
---

# Minterms and maxterms

**Summary**: The canonical forms of a switching function: a sum of minterms (rows where the output is 1) or a product of maxterms (rows where it is 0).

## Definitions
- Literal: a variable or its complement. Product term: literals ANDed. Sum term: literals ORed. Normal term: each variable appears once. (source: 08_31.pdf, p. 16-18)
- Minterm: a normal product term, true for exactly one input row. Maxterm: a normal sum term, false for exactly one row (Table 3-6). Table 3-4 is the general 3-variable table with rows 0-7. (source: 08_31.pdf, p. 16-19)

## Canonical forms
- Canonical sum: OR of the minterms where $F = 1$. Canonical product: AND of the maxterms where $F = 0$. (source: 08_31.pdf, p. 19-20)

> [!example] Canonical forms from a table (p. 19-20)
> $F = 1$ on rows 0, 3, 4, 6, 7, so
> $$F = \Sigma_{X,Y,Z}(0,3,4,6,7)$$
> $$= X'Y'Z' + X'YZ + XY'Z' + XYZ' + XYZ$$
> $F = 0$ on rows 1, 2, 5, so
> $$F = \Pi_{X,Y,Z}(1,2,5)$$
> $$= (X+Y+Z')(X+Y'+Z)(X'+Y+Z')$$

## Use
- A canonical sum gives a two-level AND-OR circuit with one AND per minterm. (source: 09_07.pdf, p. 12-14)

> [!example] Prime-number detector (4-bit input)
> $F = \Sigma_{N_3,N_2,N_1,N_0}(1,2,3,5,7,11,13)$ for inputs 0-15; the canonical sum needs seven 4-input ANDs (Fig. 3-15). The textbook treats 1 as prime; the lecture says 1 is not prime, which drops minterm 1 (the later K-map and Verilog versions use 2, 3, 5, 7, 11, 13; see [[Karnaugh map]] and [[Verilog]]). (source: 09_07.pdf, p. 4, 12; 09_19.pdf, p. 7)

- A [[Karnaugh map]] simplifies a canonical sum by merging adjacent minterms. (source: 09_07.pdf, p. 21-23)
- The $\Sigma$ and $\Pi$ lists are two of the seven ways to specify a function. (source: 08_31.pdf, p. 21)

**Covered in**: ECE 270 08_31, 09_07 (ECE 27000/week 02/08_31.pdf, week 03/09_07.pdf)
**Sources**: `ECE 27000/week 02/08_31.pdf`, `ECE 27000/week 03/09_07.pdf`, `ECE 27000/week 05/09_19.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Boolean algebra]]
- [[Karnaugh map]]
- [[Logic gate]]
