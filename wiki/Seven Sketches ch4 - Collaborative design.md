---
type: paper
area: dsl
source-ref: "Fong-Spivak 2019, ch. 4"
authors: ["[[Brendan Fong]]", "[[David I. Spivak]]"]
year: 2019
venue: book (Cambridge University Press)
file: "text_books/Category Theory/Spivak, Fong - Seven Sketches in Compositionality.pdf"
tags: [category-theory]
---

# Seven Sketches ch4 - Collaborative design

**Summary**: Co-design via feasibility relations: V-profunctors, the category Prof_V, companions and conjoints, collages, monoidal categories and compact closed structure.

**Authors**: Brendan Fong, David I. Spivak · **Year**: 2019 · **File**: `text_books/Category Theory/Spivak, Fong - Seven Sketches in Compositionality.pdf`

---
## Problem

Design problems have components (resources required, resources provided) wired together. The chapter models a component as a relation "x can be obtained given y" that respects the orders, then generalises the Boolean answer to a cost or other value. (source: Seven Sketches, ch. 4, pp. 117-146)

## Feasibility relations and profunctors (pp. 120-126)

> [!definition] Feasibility relation (Def 4.2, p. 120)
> For preorders $X, Y$, a monotone map $\Phi : X^{\mathrm{op}} \times Y \to \mathsf{Bool}$, written $\Phi : X \nrightarrow Y$. If $\Phi(x,y)$ is true, $x$ can be obtained given $y$. (source: Seven Sketches, p. 120)

> [!definition] V-profunctor (Def 4.8, p. 121)
> For a quantale $\mathcal{V}$ and $\mathcal{V}$-categories $X, Y$, a $\mathcal{V}$-functor $\Phi : X^{\mathrm{op}} \times Y \to \mathcal{V}$. Exercise 4.9 gives the elementwise form:
> $$ X(x',x) \otimes \Phi(x,y) \otimes Y(y,y') \le \Phi(x',y') $$
> (source: Seven Sketches, p. 121)

- Ex 4.11 (p. 122): Bool-profunctors as bridges between preorders. Ex 4.13 (p. 122): Cost-profunctors as weighted bridges. Remark 4.16 (p. 123): profunctors compose like matrices over a quantale.
- Section 4.2.2 (p. 125): the bridge picture recast for co-design, where arrows record what a component requires and provides.

## The category Prof_V (pp. 127-129)

> [!definition] Composite (Def 4.21, p. 127)
> For $\Phi : X \nrightarrow Y$, $\Psi : Y \nrightarrow Z$:
> $$ (\Phi \,\mathbin{;}\, \Psi)(p,r) = \bigvee_{q} \Phi(p,q) \otimes \Psi(q,r). $$
> (source: Seven Sketches, p. 127)

- Thm 4.23 (p. 127): for a skeletal quantale $\mathcal{V}$, $\mathsf{Prof}_{\mathcal{V}}$ is a category (objects $\mathcal{V}$-categories, morphisms profunctors). Def 4.24: $\mathsf{Feas} := \mathsf{Prof}_{\mathsf{Bool}}$.
- The identity on $X$ is the unit profunctor $U_X(x,y) = X(x,y)$ (p. 128). Lemmas 4.27, 4.31 (pp. 128-129): unit and associativity laws. Remark 4.33 (p. 129): the skeletal restriction can be dropped with more work.

## Companions, conjoints, collages (pp. 130-133)

- Def 4.34 (p. 130): for a $\mathcal{V}$-functor $F : P \to Q$, the companion $\widehat{F}(p,q) = Q(Fp, q)$ and conjoint $\check{F}(q,p) = Q(q, Fp)$. Ex 4.35 (p. 130): for the identity both equal the unit profunctor. Ex 4.37 (p. 131): the addition map on $\mathbb{R}^3$.
- Remark 4.39 (p. 131): V-adjoints, generalising Galois connections (Def 1.95).
- Def 4.42 (p. 131): the collage of a profunctor $\Phi : X \nrightarrow Y$ is a $\mathcal{V}$-category containing $X$ and $Y$ with $\Phi$ as the hom from $X$ to $Y$. Ex 4.43 (p. 132): a Cost collage.

## Monoidal categories and duals (pp. 134-146)

- Section 4.4 (pp. 134-138): from monoidal preorders to monoidal categories by categorification; coherence isomorphisms replace equalities. Remarks 4.46-4.47 (p. 137): strict versus non-strict, with a pointer to expert references. Ex 4.49 (p. 137): $(\mathsf{Set}, 1, \times)$. Remark 4.53 (p. 139): V-categories for V a monoidal category.

> [!definition] Dual (Def 4.58, p. 141)
> A dual of $c$ in a symmetric monoidal category: $c^*$ with unit $\eta_c : I \to c^* \otimes c$ and counit $\epsilon_c : c \otimes c^* \to I$ satisfying the snake equations. If every object has a dual the category is compact closed. (source: Seven Sketches, p. 141)

- Prop 4.60 (p. 142): a compact closed category is monoidal closed. Ex 4.61 (p. 142): $\mathsf{Corel}$, finite sets with partitions of the disjoint union as morphisms.
- Thm 4.63 (p. 144): for skeletal $\mathcal{V}$, $\mathsf{Prof}_{\mathcal{V}}$ is compact closed with monoidal product the product of V-categories; this licenses the cup and cap in wiring diagrams.

## Limitations

Read at statement level (all Defs/Props/Thms and example headings; Defs 4.2, 4.8, 4.21, 4.34, 4.58 and Thms 4.23, 4.63 checked in the text). The Section 4.4 page span is approximate. Proofs and exercise solutions were not read.

## Connections

- Previous: [[Seven Sketches ch3 - Databases]]. Next: [[Seven Sketches ch5 - Signal flow graphs]] (props are the monoidal categories where objects are $\mathbb{N}$).
- Concept pages: [[Profunctor]], [[Enriched category]], [[Quantale]], [[Monoidal category]].

**Sources**: Fong, Spivak, Seven Sketches in Compositionality (2019), ch. 4; page numbers are printed pages.
**Last updated**: 2026-11-06

---

## Related pages
[[Profunctor]] · [[Enriched category]] · [[Quantale]] · [[Monoidal category]] · [[Galois connection]]
