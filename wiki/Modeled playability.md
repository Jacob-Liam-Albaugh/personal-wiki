---
type: definition
area: dsl
source-ref: "Bilionis 2026, Def. 4.4, Ex. 4.5"
tags: [category-theory]
---

# Modeled playability

> [!definition] Execution and playability (Bilionis 2026, Def. 4.4)
> Run [[Supported experimental protocol]] $\Pi$ on system $\varphi$ from $(s_0,k_0)$ with $o_j=\mathrm{rd}(s_j)$:
> - **reject** if $(o_j,k_j)\notin D$;
> - `stop(r)` terminates with reason $r$;
> - `continue(a_j,k_{j+1})` sets $s_{j+1}=\mathrm{up}_{s_j}(a_j)$.
>
> **Playable**: the run never queries outside $D$. **Acceptingly playable**: the run is finite and stops with $r\in R^+$.
>
> (source: `Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`, p. 6)

**Intuition**: "modeled" because it is a property of the protocol against the *model* $\varphi$, not the physical device.

> [!failure] Ex. 4.5 — local admissibility is not enough (p. 6)
> A ready/done system whose update stutters: every chosen action is admissible and the run is playable, yet it never reaches an accepting stop. Accepting playability is a global property.

## Where it appears
- [[Polynomial equipment interfaces (Bilionis 2026)]] — preserved by [[Protocol transport along a lens]] (Prop. 4.6) and by [[Sequential protocol composition]] (Prop. 4.7).

**Sources**: `Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Dynamical system as lens]] · [[Supported experimental protocol]]
