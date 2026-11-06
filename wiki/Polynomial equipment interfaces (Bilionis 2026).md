---
type: paper
area: dsl
areas: [dsl]
source-ref: "Bilionis 2026, Polynomial Equipment Interfaces and Experimental Protocols (Sept 2026)"
tags: [category-theory]
authors: ["[[Ilias Bilionis]]"]
year: 2026
venue: "preprint (September 2026)"
file: "papers/DSL/Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf"
---

# Polynomial equipment interfaces and experimental protocols (Bilionis 2026)

**Summary**: Specialises the calculus of [[Polynomial functor]]s and [[Dependent lens]]es to laboratory equipment. An interface is a polynomial (positions = observations, directions = admissible requests), a system is a lens out of a state monomial, and a *supported protocol* is a selector that picks an admissible action plus the next protocol state, or stops with a typed reason. The paper proves that transporting a protocol along a lens preserves execution on the lens-exposed model, and that sequential composition is sound given a handoff condition.

**Authors**: Ilias Bilionis · **Year**: 2026 · **File**: `papers/DSL/Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`

---

## Problem

Workflows must coordinate instruments and people whose available actions depend on the current observable configuration (closed lid before a thermal program; free slot in the spent-pod container before inserting a pod) (source: Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf, p. 1). The paper asks for (i) a precise account of per-observation action menus, (ii) ways to combine component menus, (iii) translations of a common request into equipment-specific requests, and (iv) a separation of interface, equipment dynamics and experimental memory (p. 1-2). The author says the results "spell out operational consequences of the polynomial calculus"; the value claimed is separation and reuse, not new category theory (p. 2).

## Method

Everything is in **Set**. $y$ is the identity functor, $y^A$ the representable ($X\mapsto X^A$), and a set $C$ is written as the constant polynomial $\sum_{c\in C}y^0$ (p. 2). The paper's term "interface" is a [[Polynomial functor]] in sum-of-representables form.

### Interfaces and lenses (§2)

> [!definition] Equipment interface (Def. 2.1)
> A set $O$ of observable positions and a family $(A_o)_{o\in O}$, $A_o$ = admissible directions (requests) at $o$. The associated polynomial is
> $$p=\sum_{o\in O}y^{A_o},\qquad p(X)=\sum_{o\in O}X^{A_o},\quad p(u)(o,k)=(o,\,u\circ k).$$
> Canonical bijection $p(1)\cong O$; the fiber is written $p[o]=A_o$.
>
> (source: Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf, Def. 2.1, pp. 2-3)

Caveat stated by the paper: the modeled action menu must be determined by the reported position; hidden state may change a successor state but if it changes the menu the readout must expose it. The polynomial itself carries no update rule (p. 3).

> [!definition] Lens (Def. 2.2)
> A lens $f:p\to q$ is a forward map $f_1:p(1)\to q(1)$ and, for each $o\in p(1)$, a backward map
> $$f^\sharp_o:\;q[f_1(o)]\longrightarrow p[o].$$
> It induces a natural transformation $f_X:p(X)\to q(X)$,
> $$f_X(o,k)=\big(f_1(o),\;d\mapsto k(f^\sharp_o(d))\big).$$
> Composition (first-then-second) of $f:p\to q$, $g:q\to r$:
> $$(f;g)_1=g_1\circ f_1,\qquad (f;g)^\sharp_o=f^\sharp_o\circ g^\sharp_{f_1(o)}.$$
> Every natural transformation between these polynomial functors has this forward-backward form (cited to Niu-Spivak [1]). Interfaces and lenses form the category **Poly**.
>
> (source: same, Def. 2.2, p. 3)

The paper uses this as the standard [[Dependent lens]] / [[Polynomial functor]] structure; it does not reprove it and cites [1] (Niu-Spivak, *Polynomial Functors*) and [2] (Spivak, "Poly: an abundant categorical setting for mode-dependent dynamics").

### Three ways to combine interfaces (§3.1)

For $p=\sum_{i\in I}y^{A_i}$ and $q=\sum_{j\in J}y^{B_j}$ (pp. 3-4):

> [!definition] Coproduct, product, parallel tensor
> $$p+q=\sum_{x\in I+J}y^{C_x},\quad C_{\iota_I(i)}=A_i,\; C_{\iota_J(j)}=B_j$$
> $$p\times q=\sum_{(i,j)\in I J}y^{A_i+B_j}$$
> $$p\otimes q=\sum_{(i,j)\in I J}y^{A_iB_j}$$
> Units are $0$, $1$, $y$ respectively; all three extend to lenses (cited to [1]).
>
> (source: same, §3.1, p. 4)

Meaning, as the paper glosses them: the [[Poly coproduct]] picks one tagged component position and accepts a direction from it; the [[Poly product]] shows both positions and accepts *one* tagged direction from either component (it does not decide which component acts, the protocol does); the [[Poly parallel product]] (tensor) shows both positions and requests one direction from *each* in one semantic step, with no claim of wall-clock simultaneity or independence of physical effects. Fiber example: components offering `close` and `load` give a coproduct reporting one component, a product offering tagged `close` or `load`, and a tensor offering the pair (`close`,`load`) (p. 4).

Wiki note: in Spivak-Niu terminology the tensor here is the parallel product $\otimes$ of Poly ([[Poly parallel product]], also called the Dirichlet product), not the composition product $\triangleleft$ ([[Poly composition product]]), which the paper does not use.

> [!theorem] Same-position restriction (Prop. 3.1)
> If $p=\sum_{o\in O}y^{A_o}$, $q=\sum_{o\in O}y^{B_o}$ with $B_o\subseteq A_o$ for every $o$, the identity position map and the fiber inclusions $B_o\hookrightarrow A_o$ define a lens $\jmath:p\to q$.
>
> Proof: forward map $\mathrm{id}_O$; the required backward map $q[o]\to p[o]$ is the inclusion. The arrow points raw $\to$ restricted because lens directions are contravariant.
>
> (source: same, Prop. 3.1, p. 4)

### Dynamics (§4.1)

> [!definition] Deterministic system (Def. 4.1)
> With state monomial $Sy^S=\sum_{s\in S}y^S$, a deterministic system with state set $S$ and interface $p$ is a lens
> $$\varphi:Sy^S\to p.$$
> Forward map = readout $\mathrm{rd}:S\to p(1)$; backward map at $s$ = update $\mathrm{up}_s:p[\mathrm{rd}(s)]\to S$. Several systems may realise the same interface.
>
> (source: same, Def. 4.1, p. 5)

This is the [[Dynamical system as lens]] representation, which the introduction attributes to the existing theory (p. 1).

### Protocols (§4.2)

> [!definition] Supported experimental protocol (Def. 4.2)
> Given interface $p$, a protocol is a tuple
> $$\Pi=(K,k_0,D,R,R^+,\delta),$$
> with $K$ protocol states, $k_0\in K$, supported domain $D\subseteq p(1)K$ (i.e. $p(1)\times K$), terminal reasons $R$, accepted reasons $R^+\subseteq R$, and selector
> $$\delta(o,k)\in p[o]^K+R\quad\text{for }(o,k)\in D.$$
> A decision is $\mathrm{continue}(a,k')$ with $a\in p[o]$, $k'\in K$, or $\mathrm{stop}(r)$. Pairs outside $D$ are *unsupported*.
>
> (source: same, Def. 4.2, p. 5)

Wiki note: the text writes the codomain as $p[o]K+R$ where juxtaposition is the paper's Cartesian product (p. 2), so $p[o]K$ means $p[o]\times K$, pairs $(a,k')$. The PDF extraction renders it as "p[o]K"; it is not an exponent.

If $D=p(1)K$ the selector is *total*. For proper $D$, set $R_\perp=R+\{\text{unsupported}\}$ and send every pair outside $D$ to the fresh reason: the *fail-closed* selector, with target $H_R$ where
$$H_R:=y+R$$
(continuing position has fiber $1$; every reason position has empty fiber) (p. 5). The fail-closed selector does not turn an unsupported pair into supported behaviour.

> [!theorem] Protocol-lens correspondence (Prop. 4.3)
> When $D=p(1)K$,
> $$\mathbf{Poly}\big(p\otimes(Ky^K),\,H_R\big)\;\cong\;\prod_{(o,k)\in p(1)K}\big(p[o]K+R\big).$$
> The tensor is essential: a continuing direction of the source is a pair (equipment direction, next protocol state).
>
> Proof sketch (App. A, p. 15): the source $p\otimes(Ky^K)$ has positions $(o,k)$ and direction fiber $p[o]\times K$. A lens sends each position to the continuing position of $H_R$ (backward map $1\to p[o]\times K$ picks one $(a,k')$) or to a terminal $r\in R$ (empty domain, unique backward map). The constructions are mutually inverse pointwise. For proper $D$, apply the total case to $R_\perp$.
>
> (source: same, Prop. 4.3 and App. A, pp. 5, 15)

Wiki note: the extraction renders the fiber as "p[o]K"; it is read here as the product $p[o]\times K$ (since $y^{A}\otimes y^{K}=y^{AK}$), not an exponential.

### Modeled playability (§4.3)

Execution from an initialised system $(\varphi,s_0)$ and protocol $\Pi$ starts at $(s_0,k_0)$; put $o_j=\mathrm{rd}(s_j)$. If $(o_j,k_j)\notin D$ execution rejects. If $\delta(o_j,k_j)=\mathrm{stop}(r)$ it terminates with reason $r$. If $\delta(o_j,k_j)=\mathrm{continue}(a_j,k_{j+1})$ then $a_j\in p[o_j]$ and $s_{j+1}=\mathrm{up}_{s_j}(a_j)$ (p. 6).

> [!definition] Modeled playability (Def. 4.4)
> $\Pi$ is *playable* from $(\varphi,s_0)$ if the induced execution never queries a pair outside $D$. It is *acceptingly playable* if that execution is finite and terminates at $\mathrm{stop}(r)$ with $r\in R^+$.
>
> (source: same, Def. 4.4, p. 6)

> [!example] One interface, different completion (Ex. 4.5)
> Interface with positions `ready`, `done`, fibers $\{\text{tick}\}$ and $0$. Two systems with state set = positions, identity readout, differing only at `ready`: $\mathrm{up}^{\mathrm{progress}}_{\text{ready}}(\text{tick})=\text{done}$, $\mathrm{up}^{\mathrm{stutter}}_{\text{ready}}(\text{tick})=\text{ready}$. Protocol: $K=\{*\}$, full support, $R=R^+=\{\text{completed}\}$; selects $\mathrm{continue}(\text{tick},*)$ at ready, $\mathrm{stop}(\text{completed})$ at done. Playable on both; accepts after one action on the progress system, runs forever on the stuttering one. So interface plus protocol cannot distinguish accepted completion from endless admissible activity.
>
> (source: same, Ex. 4.5, p. 6)

### Transport along a lens (§4.4)

> [!definition] Transported protocol $f^*\Pi$
> For a lens $f:p\to q$ and a protocol $\Pi=(K,k_0,D,R,R^+,\delta)$ on $q$, $f^*\Pi$ on $p$ keeps $K,k_0,R,R^+$ and has
> $$D_f=\{(o,k)\in p(1)K:(f_1(o),k)\in D\},$$
> $$\delta_f(o,k)=\begin{cases}\mathrm{continue}(f^\sharp_o(a),k') & \delta(f_1(o),k)=\mathrm{continue}(a,k')\\ \mathrm{stop}(r)&\delta(f_1(o),k)=\mathrm{stop}(r).\end{cases}$$
> For a total selector with protocol lens $\chi_\Pi$:
> $$\chi_{f^*\Pi}=(f\otimes\mathrm{id}_{Ky^K});\chi_\Pi.$$
> Same formula for fail-closed extensions with their common fresh reason.
>
> (source: same, §4.4, p. 7)

> [!definition] Exposed system
> For $\varphi:Sy^S\to p$ and $f:p\to q$, the exposed system is the composite $\varphi;f:Sy^S\to q$ with
> $$\mathrm{rd}_f(s)=f_1(\mathrm{rd}(s)),\qquad \mathrm{up}^f_s(a)=\mathrm{up}_s\big(f^\sharp_{\mathrm{rd}(s)}(a)\big).$$
>
> (source: same, p. 7)

> [!theorem] Execution-preserving transport (Prop. 4.6)
> Fix $f:p\to q$, a system $\varphi:Sy^S\to p$, initial state $s_0$, and a supported protocol $\Pi$ on $q$. Executing $f^*\Pi$ on $\varphi$ and executing $\Pi$ on $\varphi;f$ produce the same equipment states and protocol states; corresponding actions are related by $f^\sharp$. They reject at the same step, terminate with the same reason after the same number of actions, or both run forever. Hence playability and accepting playability are equivalent.
>
> Proof (p. 7): both start at $(s_0,k_0)$; with $o=\mathrm{rd}(s)$, $D_f$ makes support at $(o,k)$ equivalent to support at $(f_1(o),k)$; terminal decisions copy; a continuing $\mathrm{continue}(a,k')$ selects $f^\sharp_o(a)$ in the transported protocol so both updates equal $\mathrm{up}_s(f^\sharp_o(a))$ and both next protocol states are $k'$. Induction.
>
> (source: same, Prop. 4.6, p. 7)

Functoriality of transport (stated, justified componentwise, p. 7): $(f;g)^*\Pi=f^*(g^*\Pi)$ and $(\mathrm{id}_r)^*\Pi=\Pi$; the backward composite used is $f^\sharp_o\circ g^\sharp_{f_1(o)}$. The paper stresses the guarantee compares a system only with its *own* lens-exposed model; two different instruments exposing the same interface still need separate completion checks (Ex. 4.5).

### Sequential composition (§4.5)

For protocols $\Pi=(K,k_0,D,R,R^+,\delta)$ and $\Psi=(L,l_0,E,Q,Q^+,\epsilon)$ on the same $p$, the composite $\Pi\triangleright\Psi$ has state set $K+L$, initial state $\iota_K(k_0)$, and
$$T=(R\setminus R^+)+Q,\qquad T^+=\iota_Q(Q^+).$$
Supported domain: every $(o,\iota_L(l))$ with $(o,l)\in E$; and $(o,\iota_K(k))$ with $(o,k)\in D$, except an accepted stop of $\Pi$ additionally requires $(o,l_0)\in E$. Continuations of $\Pi$ stay in the left summand; nonaccepting reasons of $\Pi$ terminate the composite; at an accepted stop of $\Pi$ the composite evaluates $\epsilon(o,l_0)$ with no intermediate equipment action; continuations of $\Psi$ enter the right summand, and terminal decisions of $\Psi$ terminate the composite (p. 8).

> [!theorem] Sequential handoff (Prop. 4.7)
> For a deterministic system $\varphi$ on $p$: if $\Pi$ is acceptingly playable from $s_0$ and terminates at modeled state $s_m$, and $\Psi$ is acceptingly playable from $s_m$, then $\Pi\triangleright\Psi$ is acceptingly playable from $s_0$, and its action word is that of $\Pi$ followed by that of $\Psi$.
>
> Proof (App. B, p. 15): before the accepted decision the composite agrees with $\Pi$ under left injection; at the accepted stop the handoff hypothesis puts $(o,l_0)\in E$; afterwards it agrees with $\Psi$ under right injection; the final reason lies in $Q^+$, hence $T^+$.
>
> (source: same, Prop. 4.7 and App. B, pp. 8, 15)

The paper explicitly does not claim associativity of $\triangleright$: it fixes a left-associated bracketing in §5.2 ("no bracket-independent associativity claim is needed", p. 10). The handoff condition is the observation check $(o,l_0)\in E$. No result value is passed across the handoff (p. 14).

Wiki note: the symbol $\triangleright$ here is protocol sequencing, unrelated to the polynomial composition product $\triangleleft$ ([[Poly composition product]]).

## Worked examples

### Espresso maker with spent-pod container (§5)

Pods $C=\{c_1,c_2,c_3\}$; chamber states $H_C=\{\text{empty}\}+\{\text{loaded}(c)\}+\{\text{brewed}(c)\}$; chamber-content map $\chi:H_C\to\mathcal P(C)$ with $\chi(\text{empty})=\emptyset$, $\chi(\text{loaded}(c))=\chi(\text{brewed}(c))=\{c\}$. A state is $s=(U,h,B,W)$ (unused, chamber, spent container, waste); admissible states $S_E$ satisfy
$$U\,\dot\cup\,\chi(h)\,\dot\cup\,B\,\dot\cup\,W=C,\qquad |B|\le 2.$$
Initial state $s_0=(C,\text{empty},\emptyset,\emptyset)$. Readout $\mathrm{rd}(U,h,B,W)=(U,h,B)$ (waste is hidden because it does not affect admissible commands); positions $O_E=\mathrm{rd}(S_E)$. With $E_B=\{\text{empty\_bin}\}$ if $B\ne\emptyset$ and $\emptyset$ otherwise, the fiber at $o=(U,h,B)$ is

```
A_o = {insert(c) | c in U} ∪ E_B   if h = empty, |B| < 2
      {empty_bin}                  if h = empty, |B| = 2
      {brew}                       if h = loaded(c)
      {eject}                      if h = brewed(c), |B| < 2
      ∅                            otherwise
```

and $p_E=\sum_{o\in O_E}y^{A_o}$ (pp. 8-9). Updates: insert moves $c$ from $U$ to chamber; brew changes only the chamber phase; eject moves the chamber pod to $B$; empty_bin moves all of $B$ to $W$.

> [!theorem] Pod custody and capacity (Prop. 5.1)
> Every displayed candidate update maps $S_E$ into $S_E$; hence readout and updates define a system lens $\varphi_E:S_Ey^{S_E}\to p_E$. (Proof: moves preserve disjointness and union; eject is exposed only when $|B|<2$.)
>
> (source: same, Prop. 5.1, p. 9)

Protocols: $\mathrm{Brew}(c)$ with phases insert, brew, eject, done (Table 1, p. 10: insert needs chamber empty, $c\in U$, $|B|<2$; brew needs loaded$(c)$; eject needs brewed$(c)$, $|B|<2$; done stops with `completed` when chamber empty, $c\in B$). $\mathrm{Service}$ has states inspect, done: stops at once if $B=\emptyset$, else $\mathrm{continue}(\text{empty\_bin},\text{done})$ (p. 9). Composite, left-associated (p. 10):
$$\Pi_1=\mathrm{Brew}(c_1)\triangleright\mathrm{Brew}(c_2),\ \Pi_2=\Pi_1\triangleright\mathrm{Service},\ \Pi_3=\Pi_2\triangleright\mathrm{Brew}(c_3),\ \Pi_{\mathrm{coffee}}=\Pi_3\triangleright\mathrm{Service}.$$

> [!theorem] Espresso playability (Prop. 5.2)
> $\Pi_{\mathrm{coffee}}$ is acceptingly playable from $s_0$; the execution has eleven actions, preserves the pod partition and $|B|\le2$, and ends with $U=\emptyset$, $h=\text{empty}$, $B=\emptyset$, $W=C$. Action word (Table 2): insert($c_1$), brew, eject, insert($c_2$), brew, eject, empty_bin, insert($c_3$), brew, eject, empty_bin.
>
> (source: same, Prop. 5.2 and Table 2, p. 10)

Without the first Service phase, $B=\{c_1,c_2\}$ and the fiber is $\{\text{empty\_bin}\}$ only, so insert($c_3$) is not an admissible direction: "an interface mismatch before it is a failed physical execution" (p. 11).

### Thermocycler (§6)

Components (p. 11): thermocycler $p_{TC}$: open $\mapsto\{\text{close}\}$, closed_ready $\mapsto\{\text{run}(\theta^\star),\text{open}\}$. Human $p_H$: plate_staged $\mapsto\{\text{load}\}$, plate_loaded $\mapsto\{\text{unload}\}$, complete $\mapsto 0$. Raw interface $p_{\mathrm{raw}}=p_{TC}\times p_H$ (six positions, tagged directions). Exposed laboratory interface $p_{\mathrm{cycle}}$ (Table 3, p. 11): (open, staged): {H:load}; (open, loaded): {TC:close, H:unload}; (closed_ready, loaded): {TC:run($\theta^\star$), TC:open}; (open, complete): none; all other positions empty. Every exposed fiber is a subset of the raw product fiber, so Prop. 3.1 gives the restriction lens $\jmath_{\mathrm{cycle}}:p_{\mathrm{raw}}\to p_{\mathrm{cycle}}$.

System $\varphi_{\mathrm{cycle}}:Sy^S\to p_{\mathrm{cycle}}$ with four-state $S$ (Table 4, p. 12); run($\theta^\star$) leaves the state at (closed_ready, loaded). Protocol: $K=\{\text{load, close, cycle, open, unload, done}\}$, $k_0=\text{load}$, $R=R^+=\{\text{completed}\}$, with Table 5 decisions H:load, TC:close, TC:run($\theta^\star$), TC:open, H:unload, stop(completed).

> [!theorem] Thermocycler playability and memory (Prop. 6.1)
> The protocol is acceptingly playable from (open, plate_staged), runs five actions and ends at (open, complete). No deterministic selector depending only on the joint equipment observation reproduces this execution on $\varphi_{\mathrm{cycle}}$.
>
> Proof idea (p. 12): the observation (closed_ready, plate_loaded) occurs immediately before and after run($\theta^\star$), with different prescribed decisions (run, then open); protocol states `cycle` and `open` supply the distinction.
>
> (source: same, Prop. 6.1, p. 12)

Two raw interfaces (p. 13): $p_A$: up $\{\text{lower, status}\}$, down $\{\text{raise, cycle, status}\}$; $p_B$: released $\{\text{seal}\}$, locked $\{\text{unseal, execute, diagnostic}\}$. Lenses $f_A:p_A\to p_{TC}$, $f_B:p_B\to p_{TC}$ send up/released to open and down/locked to closed_ready, with backward maps: close $\mapsto$ lower / seal; run($\theta^\star$) $\mapsto$ cycle / execute; open (at closed_ready) $\mapsto$ raise / unseal. Status and diagnostic have no preimage request. Laboratory lens
$$g_i=(f_i\times\mathrm{id}_{p_H});\jmath_{\mathrm{cycle}}:p_i\times p_H\to p_{\mathrm{cycle}},\quad i\in\{A,B\}.$$
By Prop. 4.6, $g_A^*\Pi_{\mathrm{cycle}}$ and $g_B^*\Pi_{\mathrm{cycle}}$ issue (lower, cycle, raise) and (seal, execute, unseal) respectively between the same human load/unload actions; both accept after five actions on the specified raw models (identity readout, total updates; status/diagnostic/thermal requests leave position unchanged).

## Results

The paper is a theory paper; there are no numerical experiments. Its findings are the propositions above:

- Prop. 4.3: protocols with total selector on $p$ are exactly lenses $p\otimes(Ky^K)\to H_R$ (p. 5).
- Prop. 4.6: protocol transport along $f:p\to q$ commutes with exposing a system through $f$; execution traces, rejection step, terminal reason and divergence all agree (p. 7). Transport is functorial in $f$ (p. 7).
- Prop. 4.7: sequential composition with a handoff check $(o,l_0)\in E$ concatenates action words (p. 8).
- Prop. 5.2: the three-pod espresso protocol takes 11 actions, with exactly two bin services, and ends with all pods in waste (p. 10).
- Prop. 6.1: the thermocycler run takes 5 actions; protocol memory is necessary because (closed_ready, plate_loaded) recurs with different required decisions (p. 12).
- Ex. 4.5: admissible activity does not imply successful completion (p. 6).

## Limitations

As stated by the author (pp. 13-14):
- Semantics is deterministic, discrete, sequential. Stochastic extension would replace successors by distributions; continuous dynamics need a time model; concurrency needs rules beyond the pointwise tensor; resource transformation (splitting, mixing, reaction) needs quantity/conservation structure.
- All guarantees are model-relative. Physical validity (faithful observation, command realisation, heat transfer, contamination, sensor uncertainty, faults, human error) is a separate obligation; a typed interface or accepting modeled execution certifies neither physical safety nor scientific success.
- Sequential composition passes no result value across a handoff; typed result-passing, recovery, and parallel regions are future work.
- Transport compares a system only with its own lens-exposed model; general equipment substitution needs a relation between distinct state models.
- The thermocycler omits temperature trajectories, timing, faults and specimen response.
- The author claims no greater computational expressiveness than state machines (p. 14).

Wiki notes (not from the paper): (i) no associativity or unit laws are established for $\triangleright$; (ii) the equality of transport with the lens composite $(f\otimes\mathrm{id});\chi_\Pi$ is stated, but its proof is left to the reader aside from Prop. 4.6; (iii) the exact categorical status of "protocols with proper $D$" (as opposed to total ones) is left outside the Prop. 4.3 correspondence, handled only through the fail-closed extension.

## Connections

- Builds on [[Polynomial functor]] theory: Niu-Spivak *Polynomial Functors* (2025) and Spivak, *Poly* (2020) are the cited foundations (refs [1], [2], p. 16). Not yet ingested in this wiki; the links above are targets for later chapter ingests.
- Uses [[Dependent lens]] composition, [[Poly product]], [[Poly coproduct]] and the [[Poly parallel product]] (tensor) from that theory, plus the representation of deterministic systems as lenses out of $Sy^S$ ([[Dynamical system as lens]]).
- Related lab pages for the harness/DSL direction: the Poly DSL (**[unverified]** whether this paper's construction is implemented there; the paper does not mention a DSL implementation).
- Protocols as lenses into $H_R=y+R$ are the paper's own construction; the paper cites SiLA 2, OPC UA LADS and SBOL-style protocol representations only as the "workflow/equipment standards" context (refs [6]-[8]) and self-driving-laboratory work (refs [3]-[5]).
- Lens-based interface translation ([[Protocol transport along a lens]]) is the compositional-reuse mechanism: one protocol, many devices.

%% refs:start %%
**Cites in this wiki**: [[Poly (Spivak 2020)]]
%% refs:end %%

**Sources**: `papers/DSL/Bilionis - Polynomial Equipment Interfaces and Experimental Protocols.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Polynomial functor]]
- [[Dependent lens]]
- [[Poly product]]
- [[Poly coproduct]]
- [[Poly parallel product]]
- [[Poly composition product]]
- [[Dynamical system as lens]]
- [[Supported experimental protocol]]
- [[Protocols are lenses]]
- [[Modeled playability]]
- [[Protocol transport along a lens]]
- [[Sequential protocol composition]]
- [[Same-position restriction lens]]
- Background: [[Poly (Spivak 2020)]], [[Poly composition product]].
