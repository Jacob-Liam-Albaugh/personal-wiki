---
type: definition
area: dsl
source-ref: "Bilionis 2026, Def. 2.2; Spivak-Niu (cited)"
---

# Dependent lens

> [!definition] Lens $f:p\to q$ (Bilionis 2026, Def. 2.2)
> A forward map on positions $f_1: p(1)\to q(1)$, and for each $o\in p(1)$ a backward map on directions
> $$f^\sharp_o: q[f_1(o)] \to p[o].$$
> On $X$: $f_X(o,k) = \big(f_1(o),\ d\mapsto k(f^\sharp_o(d))\big)$.
> Composition: $(f;g)_1 = g_1\circ f_1$, $(f;g)^\sharp_o = f^\sharp_o\circ g^\sharp_{f_1(o)}$.
>
> (source: `Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`, p. 3)

**Intuition**: positions flow forward, directions flow back. A lens $p\to q$ says how to *present* each $p$-observation as a $q$-observation, and how to *translate* a $q$-request back into a $p$-request. Every natural transformation between polynomial functors has this form (Bilionis cites Niu-Spivak).

## Uses
- **System as a lens** out of a state monomial: [[dynamical-system-as-lens]].
- **Policy restriction**: [[same-position-restriction-lens]] — raw interface → restricted one.
- **Device translation**: a lens from a vendor interface to a common one lets a protocol written once run on several devices, via [[protocol-transport-along-a-lens]].
- **Protocols themselves** are lenses into a terminal-reason polynomial: [[protocol-lens-correspondence]].

## Where it appears
- [[bilionis-2026-polynomial-equipment-interfaces]] — systems, protocols, restriction, device-to-common translations.

**Sources**: `Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[polynomial-functor]] · [[dynamical-system-as-lens]] · [[protocol-transport-along-a-lens]]
