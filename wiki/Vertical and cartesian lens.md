---
type: definition
area: dsl
source-ref: "Niu-Spivak 2024, Defs 5.51, 5.58; Props 5.18, 5.21, 5.27, 5.52"
tags: [category-theory]
---

# Vertical and cartesian lens

**Summary**: Two dual classes of [[Dependent lens]]es, those bijective on positions and those bijective on directions. They form a factorization system on Poly, are preserved by the monoidal products, and give the base-change adjunctions.

---

> [!definition] Vertical and cartesian (Def 5.51, p. 158)
> A lens $f : p \to q$ is vertical if $f_1 : p(1) \to q(1)$ is an isomorphism. It is cartesian if each $f^\sharp_i : q[f_1 i] \to p[i]$ is an isomorphism. (source: Polynomial Functors, p. 158)

> [!theorem] Factorization system (Prop 5.52, p. 158)
> Vertical and cartesian lenses form a factorization system on Poly: every lens factors as a vertical lens followed by a cartesian one. Vertical lenses satisfy 2-out-of-3 (Prop 5.53, p. 159). (source: Polynomial Functors, pp. 158-159)

- Def 5.58 (p. 160): a cartesian natural transformation is one whose naturality squares are all pullbacks. Prop 5.59 (p. 161): a lens is cartesian in the sense of Def 5.51 iff it is cartesian as a natural transformation, among other equivalent forms.
- Prop 5.63 (p. 162): [[Poly coproduct]] $+$, [[Poly product]] $\times$ and [[Poly parallel product]] $\otimes$ preserve vertical and cartesian morphisms. Prop 5.64 (p. 162): pullbacks preserve them. Prop 6.88 (p. 215): the [[Poly composition product]] preserves cartesian lenses.
- Retrofunctor versions: every retrofunctor factors as a vertical one followed by a cartesian one (Prop 8.64, p. 323). Cartesian retrofunctors are discrete opfibrations (Prop 8.66, p. 323); vertical ones are opposite to bijective-on-objects functors (Prop 8.67, p. 324). See [[Retrofunctor]].

## Monos, epis and epi-mono factorization

> [!theorem] Monos and epis of lenses (Props 5.18, 5.21; pp. 148-149)
> A lens $f$ is a mono iff $f_1$ is a mono in Set and each $f^\sharp_i$ is surjective. It is an epi iff $f_1$ is an epi and, for each $j \in q(1)$, the induced map $f^\flat_j : q[j] \to \prod_{i : f_1 i = j} p[i]$ is a mono in Set. (source: Polynomial Functors, pp. 148-149)

- Ex 5.19 (p. 149): $k y^k \to \mathbb{N} y^{\mathbb{N}}$, a clock, is a mono.
- Def 5.25 (p. 150): a factorization system $(E, M)$ in a category. Ex 5.26 (p. 151): epi-mono factorization in Set. Prop 5.27 (p. 151): Poly has epi-mono factorization.

## Slices, exponentiability and base change

- Defs 5.66, 5.67 (p. 163): slice category and exponentiable morphism. Thm 5.68 (p. 163): cartesian lenses are exponentiable. Ex 5.70 (p. 164): $2y^2 \to y^2 + y^0$.
- Prop 5.72 (p. 165): a function $f : A \to B$ induces, by pullback, $f^* : B.\mathsf{Poly} \to A.\mathsf{Poly}$.

> [!theorem] Base change (Thm 5.73, p. 165)
> $f^*$ has a left adjoint $f_!$ and a right adjoint $f_*$:
> $$ f_! p = \sum_{b} y^{\prod_{a \mapsto b} p[a]}, \qquad f_* p = \sum_{b} y^{\sum_{a \mapsto b} p[a]}. $$
> $\otimes$ preserves the op-cartesian arrows, so this is a monoidal bifibration. (source: Polynomial Functors, p. 165)

See [[Adjunction]].

**Covered in**: Niu-Spivak, Polynomial Functors ch. 5 (pp. 148-165); ch. 6 (p. 215); ch. 8 (pp. 323-324)
**Sources**: `text_books/Category Theory/Spivak, Niu - Polynomial Functors.pdf`; page numbers are printed pages. Proofs and exercises were not read.
**Last updated**: 2026-11-06

---

## Related pages
[[Dependent lens]] · [[Polynomial functor]] · [[Adjunction]] · [[Retrofunctor]] · [[Poly parallel product]] · [[Poly composition product]]
