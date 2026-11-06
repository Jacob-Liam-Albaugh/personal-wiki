---
type: definition
area: dsl
source-ref: "Bilionis 2026, Def. 4.2, Prop. 6.1"
tags: [category-theory]
---

# Supported experimental protocol

> [!definition] Supported protocol on $p$ (Bilionis 2026, Def. 4.2)
> $\Pi=(K,k_0,D,R,R^+,\delta)$ with protocol states $K$, start $k_0\in K$, support $D\subseteq p(1)K$, reasons $R$, accepting reasons $R^+\subseteq R$, and selector
> $$\delta(o,k)\in p[o]K + R\quad\text{for }(o,k)\in D:$$
> either `continue(a, k')` with $a\in p[o]$, or `stop(r)`. Pairs outside $D$ are **unsupported**. If $D=p(1)K$ the selector is total.
>
> (source: `Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`, p. 5)

**Intuition**: a protocol is a finite-state controller that only ever picks a move the instrument currently allows. $D$ records where the protocol has an opinion; elsewhere it refuses rather than guess.

## Fail-closed extension
Set $R_\perp = R+\{\text{unsupported}\}$ and send every pair outside $D$ to the fresh reason. This gives a total selector targeting $H_{R_\perp}$, where $H_R := y+R$. It does not make an unsupported pair supported (source: `Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`, App. A).

## Why protocol memory is needed
> [!theorem] Prop. 6.1 (Bilionis 2026, p. 12)
> The thermal-cycle protocol is acceptingly playable from $(\text{open}, \text{plate\_staged})$ in 5 actions (load, close, run($\theta^\star$), open, unload). No selector depending only on the joint equipment observation reproduces it: $(\text{closed\_ready}, \text{plate\_loaded})$ occurs both before and after run($\theta^\star$) with different required decisions.

So $K$ is not decoration: observation alone can't tell "about to run" from "just ran".

## Where it appears
- [[Polynomial equipment interfaces (Bilionis 2026)]] — Brew(c), Service, $\Pi_{coffee}$ (11 actions, Prop. 5.2), $\Pi_{cycle}$.

**Sources**: `Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Protocols are lenses]] · [[Modeled playability]] · [[Protocol transport along a lens]] · [[Sequential protocol composition]]
