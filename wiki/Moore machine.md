---
type: definition
area: dsl
source-ref: "Niu-Spivak 2024, Defs 4.1 and 4.4; Spivak 2020, Prop. 3.1"
tags: [category-theory]
---

# Moore machine

**Summary**: A state machine whose output depends on the state and whose state changes on an input; in Poly, a lens $Sy^S \to Iy^A$.

---

> [!definition] Moore machine (Def 4.1, p. 83)
> Three sets: a state-set $S$, a position-set (output-set) $I$ and a direction-set (input-set) $A$. Two functions: $\mathrm{return} : S \to I$ and $\mathrm{update} : S \times A \to S$. It is called an $(A, I)$-Moore machine with states $S$. (source: Polynomial Functors, Def 4.1, p. 83)

> [!definition] Moore machine as a lens (Def 4.4, p. 85)
> An $(A, I)$-Moore machine with states $S$ is a lens in Poly
> $$ \varphi : S y^S \to I y^A. $$
> The domain $Sy^S$ is the state system and the codomain $Iy^A$ is the interface. The on-positions map $\varphi_1$ is the return function and the on-directions map $\varphi^\sharp : S \times A \to S$ is the update function. (source: Polynomial Functors, Def 4.4, p. 85)

## Examples

- Ex 4.2 (p. 84): a transition diagram with inputs {orange, green}, outputs {0, 1} and 3 states.
- Ex 4.6 (p. 86): the counter, $\mathbb{N}y^{\mathbb{N}} \to \mathbb{N}y$, identity on positions and $n \mapsto n+1$ on directions.
- Ex 4.7 (p. 86): moving in the plane, $\mathbb{R}^2 y^{\mathbb{R}^2} \to \mathbb{R}^2 y^{[0,\infty) \times [0, 2\pi)}$.
- Ex 4.9 (p. 87): a function $f : A \to I$ is a memoryless Moore machine $Iy^I \to Iy^A$.

## Generalization

- Replacing the interface $Iy^A$ by any polynomial $p$ gives a dependent dynamical system $Sy^S \to p$ (Def 4.18, p. 90): the available inputs may depend on the output. See [[Dynamical system as lens]].
- A deterministic automaton is a pair of lenses $y \to Sy^S \to 2y^A$ (Prop 4.17, p. 89).
- Poly 2020 states the same lens as Prop 3.1 with outputs named $B$; this page uses the book's $I$. See [[Poly (Spivak 2020)]].

## Where it appears

[[Poly (Spivak 2020)]] · [[Polynomial Functors ch4 - Dynamical systems as dependent lenses]] · [[Dependent lens]]

**Sources**: Niu-Spivak, Polynomial Functors (2024), ch. 4 (pp. 83-90); Spivak, Poly (2020), Prop. 3.1. Page numbers are printed pages.
**Last updated**: 2026-11-06

---

## Related pages
[[Dynamical system as lens]] · [[Dependent lens]] · [[Polynomial functor]] · [[Polynomial comonoid]] · [[Poly composition product]]
