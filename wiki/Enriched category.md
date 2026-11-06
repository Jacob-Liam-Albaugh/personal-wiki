---
type: definition
area: dsl
source-ref: "Fong-Spivak 2019, Def. 2.46, Thm. 2.49, Def. 2.53, Def. 2.69"
tags: [category-theory]
---

# Enriched category

**Summary**: A category whose hom "sets" are objects of a monoidal preorder $\mathcal V$; Bool gives preorders, Cost gives Lawvere metric spaces.

---

> [!definition] V-category
> For a symmetric monoidal preorder $\mathcal V$: a set of objects and a hom-object $X(x,y)\in\mathcal V$ for each pair, such that
> $$I\le X(x,x),\qquad X(x,y)\otimes X(y,z)\le X(x,z).$$
> (source: Seven Sketches, Def. 2.46, p. 57)

> [!theorem] Preorders are Bool-categories
> Preorders correspond one-to-one with $\mathsf{Bool}$-categories. (source: Seven Sketches, Thm. 2.49, p. 58)

See [[Preorder]] and [[Monoidal category]] for the base.

## Metric spaces

- A metric space (Def. 2.51, p. 59). A Lawvere metric space is a Cost-category (Def. 2.53, p. 61): the triangle inequality and $d(x,x)=0$ are the two axioms, and distance need not be symmetric. $\mathbb R$ is an example (Ex. 2.54).
- Ex. 2.65: a monoidal monotone $[0,\infty]\to\{\text{true},\text{false}\}$ turns distances into a preorder.

## V-functors and products

- A V-functor $F : X\to Y$ satisfies $X(x,x')\le Y(Fx,Fx')$ (Def. 2.69, p. 65). Bool-functors are monotone maps; Cost-functors are non-expanding maps (Exs. 2.70-2.72). Remark 2.71: preorders and Bool-categories are equivalent categories (also Remark 3.59). See [[Functor]].
- The V-product $X\times Y$ has hom $X(x,x')\otimes Y(y,y')$ (Def. 2.74, p. 67). Ex. 2.76: product of weighted graphs.

## Matrices and profunctors

When $\mathcal V$ is closed with all joins it is a [[Quantale]]; then $\mathcal V$-matrices compose (Def. 2.100), computing shortest paths for Cost. $\mathcal V$-profunctors between $\mathcal V$-categories are the next step: [[Profunctor]]. Resource theories (monoidal preorders) are the source of the base $\mathcal V$.

**Covered in**: Fong-Spivak (Seven Sketches) ch. 2 (pp. 57-68, enrichment, Lawvere metric spaces, V-functors, V-products)
**Sources**: Fong, Spivak, Seven Sketches (2019), ch. 2; file `text_books/Category Theory/Spivak, Fong - Seven Sketches in Compositionality.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
[[Preorder]] · [[Monoidal category]] · [[Quantale]] · [[Profunctor]] · [[Category]] · [[Functor]]
