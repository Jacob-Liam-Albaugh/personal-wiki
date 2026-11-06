---
type: definition
area: dsl
source-ref: "Fong-Spivak 2019, Def. 3.70; Def. 1.95"
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

- Data migration $\Sigma \dashv \Delta \dashv \Pi$: [[Seven Sketches ch3 - Databases]].
- The adjoint quadruple between Set and Poly: [[Polynomial Functors ch5 - More categorical properties]], Thm. 5.4.
- Cofree comonoid $T_p$ is right adjoint to the forgetful functor: [[Polynomial Functors ch8 - Categorical properties of polynomial comonoids]].
- Closure of a monoidal product is an adjunction: [[Poly parallel product]].

## Where it appears

Every [[Universal property]] defines an adjoint when it holds for all inputs.

**Sources**: Fong, Spivak, Seven Sketches (2019), ch. 1, ch. 3; Niu, Spivak, Polynomial Functors (2024), ch. 5, ch. 8.
**Last updated**: 2026-11-06

---

## Related pages
[[Functor]] · [[Galois connection]] · [[Universal property]] · [[Category]] · [[Natural transformation]]
