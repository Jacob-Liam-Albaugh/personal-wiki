---
type: definition
area: dsl
source-ref: "Fong-Spivak 2019, Def. 1.30"
tags: [category-theory]
---

# Preorder

**Summary**: A set with a reflexive, transitive relation $\le$; equivalently a category with at most one morphism between any two objects.

---

> [!definition] Preorder
> A set $X$ with a relation $\le$ such that $x\le x$ and $x\le y,\ y\le z \Rightarrow x\le z$. A partial order also has antisymmetry. (source: Seven Sketches, Def. 1.30)

## Intuition

Preorders are Bool-categories (Thm. 2.49); replacing Bool by Cost gives Lawvere metric spaces. See [[Enriched category]]. Hasse diagrams draw them; monotone maps (Def. 1.59) are functors.

## Examples

- Partitions ordered by refinement (Prop. 1.19), upper sets (Prop. 1.78).
- Meets and joins (Def. 1.81); generative effects (Def. 1.93).
- Open sets of a space, in [[Seven Sketches ch7 - Logic of behavior]].

## Where it appears

[[Seven Sketches ch1 - Generative effects]]; maps between preorders can be [[Galois connection]]s.

**Sources**: Fong, Spivak, Seven Sketches (2019), ch. 1, 2.
**Last updated**: 2026-11-06

---

## Related pages
[[Category]] · [[Galois connection]] · [[Enriched category]] · [[Quantale]] · [[Functor]]
