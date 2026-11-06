---
type: theorem
area: dsl
source-ref: "Niu-Spivak 2024, Lemma 1.10"
tags: [category-theory]
---

# Yoneda lemma

**Summary**: Natural transformations from a representable functor to any functor $F$ correspond to elements of $F$ at the representing object.

---

> [!theorem] Yoneda lemma
> For a representable $y^S = \mathrm{Set}(S,-)$ and a functor $F : \mathrm{Set}\to\mathrm{Set}$,
> $$\mathrm{Nat}(y^S, F) \cong F(S)$$
> (source: Polynomial Functors, Lemma 1.10; form for Set)

## Intuition

A representable is determined by how it maps out; so a map out of it is just a choice of one element. This is why a lens between polynomials reduces to a map on positions plus maps on directions: see [[Dependent lens]].

## Examples

- Polynomials are sums of representables: [[Polynomial Functors ch2 - Polynomial functors]].
- Presheaves and sheaves: [[Seven Sketches ch7 - Logic of behavior]].

Wiki note: the general (any category) statement is standard; the digest only confirmed the Set form. **[unverified]** for the general form in the books.

**Sources**: Niu, Spivak, Polynomial Functors (2024), ch. 1.
**Last updated**: 2026-11-06

---

## Related pages
[[Functor]] · [[Natural transformation]] · [[Category]] · [[Polynomial functor]] · [[Universal property]]
