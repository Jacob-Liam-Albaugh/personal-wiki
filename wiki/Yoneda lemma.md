---
type: theorem
area: dsl
source-ref: "Niu-Spivak 2024, Lemma 1.10"
tags: [category-theory]
---

# Yoneda lemma

**Summary**: Natural transformations from a representable functor to any functor $F$ correspond to elements of $F$ at the representing object.

---

> [!definition] Representable functor (Def 1.1, p. 3)
> For a set $S$, the functor $y^S : \mathsf{Set} \to \mathsf{Set}$ sends a set $X$ to $X^S = \mathsf{Set}(S, X)$ and a function $h : X \to Y$ to post-composition with $h$. (source: Polynomial Functors, p. 3)

- Ex 1.2 (p. 4): $X \mapsto X \times X$ is representable, by $S = 2$.
- Prop 1.4 (p. 4): a function $f : R \to S$ induces a natural transformation $y^f : y^S \to y^R$, by precomposition with $f$. So $S \mapsto y^S$ is contravariant.

> [!theorem] Yoneda lemma (Lemma 1.10, p. 5)
> For a functor $F : \mathsf{Set} \to \mathsf{Set}$ and a set $S$,
> $$ F(S) \cong \mathsf{Set}^{\mathsf{Set}}(y^S, F). $$
> The isomorphism is natural; the exercises (p. 6) ask for the naturality and the two-sided inverse. (source: Polynomial Functors, p. 5)

## Intuition

A representable is determined by how it maps out; so a natural transformation out of $y^S$ is just a choice of one element of $F(S)$. This is why a lens between polynomials reduces to a map on positions plus maps on directions: see [[Dependent lens]]. Substituting $F = y^R$ gives $\mathsf{Set}(R, S) \cong \mathsf{Poly}(y^S, y^R)$, which is the contravariance of Prop 1.4.

## Examples

- Polynomials are sums of representables: [[Polynomial functor]].
- The Yoneda embedding $A \mapsto y^A$ has a left adjoint, the sections functor $\Gamma$ (Prop 5.12, p. 147): see [[Adjunction]].
- Presheaves and sheaves appear in Seven Sketches ch. 7, which is not yet folded into a topic page.

Wiki note: the general (any category) statement is standard; the digest only confirmed the Set form. **[unverified]** for the general form in the books.

## For preorders

A Yoneda lemma for preorders appears in the exercises of Seven Sketches ch. 1 (p. 20). Relatedly, monotone maps $P\to\mathbb B$ correspond to upper sets of $P$ (Seven Sketches Prop. 1.78, p. 22).

**Covered in**: Niu-Spivak, Polynomial Functors ch. 1 (pp. 3-7); Fong-Spivak (Seven Sketches) ch. 1 (pp. 20-22)
**Sources**: Niu, Spivak, Polynomial Functors (2024), ch. 1; `text_books/Category Theory/Spivak, Niu - Polynomial Functors.pdf`; `text_books/Category Theory/Spivak, Fong - Seven Sketches in Compositionality.pdf` (ch. 1).
**Last updated**: 2026-11-06

---

## Related pages
[[Functor]] · [[Natural transformation]] · [[Category]] · [[Polynomial functor]] · [[Universal property]] · [[Adjunction]]
- [[Preorder]]
