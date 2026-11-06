---
type: definition
area: dsl
source-ref: "Bilionis 2026, Def. 2.1; Spivak-Niu (cited)"
tags: [category-theory]
---

# Polynomial functor

> [!definition] Polynomial (Bilionis 2026, Def. 2.1)
> A polynomial is a sum of representables
> $$p = \sum_{o\in O} y^{A_o},\qquad p(X) = \sum_{o\in O} X^{A_o},$$
> an endofunctor of Set acting on maps by $p(u)(o,k) = (o, u\circ k)$.
> Its **positions** are $p(1)\cong O$; the **directions** at $o$ are $p[o] = A_o$.
> A constant polynomial on a set $C$ is $\sum_{c\in C} y^0$.
>
> (source: `Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`, pp. 2-3)

**Intuition**: a polynomial is a menu that depends on what you see. Each position is a state you can observe; the directions at that position are the moves allowed there. Polynomials and [[Dependent lens]]es form the category **Poly**, with $\mathbf{Poly}(p,q)$ the set of lenses $p\to q$ (cited by Bilionis to Niu-Spivak).

## Equipment-interface reading

Bilionis calls a polynomial an **equipment interface**: positions $O$ are what the instrument reports, $A_o$ the requests it accepts when it reports $o$ (source: `Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`, Def. 2.1).

> [!failure] Hidden state that changes the menu
> The menu must be a function of the reported position. If an unreported internal state changes which requests are admissible, the interface is wrong as stated: that state has to be exposed in the readout (source: `Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`, p. 3).

## Notation

Juxtaposition is Cartesian product (`AB = A\times B`); $Sy^S = \sum_{s\in S} y^S$ is the state monomial used by [[Dynamical system as lens]].

## Where it appears
- [[Polynomial equipment interfaces (Bilionis 2026)]] — the interface type of every instrument and example.

## Textbook references
- `DSL/Spivak, Niu - Polynomial Functors.pdf` (queued) — the general theory; this page should be extended from its Ch. 1-2 on ingest.
- Positions/directions notation and Prop. 2.6 ($I \cong p(1)$): [[Polynomial Functors ch2 - Polynomial functors]] (source: Spivak, Niu - Polynomial Functors.pdf, Def. 2.1, Prop. 2.6, Def. 2.8).
- Overview of the whole setting: [[Poly (Spivak 2020)]]. Monoidal structures: [[Poly product]], [[Poly parallel product]], [[Poly composition product]].

**Sources**: `Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Dependent lens]] · [[Poly coproduct]] · [[Poly product]] · [[Poly parallel product]] · [[Dynamical system as lens]]
