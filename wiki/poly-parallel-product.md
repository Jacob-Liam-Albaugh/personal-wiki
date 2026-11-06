---
type: definition
area: dsl
source-ref: "Bilionis 2026, §3.1"
---

# Parallel product $p\otimes q$

> [!definition] Parallel product $p\otimes q$
> For $p=\sum_{i\in I} y^{A_i}$ and $q=\sum_{j\in J} y^{B_j}$:
> $$p\otimes q = \sum_{(i,j)\in IJ} y^{A_i B_j}$$
> Unit: $y$.
>
> (source: `Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`, §3.1, p. 4)

**Intuition**: show both positions; request **one direction from each** in one semantic step. Bilionis claims no wall-clock simultaneity or independence of effects.

## Comparison

| | positions | directions at $(i,j)$ | unit |
|---|---|---|---|
| [[poly-coproduct]] $p+q$ | one of $I+J$ | that component's | $0$ |
| [[poly-product]] $p\times q$ | pairs $IJ$ | $A_i + B_j$ (either) | $1$ |
| [[poly-parallel-product]] $p\otimes q$ | pairs $IJ$ | $A_iB_j$ (both) | $y$ |

Wiki note: Poly also has the composition product $\triangleleft$ and the Dirichlet product; Bilionis 2026 uses neither (its $\triangleright$ is [[sequential-protocol-composition]], not $\triangleleft$). Pages for those wait for the Spivak-Niu ingest.

## Where it appears
- [[bilionis-2026-polynomial-equipment-interfaces]] — $p\otimes(Ky^K)$ in [[protocol-lens-correspondence]] (a continuing direction is an equipment direction paired with the next protocol state) and $f\otimes\mathrm{id}_{Ky^K}$ in [[protocol-transport-along-a-lens]].

**Sources**: `Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[polynomial-functor]] · [[poly-coproduct]] · [[poly-product]] · [[poly-parallel-product]]
