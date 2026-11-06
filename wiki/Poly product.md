---
type: definition
area: dsl
source-ref: "Bilionis 2026, §3.1"
tags: [category-theory]
---

# Product $p\times q$

> [!definition] Product $p\times q$
> For $p=\sum_{i\in I} y^{A_i}$ and $q=\sum_{j\in J} y^{B_j}$:
> $$p\times q = \sum_{(i,j)\in IJ} y^{A_i+B_j}$$
> Unit: $1$.
>
> (source: `Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`, §3.1, p. 4)

**Intuition**: show **both** positions; accept **one** tagged direction from either component. The interface does not decide which component acts next: the protocol does.

## Comparison

| | positions | directions at $(i,j)$ | unit |
|---|---|---|---|
| [[Poly coproduct]] $p+q$ | one of $I+J$ | that component's | $0$ |
| [[Poly product]] $p\times q$ | pairs $IJ$ | $A_i + B_j$ (either) | $1$ |
| [[Poly parallel product]] $p\otimes q$ | pairs $IJ$ | $A_iB_j$ (both) | $y$ |

Wiki note: Poly also has the composition product $\triangleleft$ and the Dirichlet product; Bilionis 2026 uses neither (its $\triangleright$ is [[Sequential protocol composition]], not $\triangleleft$). Pages for those wait for the Spivak-Niu ingest.

## Where it appears
- [[Polynomial equipment interfaces (Bilionis 2026)]] — the raw joint interface $p_{raw} = p_{TC}\times p_H$ of thermocycler and handler, and the lens $f\times\mathrm{id}$.
- Cartesian closed, with all limits: [[Polynomial Functors ch5 - More categorical properties]], Thm. 5.31. Contrast with [[Poly parallel product]]. Prop. 3.56 gives the product.

**Sources**: `Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Polynomial functor]] · [[Poly coproduct]] · [[Poly product]] · [[Poly parallel product]]
