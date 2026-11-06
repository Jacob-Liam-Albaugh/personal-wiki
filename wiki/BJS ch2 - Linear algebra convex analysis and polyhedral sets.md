---
type: paper
area: math
source-ref: "Bazaraa, Jarvis, Sherali 2010, ch. 2 (printed pp. 45-90)"
tags: [optimization]
authors: ["[[Mokhtar S. Bazaraa]]", "[[John J. Jarvis]]", "[[Hanif D. Sherali]]"]
year: 2010
venue: "Wiley, Linear Programming and Network Flows, 4th ed. (textbook)"
file: "text_books/Linear Optimization/BJS full book.pdf"
---

# BJS ch2 - Linear algebra convex analysis and polyhedral sets

**Summary**: Background in linear algebra (vectors, matrices, simultaneous equations), convex sets and functions, and a geometric treatment of polyhedral sets: faces, extreme points, extreme directions, and the representation theorem that writes every point of a polyhedral set as a convex combination of extreme points plus a nonnegative combination of extreme directions. See [[Polyhedron]], [[Convex set]], [[Convex function]].

**Authors**: Mokhtar S. Bazaraa, John J. Jarvis, Hanif D. Sherali · **Year**: 2010 · **File**: `text_books/Linear Optimization/BJS full book.pdf` (printed pp. 45-90). Cites use printed pages; pdf = printed + 16.

## Vectors, matrices, equations (§2.1-2.3, p. 45-64)
Standard material (p. 45-63): linear independence, bases and rank of a vector set, matrix operations, elementary row operations and pivoting, row echelon form and inverses (Examples 2.1-2.3). Simultaneous equations $\mathbf A\mathbf x=\mathbf b$ are solved by reducing the augmented matrix to upper triangular form with elementary operations and back substitution (§2.3, p. 61-64, Example 2.4). A general solution is a particular solution plus a free-parameter combination, e.g. a free $x_4=\lambda$ gives $x_3=-2-\tfrac14\lambda$ and $x_2=4+\tfrac14\lambda$ (p. 64, read from text). This is the machinery behind basic solutions in [[BJS ch3 - The simplex method]].

## Convex sets and functions (§2.4, p. 64-70)
A set $X\subset\mathbb R^n$ is **convex** if for $\mathbf x_1,\mathbf x_2\in X$ and $\lambda\in[0,1]$ (p. 64, read from text):
$$\lambda\mathbf x_1+(1-\lambda)\mathbf x_2\in X$$
A point of this form is a convex combination (strict if $\lambda\in(0,1)$). Examples of convex sets include half-spaces, $\{\mathbf x:\mathbf A\mathbf x=\mathbf b\}$ and $\{\mathbf x:\mathbf A\mathbf x=\mathbf b,\mathbf x\ge\mathbf0\}$. The section develops convex hulls, cones, hyperplanes and half-spaces, extreme points and extreme directions of general convex sets (p. 65-69, Example 2.5). A function $f$ is **convex** if (p. 70, read from text)
$$f(\lambda\mathbf x_1+(1-\lambda)\mathbf x_2)\le\lambda f(\mathbf x_1)+(1-\lambda)f(\mathbf x_2)$$
for all $\lambda\in[0,1]$, geometrically the chord lies above the graph. $f$ is concave iff $-f$ is convex. Convex piecewise linear functions arise in LP in parametric analysis ([[BJS ch6 - Duality and sensitivity analysis]]).

## Polyhedral sets and cones (§2.5, p. 70-71)
A **polyhedral set** is the intersection of a finite number of half-spaces. A **polyhedral cone** has the form $\{\mathbf x:\mathbf A\mathbf x\le\mathbf0\}$, the hyperplanes passing through the origin, with the rows of $\mathbf A$ as normals (p. 71, read from text). A constraint whose removal does not change the set is geometrically redundant (Figure 2.13).

## Extreme points, faces, directions (§2.6, p. 71-75)
Assume $X=\{\mathbf x:\mathbf A\mathbf x\le\mathbf b,\ \mathbf x\ge\mathbf0\}$ with $\mathbf A$ of full rank (p. 72-75, images seen at p. 73).
- Each extreme point is the unique solution of $n$ linearly independent binding defining hyperplanes. A point can be a *degenerate* extreme point when more than $n$ hyperplanes are binding there (Figure 2.14).
- A **face** $F$ of $X$ is a set of points corresponding to some nonempty set of binding defining hyperplanes. If $r(F)$ is the maximum number of linearly independent hyperplanes binding at all points of $F$, then $\dim F=n-r(F)$. Extreme points are 0-dimensional faces and an **edge** a one-dimensional face. A face of dimension $\dim X-1$ is a **facet**.
- Two extreme points are **adjacent** if the segment joining them is an edge, equivalently they share $n-1$ linearly independent binding hyperplanes. This adjacency is what a simplex pivot moves along ([[Simplex method]]).
- A **direction** of $X$ is a nonzero $\mathbf d$ with $\mathbf x+\lambda\mathbf d\in X$ for all $\mathbf x\in X$ and $\lambda\ge0$; for the set above, $\mathbf d\ge\mathbf0$ with $\mathbf A\mathbf d\le\mathbf0$. An **extreme direction** is one that cannot be written as a positive combination of two distinct directions. A normalized set $D=\{\mathbf d:\mathbf A\mathbf d\le\mathbf0,\ \mathbf1'\mathbf d=1,\ \mathbf d\ge\mathbf0\}$ has as its extreme points exactly the extreme directions (the numerical example on p. 75 lists two extreme directions, one of them $(2/3,1/3)'$, **[unverified]**).

## Representation of polyhedral sets (§2.7, p. 75-81)
Basic ideas (p. 75-77): a bounded polyhedral set (polytope) is the convex hull of its extreme points. An unbounded one needs extreme directions as well (Figure 2.18).

> [!theorem] Theorem 2.1, Representation Theorem (p. 77, image seen)
> Let $X=\{\mathbf x:\mathbf A\mathbf x\le\mathbf b,\ \mathbf x\ge\mathbf0\}$ be nonempty. Then $X$ has a nonempty finite set of extreme points $\mathbf x_1,\dots,\mathbf x_k$. The set of extreme directions is empty iff $X$ is bounded; otherwise it is nonempty and finite, $\mathbf d_1,\dots,\mathbf d_\ell$. Moreover $\bar{\mathbf x}\in X$ iff
> $$\bar{\mathbf x}=\sum_{j=1}^k\lambda_j\mathbf x_j+\sum_{j=1}^\ell\mu_j\mathbf d_j$$
> $$\sum_{j=1}^k\lambda_j=1,\quad\lambda_j\ge0,\quad\mu_j\ge0$$

The proof (p. 77-79) takes a point and the maximum number $r$ of independent binding hyperplanes, and moves along a line within a face until more hyperplanes bind, an induction on $n-r$ (Figure 2.19). Corollary 2.1 (p. 80, read from text) restates it for a bounded set as a convex combination of extreme points.

Example 2.7 (p. 81): the representation of a given polyhedron by extreme points and directions is computed explicitly. The theorem is also used in [[BJS ch7 - The decomposition principle]], where each block is represented through its extreme points and directions.

## Exercises and notes (p. 82-90)
Exercises on linear algebra, convex sets, representations and Farkas-type results, with notes on the sources (read from text, not detailed).

## Notes
- Wiki note: BT prove an equivalent resolution theorem for polyhedra with extreme rays in [[BT ch2 - Geometry of linear programming]] and [[BT ch4 - Duality theory]] (Theorem 4.15 as used in [[BT ch6 - Large scale optimization]]). BJS's version is stated for $\{\mathbf A\mathbf x\le\mathbf b,\mathbf x\ge\mathbf0\}$ and "extreme direction" corresponds to BT's extreme ray.
- Wiki note: the claim in [[Polyhedron]] that unbounded polyhedra are the sum of the convex hull of extreme points and the cone of extreme directions is Theorem 2.1 above.

**Sources**: `text_books/Linear Optimization/BJS full book.pdf` (pdf 61-106, printed pp. 45-90). Pages viewed as images: pdf 89 (printed 73) and 93 (printed 77, Theorem 2.1). All else from the text layer.
**Last updated**: 2026-11-06

---

## Related pages
- [[Polyhedron]] · [[Convex set]] · [[Convex function]] · [[Linear programming]] · [[Simplex method]] · [[Basic feasible solution]]
- [[BT ch2 - Geometry of linear programming]] · [[BJS ch1 - Introduction]] · [[BJS ch3 - The simplex method]] · [[BJS ch7 - The decomposition principle]]
