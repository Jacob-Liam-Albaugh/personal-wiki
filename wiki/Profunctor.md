---
type: definition
area: dsl
source-ref: "Fong-Spivak 2019, Def. 4.8"
tags: [category-theory]
---

# Profunctor

**Summary**: A relation-like bridge between categories: a $\mathcal V$-profunctor $X \nrightarrow Y$ is a $\mathcal V$-valued matrix compatible with the order on $X$ and $Y$; feasibility relations are Bool-profunctors.

---

> [!definition] V-profunctor
> A function $\Phi : X^{op}\times Y \to \mathcal V$ monotone in the enriched sense. They compose (Def. 4.21) into a category $\mathrm{Prof}_{\mathcal V}$ (Thm. 4.23). (source: Seven Sketches, Defs. 4.8, 4.21, Thm. 4.23)

## Intuition

Companions and conjoints (Def. 4.34) turn functors into profunctors; the collage (Def. 4.42) glues two categories along a profunctor. In the polynomial setting, bicomodules are prafunctors (Thm. 8.100), which generalize profunctors: [[Polynomial Functors ch8 - Categorical properties of polynomial comonoids]].

**Sources**: Fong, Spivak, Seven Sketches (2019), ch. 4; Niu, Spivak (2024), ch. 8.
**Last updated**: 2026-11-06

---

## Related pages
[[Enriched category]] · [[Quantale]] · [[Monoidal category]] · [[Seven Sketches ch4 - Collaborative design]] · [[Polynomial comonoid]]
