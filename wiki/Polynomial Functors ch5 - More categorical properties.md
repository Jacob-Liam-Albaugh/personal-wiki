---
type: paper
area: dsl
source-ref: "Niu-Spivak 2024, ch. 5"
authors: ["[[Nelson Niu]]", "[[David I. Spivak]]"]
year: 2024
venue: book draft
file: "text_books/Category Theory/Spivak, Niu - Polynomial Functors.pdf"
tags: [category-theory]
---

# Polynomial Functors ch5 - More categorical properties

**Summary**: Adjunctions between Set and Poly, monos and epis of lenses, epi-mono and vertical-cartesian factorizations, cartesian closure, limits and colimits, cartesian lenses and base change.

**Authors**: Nelson Niu, David I. Spivak · **Year**: 2024 · **File**: `text_books/Category Theory/Spivak, Niu - Polynomial Functors.pdf`

---
## Problem

Collect the structural facts about Poly: how it relates to Set, what monos and epis are, how it factors lenses, and which limits and colimits exist and how to compute them. (source: Polynomial Functors, ch. 5, pp. 145-173)

## Adjunctions with Set (pp. 146-148)

- Props 5.2, 5.3 (p. 146): $A \mapsto Ay^0 = A$ and $A \mapsto Ay$ are fully faithful functors $\mathsf{Set} \to \mathsf{Poly}$.

> [!theorem] Adjoint quadruple (Thm 5.4, p. 146)
> Poly has an adjoint quadruple with Set, formed by the functors $A \mapsto A$, $p \mapsto p(1)$, $A \mapsto Ay$ and $p \mapsto p(0)$ (picture (5.5)). (source: Polynomial Functors, p. 146)

- Prop 5.8 (p. 147): a two-variable adjunction
  $$ \mathsf{Poly}(Ap, q) \cong \mathsf{Set}(A, \mathsf{Poly}(p, q)) \cong \mathsf{Poly}(p, q^A). $$
  Cor 5.10 (p. 147): for a set $B$, $A \mapsto Ay^B$ is left adjoint to $q \mapsto q(B)$.
- Prop 5.12 (p. 147): the Yoneda embedding $A \mapsto y^A$ has left adjoint $\Gamma : \mathsf{Poly} \to \mathsf{Set}^{\mathrm{op}}$, $\Gamma(p) = \mathsf{Poly}(p, y) \cong \prod_i p[i]$. Cor 5.15 (p. 148): the principal monomial $p \mapsto p(1)\, y^{\Gamma(p)}$ is the adjunction $\mathsf{Poly} \rightleftarrows \mathsf{Set} \times \mathsf{Set}^{\mathrm{op}}$.

## Monos, epis and factorization (pp. 148-153)

- Prop 5.18 (p. 148): a lens is a mono iff $f_1$ is a mono in Set and each $f^\sharp_i$ is an epi (surjective) in Set. Ex 5.19 (p. 149): $k y^k \to \mathbb{N}y^{\mathbb{N}}$, a clock as a mono. Prop 5.21 (p. 149): a lens is an epi iff $f_1$ is an epi and, for each $j \in q(1)$, the induced map $f^\flat_j : q[j] \to \prod_{i : f_1 i = j} p[i]$ is a mono in Set.
- Def 5.25 (p. 150): a factorization system $(E, M)$ in a category. Ex 5.26 (p. 151): epi-mono factorization in Set. Prop 5.27 (p. 151): Poly has epi-mono factorization.
- Ex 5.29 (p. 152): $y^A \cong y^A y^0$ consistency check for the notation $A = Ay^0$.

> [!theorem] Cartesian closed (Thm 5.31, p. 152)
> Poly is cartesian closed: $\mathsf{Poly}(p, r^q) \cong \mathsf{Poly}(p \times q, r)$, where $r^q = \prod_{j \in q(1)} r \circ (y + q[j])$ (eq. 5.28). (source: Polynomial Functors, p. 152)

## Limits and colimits (pp. 153-157)

- Thm 5.33 (p. 153): Poly has all small limits (products from Prop 3.56 plus equalizers). Ex 5.35 (p. 154): positions of a limit are the limit of the positions; the direction-set at a position is the colimit of the corresponding direction-sets. Ex 5.38 (p. 154): pullbacks in Poly.
- Thm 5.43 (p. 156): Poly has all small colimits (coproducts plus coequalizers). Ex 5.45 (p. 156): general colimits in Poly can differ from colimits in $\mathsf{Set}^{\mathsf{Set}}$, since every functor is a colimit of representables but a colimit in Poly must be polynomial; limits and coproducts agree.
- Prop 5.49 (p. 157): for $p, q$ the square with $p(1)y \otimes q(1)y$, $p(1)y \otimes q$, $p \otimes q(1)y$ and $p \otimes q$ is a pushout. Cor 5.50 (p. 158): the $n$-fold version as a wide pushout. So a lens out of $p \otimes q$ is a pair of lenses agreeing on the shared part.

## Vertical and cartesian lenses (pp. 158-165)

> [!definition] Vertical and cartesian (Def 5.51, p. 158)
> A lens $f$ is vertical if $f_1$ is an isomorphism. It is cartesian if each $f^\sharp_i$ is an isomorphism. (source: Polynomial Functors, p. 158)

- Prop 5.52 (p. 158): vertical and cartesian lenses form a factorization system. Prop 5.53 (p. 159): vertical lenses satisfy 2-out-of-3.
- Def 5.58 (p. 160): a cartesian natural transformation has all naturality squares pullbacks. Prop 5.59 (p. 161): a lens is cartesian in the sense of Def 5.51 iff it is cartesian as a natural transformation, among other equivalent forms.
- Prop 5.63 (p. 162): $+$, $\times$ and $\otimes$ preserve vertical and cartesian morphisms. Prop 5.64 (p. 162): pullbacks preserve vertical and cartesian lenses.
- Defs 5.66, 5.67 (p. 163): slice category and exponentiable morphism. Thm 5.68 (p. 163): cartesian lenses are exponentiable. Ex 5.70 (p. 164): $2y^2 \to y^2 + y^0$.
- Prop 5.72 (p. 165): for a function $f : A \to B$, pullback gives $f^* : B.\mathsf{Poly} \to A.\mathsf{Poly}$. Thm 5.73 (p. 165): $f^*$ has a left adjoint $f_!$ and a right adjoint $f_*$, with $f_! p = \sum_{b} y^{\prod_{a \mapsto b} p[a]}$ and $f_* p = \sum_{b} y^{\sum_{a \mapsto b} p[a]}$; $\otimes$ preserves the op-cartesian arrows, so this is a monoidal bifibration.

## Limitations

Read at statement level: every Def, Prop, Thm and Example heading of the chapter. Props 5.2, 5.3, 5.8, 5.12, 5.18, 5.21, 5.27, 5.31, 5.33, 5.43, 5.49, 5.52, 5.53 and Defs 5.25, 5.51, 5.58, Ex 5.35, 5.45 and Thm 5.73 were opened. Proofs and exercises were not read.

## Connections

- Previous: [[Polynomial Functors ch4 - Dynamical systems as dependent lenses]]. Next: [[Polynomial Functors ch6 - The composition product]].
- Concept pages: [[Adjunction]], [[Universal property]]; the wiki's [[Poly product]], [[Poly coproduct]] and [[Poly parallel product]] cover Props 3.56, 3.3 and 5.49.

**Sources**: Niu, Spivak, Polynomial Functors (2024), ch. 5; page numbers are printed pages.
**Last updated**: 2026-11-06

---

## Related pages
[[Adjunction]] · [[Universal property]] · [[Poly product]] · [[Poly coproduct]] · [[Poly parallel product]]
