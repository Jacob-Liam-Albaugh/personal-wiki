---
type: definition
area: dsl
source-ref: "Fong-Spivak 2019, Def. 3.35, Def. 3.44, Def. 3.68"
tags: [category-theory]
---

# Functor

**Summary**: A structure-preserving map between categories: objects to objects, morphisms to morphisms, respecting identities and composition.

---

> [!definition] Functor
> $F : C \to D$ sends objects to objects and morphisms $f : A \to B$ to $F(f) : F(A) \to F(B)$ with $F(\mathrm{id}) = \mathrm{id}$ and $F(g\circ f) = F(g)\circ F(f)$. (source: Seven Sketches, Def. 3.35, p. 91)

Examples: functors between the walking-arrow-type categories and the free and commutative squares (Exs. 3.36, 3.38, 3.41). Functors between [[Preorder]]s are monotone maps (Ex. 3.42); between [[Enriched category]]s the analogue is a V-functor (Def. 2.69).

## Instances

> [!definition] Instance
> A $C$-instance is a functor $I : C\to\mathrm{Set}$ (database instance on schema $C$). (source: Seven Sketches, Def. 3.44, p. 93)

Instances and their homomorphisms form the functor category $\mathrm{Set}^C$ (Defs. 3.54, 3.60): see [[Natural transformation]]. A diagram in a category is a functor from an indexing category (Def. 3.51). Presheaves are functors $C^{op}\to\mathrm{Set}$ (Def. 7.22): see [[Topos]]. A polynomial functor is a functor $\mathrm{Set}\to\mathrm{Set}$ of a special shape: [[Polynomial functor]].

## Data migration

For $F : C\to D$, precomposition $\Delta_F : \mathrm{Set}^D\to\mathrm{Set}^C$ pulls instances back along $F$ (Def. 3.68, p. 102). Its left and right adjoints, named $\Sigma_F$ and $\Pi_F$, are the data migration functors: [[Adjunction]] (Def. 3.70). The pullback instance of Def. 3.68 is different from the categorical pullback limit (Remark 3.100).

## Other examples

- Prop functors (identity-on-objects strict symmetric monoidal, Def. 5.11) and the semantics functor $\mathrm{SFG}_R\to\mathrm{Mat}(R)$: [[Signal flow graph]].
- Operad functors, and algebras as functors $O\to\mathrm{Set}$: [[Operad]]. A decorating functor $(F,\phi):(C,+)\to(\mathrm{Set},\times)$ for decorated cospans: [[Hypergraph category]].
- Companions and conjoints turn $\mathcal V$-functors into profunctors (Def. 4.34): [[Profunctor]].

## Where it appears

[[Natural transformation]] compares two functors; [[Adjunction]] pairs two functors; [[Yoneda lemma]] concerns representable functors. Hosts: [[Category]].

**Covered in**: Fong-Spivak (Seven Sketches) ch. 3 (pp. 91-107, functors, instances, pullback along a functor, data migration)
**Sources**: Fong, Spivak, Seven Sketches (2019), ch. 3; file `text_books/Category Theory/Spivak, Fong - Seven Sketches in Compositionality.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
[[Category]] · [[Natural transformation]] · [[Adjunction]] · [[Yoneda lemma]] · [[Polynomial functor]] · [[Preorder]] · [[Signal flow graph]] · [[Operad]] · [[Topos]]
