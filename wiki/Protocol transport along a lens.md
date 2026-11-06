---
type: method
area: dsl
source-ref: "Bilionis 2026, §4.4, Prop. 4.6"
tags: [category-theory]
---

# Protocol transport along a lens

> [!algorithm] Pullback $f^*\Pi$ (Bilionis 2026, §4.4)
> For $f:p\to q$ and $\Pi$ on $q$, $f^*\Pi$ on $p$ keeps $K,k_0,R,R^+$ and sets
> - $D_f=\{(o,k): (f_1(o),k)\in D\}$,
> - $\delta_f(o,k)=$ `continue`$(f^\sharp_o(a),k')$ if $\delta(f_1(o),k)=$ `continue`$(a,k')$, and `stop(r)` if it stops.
>
> As lenses: $\chi_{f^*\Pi}=(f\otimes\mathrm{id}_{Ky^K});\chi_\Pi$.
>
> (source: `Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`, p. 7)

> [!theorem] Prop. 4.6 (p. 7)
> Executing $f^*\Pi$ on $\varphi$ and $\Pi$ on $\varphi;f$ give the same equipment and protocol states, actions related by $f^\sharp$, and the same rejection step, terminal reason, step count and divergence. Hence (accepting) playability transfers both ways.

**Intuition / when to use it**: write a protocol once against a common interface $q$, then run it on each vendor device through its translation lens $p_i\to q$. Functoriality $(f;g)^*\Pi=f^*(g^*\Pi)$, $\mathrm{id}^*\Pi=\Pi$ is argued componentwise in the paper, not as a separate proposition.

> [!example] Two thermocyclers (p. 13)
> $\Pi_{cycle}$ transported along $g_i=(f_i\times\mathrm{id}_{p_H});\jmath_{cycle}$ for devices A and B (see [[Same-position restriction lens]], [[Poly product]]).

**Sources**: `Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Dependent lens]] · [[Dynamical system as lens]] · [[Protocols are lenses]] · [[Modeled playability]] · [[Polynomial equipment interfaces (Bilionis 2026)]]
