---
type: definition
area: dsl
source-ref: "Fong-Spivak 2019, Def. 3.49, Def. 3.54, Def. 3.60"
tags: [category-theory]
---

# Natural transformation

**Summary**: A family of morphisms $\alpha_c : F(c) \to G(c)$ between two parallel functors that commutes with every morphism of the source category.

---

> [!definition] Natural transformation
> For $F, G : C \to D$, a natural transformation $\alpha : F \Rightarrow G$ assigns $\alpha_c : F(c)\to G(c)$ so that
> $$\alpha_{c'} \circ F(f) = G(f)\circ \alpha_c$$
> for every $f : c \to c'$. (source: Seven Sketches, Def. 3.49, p. 95)

## Functor categories and instance homomorphisms

- Functors $C\to D$ and natural transformations form the functor category $D^C$ (Def. 3.54, p. 96). Ex. 3.56: $\mathsf{Set}^{\mathbf 1}\simeq\mathsf{Set}$. Remark 3.59: preorders and Bool-categories form equivalent categories.
- An instance homomorphism is a natural transformation between instances; the category of $C$-instances is $\mathsf{Set}^C$ (Def. 3.60, p. 97). Ex. 3.63: graph homomorphisms. See [[Functor]] for instances.

## Examples

- The maps of Poly are natural transformations between polynomials, which unpack to [[Dependent lens|dependent lenses]]: [[Polynomial functor]].
- The [[Yoneda lemma]] counts natural transformations out of a representable.
- In a sheaf topos, morphisms of sheaves are natural transformations of presheaves; a modality is a sheaf morphism $j:\Omega\to\Omega$: [[Topos]].

## Where it appears

Adjunctions have a unit and counit that are natural transformations: [[Adjunction]]. Naturality of $\mathrm{Set}$-valued diagrams over a [[Category]] is how data migration functors are compared.

**Covered in**: Fong-Spivak (Seven Sketches) ch. 3 (pp. 95-101, natural transformations, functor categories, instance homomorphisms)
**Sources**: Fong, Spivak, Seven Sketches (2019), ch. 3; file `text_books/Category Theory/Spivak, Fong - Seven Sketches in Compositionality.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
[[Functor]] · [[Category]] · [[Adjunction]] · [[Yoneda lemma]] · [[Dependent lens]] · [[Polynomial functor]] · [[Topos]]
