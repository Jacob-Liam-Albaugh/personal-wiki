---
type: concept
area: digital
areas: [digital]
source-ref: "ECE 270 lectures 09_07, 09_12, 09_19 (Wakerly ch. 3)"
tags: [digital-logic]
---

# Karnaugh map

**Summary**: A grid drawing of a truth table in which neighbouring cells differ in one variable, so groups of 1s read off as simplified product terms.

## Layout
- 2-, 3- and 4-variable maps (Fig. 3-23). Rows and columns use Gray-code order 00, 01, 11, 10 so adjacent cells differ in exactly one bit. (source: 09_07.pdf, p. 21-23)
- Each cell is a minterm; see [[Minterms and maxterms]].

## Using it
1. Mark a 1 in each cell where the function is 1.
2. Circle rectangular groups of 1s of size 1, 2, 4, 8 (powers of two).
3. Each group becomes one product term; variables that change inside the group drop out.
(source: 09_07.pdf, p. 21-23; the steps are the Wiki's summary of Fig. 3-24)

> [!definition] Minimization by adjacency
> Two product terms differing in one variable combine by the combining theorem
> $$X\cdot Y + X\cdot Y' = X$$
> A Karnaugh map draws all such adjacent pairs next to each other.
> (source: 09_07.pdf, p. 21-23)

## Example
> [!example] Prime-number detector (p. 12, 19-21)
> 4-bit inputs 0-15, $F = \Sigma(1,2,3,5,7,11,13)$. Seven 4-input ANDs shrink to four product terms (Fig. 3-22, 3-24):
> $$F = N_3'N_0 + N_3'N_2'N_1 + N_2'N_1N_0 + N_2N_1'N_0$$
> as read from Fig. 3-24 (some labels in the render are small). The lecture 09_19 redraws the map, circles $N_3' N_2' N_1$, and treats 1 as not prime (output true for 2, 3, 5, 7, 11, 13). (source: 09_07.pdf, p. 12, 19-21; 09_19.pdf, p. 7-9)

The same function written in [[Verilog]] as a sum-of-products `assign` and as a conditional-operator form: see that page.

## Limits
- The 4-input even-parity function has no adjacent 1s, so the map gives no simplification (Fig. 3-25). (source: 09_07.pdf, p. 23)
- A minimal sum of products can still contain a static-1 hazard; adding the consensus term, the group covering two adjacent groups, fixes it. See [[Hazards]]. (source: 09_12.pdf, p. 5-6)
- Wiki note: the slides show only up to four variables.

**Covered in**: ECE 270 09_07 (Circuit analysis and Karnaugh maps), 09_12, 09_19 (ECE 27000/week 03/09_07.pdf, week 04/09_12.pdf, week 05/09_19.pdf)
**Sources**: `ECE 27000/week 03/09_07.pdf`, `ECE 27000/week 04/09_12.pdf`, `ECE 27000/week 05/09_19.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Boolean algebra]]
- [[Minterms and maxterms]]
- [[Hazards]]
- [[Logic gate]]
