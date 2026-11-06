---
type: definition
area: dsl
source-ref: "Fong-Spivak 2019, Def. 2.46"
tags: [category-theory]
---

# Enriched category

**Summary**: A category whose hom "sets" are objects of a monoidal preorder $\mathcal V$; Bool gives preorders, Cost gives Lawvere metric spaces.

---

> [!definition] V-category
> A set of objects with $\mathcal V(x,y) \in \mathcal V$, such that $I \le \mathcal V(x,x)$ and $\mathcal V(x,y)\otimes\mathcal V(y,z)\le \mathcal V(x,z)$. (source: Seven Sketches, Def. 2.46)

## Intuition

Thm. 2.49: Bool-categories are preorders. Cost-categories are Lawvere metric spaces (Def. 2.53). $\mathcal V$-functors (Def. 2.69) and products (Def. 2.74) follow. Composition of $\mathcal V$-matrices (Def. 2.100) computes shortest paths when $\mathcal V$ = Cost. When $\mathcal V$ is closed, it is a [[Quantale]].

## Where it appears

[[Seven Sketches ch2 - Resource theories]], [[Seven Sketches ch4 - Collaborative design]] ([[Profunctor]]s).

**Sources**: Fong, Spivak, Seven Sketches (2019), ch. 2.
**Last updated**: 2026-11-06

---

## Related pages
[[Preorder]] · [[Monoidal category]] · [[Quantale]] · [[Profunctor]] · [[Category]]
