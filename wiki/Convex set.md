---
type: definition
area: math
areas: [math, optimization]
source-ref: "Basu 2018 ch. 2, Defs 2.2-2.9, Thms 2.3, 2.8, 2.20, 2.41, 2.63, 2.66"
tags: [optimization]
---

# Convex set

**Summary**: A set containing the whole segment between any two of its points. Convexity is what makes separation by hyperplanes, duality and tractable optimisation work.

---

> [!definition] Convex set
> $X\subseteq\mathbb R^d$ is convex if for all $x,y\in X$ and $\lambda\in[0,1]$:
> $$\lambda x+(1-\lambda)y\in X.$$
>
> (source: Basu 2018, p. 7)

## Examples

Intervals, hyperplanes, halfspaces, norm balls, ellipsoids, cones, and any [[Polyhedron]] (finite intersection of halfspaces). The PSD matrices form a convex cone.

## Operations that keep convexity (Thm 2.3, p. 8)

Intersection, scaling, Minkowski sum, linear image, linear preimage. Union does not.

## Hulls

- $\mathrm{conv}(X)$ is the smallest convex set containing $X$; it is the set of finite convex combinations (Thm 2.8, p. 8).
- Caratheodory: in $\mathbb R^d$ a point of $\mathrm{conv}(X)$ lies in the hull of at most $d+1$ points of $X$ (Thm 2.67, p. 29).
- Radon and Helly give intersection and partition guarantees in dimension $d$ (Thms 2.60, 2.63).

## Main theorems

- **Separation**: a closed convex $C$ and a point outside it are separated by a hyperplane (Thm 2.20, p. 13). Hence a closed convex set is the intersection of the halfspaces containing it.
- **Supporting hyperplane** at every boundary point (Thm 2.23, p. 14).
- **Krein-Milman**: a compact convex set is the hull of its extreme points (Thm 2.41, p. 19).
- **Minkowski-Weyl**: a set is a polyhedron iff it is $\mathrm{conv}(V)+\mathrm{cone}(R)$ for finite $V,R$ (Thm 2.82). See [[Polyhedral representation theorem (n.d.)]].
- **Farkas lemma**: either $b\in\{Ax:x\ge0\}$ or a separating $u$ exists (Thm 2.25, p. 14); this is the root of [[LP duality]].

## Where it is used

A function is convex iff its epigraph is a convex set ([[Convex function]]). Feasible regions of [[Linear programming]] are polyhedra. Full treatment in [[Basu ch2 - Convex sets]].

## Where it appears
- Polyhedra as intersections of halfspaces, hyperplanes, convex hulls: [[Polyhedron]], [[BT ch2 - Geometry of linear programming]] (source: MIT (ch 1-5).pdf, Def. 2.1-2.5, pp. 42-44).
- Separating hyperplane theorem for a closed convex set and an outside point, used to prove [[Farkas lemma]] and strong duality: [[BT ch4 - Duality theory]] (Thm 4.11, p. 170).
- Convex sets, polyhedral sets, extreme points and directions: [[BJS ch2 - Linear algebra convex analysis and polyhedral sets]].

**Sources**: `Math/Convexity/Basu - Intro to Convexity.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Convex function]] · [[Polyhedron]] · [[Linear programming]] · [[LP duality]]
- [[Basu ch2 - Convex sets]] · [[Polyhedral representation theorem (n.d.)]]
