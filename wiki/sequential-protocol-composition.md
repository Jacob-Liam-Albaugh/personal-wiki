---
type: method
area: dsl
source-ref: "Bilionis 2026, §4.5, Prop. 4.7, App. B"
---

# Sequential protocol composition

> [!algorithm] $\Pi\triangleright\Psi$ (Bilionis 2026, §4.5)
> For $\Pi=(K,k_0,D,R,R^+,\delta)$ and $\Psi=(L,l_0,E,Q,Q^+,\epsilon)$ on the same $p$:
> - states $K+L$, start $\iota_K(k_0)$;
> - reasons $T=(R\setminus R^+)+Q$, accepting $T^+=\iota_Q(Q^+)$;
> - an accepting stop of $\Pi$ at observation $o$ hands off immediately to $\epsilon(o,l_0)$ (no intermediate action), requiring $(o,l_0)\in E$;
> - a non-accepting stop of $\Pi$ ends the composite.
>
> (source: `Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`, p. 8)

> [!theorem] Prop. 4.7 (p. 8; proof App. B, p. 15)
> If $\Pi$ is acceptingly playable from $s_0$ ending at $s_m$, and $\Psi$ is acceptingly playable from $s_m$, then $\Pi\triangleright\Psi$ is acceptingly playable from $s_0$ and its action word is $\Pi$'s followed by $\Psi$'s.

> [!failure] Not claimed
> No associativity or unit laws (§5.2 says a bracket-independent claim is not needed), and no result value passes across the handoff (p. 14). $\triangleright$ is not the Poly composition product $\triangleleft$.

> [!example] $\Pi_{coffee}$ (p. 10)
> Built left-associated from Service and Brew phases. Without the first Service phase, insert($c_3$) is not admissible at $B=\{c_1,c_2\}$ (full bin).

**Sources**: `Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[supported-experimental-protocol]] · [[modeled-playability]] · [[bilionis-2026-polynomial-equipment-interfaces]]
