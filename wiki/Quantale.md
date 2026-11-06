---
type: definition
area: dsl
source-ref: "Fong-Spivak 2019, Def. 2.79, Def. 2.90, Def. 2.100"
tags: [category-theory]
---

# Quantale

**Summary**: A closed symmetric monoidal preorder that has all joins; the right base for enrichment because $\mathcal V$-matrices then compose.

---

> [!definition] Closed
> A symmetric monoidal preorder $\mathcal V$ is closed if each pair $v,w$ has a hom-element $v\multimap w$ with
> $$a\otimes v\le w \iff a\le (v\multimap w).$$
> (source: Seven Sketches, Def. 2.79, p. 69)

> [!definition] Quantale
> A symmetric monoidal preorder $(\mathcal V,\le,I,\otimes)$ that is closed and has all joins (unital commutative quantale). (source: Seven Sketches, Def. 2.90, p. 71)

Closure is an instance of [[Adjunction]]: $-\otimes v$ is left adjoint to $v\multimap -$ (a [[Galois connection]]).

## Examples and properties

- Cost is closed, with $\multimap$ given by truncated subtraction (Ex. 2.83), and is a quantale (Ex. 2.91). Bool is a quantale. $(\mathbb B,\le,\mathrm{false},\vee)$ is a non-example of closedness (Ex. 2.85).
- Prop. 2.87: properties of $\multimap$. Remark 2.89: $\mathcal V$ is enriched in itself. Remark 2.95: the "navigator" reading of Cost.
- Prop. 2.96: in a preorder, all joins exist iff all meets exist. Prop. 2.98: a symmetric monoidal preorder with all joins is closed iff $\otimes$ distributes over joins.

## V-matrices

> [!definition] V-matrix
> A function $M : X\times Y\to\mathcal V$, with product
> $$(M\ast N)(x,z)=\bigvee_y M(x,y)\otimes N(y,z).$$
> (source: Seven Sketches, Def. 2.100, p. 73)

Ex. 2.102: Boolean matrix multiplication. Over Cost this computes shortest paths. Remark 2.97: Hausdorff distance generalises to any quantale. In a quantale, $\mathcal V$-categories can be presented by generators. Rigs include quantales (Exs. 5.37-5.42): [[Signal flow graph]].

## Where it appears

Basis for [[Enriched category]] and [[Profunctor]] (composition of profunctors is the $\mathcal V$-matrix product); a [[Monoidal category]] with extra structure.

**Covered in**: Fong-Spivak (Seven Sketches) ch. 2 (pp. 69-76, closed structure, quantales, V-matrices)
**Sources**: Fong, Spivak, Seven Sketches (2019), ch. 2; file `text_books/Category Theory/Spivak, Fong - Seven Sketches in Compositionality.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
[[Enriched category]] · [[Preorder]] · [[Monoidal category]] · [[Adjunction]] · [[Galois connection]] · [[Profunctor]]
