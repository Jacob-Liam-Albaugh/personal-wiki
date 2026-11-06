---
type: definition
area: math
source-ref: "Bertsimas, Tsitsiklis 1997, Def. 2.9, Thm 2.3; Bazaraa, Jarvis, Sherali 2010, ch. 2-3"
tags: [optimization]
---

# Basic feasible solution

> [!definition] Basic (feasible) solution (source: MIT (ch 1-5).pdf, p. 50, Def. 2.9)
> For a polyhedron $P$ given by equalities and inequalities, $\mathbf x^*$ is a basic solution if (i) all equality constraints are active at $\mathbf x^*$, and (ii) among the active constraints, $n$ are linearly independent. If it also satisfies all constraints it is a basic feasible solution (BFS).

**Intuition**: a corner of the feasible [[Polyhedron]] written algebraically. In standard form, choose $m$ independent columns as a basis matrix $\mathbf B$, set the other variables to zero and solve $\mathbf x_B=\mathbf B^{-1}\mathbf b$ (BT ch3, §3.1). It is feasible when $\mathbf x_B\ge\mathbf 0$.

## Key facts
- For nonempty $P$, vertex, extreme point and BFS are the same thing (BT Thm 2.3, p. 50). BT define extreme point and vertex in Def. 2.6-2.7 (pp. 46-47).
- A basic solution is degenerate if more than $n$ constraints are active; in standard form this means some basic variable is zero (BT Def. 2.10-2.11, pp. 58-59). Degeneracy depends on the representation and is what causes cycling in the [[Simplex method]] (BT ch3, §3.4; BJS ch4, §4.6).
- If an LP has an extreme point and a finite optimum, an optimal extreme point exists (BT Thm 2.7-2.8, pp. 65-66), so the simplex method can restrict itself to BFSs.
- A basis is optimal when $\mathbf B^{-1}\mathbf b\ge\mathbf 0$ and the reduced costs are nonnegative (BT Def. 3.3, p. 87).
- Finding a first BFS: artificial variables, two-phase and big-M methods (BT ch3, §3.5; BJS ch4, §4.1-4.5).
- In network flow, a basis is a rooted spanning tree (BJS ch9, Thm 9.1; see [[Network flow problem]]).

## Where it appears
- [[BT ch2 - Geometry of linear programming]]: definitions and equivalence theorem.
- [[BT ch3 - The simplex method]]: basic directions, reduced costs, basis change.
- [[BJS ch2 - Linear algebra convex analysis and polyhedral sets]], [[BJS ch3 - The simplex method]], [[BJS ch4 - Starting solution and convergence]]: the same notions with the book's own notation.
- [[BJS ch9 - Minimal cost network flows]]: tree bases.

**Sources**: `Linear Optimization/MIT (ch 1-5).pdf` (ch. 2-3); `Linear Optimization/BJS full book.pdf` (ch. 2-4, 9).
**Last updated**: 2026-11-06

---

## Related pages
- [[Polyhedron]] · [[Linear programming]] · [[Simplex method]] · [[Dual simplex method]] · [[Convex set]]
