---
type: definition
area: dsl
source-ref: "Fong-Spivak 2019, Def. 3.6"
tags: [category-theory]
---

# Category

**Summary**: A collection of objects with composable morphisms between them, an identity on each object, and associative composition.

---

> [!definition] Category
> Objects, morphisms $f : A \to B$, composition $g \circ f$, and identities $\mathrm{id}_A$, subject to associativity and unit laws. (source: Seven Sketches, Def. 3.6)

## Intuition

A category generalizes a [[Preorder]] (at most one morphism between objects) and a monoid (one object). A graph generates a *free category* of paths (Def. 3.7). Set, with functions as morphisms, is the running example.

## Examples

- Preorders: [[Seven Sketches ch1 - Generative effects]].
- Database schemas: [[Seven Sketches ch3 - Databases]].
- Polynomial comonoids are small categories: [[Polynomial comonoid]].

## Where it appears

[[Functor]]s map between categories, [[Natural transformation]]s map between functors, [[Adjunction]] relates two categories. A category with a tensor is a [[Monoidal category]].

**Sources**: Fong, Spivak, Seven Sketches (2019), ch. 3.
**Last updated**: 2026-11-06

---

## Related pages
[[Functor]] · [[Natural transformation]] · [[Adjunction]] · [[Monoidal category]] · [[Universal property]] · [[Preorder]] · [[Enriched category]]
