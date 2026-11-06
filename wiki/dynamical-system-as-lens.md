---
type: definition
area: dsl
source-ref: "Bilionis 2026, Def. 4.1"
---

# Dynamical system as a lens

> [!definition] System with interface $p$ (Bilionis 2026, Def. 4.1)
> A deterministic system with state set $S$ and interface $p$ is a [[dependent-lens]] $\varphi: Sy^S\to p$:
> - forward (readout) $\mathrm{rd}: S\to p(1)$,
> - backward (update) at $s$: $\mathrm{up}_s: p[\mathrm{rd}(s)]\to S$.
>
> (source: `Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`, p. 5)

**Intuition**: the state shows a position; only directions admissible *at that position* can be applied. The polynomial fixes the menu, not the dynamics: $\mathrm{rd}$ and $\mathrm{up}$ are extra data.

## Exposing a system through a lens
For $f:p\to q$, the composite $\varphi;f: Sy^S\to q$ is the same machine seen through $q$:
$$\mathrm{rd}_f(s)=f_1(\mathrm{rd}(s)),\qquad \mathrm{up}^f_s(a)=\mathrm{up}_s\big(f^\sharp_{\mathrm{rd}(s)}(a)\big)$$
(source: `Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`, p. 7). This is what [[protocol-transport-along-a-lens]] compares against.

## Examples
> [!example] Espresso machine with spent-pod bin (source: `Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`, §5, pp. 8-10)
> State $(U,h,B,W)$: unused capsules, holder, bin ($|B|\le 2$), waste. Readout shows $(U,h,B)$. Prop. 5.1: the updates insert / brew / eject / empty_bin preserve the state invariant, so they define a lens $\varphi_E$.

## Where it appears
- [[bilionis-2026-polynomial-equipment-interfaces]] — espresso system $\varphi_E$, thermocycler $\varphi_{cycle}$, exposed systems $\varphi;f$.

**Sources**: `Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[polynomial-functor]] · [[dependent-lens]] · [[modeled-playability]]
