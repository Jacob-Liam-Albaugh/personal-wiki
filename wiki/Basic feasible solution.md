---
type: definition
area: math
source-ref: "Bertsimas, Tsitsiklis 1997, Def. 2.9, Thm 2.3; Bazaraa, Jarvis, Sherali 2010, ch. 2-3"
tags: [optimization]
---

# Basic feasible solution

> [!definition] Basic (feasible) solution (source: MIT (ch 1-5).pdf, p. 50, Def. 2.9)
> For a polyhedron $P$ given by equalities and inequalities, $\mathbf x^*$ is a basic solution if (i) all equality constraints are active at $\mathbf x^*$, and (ii) among the active constraints, $n$ are linearly independent. If it also satisfies all constraints it is a basic feasible solution (BFS).

**Intuition**: a corner of the feasible [[Polyhedron]] written algebraically. In standard form, choose $m$ independent columns as a basis matrix $\mathbf B$, set the other variables to zero and solve $\mathbf x_B=\mathbf B^{-1}\mathbf b$ (BT ch3, §3.1). It is feasible when $\mathbf x_B\ge\mathbf 0$. Whether a point is basic depends on how $P$ is written: BT Figure 2.6 (p. 50) replaces $x_1+x_2+x_3=1$ by two inequalities, which makes a point basic.

> [!theorem] Equivalence (p. 50, Thm 2.3)
> For nonempty $P$ and $\mathbf x^*\in P$: $\mathbf x^*$ is a vertex $\iff$ an extreme point $\iff$ a basic feasible solution.

The extreme point and vertex definitions (BT Def. 2.6-2.7, pp. 46-47) are on [[Polyhedron]]. Two basic solutions are adjacent if $n-1$ common linearly independent constraints are active; the segment between adjacent feasible ones is an edge (BT p. 53).

## Standard form

Take $P=\{\mathbf x\mid\mathbf A\mathbf x=\mathbf b,\mathbf x\ge0\}$ with $\mathbf A$ of full row rank $m$ (BT §2.3, pp. 53-57). Bazaraa et al. define the same objects through the rank-$m$ matrix $\mathbf A$: a basis $\mathbf B$ is $m$ linearly independent columns, $\mathbf x_B=\mathbf B^{-1}\mathbf b$, $\mathbf x_N=\mathbf0$ (BJS §3.2, pp. 94-102).

> [!theorem] Basic solutions in standard form (p. 53, Thm 2.4)
> $\mathbf x$ is a basic solution iff $\mathbf A\mathbf x=\mathbf b$ and there are indices $B(1),\dots,B(m)$ with
> (a) the columns $\mathbf A_{B(1)},\dots,\mathbf A_{B(m)}$ linearly independent, and
> (b) $x_i=0$ for $i\ne B(1),\dots,B(m)$.

The columns form a basis matrix $\mathbf B$, the $x_{B(i)}$ are basic variables and the rest nonbasic. Construction: pick $m$ independent columns, set the other $n-m$ variables to zero, solve $\mathbf B\mathbf x_B=\mathbf b$ (BT p. 54).

> [!theorem] Full row rank is harmless (p. 57, Thm 2.5)
> If $\mathrm{rank}(\mathbf A)=k<m$ and rows $i_1..i_k$ are independent, deleting the other rows leaves the same polyhedron $P$.

> [!theorem] Theorems 3.1-3.4, summary of results (p. 102, image seen)
> - **3.1**: the extreme points correspond to the basic feasible solutions, and both are nonempty if the feasible region is nonempty.
> - **3.2**: if the region is nonempty, a finite optimum exists iff $\mathbf c\mathbf d_j\ge0$ for every extreme direction $\mathbf d_j$; otherwise the optimal value is unbounded.
> - **3.3**: if an optimum exists, an optimal extreme point (optimal basic feasible solution) exists.
> - **3.4**: every extreme point has a corresponding basis (not necessarily unique), and every basis has a unique corresponding extreme point. An extreme point with more than one basis is degenerate, and this happens iff $\mathbf A\mathbf x=\mathbf b$ does not itself force the degenerate basic variables to be zero.

BT's Theorems 2.3, 2.6-2.8 and Cor. 2.2 (on [[Polyhedron]]) play the roles of BJS Theorems 3.1-3.4. Optimality of an extreme point is argued geometrically first in BJS (§3.1, pp. 91-94). Enumerating all basic feasible solutions is bounded by $\binom nm$ but is rejected: that count is large, it does not detect unboundedness, and an empty region is found only after trying all column subsets (BJS p. 102). The [[Simplex method]] moves between them without enumerating.

## Degeneracy

A basic solution is degenerate if more than $n$ constraints are active (Def. 2.10, BT p. 58). In standard form this means some basic variable is zero (Def. 2.11, p. 59). Example 2.4 (p. 58): for the polyhedron there, $(2,6,0)$ is a nondegenerate BFS and $(4,0,2)$ is degenerate. Degeneracy depends on the representation, and it is what later causes cycling in the simplex method ([[Simplex initialization and anticycling]]).

## Key facts
- For nonempty $P$, vertex, extreme point and BFS are the same thing (BT Thm 2.3, p. 50). BT define extreme point and vertex in Def. 2.6-2.7 (pp. 46-47).
- A basic solution is degenerate if more than $n$ constraints are active; in standard form this means some basic variable is zero (BT Def. 2.10-2.11, pp. 58-59). Degeneracy is what causes cycling in the [[Simplex method]] ([[Simplex initialization and anticycling]]).
- If an LP has an extreme point and a finite optimum, an optimal extreme point exists (BT Thm 2.7-2.8, pp. 65-66), so the simplex method can restrict itself to BFSs.
- A basis is optimal when $\mathbf B^{-1}\mathbf b\ge\mathbf 0$ and the reduced costs are nonnegative (BT Def. 3.3, p. 87).
- Finding a first BFS: artificial variables, two-phase and big-M methods ([[Simplex initialization and anticycling]]).
- In network flow, a basis is a rooted spanning tree (BJS ch9, Thm 9.1; see [[Network flow problem]]).

**Covered in**: Bertsimas-Tsitsiklis ch. 2 §2.2-2.4 (pp. 46-61, basic solutions, standard form, degeneracy); Bazaraa-Jarvis-Sherali ch. 3 §3.1-3.2 (pp. 91-102)
**Sources**: `text_books/Linear Optimization/MIT (ch 1-5).pdf` (ch. 2-3); `text_books/Linear Optimization/BJS full book.pdf` (ch. 2-4, 9).
**Last updated**: 2026-11-06

---

## Related pages
- [[Polyhedron]] · [[Linear programming]] · [[Simplex method]] · [[Dual simplex method]] · [[Simplex initialization and anticycling]] · [[Convex set]]
- [[Network flow problem]]
