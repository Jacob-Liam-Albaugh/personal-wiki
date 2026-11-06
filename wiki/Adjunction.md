---
type: definition
area: dsl
source-ref: "Fong-Spivak 2019, Def. 3.70; Def. 1.95; Niu-Spivak 2024, Thm 5.4"
tags: [category-theory]
---

# Adjunction

**Summary**: A pair of functors $L \dashv R$ in opposite directions with a natural bijection between maps $L(a) \to b$ and maps $a \to R(b)$.

---

> [!definition] Adjunction
> $L : C \to D$ is left adjoint to $R : D \to C$ if
> $$D(L(c), d) \cong C(c, R(d))$$
> naturally in $c$ and $d$. (source: Seven Sketches, Def. 3.70)

## Intuition

For preorders this is a [[Galois connection]] (Def. 1.95): $L(a)\le b$ iff $a\le R(b)$. Right adjoints preserve meets/limits, left adjoints preserve joins/colimits (Prop. 1.111).

## Examples

- Data migration $\Sigma \dashv \Delta \dashv \Pi$: [[Functor]].
- Closure of a monoidal product is an adjunction $\mathsf{Poly}(p \otimes q, r) \cong \mathsf{Poly}(p, [q, r])$ (Prop 4.85, p. 126): [[Poly parallel product]]. Cartesian closure of Poly (Thm 5.31): [[Poly product]].

### Adjunctions between Set and Poly

- Props 5.2, 5.3 (p. 146): $A \mapsto Ay^0 = A$ and $A \mapsto Ay$ are fully faithful functors $\mathsf{Set} \to \mathsf{Poly}$.

> [!theorem] Adjoint quadruple (Thm 5.4, p. 146)
> Poly has an adjoint quadruple with Set, formed by the functors $A \mapsto A$, $p \mapsto p(1)$, $A \mapsto Ay$ and $p \mapsto p(0)$ (picture (5.5)). (source: Polynomial Functors, p. 146)

- Prop 5.8 (p. 147): a two-variable adjunction
  $$ \mathsf{Poly}(Ap, q) \cong \mathsf{Set}(A, \mathsf{Poly}(p, q)) \cong \mathsf{Poly}(p, q^A). $$
  Cor 5.10 (p. 147): for a set $B$, $A \mapsto Ay^B$ is left adjoint to $q \mapsto q(B)$.
- Prop 5.12 (p. 147): the Yoneda embedding $A \mapsto y^A$ ([[Yoneda lemma]]) has left adjoint $\Gamma : \mathsf{Poly} \to \mathsf{Set}^{\mathrm{op}}$, $\Gamma(p) = \mathsf{Poly}(p, y) \cong \prod_i p[i]$. Cor 5.15 (p. 148): the principal monomial $p \mapsto p(1)\, y^{\Gamma(p)}$ is the adjunction $\mathsf{Poly} \rightleftarrows \mathsf{Set} \times \mathsf{Set}^{\mathrm{op}}$. See [[Dependent lens]] for sections.

### Adjunctions on polynomial comonoids

- Cofree comonoid: the forgetful functor $\mathsf{Cat}^\sharp \to \mathsf{Poly}$ has right adjoint $\mathbb{T}_-$ (Thm 8.45): [[Cofree comonoid on a polynomial]]. The forgetful functor is comonadic (Prop 8.71, Porst): [[Retrofunctor]].
- The arrow-fields functor $\mathsf{Cat}^\sharp \to \mathsf{Mon}^{\mathrm{op}}$ is right adjoint to the inclusion of representable-carrier comonoids (Thm 8.59, p. 321); the inclusion of discrete categories has a left adjoint (Prop 8.63): [[Retrofunctor]].
- Base change $f_! \dashv f^* \dashv f_*$ on slices of Poly (Thm 5.73): [[Vertical and cartesian lens]].
- Left $C$-comodules are functors $C \to \mathsf{Poly}$ and bicomodules are parametric right adjoints (Props 8.88, 8.104): [[Polynomial comonoid]].

## Adjunctions in Seven Sketches

> [!definition] Adjunction
> Functors $L : C \to D$, $R : D \to C$ with a bijection
> $$D(L c, d) \cong C(c, R d)$$
> natural in $c$ and $d$. (source: Seven Sketches, Def. 3.70, p. 102)

Data migration: for $F : C \to D$, precomposition $\Delta_F : \mathsf{Set}^D \to \mathsf{Set}^C$ (pullback of instances, Def. 3.68, p. 102) has a left adjoint $\Sigma_F$ and a right adjoint $\Pi_F$; these are the data migration functors between database schemas. Galois connections are adjunctions between preorders (Ex. 3.71, see [[Galois connection]]). Currying is an adjunction (Ex. 3.72). Free/forgetful pairs from algebra and topology are adjunctions (Ex. 3.74). For preorders, V-adjoints (Remark 4.39) generalise to enriched categories ([[Profunctor]]).

## Where it appears

Every [[Universal property]] defines an adjoint when it holds for all inputs.

**Covered in**: Niu-Spivak, Polynomial Functors ch. 5 (pp. 146-148, 165); ch. 8 (pp. 315, 321-325); Fong-Spivak (Seven Sketches) ch. 3 (pp. 102-107); ch. 1 (pp. 27-34, Galois connections)
**Sources**: Fong, Spivak, Seven Sketches (2019), ch. 1, ch. 3; Niu, Spivak, Polynomial Functors (2024), ch. 5, ch. 8; `text_books/Category Theory/Spivak, Niu - Polynomial Functors.pdf`; `text_books/Category Theory/Spivak, Fong - Seven Sketches in Compositionality.pdf` (ch. 1, 3).
**Last updated**: 2026-11-06

---

## Related pages
[[Functor]] · [[Galois connection]] · [[Universal property]] · [[Category]] · [[Natural transformation]] · [[Yoneda lemma]] · [[Cofree comonoid on a polynomial]] · [[Vertical and cartesian lens]]
- [[Profunctor]]
