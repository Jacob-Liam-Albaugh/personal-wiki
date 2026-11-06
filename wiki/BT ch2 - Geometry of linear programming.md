---
type: paper
area: math
source-ref: "Bertsimas, Tsitsiklis 1997, ch. 2 (printed pp. 41-80)"
tags: [optimization]
authors: ["[[Dimitris Bertsimas]]", "[[John N. Tsitsiklis]]"]
year: 1997
venue: "Athena Scientific (textbook)"
file: "Linear Optimization/MIT (ch 1-5).pdf"
---

# BT ch2 - Geometry of linear programming

**Summary**: Chapter 2 defines [[Polyhedron|polyhedra]] and convex sets, gives three equivalent notions of a corner (extreme point, vertex, [[Basic feasible solution]]), specializes to standard form, treats degeneracy, and proves that an LP with an extreme point has an optimal extreme point.

**Authors**: Dimitris Bertsimas, John N. Tsitsiklis · **Year**: 1997 · **File**: `Linear Optimization/MIT (ch 1-5).pdf` (pdf pp. 57-96). Cites use printed pages; pdf = printed + 16.

---

## Problem
Make the "optimum is at a corner" observation of [[BT ch1 - Introduction]] rigorous, and give corners an algebraic test usable by the [[Simplex method]].

## Method

> [!definition] Polyhedron (source: MIT (ch 1-5).pdf, p. 42, Def. 2.1)
> A set that can be described as $\{\mathbf x\in\mathbb R^n\mid \mathbf A\mathbf x\ge\mathbf b\}$, with $\mathbf A$ an $m\times n$ matrix and $\mathbf b\in\mathbb R^m$.

Hyperplanes and halfspaces (Def. 2.3), convex sets (Def. 2.4) and convex combinations / convex hull (Def. 2.5) follow (pp. 43-44). See [[Convex set]].

> [!theorem] Convexity facts (p. 44, Thm 2.1)
> (a) Intersections of convex sets are convex. (b) Every polyhedron is convex. (c) A convex combination of finitely many elements of a convex set lies in the set. (d) The convex hull of finitely many vectors is convex.

Proofs are short: a halfspace is convex because $\mathbf a'(\lambda\mathbf x+(1-\lambda)\mathbf y)\ge\lambda b+(1-\lambda)b=b$; (c) is induction on the number of points (pp. 45-46).

**Three definitions of a corner** (§2.2, pp. 46-50):

> [!definition] Extreme point (p. 46, Def. 2.6)
> $\mathbf x\in P$ is extreme if there are no $\mathbf y,\mathbf z\in P$, both different from $\mathbf x$, and $\lambda\in[0,1]$ with
> $$\mathbf x=\lambda\mathbf y+(1-\lambda)\mathbf z .$$

> [!definition] Vertex (p. 47, Def. 2.7)
> $\mathbf x\in P$ is a vertex if some $\mathbf c$ gives $\mathbf c'\mathbf x<\mathbf c'\mathbf y$ for all $\mathbf y\in P$, $\mathbf y\ne\mathbf x$. That is, $\mathbf x$ is the unique optimum of some LP over $P$.

> [!definition] Basic (feasible) solution (p. 50, Def. 2.9)
> For $P$ given by equalities and inequalities, $\mathbf x^*$ is a basic solution if (i) all equality constraints are active at $\mathbf x^*$, and (ii) among the active constraints, $n$ are linearly independent. If it also satisfies all constraints it is a basic feasible solution.

> [!theorem] Equivalence (p. 50, Thm 2.3)
> For nonempty $P$ and $\mathbf x^*\in P$: $\mathbf x^*$ is a vertex $\iff$ an extreme point $\iff$ a basic feasible solution.

Whether a point is "basic" depends on how $P$ is written (the book's Figure 2.6: replacing $x_1+x_2+x_3=1$ by two inequalities makes a point basic) (p. 50). Two basic solutions are adjacent if $n-1$ common linearly independent constraints are active; the segment between adjacent feasible ones is an edge (p. 53).

**Standard form** (§2.3, pp. 53-57). Take $P=\{\mathbf x\mid\mathbf A\mathbf x=\mathbf b,\mathbf x\ge0\}$ with $\mathbf A$ of full row rank $m$.

> [!theorem] Basic solutions in standard form (p. 53, Thm 2.4)
> $\mathbf x$ is a basic solution iff $\mathbf A\mathbf x=\mathbf b$ and there are indices $B(1),\dots,B(m)$ with
> (a) the columns $\mathbf A_{B(1)},\dots,\mathbf A_{B(m)}$ linearly independent, and
> (b) $x_i=0$ for $i\ne B(1),\dots,B(m)$.

The columns form a basis matrix $\mathbf B$, the $x_{B(i)}$ are basic variables and the rest nonbasic. Construction: pick $m$ independent columns, set the other $n-m$ variables to zero, solve $\mathbf B\mathbf x_B=\mathbf b$ (p. 54).

> [!theorem] Full row rank is harmless (p. 57, Thm 2.5)
> If $\mathrm{rank}(\mathbf A)=k<m$ and rows $i_1..i_k$ are independent, deleting the other rows leaves the same polyhedron $P$.

**Degeneracy** (§2.4, pp. 58-61). A basic solution is degenerate if more than $n$ constraints are active (Def. 2.10, p. 58). In standard form, this means some basic variable is zero (Def. 2.11, p. 59). Example 2.4 (p. 58): for the polyhedron there, $(2,6,0)$ is a nondegenerate BFS and $(4,0,2)$ is degenerate. Degeneracy depends on the representation, and it is what later causes cycling in the [[Simplex method]] ([[BT ch3 - The simplex method]]).

**Existence and optimality of extreme points** (§2.5-2.6, pp. 62-67):

> [!theorem] Existence (p. 63, Thm 2.6; Def. 2.12: $P$ contains a line if $\mathbf x+\lambda\mathbf d\in P$ for all $\lambda$, some $\mathbf d\neq0$)
> For nonempty $P=\{\mathbf a_i'\mathbf x\ge b_i\}$ these are equivalent: (a) $P$ has an extreme point; (b) $P$ contains no line; (c) $n$ of the $\mathbf a_i$ are linearly independent.

> [!theorem] (p. 65, Cor. 2.2) Every nonempty bounded polyhedron and every nonempty standard-form polyhedron has a basic feasible solution.

> [!theorem] Optimality of extreme points (p. 65, Thm 2.7)
> If $P$ has at least one extreme point and an optimal solution exists for $\min\mathbf c'\mathbf x$ over $P$, then some optimal solution is an extreme point.

Proof idea (pp. 65-66): the optimal set $Q=\{\mathbf x\in P\mid\mathbf c'\mathbf x=v\}$ is itself a polyhedron without a line, hence has an extreme point, which is extreme in $P$. Theorem 2.8 (p. 66) strengthens this: if $P$ has an extreme point, then either the optimal cost is $-\infty$ or some extreme point is optimal (existence of an optimum is not assumed). Its proof moves along a direction $\mathbf d$ orthogonal to the active constraints with $\mathbf c'\mathbf d\le0$ until a new constraint becomes active, raising the rank of the active set without raising the cost.

**Representation** (§2.7, p. 68, Thm 2.9): a nonempty bounded polyhedron is the convex hull of its extreme points. Proof by induction on dimension: write a point as a convex combination of a point $\mathbf y$ and a point $\mathbf u$ on a lower-dimensional face (Fig. 2.16). Cor. 2.6: the convex hull of finitely many vectors is a polyhedron.

**Fourier-Motzkin elimination** (§2.8, pp. 71-74). To project out $x_n$ from $\sum_j a_{ij}x_j\ge b_i$: solve each row for $x_n$, giving lower bounds $x_n\ge d_i+\mathbf f_i'\mathbf x$ (when $a_{in}>0$), upper bounds $d_j+\mathbf f_j'\mathbf x\ge x_n$ (when $a_{jn}<0$) and $x_n$-free rows $0\ge d_k+\mathbf f_k'\mathbf x$. The projection $Q$ keeps the free rows and all pairs
$$d_j+\mathbf f_j'\mathbf x\ \ge\ d_i+\mathbf f_i'\mathbf x$$
(eqs. 2.4-2.6 and the algorithm, p. 72). It can blow up the constraint count exponentially (Exercise 2.20), so it is a proof tool, not a practical solver (p. 71). Cor. 2.4-2.5: projections and linear images of polyhedra are polyhedra.

## Results
Optimal solutions of LPs can be sought among basic feasible solutions (Thms 2.7-2.8), and a standard-form polyhedron always has one when nonempty (Cor. 2.2).

## Limitations
The chapter says the proofs in 2.5-2.6 may be skipped by readers who only care about standard form, since ch. 3 reproves those results via the simplex method (p. 41).

## Connections
- [[BJS ch2 - Linear algebra convex analysis and polyhedral sets]] and [[BJS ch3 - The simplex method]] cover the same ground; BJS use extreme directions where BT use "contains a line".
- Used by [[BT ch3 - The simplex method]] (basis changes move between adjacent BFS) and [[BT ch4 - Duality theory]] (representation and cones, §4.8-4.9).

**Sources**: `Linear Optimization/MIT (ch 1-5).pdf` (pdf 57-96); also `MIT (ch 1-2).pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Polyhedron]] · [[Basic feasible solution]] · [[Linear programming]] · [[Simplex method]] · [[Convex set]]
- [[BT ch1 - Introduction]] · [[BT ch3 - The simplex method]] · [[BJS ch2 - Linear algebra convex analysis and polyhedral sets]]
