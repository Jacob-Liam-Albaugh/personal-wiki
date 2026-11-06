---
type: definition
area: dsl
source-ref: "Fong-Spivak 2019, Def. 2.2; Niu-Spivak 2024, ch. 3 and 6"
tags: [category-theory]
---

# Monoidal category

**Summary**: A category with a tensor product of objects and a unit object, associative and unital up to coherent isomorphism; symmetric if the tensor commutes.

---

> [!definition] Monoidal category
> A category $C$ with $\otimes : C\times C \to C$ and a unit $I$ satisfying associativity and unit laws. Fong-Spivak state the preorder case first: a symmetric monoidal preorder (Def. 2.2). (source: Seven Sketches, Def. 2.2)

## Intuition

Objects are resources or systems; $\otimes$ means "side by side". A prop is a symmetric strict monoidal category on $\mathbb N$ (Def. 5.2). Monoid and comonoid objects live in any monoidal category (Def. 5.65).

## Examples

- Poly has four: $(+,0)$, $(\times,1)$, $(\otimes,y)$, $(\circ,y)$: [[Poly (Spivak 2020)]], [[Poly parallel product]], [[Poly composition product]].
- Comonoids for $(\circ,y)$ are categories: [[Polynomial comonoid]].
- Resource theories: [[Seven Sketches ch2 - Resource theories]].
- Compact closed categories: [[Seven Sketches ch4 - Collaborative design]].

## Where it appears

Enrichment needs a monoidal base: [[Enriched category]]. Wiring diagrams: [[Operad]].

**Sources**: Fong, Spivak, Seven Sketches (2019), ch. 2, 5; Spivak (2020).
**Last updated**: 2026-11-06

---

## Related pages
[[Category]] · [[Enriched category]] · [[Operad]] · [[Poly parallel product]] · [[Poly composition product]] · [[Polynomial comonoid]]
