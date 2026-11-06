---
type: theorem
area: dsl
source-ref: "Bilionis 2026, Prop. 4.3, App. A"
---

# Protocols are lenses

> [!theorem] Prop. 4.3 (Bilionis 2026)
> For a total support $D=p(1)K$,
> $$\mathbf{Poly}\big(p\otimes Ky^K,\ H_R\big)\ \cong \prod_{(o,k)\in p(1)K}\big(p[o]K+R\big),\qquad H_R=y+R.$$
> So total selectors $\delta$ are exactly lenses $\chi_\Pi: p\otimes Ky^K\to H_R$.
>
> (source: `Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`, p. 5; proof App. A, p. 15)

**Intuition / when to use it**: it lets protocols be manipulated with lens algebra — transporting along a lens becomes precomposition.

> [!proof]
> A lens sends each position $(o,k)$ either to the continuing position $\ast$ of $y$, whose backward map $1\to p[o]K$ picks a pair $(a,k')$, or to a terminal $r\in R$, which has no directions so its backward map is the unique empty one. Reading $\delta$ off a lens and building a lens from $\delta$ are pointwise inverse. Partial $D$ goes through the fail-closed extension (see [[supported-experimental-protocol]]).

The [[poly-parallel-product]] is essential: a continuing direction is a pair (equipment direction, next protocol state).

**Sources**: `Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[supported-experimental-protocol]] · [[protocol-transport-along-a-lens]] · [[poly-parallel-product]] · [[bilionis-2026-polynomial-equipment-interfaces]]
