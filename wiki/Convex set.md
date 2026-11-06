---
type: definition
area: math
areas: [math, optimization]
source-ref: "Basu 2018 ch. 1-2, Defs 2.2-2.9, Thms 2.3, 2.8, 2.20, 2.41, 2.49, 2.60, 2.63, 2.66, 2.70, 2.82, 2.85, 2.89 (pp. 4-41)"
tags: [optimization]
---

# Convex set

**Summary**: A set containing the whole segment between any two of its points. Convexity is what makes separation by hyperplanes, duality and tractable optimisation work. A closed convex set has two descriptions, extrinsic (halfspaces) and intrinsic (extreme points and recession directions), and the finite versions of both coincide for polyhedra.

---

> [!definition] Convex set
> $X\subseteq\mathbb R^d$ is convex if for all $x,y\in X$ and $\lambda\in[0,1]$:
> $$\lambda x+(1-\lambda)y\in X.$$
>
> (source: Basu 2018, p. 7)

## Preliminaries (Basu ch. 1, pp. 4-7)

Norms, induced distance, balls, Minkowski sum $X+Y=\{x+y\}$, open and closed sets, closure, interior, boundary, compactness (Defs 1.1-1.9). Weierstrass: a continuous function on a compact set attains its inf and sup (Thm 1.11). A symmetric matrix is positive semidefinite (PSD) iff all eigenvalues are nonnegative iff $A=B^\top B$ iff $u^\top Au\ge0$ for all $u$ (Thm 1.18, p. 7). A PD matrix $A$ gives a norm $\sqrt{x^\top Ax}$ (Ex. 1). An ellipsoid is the unit ball of such a norm (Def 2.2).

## Examples

Intervals, hyperplanes, halfspaces, norm balls, ellipsoids, cones, and any [[Polyhedron]] (finite intersection of halfspaces) (Ex. 2.1, Ex. 2). The PSD matrices form a convex cone.

## Operations that keep convexity (Thm 2.3, p. 8)

Intersection (arbitrary), scaling, Minkowski sum, linear image, linear preimage. Union does not.

## Hulls, cones, affine sets (pp. 8-12)

- $\mathrm{conv}(X)$ is the smallest convex set containing $X$; it is the set of finite convex combinations (Thm 2.8, p. 8).
- Relax the multipliers: nonnegative gives a convex cone $\mathrm{cone}(X)$, sum to one with any sign gives an affine set $\mathrm{aff}(X)$, any sign gives a linear subspace (Def 2.9, Thm 2.11, pp. 9-10).
- Affine independence has five equivalent forms, among them: $\{(x,1)\}$ is linearly independent (Prop 2.15, p. 11). An affine set is a translate of a linear subspace, or $\{x: Ax=b\}$ (Thm 2.16, p. 11-12). $\dim(X)$ is $\dim\mathrm{aff}(X)$, one less than the largest number of affinely independent points in $X$ (Prop 2.19, p. 12).
- Caratheodory (Thms 2.66-2.67, p. 29): a point in $\mathrm{cone}(X)$ lies in the cone of at most $d$ linearly independent points of $X$; a point in $\mathrm{conv}(X)$ lies in the hull of at most $d+1$ points. Hence the hull of a compact set is compact (Thm 2.68, p. 30).

## Radon, Helly and centerpoints (pp. 25-30)

- Radon (Thm 2.60): any $d+2$ points in $\mathbb R^d$ split into two sets whose hulls intersect.
- Consequence: halfspaces in $\mathbb R^d$ have VC dimension $d+1$ (Prop 2.62, p. 26). Radon and Helly are the origin of the VC-dimension count for linear classifiers.
- Helly (Thm 2.63, p. 26): if finitely many convex sets in $\mathbb R^d$ have empty intersection, some $d+1$ of them already do. Also for infinite families of compact convex sets (Cor 2.64).
- Centerpoints (p. 28): for any distribution on $\mathbb R^d$ there is a point with every halfspace through it holding mass at least $1/(d+1)$ (Thm 2.65). For a uniform triangle the value is $4/9$.

## Description 1, extrinsic: halfspaces (pp. 12-17)

> [!theorem] Separating hyperplane (Thm 2.20)
> If $C$ is closed convex and $x\notin C$, there are $a\ne0$ and $\delta$ with
> $$\langle a,y\rangle\le\delta\ \ \forall y\in C,\qquad \langle a,x\rangle>\delta.$$
>
> (source: p. 13; proof takes the nearest point of $C$ to $x$ by Weierstrass)

- Corollary 2.21: every closed convex set is an intersection of halfspaces. A finite intersection is a polyhedron (Def 2.22, p. 13).
- Supporting hyperplane at any boundary point (Thm 2.23, p. 14; sharper relative-boundary version Thm 2.39).
- General convex sets are handled by a separation oracle (p. 14); this is the interface of [[Cutting-plane methods]].
- Farkas' lemma (Thm 2.25, p. 14-15): either $b=Ax$ with $x\ge0$, or there is $u$ with $A^\top u\le0$, $\langle u,b\rangle>0$. It follows from separation, using that finitely generated cones are closed (Lemma 2.26). This is the root of [[Farkas lemma]], [[Linear programming]] and [[LP duality]].
- Polar: $X^\circ=\{y:\langle y,x\rangle\le1\ \forall x\in X\}$. It is closed and convex, and $(X^\circ)^\circ=\mathrm{cl}\,\mathrm{conv}(X\cup\{0\})$ (Prop 2.30, p. 15). The $\ell_p$ and $\ell_q$ unit balls are polar when $1/p+1/q=1$, by Holder (Ex. 2.31, Prop 2.32). Gauges and support functions are the function-side of polarity ([[Convex function]]).

## Description 2, intrinsic: faces, extreme points, recession cone (pp. 17-25)

- A face $F$ of $C$: if a point of $F$ is an average of two points of $C$, both lie in $F$. Extreme points are 0-dimensional faces (Def 2.33, p. 17). Exposed face: cut out by a supporting hyperplane (Def 2.38). A point lies in a proper face iff it is in the relative boundary (Thm 2.40, p. 18).
- Krein-Milman (Thm 2.41, p. 19): a compact convex set is the hull of its extreme points. Fails without compactness (the orthant has one extreme point; the open ball has none).
- Recession direction $r$: $x+\lambda r\in C$ for all $\lambda\ge0$. These form the closed convex cone $\mathrm{rec}(C)$; $\mathrm{lin}(C)=\mathrm{rec}(C)\cap-\mathrm{rec}(C)$ is the lineality space (Props 2.42-2.44, Def 2.45, pp. 19-20). A closed convex set is compact iff $\mathrm{rec}(C)=\{0\}$ (Thm 2.47).
- Pointed closed convex set ($\mathrm{lin}(C)=\{0\}$): $C=\mathrm{conv}(\mathrm{ext}(C))+\mathrm{rec}(C)$ (Thm 2.49, p. 21). A pointed closed cone is generated by its extreme rays (Thm 2.56). Corollary 2.57:
$$C=\mathrm{conv}(\mathrm{ext}(C))+\mathrm{cone}(\mathrm{extr}(C)).$$
- General case adds a spanning set of $\mathrm{lin}(C)$ (Thm 2.59, p. 24). The halfspace description is not unique; the intrinsic one is closer to canonical (§2.3.3, p. 24-25).

## Polyhedra (Basu §2.5, pp. 30-41)

Notation $P=\{x:Ax\le b\}$; the inequalities active at $x$ are $\mathrm{tight}(x)$.

> [!theorem] Extreme points of a polyhedron (Thm 2.70)
> $x\in P$ is an extreme point iff the rows of $A$ tight at $x$ have rank $d$.
>
> (source: p. 31)

So there are finitely many extreme points (Cor 2.71) and finitely many extreme rays (Thm 2.75, Cor 2.76: $r$ spans an extreme ray of $\{Ax\le0\}$ iff its tight rows have rank $d-1$). Vertices are extreme points, which is the geometric side of the [[Simplex method]] and [[Basic feasible solution]].

> [!theorem] Minkowski-Weyl (Thms 2.77, 2.81, 2.82)
> For $X\subseteq\mathbb R^d$ these are equivalent:
> 1. H-description: $X=\{x:Ax\le b\}$.
> 2. V-description: $X=\mathrm{conv}(V)+\mathrm{cone}(R)$ for finite $V,R$.
>
> (source: pp. 33-34; Part I from Thm 2.59 and finiteness of extreme points and rays. Part II by polarity: Thm 2.79 gives the polar of $\mathrm{conv}(V)+\mathrm{cone}(R)$ as a finite system, and double polarity returns $X$.)

A separate three-page proof by Fourier-Motzkin elimination is on [[Polyhedral representation theorem (n.d.)]].

- Valid inequalities (Thm 2.85, p. 35): $\langle c,x\rangle\le\delta$ is valid for nonempty $P$ iff $c^\top=y^\top A$ and $y^\top b\le\delta$ for some $y\ge0$. This is the source of LP strong duality ([[Lagrangian duality]]). Infeasibility certificate: $P=\emptyset$ iff $0\le-1$ is a nonnegative combination of the rows (Thm 2.88, p. 36).
- Faces of polyhedra (Thm 2.89, p. 36-38): for a face $F$ of $P$, being a face, being exposed, and $F=\{x\in P:A_Ix=b_I\}$ for some row set $I$ are the same. So a polyhedron has finitely many faces, each a polyhedron (Thm 2.90).
- Dimension (Def 2.91, Cor 2.93, p. 38-39): with $A_=$ the implicit equalities, $\dim P=d-\mathrm{rank}(A_=)$.
- Facets (Thm 2.95, p. 39-40) correspond to irredundant inequalities; a full-dimensional polyhedron has an essentially unique irredundant system, unique up to permutation and positive scaling (Thm 2.97, p. 41).

## Separation and existence in linear programming

The separating hyperplane theorem in BT's form (Thm 4.11, p. 170): if $S\subset\mathbb R^n$ is nonempty, closed and convex and $\mathbf x^*\notin S$, there is $\mathbf c$ with $\mathbf c'\mathbf x^*<\mathbf c'\mathbf x$ for all $\mathbf x\in S$. Polyhedra are closed (BT §4.7, p. 169), and a cone generated by finitely many vectors is closed and convex, which is what the proof of [[Farkas lemma]] needs. Weierstrass (BT Thm 4.10, p. 170): a continuous function on a nonempty closed bounded set attains its extremes. BJS ch. 2 (pp. 44-90) develop convex sets, extreme points, hyperplanes and cones for LP; see [[Polyhedron]].

## Where it is used

A function is convex iff its epigraph is a convex set ([[Convex function]]). Feasible regions of [[Linear programming]] are polyhedra. Optimisation over a convex set uses its normal cone ([[KKT conditions]]).

## Where it appears
- Polyhedra as intersections of halfspaces, hyperplanes, convex hulls: [[Polyhedron]] (Bertsimas-Tsitsiklis Def. 2.1-2.5, pp. 42-44, source: MIT (ch 1-5).pdf).
- Separating hyperplane theorem for a closed convex set and an outside point, used to prove [[Farkas lemma]] and strong duality (Bertsimas-Tsitsiklis Thm 4.11, p. 170): [[LP duality]].
- Convex sets, polyhedral sets, extreme points and directions (Bazaraa-Jarvis-Sherali ch. 2): [[Polyhedron]].

**Covered in**: Basu, Introduction to Convexity ch. 1-2 (pp. 4-41); Bertsimas-Tsitsiklis ch. 2 and 4 (separation use); Bazaraa-Jarvis-Sherali ch. 2 (cross-reference)
**Sources**: `text_books/Mathmatics/Basu - Intro to Convexity.pdf` (pp. 1-41 read, most proofs skimmed; proofs of Thm 2.89 and 2.95 not checked); `text_books/Linear Optimization/MIT (ch 1-5).pdf` (§4.7).
**Last updated**: 2026-11-06

---

## Related pages
- [[Convex function]] · [[Polyhedron]] · [[Linear programming]] · [[LP duality]] · [[Simplex method]]
- [[Farkas lemma]] · [[Lagrangian duality]] · [[Cutting-plane methods]] · [[Polyhedral representation theorem (n.d.)]]
