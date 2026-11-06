---
type: definition
area: dsl
source-ref: "Fong-Spivak 2019, Def. 3.35"
tags: [category-theory]
---

# Functor

**Summary**: A structure-preserving map between categories: objects to objects, morphisms to morphisms, respecting identities and composition.

---

> [!definition] Functor
> $F : C \to D$ sends objects to objects and morphisms $f : A \to B$ to $F(f) : F(A) \to F(B)$ with $F(\mathrm{id}) = \mathrm{id}$ and $F(g\circ f) = F(g)\circ F(f)$. (source: Seven Sketches, Def. 3.35)

## Intuition

A database *instance* on a schema $C$ is a functor $C \to \mathrm{Set}$ (Def. 3.44). Presheaves are functors $C^{op} \to \mathrm{Set}$. A polynomial functor is a functor $\mathrm{Set}\to\mathrm{Set}$ of a special shape: see [[Polynomial functor]].

## Examples

- Monotone maps are functors between [[Preorder]]s.
- Pullback along a functor, and data migration: [[Seven Sketches ch3 - Databases]].
- Prop functors: [[Seven Sketches ch5 - Signal flow graphs]].

## Where it appears

[[Natural transformation]] compares two functors; [[Adjunction]] pairs two functors; [[Yoneda lemma]] concerns representable functors.

**Sources**: Fong, Spivak, Seven Sketches (2019), ch. 3.
**Last updated**: 2026-11-06

---

## Related pages
[[Category]] · [[Natural transformation]] · [[Adjunction]] · [[Yoneda lemma]] · [[Polynomial functor]]
