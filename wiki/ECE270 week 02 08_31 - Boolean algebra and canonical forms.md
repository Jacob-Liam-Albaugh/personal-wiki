---
type: lecture
area: digital
areas: [digital]
course: ece270
lecture: week 02 08_31
source-ref: "ECE 27000/week 02/08_31.pdf, 26 slides (Wakerly ch. 3 figures and tables)"
tags: [digital-logic]
---

# ECE270 week 02 08_31 - Boolean algebra and canonical forms

**Summary**: Switching algebra: the theorems T1-T15, DeMorgan's laws, and the vocabulary of literals, product and sum terms, [[Minterms and maxterms]], and the canonical sum and product. A function can be given as a circuit, truth table, sum of minterms, product of maxterms, or $\Sigma$ / $\Pi$ lists.

**File**: `ECE 27000/week 02/08_31.pdf`

---

## Topics
- **Logic in programs (p. 2)**: `if ((x < 0) or (x > 400))` bounces a ball; `if (found(login) and (password(login)))` admits a user.
- **Combinational vs sequential (p. 3-4)**: combinational output depends on current inputs only (chess, go: history does not matter); sequential output depends on inputs and previous output, so it has memory (Monopoly). Sequential circuits feed outputs back (see [[Sequential logic]]).
- **Notation (p. 5-6)**: inverter output is $Y = X'$ (Verilog `!`, `~`); AND is $X\cdot Y$ (Verilog `&`, also $\wedge$); OR is $X+Y$ (Verilog `|`, also $\vee$). See [[Verilog]].
- **Implication (p. 7)**: $P \Rightarrow Q$. "If not Q then not P" is correct (contrapositive); "if not P then not Q" is wrong. Example: rain implies a wet lawn, but a dry day can still give a wet lawn from sprinklers.
- **Theorems (p. 8-12)**: Table 3-1 (one variable), Table 3-2 (two or three variables), Table 3-3 (N variables). Each has a dual (replace + by $\cdot$ and 1 by 0). Slide message: you need not memorize every rule; know the content of a theorem more than its name (Feynman quote, p. 13).
- **DeMorgan equivalent circuits (p. 14-15)**: a NAND equals an OR of inverted inputs; a NOR equals an AND of inverted inputs (Figs. 3-3, 3-4). This gives two symbols for each gate (bubble pushing).
- **Truth tables and terms (p. 16-21)**: general 3-variable table with rows 0-7 (Table 3-4); definitions of literal, product term, sum of products, sum term, product of sums, normal term (each variable once), minterm, maxterm (Table 3-6).
- **Canonical forms (p. 19-20)**: canonical sum = sum of minterms where the output is 1, canonical product = product of maxterms where the output is 0.
- **Ways to specify a function (p. 21)**: CMOS circuit, truth table, sum of minterms, product of maxterms, $\Sigma$ list, $\Pi$ list, Verilog statement (later).
- **Circuit to table (p. 22-26)**: Fig. 3-5 is analyzed by listing each gate output as a bit string over all 8 input rows (Fig. 3-6), giving Table 3-7.

## Key results
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
> The slide flags the expansion as "pay attention, not obvious" (p. 11).

> [!proof] Worked proof (p. 11)
> $X + X\cdot Y = X\cdot 1 + X\cdot Y = X(1+Y) = X\cdot 1 = X$, using T1D, T8, T2, T1D.

> [!example] Canonical forms from a table (p. 19-20)
> $F = 1$ on rows 0, 3, 4, 6, 7, so
> $$F = \Sigma_{X,Y,Z}(0,3,4,6,7)$$
> $$= X'Y'Z' + X'YZ + XY'Z' + XYZ' + XYZ$$
> $F = 0$ on rows 1, 2, 5, so
> $$F = \Pi_{X,Y,Z}(1,2,5)$$
> $$= (X+Y+Z')(X+Y'+Z)(X'+Y+Z')$$

**Connections**: the algebra here is the basis for minimization with [[Karnaugh map]]s ([[ECE270 week 03 09_07 - Circuit analysis and Karnaugh maps]]) and for [[Verilog]] expressions. Gate-level realizations: [[Logic gate]] and [[NAND and NOR universality]]. Previous lecture: [[ECE270 week 02 08_29 - CMOS electrical behavior]].

**Sources**: `ECE 27000/week 02/08_31.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Boolean algebra]] · [[Minterms and maxterms]] · [[Logic gate]] · [[Sequential logic]] · [[Karnaugh map]] · [[Verilog]]
- [[ECE270 week 02 08_29 - CMOS electrical behavior]]
