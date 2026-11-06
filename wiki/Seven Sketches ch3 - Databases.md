---
type: paper
area: dsl
source-ref: "Fong-Spivak 2019, ch. 3"
authors: ["[[Brendan Fong]]", "[[David I. Spivak]]"]
year: 2019
venue: book (Cambridge University Press)
file: "DSL/Spivak, Fong - Seven Sketches in Compositionality.pdf"
tags: [category-theory]
---

# Seven Sketches ch3 - Databases

**Summary**: Categories as database schemas: free categories, functors, instances as set-valued functors, natural transformations, data migration by adjoints, and limits.

**Authors**: Brendan Fong, David I. Spivak · **Year**: 2019 · **File**: `DSL/Spivak, Fong - Seven Sketches in Compositionality.pdf`

---
## Problem

Use categories to describe the shape of data (a schema), functors to Set for the data itself (an instance), and adjoint functors for moving data between schemas. (source: Seven Sketches, ch. 3, pp. 77-115)

## Categories (pp. 81-90)

> [!definition] Category (Def 3.6, p. 81)
> Objects, morphisms $f : A \to B$, identities and composition, with unit and associativity laws. (source: Seven Sketches, p. 81)

- Def 3.7 (p. 82): the free category $\mathrm{Free}(G)$ on a graph $G$ has paths as morphisms. Ex 3.13 (p. 83): $\mathbb{N}$ is free on one vertex with one loop. Ex 3.18 (p. 84): imposing an equation can force others. Remark 3.20 (p. 85): a schema is a finite presentation of a category. Remark 3.23 (p. 86): preorders and free categories are the two ends of a spectrum.
- Def 3.24 (p. 87): the category $\mathsf{Set}$. Ex 3.27 (p. 88): opposite category. Def 3.28 (p. 88): isomorphism; Ex 3.29: $\{a,b,c\} \cong 3$. Ex 3.34 (p. 89): nearly-inverse maps that are not isomorphisms.

## Functors, instances, natural transformations (pp. 91-101)

> [!definition] Functor (Def 3.35, p. 91)
> Maps objects to objects and morphisms to morphisms, preserving identities and composition. (source: Seven Sketches, p. 91)

- Ex 3.36, 3.38, 3.41 (pp. 91-92): functors between the walking-arrow-type categories and the free and commutative squares. Ex 3.42 (p. 92): functors between preorders are monotone maps.
- Def 3.44 (p. 93): a $C$-instance is a functor $I : C \to \mathsf{Set}$. Ex 3.46 (p. 94): instances on the one-loop schema with $s \circ s = s$ are sets with an idempotent map (citizen to president, number to 0, expression to its value).
- Def 3.49 (p. 95): a natural transformation $\alpha : F \Rightarrow G$ with components $\alpha_c$ whose naturality squares commute. Def 3.51 (p. 95): a diagram is a functor from an indexing category.
- Def 3.54 (p. 96): the functor category $D^C$. Ex 3.56 (p. 96): $\mathsf{Set}^{\mathbf{1}} \simeq \mathsf{Set}$. Remark 3.59 (p. 97): preorders and Bool-categories form equivalent categories.
- Def 3.60 (p. 97): an instance homomorphism is a natural transformation; the category of $C$-instances is $\mathsf{Set}^C$. Ex 3.63 (p. 99): graph homomorphisms.

## Adjunctions and data migration (pp. 102-107)

> [!definition] Adjunction (Def 3.70, p. 102)
> Functors $L : C \to D$, $R : D \to C$ with a bijection
> $$ D(L c, d) \cong C(c, R d) $$
> natural in $c$ and $d$. (source: Seven Sketches, p. 102)

- Def 3.68 (p. 102): for $F : C \to D$, precomposition $\Delta_F : \mathsf{Set}^D \to \mathsf{Set}^C$ (pullback of instances). Its left and right adjoints, named $\Sigma$ and $\Pi$ (p. 102), are the data migration functors. Ex 3.71 (p. 103): Galois connections are adjunctions between preorders. Ex 3.72 (p. 103): currying. Ex 3.74 (p. 104): free/forgetful pairs from algebra and topology.

## Limits (pp. 108-114)

> [!definition] Terminal object, product (Defs 3.79, 3.86; pp. 108)
> A terminal object has a unique morphism from every object. A product $X \times Y$ is an object with projections such that any pair of maps into $X$ and $Y$ factors uniquely through it. (source: Seven Sketches, p. 108)

- Prop 3.84 (p. 108): terminal objects are isomorphic; Remark 3.85: "the limit" versus "a limit". Ex 3.87 (p. 109): products in Set are Cartesian products; Ex 3.89 (p. 110): products of categories.
- Def 3.92 (p. 111): a cone over a diagram $D : J \to C$; a limit is a universal cone. Exs 3.93-3.94: terminal objects and products are limits over the empty and discrete graphs.
- Thm 3.95 (p. 112): limits in Set are computed as compatible tuples. Ex 3.99 (p. 112): pullbacks, from a cospan shape. Remark 3.100 (p. 113): this pullback is not the instance pullback of Def 3.68.
- Def 3.102 (p. 114): colimits are limits in $C^{\mathrm{op}}$ (cocone); the chapter notes this definition is compressed and defers work to ch. 6.

## Limitations

Read at statement level (all Defs/Props/Thms and example headings; Def 3.70 not opened in full). Defs 3.68 and 3.46 were checked in the text. Proofs, exercises and the FQL discussion (p. 79) were not read.

## Connections

- Previous: [[Seven Sketches ch2 - Resource theories]]. Next: [[Seven Sketches ch4 - Collaborative design]]; colimits and cospans continue in [[Seven Sketches ch6 - Electric circuits]].
- Concept pages: [[Category]], [[Functor]], [[Natural transformation]], [[Adjunction]], [[Universal property]].

**Sources**: Fong, Spivak, Seven Sketches in Compositionality (2019), ch. 3; page numbers are printed pages.
**Last updated**: 2026-11-06

---

## Related pages
[[Category]] · [[Functor]] · [[Natural transformation]] · [[Adjunction]] · [[Universal property]]
