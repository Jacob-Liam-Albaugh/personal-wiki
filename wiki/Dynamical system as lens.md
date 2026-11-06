---
type: definition
area: dsl
source-ref: "Bilionis 2026, Def. 4.1"
tags: [category-theory]
---

# Dynamical system as a lens

> [!definition] System with interface $p$ (Bilionis 2026, Def. 4.1)
> A deterministic system with state set $S$ and interface $p$ is a [[Dependent lens]] $\varphi: Sy^S\to p$:
> - forward (readout) $\mathrm{rd}: S\to p(1)$,
> - backward (update) at $s$: $\mathrm{up}_s: p[\mathrm{rd}(s)]\to S$.
>
> (source: `Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`, p. 5)

**Intuition**: the state shows a position; only directions admissible *at that position* can be applied. The polynomial fixes the menu, not the dynamics: $\mathrm{rd}$ and $\mathrm{up}$ are extra data.

## Exposing a system through a lens
For $f:p\to q$, the composite $\varphi;f: Sy^S\to q$ is the same machine seen through $q$:
$$\mathrm{rd}_f(s)=f_1(\mathrm{rd}(s)),\qquad \mathrm{up}^f_s(a)=\mathrm{up}_s\big(f^\sharp_{\mathrm{rd}(s)}(a)\big)$$
(source: `Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`, p. 7). This is what [[Protocol transport along a lens]] compares against.

## Dependent dynamical systems (Niu-Spivak ch. 4)

> [!definition] Dependent dynamical system (Def 4.18, p. 90)
> A lens $\varphi : Sy^S \to p$ for any set $S$ and polynomial $p$. The interface $p$ has positions and direction-sets that vary with the position. (source: Polynomial Functors, p. 90)

The special case $p = Iy^A$ is a [[Moore machine]] (Def 4.4). Further examples:

- Def 4.15, Prop 4.17 (p. 89): a deterministic state automaton (states $S$, symbols $A$, update $u : S \times A \to S$, initial state $s_0$, accept states $F \subseteq S$) is a pair of lenses $y \to Sy^S \to 2y^A$.
- Ex 4.21 (p. 91): halting automata, $Sy^S \to y^A + 1$, where the position "accept" has no directions.
- Def 4.25, Ex 4.26 (p. 93): a graph $E \rightrightarrows V$ has the emanation polynomial $\sum_{v \in V} y^{s^{-1}(v)}$, positions vertices and directions outgoing edges.
- Ex 4.66 (p. 118): graphs as wiring diagrams and cellular automata, with a set $\tau(v)$ attached to each vertex.
- Ex 4.43 (p. 103): the do-nothing section; a system's states are treated only through labels, which motivates sections ([[Dependent lens]]).

## Interaction, closure and coalgebras

- Prop 4.54 (p. 113) and the closure $[q, r]$ (Prop 4.85, p. 126): a robot with interface $q$ that does not know its environment, $f : p \otimes q \to r$ giving $f' : p \to [q, r]$ (Ex 4.92, p. 127). See [[Poly parallel product]].
- Ex 6.36 (p. 191): substitution products of dynamical systems as trees, using the halting automaton $p = y^A + 1$. Ex 6.38 (p. 193): composition products of systems can be misleading. Ex 6.41 (p. 197): systems with composite interfaces. Ex 6.43 (p. 199): the $n$-fold product $\varphi^{\triangleright n}$ of $\varphi : Sy^S \to p$. Ex 6.44 (p. 200): transition lenses for state systems. See [[Poly composition product]].
- Ex 6.67 (p. 208): taking $A = B = S$ in (6.65), systems $Sy^S \to p$ are coalgebras of the polynomial functor $p$. Prop 7.98 (p. 271): retrofunctors $Sy^S \nrightarrow C$ are $C$-coalgebras carried by $S$; these are discrete opfibrations, equivalently copresheaves on $C$ (Props 7.103-7.109): [[Polynomial comonoid]].
- Every system $\varphi$ with interface $p$ gives a retrofunctor into the cofree comonoid $\mathbb{T}_p$ (Prop 8.49): [[Cofree comonoid on a polynomial]]. Ex 7.82 (p. 265): systems of ODEs as retrofunctors.
- Cellular automata as bicomodules (Ex 8.106, p. 337): [[Polynomial comonoid]].

## Examples
> [!example] Espresso machine with spent-pod bin (source: `Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`, §5, pp. 8-10)
> State $(U,h,B,W)$: unused capsules, holder, bin ($|B|\le 2$), waste. Readout shows $(U,h,B)$. Prop. 5.1: the updates insert / brew / eject / empty_bin preserve the state invariant, so they define a lens $\varphi_E$.

## Where it appears
- [[Polynomial equipment interfaces (Bilionis 2026)]] — espresso system $\varphi_E$, thermocycler $\varphi_{cycle}$, exposed systems $\varphi;f$.
- Moore machines as lenses $Sy^S \to Iy^A$ (Def. 4.4, p. 85; Poly 2020 Prop. 3.1 names the outputs $B$): [[Moore machine]].
- Comonoid generalization (Def. 3.2): [[Polynomial comonoid]].

**Covered in**: Niu-Spivak, Polynomial Functors ch. 4 (pp. 89-128); ch. 6 (pp. 191-200, 208)
**Sources**: `Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`; `text_books/Category Theory/Spivak, Niu - Polynomial Functors.pdf`; page numbers are printed pages.
**Last updated**: 2026-11-06

---

## Related pages
- [[Polynomial functor]] · [[Dependent lens]] · [[Modeled playability]] · [[Moore machine]] · [[Polynomial comonoid]] · [[Poly composition product]]
