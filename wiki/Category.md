---
type: definition
area: dsl
source-ref: "Fong-Spivak 2019, Def. 3.6, Def. 3.7, Def. 3.24, Def. 3.28"
tags: [category-theory]
---

# Category

**Summary**: A collection of objects with composable morphisms between them, an identity on each object, and associative composition.

---

> [!definition] Category
> Objects, morphisms $f : A \to B$, composition $g \circ f$, and identities $\mathrm{id}_A$, subject to associativity and unit laws. (source: Seven Sketches, Def. 3.6, p. 81)

## Intuition

A category generalizes a [[Preorder]] (at most one morphism between objects) and a monoid (one object). Preorders and free categories are the two ends of a spectrum (Remark 3.23, p. 86). Set, with functions as morphisms (Def. 3.24), is the running example. A schema for a database is a finite presentation of a category (Remark 3.20).

## Free categories

- The free category $\mathrm{Free}(G)$ on a graph $G$ has paths as morphisms (Def. 3.7, p. 82). Ex. 3.13: $\mathbb N$ is free on one vertex with one loop. Ex. 3.18: imposing an equation can force others.
- Props are free symmetric monoidal analogues on a signature: [[Signal flow graph]].

## Isomorphism and opposites

- The opposite category (Ex. 3.27). An isomorphism is a morphism with a two-sided inverse (Def. 3.28, p. 88); $\{a,b,c\}\cong 3$ in Set (Ex. 3.29). Nearly-inverse maps need not be isomorphisms (Ex. 3.34).

## Databases as categories

A schema is a category $C$; an instance is a functor $C\to\mathrm{Set}$ (Def. 3.44); a morphism of instances is a natural transformation. See [[Functor]] for instances, pullback ($\Delta_F$) and data migration, and [[Natural transformation]] for instance homomorphisms and $\mathrm{Set}^C$. An instance on the one-loop schema with $s\circ s=s$ is a set with an idempotent map (Ex. 3.46: citizen to president, number to 0, expression to its value).

## Examples

- Preorders: [[Preorder]]. Enriched versions: [[Enriched category]].
- Categories of categories and structure: the sheaf toposes of [[Topos]] are categories with finite limits and a subobject classifier. $\mathrm{Cospan}_C$, $\mathrm{Prof}_{\mathcal V}$, $\mathrm{Mat}(R)$ and $\mathrm{Rel}_R$ are categories built from other data: [[Hypergraph category]], [[Profunctor]], [[Signal flow graph]].
- Polynomial comonoids are small categories: [[Polynomial comonoid]].

## Where it appears

[[Functor]]s map between categories, [[Natural transformation]]s map between functors, [[Adjunction]] relates two categories. A category with a tensor is a [[Monoidal category]]. Limits and colimits: [[Universal property]].

**Covered in**: Fong-Spivak (Seven Sketches) ch. 3 (pp. 81-90, categories, free categories, Set, isomorphism)
**Sources**: Fong, Spivak, Seven Sketches (2019), ch. 3; file `text_books/Category Theory/Spivak, Fong - Seven Sketches in Compositionality.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
[[Functor]] · [[Natural transformation]] · [[Adjunction]] · [[Monoidal category]] · [[Universal property]] · [[Preorder]] · [[Enriched category]] · [[Signal flow graph]] · [[Topos]]
