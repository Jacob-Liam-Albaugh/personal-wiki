---
type: definition
area: dsl
source-ref: "Fong-Spivak 2019, Def. 3.49"
tags: [category-theory]
---

# Natural transformation

**Summary**: A family of morphisms $\alpha_c : F(c) \to G(c)$ between two parallel functors that commutes with every morphism of the source category.

---

> [!definition] Natural transformation
> For $F, G : C \to D$, a natural transformation $\alpha : F \Rightarrow G$ assigns $\alpha_c : F(c)\to G(c)$ so that
> $$\alpha_{c'} \circ F(f) = G(f)\circ \alpha_c$$
> for every $f : c \to c'$. (source: Seven Sketches, Def. 3.49)

## Intuition

Instance homomorphisms are natural transformations (Def. 3.60). Functors $C\to D$ and natural transformations form the functor category (Def. 3.54).

## Examples

- The maps of Poly are natural transformations between polynomials, which unpack to [[Dependent lens|dependent lenses]]: [[Polynomial Functors ch3 - The category of polynomial functors]].
- The [[Yoneda lemma]] counts natural transformations out of a representable.

## Where it appears

Adjunctions have a unit and counit that are natural transformations: [[Adjunction]].

**Sources**: Fong, Spivak, Seven Sketches (2019), ch. 3.
**Last updated**: 2026-11-06

---

## Related pages
[[Functor]] · [[Category]] · [[Adjunction]] · [[Yoneda lemma]] · [[Dependent lens]] · [[Polynomial functor]]
