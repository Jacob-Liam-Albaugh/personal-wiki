---
type: theorem
area: dsl
source-ref: "Bilionis 2026, Prop. 3.1"
---

# Same-position restriction lens

> [!theorem] Prop. 3.1 (Bilionis 2026)
> If $p=\sum_o y^{A_o}$, $q=\sum_o y^{B_o}$ have the same positions and $B_o\subseteq A_o$ for all $o$, then identity on positions with the inclusions $B_o\hookrightarrow A_o$ is a lens $\jmath: p\to q$.
>
> (source: `Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`, p. 4)

**Intuition / when to use it**: to impose a *policy* (fewer allowed requests) on a raw interface. The arrow runs raw → restricted because directions go backward: a restricted request is translated back into the same raw request.

> [!proof]
> A lens needs $f_1$ (take the identity) and $f^\sharp_o: q[o]=B_o\to A_o=p[o]$ (take the inclusion). Nothing else to check.

## Where it appears
- [[bilionis-2026-polynomial-equipment-interfaces]] — $\jmath_{cycle}: p_{raw}\to p_{cycle}$ restricting the thermocycler + plate handler.

**Sources**: `Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[dependent-lens]] · [[protocol-transport-along-a-lens]]
