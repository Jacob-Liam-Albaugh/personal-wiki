---
type: definition
area: dsl
source-ref: "Fong-Spivak 2019, Defs. 4.2, 4.8, 4.21, 4.34, 4.42, Thms. 4.23, 4.63"
tags: [category-theory]
---

# Profunctor

**Summary**: A relation-like bridge between categories: a $\mathcal V$-profunctor $X \nrightarrow Y$ is a $\mathcal V$-valued matrix compatible with the order on $X$ and $Y$; feasibility relations are Bool-profunctors.

---

Design problems have components with resources required and provided, wired together. A component is modelled as a relation "$x$ can be obtained given $y$" that respects the orders, with the Boolean answer later generalised to a cost or other value.

> [!definition] Feasibility relation
> For preorders $X,Y$, a monotone map $\Phi : X^{\mathrm{op}}\times Y\to\mathsf{Bool}$, written $\Phi:X\nrightarrow Y$. If $\Phi(x,y)$ is true, $x$ can be obtained given $y$. (source: Seven Sketches, Def. 4.2, p. 120)

> [!definition] V-profunctor
> For a [[Quantale]] $\mathcal V$ and $\mathcal V$-categories $X,Y$, a $\mathcal V$-functor $\Phi : X^{op}\times Y\to\mathcal V$, equivalently
> $$X(x',x)\otimes\Phi(x,y)\otimes Y(y,y')\le\Phi(x',y').$$
> (source: Seven Sketches, Def. 4.8 and Exercise 4.9, p. 121)

Ex. 4.11: Bool-profunctors as bridges between preorders. Ex. 4.13: Cost-profunctors as weighted bridges. Remark 4.16: profunctors compose like matrices over a quantale. Section 4.2.2 recasts the bridge picture for co-design, where arrows record what a component requires and provides. See [[Enriched category]], [[Preorder]].

## The category Prof_V

> [!definition] Composite
> For $\Phi:X\nrightarrow Y$, $\Psi:Y\nrightarrow Z$:
> $$(\Phi\mathbin{;}\Psi)(p,r)=\bigvee_q\Phi(p,q)\otimes\Psi(q,r).$$
> (source: Seven Sketches, Def. 4.21, p. 127)

- For skeletal $\mathcal V$, $\mathrm{Prof}_{\mathcal V}$ is a category: objects $\mathcal V$-categories, morphisms profunctors (Thm. 4.23). $\mathrm{Feas}:=\mathrm{Prof}_{\mathsf{Bool}}$ (Def. 4.24).
- The identity on $X$ is the unit profunctor $U_X(x,y)=X(x,y)$; unit and associativity laws are Lemmas 4.27, 4.31. The skeletal restriction can be dropped with more work (Remark 4.33).
- $\mathrm{Prof}_{\mathcal V}$ is compact closed for skeletal $\mathcal V$, with monoidal product the product of $\mathcal V$-categories (Thm. 4.63, p. 144). This licenses the cup and cap in co-design wiring diagrams: [[Monoidal category]].

## Companions, conjoints, collages

- For a $\mathcal V$-functor $F:P\to Q$, the companion $\widehat F(p,q)=Q(Fp,q)$ and conjoint $\check F(q,p)=Q(q,Fp)$ (Def. 4.34, p. 130). For the identity both equal the unit profunctor (Ex. 4.35); Ex. 4.37: the addition map on $\mathbb R^3$. See [[Functor]].
- $\mathcal V$-adjoints generalise Galois connections (Remark 4.39): [[Galois connection]].
- The collage of $\Phi:X\nrightarrow Y$ is a $\mathcal V$-category containing $X$ and $Y$ with $\Phi$ as the hom from $X$ to $Y$ (Def. 4.42; Cost collage Ex. 4.43).

## Polynomial setting

Bicomodules are prafunctors (Thm. 8.100), which generalize profunctors: [[Polynomial comonoid]].

**Covered in**: Fong-Spivak (Seven Sketches) ch. 4 (pp. 117-133 and 144, feasibility relations, V-profunctors, Prof_V, companions, conjoints, collages); Niu-Spivak ch. 8
**Sources**: Fong, Spivak, Seven Sketches (2019), ch. 4; Niu, Spivak (2024), ch. 8; file `text_books/Category Theory/Spivak, Fong - Seven Sketches in Compositionality.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
[[Enriched category]] · [[Quantale]] · [[Monoidal category]] · [[Preorder]] · [[Galois connection]] · [[Functor]] · [[Polynomial comonoid]]
