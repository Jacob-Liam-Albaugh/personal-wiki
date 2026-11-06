---
type: definition
area: math
source-ref: "Bertsimas, Tsitsiklis 1997, Def. 2.1, ch. 2, ch. 4 §4.8-4.9; Bazaraa, Jarvis, Sherali 2010, §2.4-2.7"
tags: [optimization]
---

# Polyhedron

> [!definition] Polyhedron (source: MIT (ch 1-5).pdf, p. 42, Def. 2.1)
> A set that can be described in the form
> $$\{\mathbf x\in\mathbb R^n\mid \mathbf A\mathbf x\ge\mathbf b\},$$
> with $\mathbf A$ an $m\times n$ matrix and $\mathbf b\in\mathbb R^m$.

**Intuition**: an intersection of finitely many halfspaces. It is a [[Convex set]]. The feasible set of every [[Linear programming]] problem is a polyhedron, and a bounded one is a polytope (a convex hull of finitely many points). Bazaraa et al. call it a polyhedral set, and a polyhedral cone has the form $\{\mathbf x:\mathbf A\mathbf x\le\mathbf0\}$: hyperplanes through the origin with the rows of $\mathbf A$ as normals (BJS §2.5, pp. 70-71). A constraint whose removal does not change the set is geometrically redundant (BJS Figure 2.13).

## Convexity

Hyperplanes and halfspaces (BT Def. 2.3), convex sets (Def. 2.4) and convex combinations and convex hulls (Def. 2.5) are the vocabulary (BT pp. 43-44). A set $X$ is convex if $\lambda\mathbf x_1+(1-\lambda)\mathbf x_2\in X$ for $\mathbf x_1,\mathbf x_2\in X$ and $\lambda\in[0,1]$ (BJS p. 64); a convex combination is strict if $\lambda\in(0,1)$. A function is convex when
$$f(\lambda\mathbf x_1+(1-\lambda)\mathbf x_2)\le\lambda f(\mathbf x_1)+(1-\lambda)f(\mathbf x_2)$$
(BJS p. 70; see [[Convex function]]). Examples: halfspaces, $\{\mathbf x:\mathbf A\mathbf x=\mathbf b\}$ and $\{\mathbf x:\mathbf A\mathbf x=\mathbf b,\mathbf x\ge\mathbf0\}$. BJS also develop cones, hyperplanes, extreme points and extreme directions of general convex sets (pp. 65-69, Example 2.5).

> [!theorem] Convexity facts (p. 44, Thm 2.1)
> (a) Intersections of convex sets are convex. (b) Every polyhedron is convex. (c) A convex combination of finitely many elements of a convex set lies in the set. (d) The convex hull of finitely many vectors is convex.

Proofs are short: a halfspace is convex because $\mathbf a'(\lambda\mathbf x+(1-\lambda)\mathbf y)\ge\lambda b+(1-\lambda)b=b$; (c) is induction on the number of points (BT pp. 45-46).

## Corners of a polyhedron

> [!definition] Extreme point (p. 46, Def. 2.6)
> $\mathbf x\in P$ is extreme if there are no $\mathbf y,\mathbf z\in P$, both different from $\mathbf x$, and $\lambda\in[0,1]$ with
> $$\mathbf x=\lambda\mathbf y+(1-\lambda)\mathbf z .$$

> [!definition] Vertex (p. 47, Def. 2.7)
> $\mathbf x\in P$ is a vertex if some $\mathbf c$ gives $\mathbf c'\mathbf x<\mathbf c'\mathbf y$ for all $\mathbf y\in P$, $\mathbf y\ne\mathbf x$. That is, $\mathbf x$ is the unique optimum of some LP over $P$.

Extreme point, vertex and [[Basic feasible solution]] coincide (BT Thm 2.3, p. 50, stated on the BFS page). Each extreme point is the unique solution of $n$ linearly independent binding defining hyperplanes; it is a degenerate extreme point when more than $n$ hyperplanes are binding there (BJS Figure 2.14, pp. 72-75, for $X=\{\mathbf x:\mathbf A\mathbf x\le\mathbf b,\ \mathbf x\ge\mathbf0\}$ with $\mathbf A$ of full rank).

## Faces, edges and adjacency

- A **face** $F$ of $X$ is a set of points corresponding to some nonempty set of binding defining hyperplanes. If $r(F)$ is the maximum number of linearly independent hyperplanes binding at all points of $F$, then $\dim F=n-r(F)$. Extreme points are 0-dimensional faces and an **edge** a one-dimensional face. A face of dimension $\dim X-1$ is a **facet** (BJS pp. 71-75).
- Two extreme points are **adjacent** if the segment joining them is an edge, equivalently they share $n-1$ linearly independent binding hyperplanes (BJS; BT p. 53 for basic solutions). The adjacency is what a simplex pivot moves along ([[Simplex method]]).
- Whether a point is "basic" depends on how $P$ is written (BT Figure 2.6, p. 50).

## Directions and extreme rays

A **direction** of $X$ is a nonzero $\mathbf d$ with $\mathbf x+\lambda\mathbf d\in X$ for all $\mathbf x\in X$ and $\lambda\ge0$; for the set above, $\mathbf d\ge\mathbf0$ with $\mathbf A\mathbf d\le\mathbf0$. An **extreme direction** is one that cannot be written as a positive combination of two distinct directions. A normalized set $D=\{\mathbf d:\mathbf A\mathbf d\le\mathbf0,\ \mathbf1'\mathbf d=1,\ \mathbf d\ge\mathbf0\}$ has as its extreme points exactly the extreme directions (the numerical example on BJS p. 75 lists two extreme directions, one of them $(2/3,1/3)'$, **[unverified]**). BT's "extreme ray" of the recession cone is BJS's extreme direction.

- Definition 4.1 (BT p. 174): $C$ is a cone if $\lambda\mathbf x\in C$ for all $\lambda\ge0$, $\mathbf x\in C$.
- Extreme rays of a pointed polyhedral cone and of the recession cone (Def. 4.2, Thm 4.12-4.14, BT pp. 175-178). Theorems 4.13-4.14 tie optimality of a linear cost over a pointed polyhedron to extreme points and rays. These statements are paraphrased from headings and the text layer, not read as page images. **[unverified]**
- When the simplex method ends with an unboundedness certificate (a column of $\mathbf B^{-1}\mathbf A$ with no positive entry), the $j$th basic direction is an extreme ray of the recession cone (BT p. 179; [[Simplex method]]).

## Existence and optimality of extreme points

> [!theorem] Existence (p. 63, Thm 2.6; Def. 2.12: $P$ contains a line if $\mathbf x+\lambda\mathbf d\in P$ for all $\lambda$, some $\mathbf d\neq0$)
> For nonempty $P=\{\mathbf a_i'\mathbf x\ge b_i\}$ these are equivalent: (a) $P$ has an extreme point; (b) $P$ contains no line; (c) $n$ of the $\mathbf a_i$ are linearly independent.

> [!theorem] (p. 65, Cor. 2.2) Every nonempty bounded polyhedron and every nonempty standard-form polyhedron has a basic feasible solution.

> [!theorem] Optimality of extreme points (p. 65, Thm 2.7)
> If $P$ has at least one extreme point and an optimal solution exists for $\min\mathbf c'\mathbf x$ over $P$, then some optimal solution is an extreme point.

Proof idea (BT pp. 65-66): the optimal set $Q=\{\mathbf x\in P\mid\mathbf c'\mathbf x=v\}$ is itself a polyhedron without a line, hence has an extreme point, which is extreme in $P$. Theorem 2.8 (p. 66) strengthens this: if $P$ has an extreme point, then either the optimal cost is $-\infty$ or some extreme point is optimal (existence of an optimum is not assumed). Its proof moves along a direction $\mathbf d$ orthogonal to the active constraints with $\mathbf c'\mathbf d\le0$ until a new constraint becomes active, raising the rank of the active set without raising the cost. BT say the proofs in 2.5-2.6 may be skipped by readers who only care about standard form, since ch. 3 reproves them via the simplex method (p. 41).

## Representation theorems

A bounded polyhedral set (polytope) is the convex hull of its extreme points; an unbounded one needs extreme directions as well (BJS pp. 75-77, Figure 2.18).

**Bounded case** (BT §2.7, p. 68, Thm 2.9): a nonempty bounded polyhedron is the convex hull of its extreme points. Proof by induction on dimension: write a point as a convex combination of a point $\mathbf y$ and a point $\mathbf u$ on a lower-dimensional face (BT Fig. 2.16). Cor. 2.6: the convex hull of finitely many vectors is a polyhedron.

> [!theorem] Theorem 2.1, Representation Theorem (p. 77, image seen)
> Let $X=\{\mathbf x:\mathbf A\mathbf x\le\mathbf b,\ \mathbf x\ge\mathbf0\}$ be nonempty. Then $X$ has a nonempty finite set of extreme points $\mathbf x_1,\dots,\mathbf x_k$. The set of extreme directions is empty iff $X$ is bounded; otherwise it is nonempty and finite, $\mathbf d_1,\dots,\mathbf d_\ell$. Moreover $\bar{\mathbf x}\in X$ iff
> $$\bar{\mathbf x}=\sum_{j=1}^k\lambda_j\mathbf x_j+\sum_{j=1}^\ell\mu_j\mathbf d_j$$
> $$\sum_{j=1}^k\lambda_j=1,\quad\lambda_j\ge0,\quad\mu_j\ge0$$

The proof (BJS pp. 77-79) takes a point and the maximum number $r$ of independent binding hyperplanes, and moves along a line within a face until more hyperplanes bind, an induction on $n-r$ (Figure 2.19). Corollary 2.1 (p. 80, read from text) restates it for a bounded set as a convex combination of extreme points. Example 2.7 (p. 81): the representation of a given polyhedron by extreme points and directions is computed explicitly. The theorem is used in [[Dantzig-Wolfe decomposition]], where each block is represented through its extreme points and directions.

> [!theorem] Theorem 4.15, resolution theorem (p. 179)
> Let $P=\{\mathbf x\mid\mathbf A\mathbf x\ge\mathbf b\}$ be nonempty with at least one extreme point, extreme points $\mathbf x^1,\dots,\mathbf x^k$ and a complete set of extreme rays $\mathbf w^1,\dots,\mathbf w^r$. Then $P=Q$ with
> $$Q=\Big\{\sum_i\lambda_i\mathbf x^i+\sum_j\theta_j\mathbf w^j\ \Big|\ \lambda_i,\theta_j\ge0,\ \sum_i\lambda_i=1\Big\}$$

Corollaries (BT pp. 182-183): a bounded polyhedron is the convex hull of its extreme points; Theorem 4.16: a finitely generated set is a polyhedron (the converse of the resolution theorem). Example 4.10 (p. 181) decomposes an unbounded polyhedron. BJS's version is stated for $\{\mathbf A\mathbf x\le\mathbf b,\mathbf x\ge\mathbf0\}$; BT's resolution theorem needs only an extreme point, and the BT proof uses the simplex method and duality while BJS argue directly on binding hyperplanes. Basu's route is Minkowski-Weyl (below).

## Projection: Fourier-Motzkin elimination

To project out $x_n$ from $\sum_j a_{ij}x_j\ge b_i$ (BT §2.8, pp. 71-74): solve each row for $x_n$, giving lower bounds $x_n\ge d_i+\mathbf f_i'\mathbf x$ (when $a_{in}>0$), upper bounds $d_j+\mathbf f_j'\mathbf x\ge x_n$ (when $a_{jn}<0$) and $x_n$-free rows $0\ge d_k+\mathbf f_k'\mathbf x$. The projection $Q$ keeps the free rows and all pairs
$$d_j+\mathbf f_j'\mathbf x\ \ge\ d_i+\mathbf f_i'\mathbf x$$
(eqs. 2.4-2.6 and the algorithm, p. 72). It can blow up the constraint count exponentially (Exercise 2.20), so it is a proof tool, not a practical solver (p. 71). Cor. 2.4-2.5: projections and linear images of polyhedra are polyhedra.

## Polyhedral theory in the convex-analysis view

Basu derives the same facts from general convexity (Basu §2.5, pp. 30-41; full statements on [[Convex set]]):
- Extreme points of $P=\{x:Ax\le b\}$ are the $x$ whose tight rows have rank $d$ (Thm 2.70, p. 31). There are finitely many extreme points and extreme rays (Cor 2.71, Thm 2.75); $r$ spans an extreme ray of $\{Ax\le0\}$ iff its tight rows have rank $d-1$ (Cor 2.76).
- Every face is exposed and has the form $\{x\in P:A_Ix=b_I\}$ (Thm 2.89, pp. 36-38), so there are finitely many faces, each a polyhedron.
- $\dim P=d-\mathrm{rank}(A_=)$ with $A_=$ the implicit equalities (Cor 2.93).
- Facets correspond to irredundant inequalities, unique up to permutation and positive scaling for full-dimensional $P$ (Thms 2.95, 2.97, pp. 39-41).
- Minkowski-Weyl (Thm 2.82): a set has an H-description iff it has a V-description.

## Key facts
- Every polyhedron is convex; intersections of convex sets are convex (BT Thm 2.1, p. 44).
- A nonempty polyhedron has an extreme point iff it contains no line (BT Thm 2.6, p. 63).
- A nonempty bounded polyhedron is the convex hull of its extreme points (BT Thm 2.9, p. 68).
- Extreme point = vertex = [[Basic feasible solution]] (BT Thm 2.3, p. 50). These are the corners the [[Simplex method]] walks along.
- If an LP over a polyhedron with an extreme point has a finite optimum, an optimal extreme point exists (BT Thm 2.7-2.8, pp. 65-66).
- Projections and linear images of polyhedra are polyhedra, proved by Fourier-Motzkin elimination (BT §2.8, pp. 71-74).
- A polyhedron is the sum of the convex hull of its extreme points and the cone of its extreme directions (BJS Thm 2.1; BT Thm 4.15).
- Farkas' lemma and separating hyperplanes, used for the geometric proof of duality, are on [[Farkas lemma]].

## Representations
- a nonempty polyhedron is exactly conv(V) + cone(D) for finite V and D (Minkowski-Weyl; source: Basu 2018, Thms 2.77, 2.81, 2.82, pp. 33-34). Extreme points correspond to constraint sets whose tight rows have rank d (Thm 2.70, p. 31).

**Covered in**: Bertsimas-Tsitsiklis ch. 2 (pp. 42-74, geometry and representation) and ch. 4 §4.8-4.9 (pp. 174-183, cones and resolution theorem); Bazaraa-Jarvis-Sherali ch. 2 (pp. 45-90, convex sets, polyhedral sets, faces, representation); Basu ch. 2 §2.5 (pp. 30-41)
**Sources**: `text_books/Linear Optimization/MIT (ch 1-5).pdf` (ch. 2, 4); `text_books/Linear Optimization/BJS full book.pdf` (ch. 2); `text_books/Mathmatics/Basu - Intro to Convexity.pdf` (§2.5).
**Last updated**: 2026-11-06

---

## Related pages
- [[Basic feasible solution]] · [[Linear programming]] · [[Convex set]] · [[Convex function]] · [[Simplex method]] · [[LP duality]] · [[Farkas lemma]] · [[Dantzig-Wolfe decomposition]]
- [[Polyhedral representation theorem (n.d.)]]
