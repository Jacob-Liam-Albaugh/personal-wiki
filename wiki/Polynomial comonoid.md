---
type: theorem
area: dsl
source-ref: "Niu-Spivak 2024, Thm. 7.28; Spivak 2020, §3"
tags: [category-theory]
---

# Polynomial comonoid

**Summary**: A comonoid in $(\mathrm{Poly},y,\circ)$ is a small category; their morphisms are retrofunctors (cofunctors), forming Cat$^\sharp$.

---

> [!theorem] Ahman-Uustalu
> Comonoids in Poly under the [[Poly composition product]] are small categories. (source: Polynomial Functors, Thm. 7.28; Poly, Thm. 2.6)

## Intuition

A comonoid is a carrier $c$ with eraser $\epsilon : c\to y$ and duplicator $\delta : c\to c\circ c$ (Def. 7.14). Positions are objects, directions at an object are morphisms out of it, and carrier $= \sum_i y^{C[i]}$. A morphism is a retrofunctor: a map $F$ on objects and, for each $c$, $F^\sharp_c : C'[Fc]\to C[c]$ (Defs. 7.49, 7.55). The contractible groupoid $Sy^S$ is the store comonad (Poly 2020).

## Examples

- Coalgebras are retrofunctors $Sy^S\not\to C$ (Def. 7.96): [[Moore machine]], [[Dynamical system as lens]].
- Cat$^\sharp$ has the cofree comonoid on a polynomial (trees, Thm. 8.45) and all small limits and colimits: [[Polynomial Functors ch8 - Categorical properties of polynomial comonoids]].
- Cartesian retrofunctors are discrete opfibrations (Prop. 8.66).

**Sources**: Niu, Spivak, Polynomial Functors (2024), ch. 7, 8; Spivak, Poly (2020).
**Last updated**: 2026-11-06

---

## Related pages
[[Poly composition product]] · [[Category]] · [[Functor]] · [[Polynomial Functors ch7 - Polynomial comonoids and retrofunctors]] · [[Polynomial functor]] · [[Moore machine]]
