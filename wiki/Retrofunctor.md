---
type: definition
area: dsl
source-ref: "Niu-Spivak 2024, Defs 7.49, 7.55; Ex 7.71; Props 7.79, 7.80"
tags: [category-theory]
---

# Retrofunctor

**Summary**: A morphism of small categories that maps objects forwards and morphisms backwards. Equivalently a morphism of [[Polynomial comonoid]]s; small categories and retrofunctors form $\mathsf{Cat}^\sharp = \mathrm{Comon}(\mathsf{Poly})$. Also called a cofunctor.

---

> [!definition] Comonoid morphism (Def 7.49, p. 255)
> A morphism of polynomial comonoids is a lens commuting with the erasers and duplicators. (source: Polynomial Functors, p. 255)

> [!definition] Retrofunctor (Def 7.55, p. 256)
> For small categories $C, C'$, a retrofunctor $F : C \nrightarrow C'$ is a function $F : \mathrm{Ob}\, C \to \mathrm{Ob}\, C'$ together with, for each object $c$, a backward function $F^\sharp_c : C'[Fc] \to C[c]$ on morphisms out of the object. Three laws hold: identities are preserved ($F^\sharp_c(\mathrm{id}_{Fc}) = \mathrm{id}_c$), codomains are preserved ($F(\mathrm{cod}\, F^\sharp_c g) = \mathrm{cod}\, g$), and composites are preserved (eq. 7.58). (source: Polynomial Functors, p. 256)

Retrofunctors are exactly the comonoid morphisms of Def 7.49, so $\mathsf{Cat}^\sharp$ is the category of polynomial comonoids.

## Facts and examples

- Prop 7.61 (p. 258): if $g : Fc \to \_$ is an isomorphism in $D$, then $F^\sharp_c g$ is an isomorphism in $C$.
- Ex 7.63 (p. 259): retrofunctors to discrete categories. Ex 7.65 (p. 260): to the walking arrow. Ex 7.68 (p. 260): to the walking commutative square.
- Ex 7.71 (p. 262): retrofunctors $C \nrightarrow y^{\mathbb{N}}$ are arrow fields, called admissible sections in earlier literature. Cor 8.58 (p. 320): $\mathsf{Cat}^\sharp(C, y^{\mathbb{N}})$ is a monoid (Prop 8.57: $y^{\mathbb{N}}$ is a $\times$-monoid in $\mathsf{Cat}^\sharp$).
- Ex 7.77 (p. 263): groups $G$ and $y^G$. Prop 7.79 (p. 264): a fully faithful functor $\mathsf{Mon}^{\mathrm{op}} \to \mathsf{Cat}^\sharp$ onto categories with representable carriers. Prop 7.80 (p. 264): $\mathsf{Cat}^\sharp(C, Ay) \cong \mathsf{Set}(\mathrm{Ob}\, C, A)$.
- Thm 8.59 (p. 321): the arrow-fields functor $\mathsf{Cat}^\sharp \to \mathsf{Mon}^{\mathrm{op}}$ is right adjoint to the inclusion of Prop 7.79. Props 8.60, 8.61 (pp. 321-322): a commutative square of left adjoints; $y^{-}$ identifies representable-carrier categories with $\mathsf{Mon}^{\mathrm{op}}$. Prop 8.63 (p. 322): the inclusion of linear comonoids (discrete categories) has a left adjoint.
- Ex 7.82 (p. 265): systems of ODEs. Ex 7.84 (p. 266): retrofunctors from state categories to $C$ are $C$-coalgebras. Ex 7.85 (p. 266): retrofunctors between state categories are very well-behaved lenses. Exs 7.88, 7.90 (pp. 268-269): objects are not representable in $\mathsf{Cat}^\sharp$.
- Factorization: every retrofunctor is a vertical one followed by a cartesian one (Prop 8.64, p. 323); see [[Vertical and cartesian lens]].

## Limits, colimits, monoidal structure

- Prop 8.71 (Porst, p. 325): the forgetful functor $U : \mathsf{Cat}^\sharp \to \mathsf{Poly}$ is comonadic. Cor 8.72 (p. 325): $\mathsf{Cat}^\sharp$ has all small colimits, created by $U$; Ex 8.73: coproducts are the usual disjoint union. Cor 8.76 (p. 326): it has all small limits, via [[Cofree comonoid on a polynomial]] and Thm 5.33 ([[Poly product]]).
- Prop 8.77 (p. 326): $(y, \otimes)$ extends to $\mathsf{Cat}^\sharp$, with $U$ strong monoidal; the parallel product of two categories is their product in Cat ([[Poly parallel product]]).

## Open questions

Combinatorial description of limits in $\mathsf{Cat}^\sharp$, and whether $U$ (faithful, so it reflects monos) detects all monos: see the open questions on [[Polynomial comonoid]].

**Covered in**: Niu-Spivak, Polynomial Functors ch. 7 (pp. 254-270); ch. 8 (pp. 320-327)
**Sources**: `text_books/Category Theory/Spivak, Niu - Polynomial Functors.pdf`; page numbers are printed pages.
**Last updated**: 2026-11-06

---

## Related pages
[[Polynomial comonoid]] · [[Cofree comonoid on a polynomial]] · [[Vertical and cartesian lens]] · [[Category]] · [[Functor]] · [[Poly parallel product]]
