---
type: definition
area: dsl
source-ref: "Bilionis 2026, §3.1"
---

# Coproduct $p+q$

> [!definition] Coproduct $p+q$
> For $p=\sum_{i\in I} y^{A_i}$ and $q=\sum_{j\in J} y^{B_j}$:
> $$p+q = \sum_{x\in I+J} y^{C_x},\quad C_{\iota_I(i)}=A_i,\ C_{\iota_J(j)}=B_j$$
> Unit: $0$.
>
> (source: `Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`, §3.1, p. 4)

**Intuition**: choose **one** tagged component position; accept a direction from that component only.

## Comparison

| | positions | directions at $(i,j)$ | unit |
|---|---|---|---|
| [[poly-coproduct]] $p+q$ | one of $I+J$ | that component's | $0$ |
| [[poly-product]] $p\times q$ | pairs $IJ$ | $A_i + B_j$ (either) | $1$ |
| [[poly-parallel-product]] $p\otimes q$ | pairs $IJ$ | $A_iB_j$ (both) | $y$ |

Wiki note: Poly also has the composition product $\triangleleft$ and the Dirichlet product; Bilionis 2026 uses neither (its $\triangleright$ is [[sequential-protocol-composition]], not $\triangleleft$). Pages for those wait for the Spivak-Niu ingest.

## Where it appears
- [[bilionis-2026-polynomial-equipment-interfaces]] — the contrast case when comparing the three products fiber by fiber.

**Sources**: `Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[polynomial-functor]] · [[poly-coproduct]] · [[poly-product]] · [[poly-parallel-product]]
