---
type: lecture
area: digital
areas: [digital]
course: ece270
lecture: week 03 09_07
source-ref: "ECE 27000/week 03/09_07.pdf, 25 slides (Wakerly ch. 3 figures)"
tags: [digital-logic]
---

# ECE270 week 03 09_07 - Circuit analysis and Karnaugh maps

**Summary**: Analyzing circuits into expressions, realizing a function as two-level AND-OR, OR-AND, NAND-NAND or NOR-NOR circuits, minimizing with the [[Karnaugh map]], and a first look at timing hazards.

**File**: `ECE 27000/week 03/09_07.pdf`

---

## Topics
- **Specifying functions (p. 2-6)**: the list from last lecture plus simulator timing responses (Fig. 3-7). A 4-bit example: $F = \Sigma_{N_3,N_2,N_1,N_0}(1,2,3,5,7,11,13)$, a prime-number detector for inputs 0-15 (p. 4, 12).
- **Circuit analysis (p. 5-6, 8-12)**: label each gate output with its expression and simplify. Fig. 3-8 gives $F=(X+Y')Z + X'YZ'$ which expands to $XZ + Y'Z + X'YZ'$. Fig. 3-9 is the two-level AND-OR form; Fig. 3-10 is an OR-AND version, shown equal to $(X+Y'+Z')(X'+Z)(Y+Z)$ by algebra. Figs. 3-11 to 3-13 analyze a mixed NAND/NOR circuit by first rewriting the gate symbols with DeMorgan.
- **Same function, different circuits (p. 11-13)**: Fig. 3-14 shows $G = WXY + YZ$ as AND-OR, NAND-NAND, and with 2-input gates only.
- **Design examples (p. 12-16)**: canonical-sum prime detector (Fig. 3-15, seven 4-input ANDs), an alarm circuit with $ALARM = PANIC + ENABLE\cdot EXITING'\cdot SECURE'$ and $SECURE = WINDOW\cdot DOOR\cdot GARAGE$, expanded by DeMorgan to a sum of products (Figs. 3-16, 3-17).
- **NAND-NAND and NOR-NOR (p. 15-18)**: AND-OR with inverter pairs becomes NAND-NAND; OR-AND becomes NOR-NOR (Figs. 3-18 to 3-20). Slide notes: NAND and NOR are faster than AND and OR in CMOS, but people do not usually think in NAND or NOR. Fig. 3-21 shows symbol manipulations and moving inverters to avoid nonstandard gates. See [[NAND and NOR universality]].
- **Minimization (p. 19-23)**: goals are fewer first-level gates, fewer inputs to first-level gates and fewer inputs to the second-level gate, because this reduces cost. The prime detector shrinks from 7 terms to 4 (Fig. 3-22, 3-24). Assumption to question: that signals and their inversions are always available.
- **Karnaugh maps (p. 21-23)**: 2-, 3- and 4-variable maps (Fig. 3-23); adjacent cells differ in exactly one bit, so rows and columns use Gray-code order 00, 01, 11, 10. Circle groups of 1s to get product terms (Fig. 3-24). The 4-input even-parity function has no adjacent 1s, so no simplification (Fig. 3-25).
- **Timing hazard (p. 24-25)**: a static hazard: one path through an inverter is slower, so $F$ glitches when $Z$ changes (p. 24, diagram with $ZP$, $XZP$, $YZ$). Fig. 3-31 shows a dynamic hazard where an output changes 1-0-1-0 instead of 1-0 because of paths of different speeds (slow, slower OR gates).

## Key results
> [!definition] Minimization by adjacency
> Two product terms differing in one variable combine by the combining theorem
> $$X\cdot Y + X\cdot Y' = X$$
> A [[Karnaugh map]] draws all such adjacent pairs next to each other.
> (source: 09_07.pdf, p. 21-23)

> [!example] Prime-number detector (p. 12, 19-21)
> $$F = \Sigma(1,2,3,5,7,11,13)$$
> After circling the K-map the slides give four product terms:
> $$F = N_3'N_0 + N_3'N_2'N_1 + N_2'N_1N_0 + N_2N_1'N_0$$
> as read from Fig. 3-24 (some labels in the render are small).

> [!failure] Hazards
> A circuit that is logically correct can glitch because gate delays differ (see [[ECE270 week 02 08_29 - CMOS electrical behavior]]). Slide 24 labels this "Timing Hazard" (p. 24-25).

**Connections**: continues [[ECE270 week 02 08_31 - Boolean algebra and canonical forms]]. Next: [[ECE270 week 04 09_12 - Hazards, documentation and timing]].

**Sources**: `ECE 27000/week 03/09_07.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Karnaugh map]] · [[Boolean algebra]] · [[Minterms and maxterms]] · [[Logic gate]] · [[NAND and NOR universality]] · [[Hazards]]
