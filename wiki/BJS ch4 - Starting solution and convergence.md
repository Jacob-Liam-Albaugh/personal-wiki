---
type: paper
area: math
source-ref: "Bazaraa, Jarvis, Sherali 2010, ch. 4 (printed pp. 151-200)"
tags: [optimization]
authors: ["[[Mokhtar S. Bazaraa]]", "[[John J. Jarvis]]", "[[Hanif D. Sherali]]"]
year: 2010
venue: "Wiley, Linear Programming and Network Flows, 4th ed. (textbook)"
file: "text_books/Linear Optimization/BJS full book.pdf"
---

# BJS ch4 - Starting solution and convergence

**Summary**: How to start the simplex method when no identity basis is visible (artificial variables, the two-phase method, the big-M method, a single artificial variable), and how to guarantee finite termination under degeneracy (Beale's cycling example, the lexicographic rule, Bland's rule). See [[Simplex method]], [[BJS ch3 - The simplex method]].

**Authors**: Mokhtar S. Bazaraa, John J. Jarvis, Hanif D. Sherali · **Year**: 2010 · **File**: `text_books/Linear Optimization/BJS full book.pdf` (printed pp. 151-200). Cites use printed pages; pdf = printed + 16.

## The initial basic feasible solution (§4.1, p. 151-153)
The simplex method needs a basis $\mathbf B$ with $\hat{\mathbf b}=\mathbf B^{-1}\mathbf b\ge\mathbf0$ (p. 151, text). It can always be started from the identity (text). Easy case: constraints $\mathbf A\mathbf x\le\mathbf b$, $\mathbf x\ge\mathbf0$ with $\mathbf b\ge\mathbf0$, where the slack variables form the identity basis. Otherwise artificial variables $\mathbf x_a$ are added so that $\mathbf A\mathbf x+\mathbf x_a=\mathbf b$. A slack that already has a unit column (coefficient $+1$ in one row only) needs no artificial in that row, so fewer artificials are needed (Example 4.2, p. 154, text).

## Two-phase method (§4.2, p. 154-164)
**Phase I** minimizes the sum of the artificial variables $x_0=\mathbf 1\mathbf x_a$ subject to $\mathbf A\mathbf x+\mathbf x_a=\mathbf b$, $\mathbf x,\mathbf x_a\ge\mathbf0$. If the original problem is feasible the optimum is zero, and the artificials leave the basis (p. 154, text). At the end of Phase I:
- if $x_0>0$ the problem is infeasible and one stops;
- otherwise the $x_0$ row and column are dropped, remaining artificials at level zero are removed from the basis, and **Phase II** starts with the original cost row (p. 165, text).

The tableau starts with the $x_0$ row $z_j-c_j=-1$ for the artificials and is brought to canonical form by adding each constraint row to row $x_0$. During Phase I the original $z$ row is carried along (and may break ties). Example 4.3 (Figure 4.1, p. 156, image seen) has $x_0$ initially $0$ with artificials $x_6,x_7$ in rows 1 and 2, and after canonicalization the $x_0$ row has right-hand side $3$. Two pivots then give $x_0=0$ with basis $\{x_1,x_2,x_5\}$ and the vertex $(1/2,3/2)$ of the region, a point on the path to the optimum in Figure 4.1. Examples 4.4-4.5 (p. 158-164, text) treat redundant constraints (an artificial stays basic at zero) and infeasibility.

## Big-M method (§4.3-4.4, p. 165-173)
Combine both phases in one problem (p. 166, image seen):
$$\min\ z_{bigM}=\mathbf c\mathbf x+M\,\mathbf 1\mathbf x_a$$
$$\mathbf A\mathbf x+\mathbf x_a=\mathbf b,\quad\mathbf x,\mathbf x_a\ge\mathbf0$$
$M$ is a very large positive number acting as a penalty on any solution with $\mathbf x_a\ne\mathbf0$. Equivalently, it minimizes $\mathbf 1\mathbf x_a$ first and, among the minimizers, $\mathbf c\mathbf x$. The starting point $\mathbf x_a=\mathbf b$ has the unattractive value $M\mathbf 1\mathbf b$, so the simplex method drives the artificials out. In tableau form, with cost row $(1,-1,2,0,0,0,-M,-M)$ for Example 4.6, rows 1 and 2 are multiplied by $M$ and added to row 0, giving $z_2-c_2=2+2M$ and right-hand side $3M$ (p. 166, image seen).

Cases (§4.3, p. 167-171, text): the optimum with $\mathbf x_a=\mathbf0$ is optimal for the original problem; an optimum with some artificial positive means the original is infeasible; an unbounded big-M problem needs care. Section 4.4 (p. 172-173) is titled "How big should big-M be?" and was not read.

## Single artificial variable (§4.5, p. 173-175)
A single artificial variable is appended to the Phase I tableau, and one pivot on its column gives a tableau ready for the two-phase method (Example 4.10, p. 174-175, text layer garbled so the column is not transcribed). The two-phase or big-M analysis carries over (Exercise 4.19, p. 175).

## Degeneracy, cycling, stalling (§4.6, p. 175-181)
Degeneracy causes conceptual and computational problems (p. 175, text): a zero reduced cost at an optimal degenerate point does not prove alternative optima, the dual interpretation $\partial z/\partial b_i=w_i$ is not a realizable rate of change, and not every optimal basis satisfies $z_j-c_j\le0$ for all $j$.

> [!theorem] Theorem 4.1 (p. 176, text)
> Given an optimal extreme point solution of a minimization LP, there exists an associated optimal basis with $z_j-c_j\le0$ for all $j=1,\dots,n$.

The anti-cycling rules below prove it constructively by making sure no basis repeats.

**Beale's example** (Example 4.11, p. 176-178): a seven-variable problem with three equality rows and optimum $x_1=3/4$, $x_4=x_6=1$, other variables zero, value $-5/4$. With the largest-coefficient entering rule and arbitrary tie-breaking, the simplex method cycles (the tableaux repeat).

**Lexicographic rule** (p. 178-179, read from text; the formulas were garbled so are described). Choose the entering $x_k$ as usual. Let $I_0$ be the set of rows attaining the minimum ratio $\hat b_i/y_{ik}$ over $y_{ik}>0$. If $I_0$ is a single row it leaves. Otherwise form $I_1$ from the rows of $I_0$ minimizing the same ratio with column $\mathbf y_1$ of $\mathbf B^{-1}$ in place of $\hat{\mathbf b}$, then $I_2$, and so on, until a single row $r$ remains. This must happen by column $m$, since otherwise two rows of $\mathbf B^{-1}$ would be proportional, contradicting independence. Example 4.12 (p. 179-180) applies it to Beale's problem: at the first pivot $I_0=\{1,2\}$, $I_1=\{2\}$, so $x_2$ leaves where the arbitrary rule had $x_1$ leave, and the process reaches optimality.

**Bland's rule** (p. 180, text). Order the variables. Among nonbasic variables with $z_j-c_j>0$ choose the one of smallest index to enter. Among the tied rows of the minimum ratio test choose the leaving variable of smallest index. On Beale's problem the first four tableaux coincide with the earlier ones and the rule then avoids the cycle.

**Practice and stalling** (p. 180-181, text): commercial codes mostly ignore these rules, because the lexicographic rule is expensive and Bland's rule makes long simplex paths, and because round-off tends to break ties anyway. Stalling is a long run of degenerate pivots without objective improvement, even without cycling.

## Validation of the rules (§4.7, p. 182-200)
A vector $\mathbf x$ is lexicographically positive if it is not identically zero and its first nonzero component is positive (p. 182, text). The proof shows each row of $(\hat{\mathbf b},\mathbf B^{-1})$ stays lexicographically positive (a "strongly feasible" basis) under the lexicographic rule, while the cost row gains lexicographically, so no basis repeats. Bland's rule validation and the remaining pages through the notes and exercises (p. 183-200) were not read.

## Notes
- Wiki note: BT cover the same material in [[BT ch3 - The simplex method]].
- Wiki note: the two-phase method is itself an LP whose feasibility is guaranteed, so it also proves that a feasible LP has a basic feasible solution ([[Basic feasible solution]]).

**Sources**: `text_books/Linear Optimization/BJS full book.pdf` (pdf 167-216, printed pp. 151-200). Pages viewed as images: pdf 172 (printed 156) and 182 (printed 166). The rest from the text layer, which garbles math.
**Last updated**: 2026-11-06

---

## Related pages
- [[Simplex method]] · [[Basic feasible solution]] · [[Linear programming]]
- [[BJS ch3 - The simplex method]] · [[BJS ch5 - Special simplex implementations and optimality conditions]] · [[BT ch3 - The simplex method]]
