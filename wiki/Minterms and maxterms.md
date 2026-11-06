---
type: concept
area: digital
areas: [digital]
source-ref: "ECE 270 lecture 08_31 (Wakerly ch. 3)"
tags: [digital-logic]
---

# Minterms and maxterms

**Summary**: The canonical forms of a switching function: a sum of minterms (rows where the output is 1) or a product of maxterms (rows where it is 0).

## Definitions
- Literal: a variable or its complement. Product term: literals ANDed. Sum term: literals ORed. Normal term: each variable appears once. (source: 08_31.pdf, p. 16-18)
- Minterm: a normal product term, true for exactly one input row. Maxterm: a normal sum term, false for exactly one row (Table 3-6). (source: 08_31.pdf, p. 18-19)

## Canonical forms
- Canonical sum: OR of the minterms where $F = 1$. Canonical product: AND of the maxterms where $F = 0$. (source: 08_31.pdf, p. 19-20)

## Example
$F = 1$ on rows 0, 3, 4, 6, 7:
$$F = \Sigma_{X,Y,Z}(0,3,4,6,7)$$
$F = 0$ on rows 1, 2, 5:
$$F = \Pi_{X,Y,Z}(1,2,5)$$
(source: 08_31.pdf, p. 19-20)

## Use
- A canonical sum gives a two-level AND-OR circuit with one AND per minterm, for example seven 4-input ANDs for the prime detector. (source: 09_07.pdf, p. 12-14)
- A [[Karnaugh map]] simplifies a canonical sum by merging adjacent minterms. (source: 09_07.pdf, p. 21-23)
- The $\Sigma$ and $\Pi$ lists are two of the seven ways to specify a function. (source: 08_31.pdf, p. 21)

## Where it appears
[[ECE270 week 02 08_31 - Boolean algebra and canonical forms]], [[ECE270 week 03 09_07 - Circuit analysis and Karnaugh maps]].

**Sources**: `ECE 27000/week 02/08_31.pdf`, `ECE 27000/week 03/09_07.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Boolean algebra]]
- [[Karnaugh map]]
- [[Logic gate]]
- [[ECE270 week 02 08_31 - Boolean algebra and canonical forms]]
