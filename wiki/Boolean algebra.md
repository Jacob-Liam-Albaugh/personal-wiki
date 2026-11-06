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
- Inverter $Y = X'$ (Verilog `!` or `~`), AND $X \cdot Y$ (`&`, also $\wedge$), OR $X + Y$ (`|`, also $\vee$). See [[Verilog]]. (source: 08_31.pdf, p. 5-6)
- A bit is 0 or 1; 0 is low or false, 1 is high or true. (source: 08_22.pdf, p. 21-22)
- Logic in programs: `if ((x < 0) or (x > 400))` bounces a ball; `if (found(login) and (password(login)))` admits a user. (source: 08_31.pdf, p. 2)
- Implication $P \Rightarrow Q$: if not Q then not P is correct (contrapositive); if not P then not Q is wrong. Rain implies a wet lawn, but a dry day can still give a wet lawn from sprinklers. (source: 08_31.pdf, p. 7)
- Combinational output depends on current inputs only (chess, go); sequential output depends on inputs and previous output, so it has memory (Monopoly). See [[Sequential logic]]. (source: 08_31.pdf, p. 3-4)

## Theorems
Each theorem has a dual: swap + with $\cdot$ and 0 with 1. Tables 3-1 (one variable), 3-2 (two or three variables) and 3-3 (N variables) list them; the slides say to know the content of a theorem more than its name (Feynman quote, p. 13). (source: 08_31.pdf, p. 8-13)

> [!theorem] Switching-algebra theorems (Tables 3-1 to 3-3)
> Identities and null elements:
> $$X + 0 = X,\quad X + 1 = 1$$
> Idempotency, involution, complements:
> $$X + X = X,\quad (X')' = X,\quad X + X' = 1$$
> Commutativity, associativity, distributivity:
> $$X + Y = Y + X$$
> $$(X+Y)+Z = X+(Y+Z)$$
> $$X\cdot Y + X\cdot Z = X\cdot(Y+Z)$$
> Covering, combining, consensus:
> $$X + X\cdot Y = X$$
> $$X\cdot Y + X\cdot Y' = X$$
> $$X\cdot Y + X'\cdot Z + Y\cdot Z = X\cdot Y + X'\cdot Z$$
> (source: 08_31.pdf, p. 8-10; each also holds in dual form)

> [!theorem] DeMorgan and Shannon expansion (Table 3-3)
> $$(X_1 \cdots X_n)' = X_1' + \dots + X_n'$$
> $$(X_1 + \dots + X_n)' = X_1' \cdots X_n'$$
> $$F(X_1,\dots,X_n) = X_1 \cdot F(1,X_2,\dots) + X_1' \cdot F(0,X_2,\dots)$$
> The slide flags the expansion as "pay attention, not obvious". (source: 08_31.pdf, p. 11)

> [!proof] Worked proof (p. 11)
> $X + X\cdot Y = X\cdot 1 + X\cdot Y = X(1+Y) = X\cdot 1 = X$, using T1D, T8, T2, T1D.

- DeMorgan gives two symbols per gate: a NAND equals an OR of inverted inputs and a NOR an AND of inverted inputs (Figs. 3-3, 3-4; bubble pushing). See [[Logic gate]]. (source: 08_31.pdf, p. 14-15)

## Forms of a function
- Literal, product term, sum of products, sum term, product of sums, normal term. See [[Minterms and maxterms]] for the canonical sum and product. (source: 08_31.pdf, p. 16-21)
- Ways to specify one function: circuit (CMOS), truth table, sum of minterms, product of maxterms, $\Sigma$ list, $\Pi$ list, Verilog; simulator timing responses are a further view (Fig. 3-7). (source: 08_31.pdf, p. 21; 09_07.pdf, p. 2-6)
- Circuit to table: list each gate output as a bit string over all 8 input rows (Fig. 3-6), giving Table 3-7 for the circuit of Fig. 3-5. (source: 08_31.pdf, p. 22-26)

## Circuit analysis
Label each gate output with its expression and simplify. (source: 09_07.pdf, p. 5-12)
- Fig. 3-8: $F=(X+Y')Z + X'YZ'$ expands to $XZ + Y'Z + X'YZ'$.
- Fig. 3-9 is the two-level AND-OR form; Fig. 3-10 an OR-AND version shown equal to $(X+Y'+Z')(X'+Z)(Y+Z)$ by algebra.
- Figs. 3-11 to 3-13 analyze a mixed NAND/NOR circuit by first rewriting the gate symbols with DeMorgan.
- Fig. 3-14: $G = WXY + YZ$ as AND-OR, NAND-NAND, and with 2-input gates only. See [[NAND and NOR universality]].

> [!example] Alarm circuit (Figs. 3-16, 3-17)
> $$ALARM = PANIC + ENABLE\cdot EXITING'\cdot SECURE'$$
> $$SECURE = WINDOW\cdot DOOR\cdot GARAGE$$
> Expanded by DeMorgan to a sum of products. (source: 09_07.pdf, p. 12-16)

## Simplification
- Combining theorem on adjacent terms drives [[Karnaugh map]] minimization. (source: 09_07.pdf, p. 21-23)
- Minimization goals: fewer first-level gates, fewer inputs to first-level gates, fewer inputs to the second-level gate, because this reduces cost. Assumption to question: that signals and their inversions are always available. (source: 09_07.pdf, p. 19-23)
- Adding the consensus term removes a static hazard; see [[Hazards]]. (source: 09_12.pdf, p. 5)

Wiki note: the slides call it switching algebra; it is the two-element Boolean algebra.

**Covered in**: ECE 270 08_22, 08_31, 09_07 (ECE 27000/week 02/08_31.pdf, week 03/09_07.pdf)
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
