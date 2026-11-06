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
> $f \dashv g$ ($f$ left adjoint, $g$ right adjoint) when
> $$f(p) \le q \iff p \le g(q)$$
> for all $p\in P$, $q\in Q$. (source: Seven Sketches, Def. 1.95, p. 27)

It is the case of [[Adjunction]] where both categories are [[Preorder]]s (Ex. 3.71).

## Examples

- $3\times - : \mathbb Z\to\mathbb R$ has left adjoint $\lceil x/3\rceil$ (Ex. 1.97, p. 27).
- For a function $g : S\to T$, the image $g_!$ and preimage $g^*$ on power sets are adjoint (Exs. 1.102, 1.104, p. 29). The preimage $f^*$ has both a left adjoint (direct image $f_!$) and a right adjoint (Ex. 1.117, pp. 32-33, apples and buckets).

## Properties

- Prop. 1.107 (p. 30): equivalent characterisations of a Galois connection.
- Prop. 1.111 (p. 31): right adjoints preserve meets; left adjoints preserve joins. Right adjoints need not preserve joins (Ex. 1.113).
- Generative effects are the failure of $f$ to preserve joins (Def. 1.93): a map with a generative effect cannot be a left adjoint.

> [!theorem] Adjoint functor theorem for preorders
> If $Q$ has all meets, a monotone $g : Q\to P$ preserves meets iff it is a right adjoint; dually, a monotone map preserving all joins has a right adjoint. (source: Seven Sketches, Thm. 1.115, p. 32)

## Closure operators

> [!definition] Closure operator
> A monotone $j : P\to P$ with $p\le j(p)$ and $j(j(p))=j(p)$. (source: Seven Sketches, Def. 1.120, p. 33)

Every Galois connection gives the closure operator $g\circ f$, and conversely every closure operator arises this way (Ex. 1.122, p. 34). Computational closure operators are Ex. 1.121. Logic as closure is Ex. 1.123, and returns as modalities in [[Topos]] (Def. 7.69).

## Generalisations

V-adjoints generalise Galois connections to enriched categories (Remark 4.39): see [[Profunctor]]. Closedness of a monoidal preorder, $a\otimes v\le w\iff a\le(v\multimap w)$, is a Galois connection in each variable: see [[Quantale]].

**Covered in**: Fong-Spivak (Seven Sketches) ch. 1 (pp. 27-34, Galois connections, adjoint functor theorem, closure operators)
**Sources**: Fong, Spivak, Seven Sketches (2019), ch. 1; file `text_books/Category Theory/Spivak, Fong - Seven Sketches in Compositionality.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
[[Adjunction]] · [[Preorder]] · [[Functor]] · [[Quantale]] · [[Profunctor]] · [[Topos]]
