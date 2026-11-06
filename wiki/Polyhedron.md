---
type: definition
area: math
source-ref: "Bertsimas, Tsitsiklis 1997, Def. 2.1; Bazaraa, Jarvis, Sherali 2010, §2.5"
tags: [optimization]
---

# Polyhedron

> [!definition] Polyhedron (source: MIT (ch 1-5).pdf, p. 42, Def. 2.1)
> A set that can be described in the form
> $$\{\mathbf x\in\mathbb R^n\mid \mathbf A\mathbf x\ge\mathbf b\},$$
> with $\mathbf A$ an $m\times n$ matrix and $\mathbf b\in\mathbb R^m$.

**Intuition**: an intersection of finitely many halfspaces. It is a [[Convex set]]. The feasible set of every [[Linear programming]] problem is a polyhedron, and a bounded one is a polytope (a convex hull of finitely many points).

## Key facts
- Every polyhedron is convex; intersections of convex sets are convex (BT Thm 2.1, p. 44).
- A nonempty polyhedron has an extreme point iff it contains no line (BT Thm 2.6, p. 63).
- A nonempty bounded polyhedron is the convex hull of its extreme points (BT Thm 2.9, p. 68).
- Extreme point = vertex = [[Basic feasible solution]] (BT Thm 2.3, p. 50). These are the corners the [[Simplex method]] walks along.
- If an LP over a polyhedron with an extreme point has a finite optimum, an optimal extreme point exists (BT Thm 2.7-2.8, pp. 65-66).
- Projections and linear images of polyhedra are polyhedra, proved by Fourier-Motzkin elimination (BT §2.8, pp. 71-74).
- BJS handle unbounded polyhedra with extreme directions; a polyhedron is then the sum of the convex hull of its extreme points and the cone of its extreme directions ([[BJS ch2 - Linear algebra convex analysis and polyhedral sets]]).

## Where it appears
- [[BT ch2 - Geometry of linear programming]]: definitions and theorems above.
- [[BJS ch2 - Linear algebra convex analysis and polyhedral sets]]: polyhedral sets and cones, representation theorem.
- [[BT ch4 - Duality theory]]: cones, extreme rays and the representation of polyhedra in §4.8-4.9.

## Representations
- a nonempty polyhedron is exactly conv(V) + cone(D) for finite V and D (Minkowski-Weyl; source: Basu 2018, Thms 2.77, 2.81, 2.82, pp. 33-34). Extreme points correspond to constraint sets whose tight rows have rank d (Thm 2.70, p. 31).

**Sources**: `Linear Optimization/MIT (ch 1-5).pdf`; `Linear Optimization/BJS full book.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Basic feasible solution]] · [[Linear programming]] · [[Convex set]] · [[Convex function]] · [[Simplex method]] · [[LP duality]]
- [[Polyhedral representation theorem (n.d.)]], [[Basu ch2 - Convex sets]], [[Convex set]].
