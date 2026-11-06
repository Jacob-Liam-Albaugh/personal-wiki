---
type: theorem
area: dsl
source-ref: "Bilionis 2026, Prop. 4.3, App. A"
tags: [category-theory]
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
> A lens sends each position $(o,k)$ either to the continuing position $\ast$ of $y$, whose backward map $1\to p[o]K$ picks a pair $(a,k')$, or to a terminal $r\in R$, which has no directions so its backward map is the unique empty one. Reading $\delta$ off a lens and building a lens from $\delta$ are pointwise inverse. Partial $D$ goes through the fail-closed extension (see [[Supported experimental protocol]]).

The [[Poly parallel product]] is essential: a continuing direction is a pair (equipment direction, next protocol state).

**Sources**: `Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Supported experimental protocol]] · [[Protocol transport along a lens]] · [[Poly parallel product]] · [[Polynomial equipment interfaces (Bilionis 2026)]]
