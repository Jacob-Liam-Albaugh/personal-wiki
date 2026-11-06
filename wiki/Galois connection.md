---
type: definition
area: dsl
source-ref: "Fong-Spivak 2019, Def. 1.95"
tags: [category-theory]
---

# Galois connection

**Summary**: A pair of monotone maps $f : P \to Q$, $g : Q \to P$ between preorders with $f(p)\le q$ iff $p\le g(q)$; an adjunction between preorders.

---

> [!definition] Galois connection
> $f \dashv g$ when
> $$f(p) \le q \iff p \le g(q)$$
> (source: Seven Sketches, Def. 1.95)

## Intuition

Right adjoints preserve meets (Prop. 1.111); left adjoints preserve joins. Adjoint functor theorem for preorders: a monotone map preserving all joins has a right adjoint (Thm. 1.115). Closure operators (Def. 1.120) arise as $g\circ f$.

## Where it appears

[[Seven Sketches ch1 - Generative effects]]; generative effects are failure of $f$ to preserve joins (Def. 1.93).

**Sources**: Fong, Spivak, Seven Sketches (2019), ch. 1.
**Last updated**: 2026-11-06

---

## Related pages
[[Adjunction]] · [[Preorder]] · [[Functor]] · [[Quantale]]
