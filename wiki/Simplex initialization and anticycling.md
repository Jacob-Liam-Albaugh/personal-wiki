---
type: method
area: math
source-ref: "Bertsimas, Tsitsiklis 1997, ch. 3 §3.4-3.5; Bazaraa, Jarvis, Sherali 2010, ch. 4"
tags: [optimization]
---

# Simplex initialization and anticycling

**Summary**: The two things the [[Simplex method]] needs beyond its basic iteration: a starting [[Basic feasible solution]] (artificial variables, two-phase, big-M, a single artificial variable) and a guarantee against cycling at degenerate vertices (lexicographic rule, Bland's rule).

## Starting basis

The simplex method needs a basis $\mathbf B$ with $\hat{\mathbf b}=\mathbf B^{-1}\mathbf b\ge\mathbf0$; it can always be started from the identity (BJS §4.1, pp. 151-153). Easy case: constraints $\mathbf A\mathbf x\le\mathbf b$, $\mathbf x\ge\mathbf0$ with $\mathbf b\ge\mathbf0$, where the slack variables form the identity basis. Otherwise artificial variables $\mathbf x_a$ are added so that $\mathbf A\mathbf x+\mathbf x_a=\mathbf b$. A slack that already has a unit column (coefficient $+1$ in one row only) needs no artificial in that row, so fewer artificials are needed (BJS Example 4.2, p. 154).

## Two-phase method

Make $\mathbf b\ge0$, add artificial variables (BT §3.5, pp. 111-118):
$$\min\ y_1+\cdots+y_m\quad\text{s.t.}\quad \mathbf A\mathbf x+\mathbf y=\mathbf b,\ \mathbf x,\mathbf y\ge0$$
(p. 112). $\mathbf x=0,\mathbf y=\mathbf b$ is a BFS. Positive optimal cost means the original is infeasible; zero cost gives a feasible $\mathbf x$. If artificials remain in the final basis at level zero, pivot them out using any nonzero entry of $\mathbf B^{-1}\mathbf A_j$; a row of zeros there means $\mathbf A$ has a redundant row, which is deleted (BT pp. 112-115, Example 3.8). Two-phase summary (BT p. 117): infeasibility is detected in Phase I, redundancy is repaired at the end of Phase I, unboundedness appears in Phase II, else Phase II ends optimal.

BJS (§4.2, pp. 154-164): **Phase I** minimizes the sum of the artificial variables $x_0=\mathbf 1\mathbf x_a$ subject to $\mathbf A\mathbf x+\mathbf x_a=\mathbf b$, $\mathbf x,\mathbf x_a\ge\mathbf0$. If the original problem is feasible the optimum is zero, and the artificials leave the basis (p. 154). At the end of Phase I:
- if $x_0>0$ the problem is infeasible and one stops;
- otherwise the $x_0$ row and column are dropped, remaining artificials at level zero are removed from the basis, and **Phase II** starts with the original cost row (p. 165).

The tableau starts with the $x_0$ row $z_j-c_j=-1$ for the artificials and is brought to canonical form by adding each constraint row to row $x_0$. During Phase I the original $z$ row is carried along (and may break ties). Example 4.3 (Figure 4.1, p. 156, image seen) has $x_0$ initially $0$ with artificials $x_6,x_7$ in rows 1 and 2, and after canonicalization the $x_0$ row has right-hand side $3$. Two pivots then give $x_0=0$ with basis $\{x_1,x_2,x_5\}$ and the vertex $(1/2,3/2)$ of the region, a point on the path to the optimum in Figure 4.1. Examples 4.4-4.5 (pp. 158-164) treat redundant constraints (an artificial stays basic at zero) and infeasibility. The two-phase method is itself an LP whose feasibility is guaranteed, so it also proves that a feasible LP has a basic feasible solution.

## Big-M method

Combine both phases in one problem (BJS §4.3-4.4, pp. 165-173; p. 166, image seen):
$$\min\ z_{bigM}=\mathbf c\mathbf x+M\,\mathbf 1\mathbf x_a$$
$$\mathbf A\mathbf x+\mathbf x_a=\mathbf b,\quad\mathbf x,\mathbf x_a\ge\mathbf0$$
$M$ is a very large positive number acting as a penalty on any solution with $\mathbf x_a\ne\mathbf0$. BT's version minimizes $\sum_jc_jx_j+M\sum_iy_i$ with $M$ symbolic and larger than any number it is compared with (BT p. 117). Equivalently, it minimizes $\mathbf 1\mathbf x_a$ first and, among the minimizers, $\mathbf c\mathbf x$. The starting point $\mathbf x_a=\mathbf b$ has the unattractive value $M\mathbf 1\mathbf b$, so the simplex method drives the artificials out. In tableau form, with cost row $(1,-1,2,0,0,0,-M,-M)$ for Example 4.6, rows 1 and 2 are multiplied by $M$ and added to row 0, giving $z_2-c_2=2+2M$ and right-hand side $3M$ (p. 166, image seen).

Cases (p. 167-171): the optimum with $\mathbf x_a=\mathbf0$ is optimal for the original problem; an optimum with some artificial positive means the original is infeasible; an unbounded big-M problem needs care. BJS section 4.4 (pp. 172-173) is titled "How big should big-M be?" and was not read.

## Single artificial variable

A single artificial variable is appended to the Phase I tableau, and one pivot on its column gives a tableau ready for the two-phase method (BJS §4.5, pp. 173-175, Example 4.10; the column is not transcribed). The two-phase or big-M analysis carries over (Exercise 4.19, p. 175).

## Degenerate pivots and stalling

With $\theta^*=0$ the basis changes but the point does not (BT Fig. 3.3, p. 93: after a basis change the basic directions $\mathbf h,-\mathbf g$ can lead to a better vertex). Degeneracy causes conceptual and computational problems (BJS p. 175): a zero reduced cost at an optimal degenerate point does not prove alternative optima, the dual interpretation $\partial z/\partial b_i=w_i$ is not a realizable rate of change, and not every optimal basis satisfies $z_j-c_j\le0$ for all $j$.

> [!theorem] Theorem 4.1 (p. 176, text)
> Given an optimal extreme point solution of a minimization LP, there exists an associated optimal basis with $z_j-c_j\le0$ for all $j=1,\dots,n$.

The anticycling rules below prove it constructively by making sure no basis repeats.

## Cycling

BT Example 3.6 (p. 104) cycles through six degenerate pivots (all $\theta^*=0$) back to the starting tableau (BT §3.4, pp. 108-111).

**Beale's example** (BJS Example 4.11, pp. 176-178): a seven-variable problem with three equality rows and optimum $x_1=3/4$, $x_4=x_6=1$, other variables zero, value $-5/4$. With the largest-coefficient entering rule and arbitrary tie-breaking, the simplex method cycles (the tableaux repeat).

**Lexicographic rule.** BT: if all rows except the zeroth are lexicographically positive and the pivot row is chosen as the lexicographically smallest of $(\text{row})/u_i$ over $u_i>0$ then rows stay lexicographically positive, the zeroth row strictly increases lexicographically, and no basis repeats (Thm 3.4, p. 110). BJS (pp. 178-179, formulas described from the text layer): choose the entering $x_k$ as usual. Let $I_0$ be the set of rows attaining the minimum ratio $\hat b_i/y_{ik}$ over $y_{ik}>0$. If $I_0$ is a single row it leaves. Otherwise form $I_1$ from the rows of $I_0$ minimizing the same ratio with column $\mathbf y_1$ of $\mathbf B^{-1}$ in place of $\hat{\mathbf b}$, then $I_2$, and so on, until a single row $r$ remains. This must happen by column $m$, since otherwise two rows of $\mathbf B^{-1}$ would be proportional, contradicting independence. BJS Example 4.12 (pp. 179-180) applies it to Beale's problem: at the first pivot $I_0=\{1,2\}$, $I_1=\{2\}$, so $x_2$ leaves where the arbitrary rule had $x_1$ leave, and the process reaches optimality.

**Bland's rule** (BT p. 111; BJS p. 180). Enter the smallest-index variable with $r_j<0$ (BJS: $z_j-c_j>0$); among tied rows of the minimum ratio test take the leaving variable of smallest index. It prevents cycling and suits revised implementations that compute reduced costs one at a time. On Beale's problem the first four tableaux coincide with the earlier ones and the rule then avoids the cycle.

**Validation** (BJS §4.7, pp. 182-200). A vector $\mathbf x$ is lexicographically positive if it is not identically zero and its first nonzero component is positive (p. 182). The proof shows each row of $(\hat{\mathbf b},\mathbf B^{-1})$ stays lexicographically positive (a "strongly feasible" basis) under the lexicographic rule, while the cost row gains lexicographically, so no basis repeats. The validation of Bland's rule and the remaining pages through the notes and exercises (pp. 183-200) were not read.

**Practice and stalling** (BJS pp. 180-181): commercial codes mostly ignore these rules, because the lexicographic rule is expensive and Bland's rule makes long simplex paths, and because round-off tends to break ties anyway. Stalling is a long run of degenerate pivots without objective improvement, even without cycling.

## Key facts
- Phase I either returns a BFS, proves infeasibility, or exposes a redundant row; Phase II then detects unboundedness or optimality.
- Lexicographic and Bland rules guarantee finite termination; commercial codes rely on perturbation and round-off instead.
- Degeneracy is a property of the representation ([[Basic feasible solution]]).

**Covered in**: Bertsimas-Tsitsiklis ch. 3 §3.4-3.5 (pp. 108-118, anticycling and initialization); Bazaraa-Jarvis-Sherali ch. 4 (pp. 151-200)
**Sources**: `text_books/Linear Optimization/MIT (ch 1-5).pdf` (ch. 3); `text_books/Linear Optimization/BJS full book.pdf` (ch. 4).
**Last updated**: 2026-11-06

---

## Related pages
- [[Simplex method]] · [[Basic feasible solution]] · [[Linear programming]] · [[Revised simplex method]]
