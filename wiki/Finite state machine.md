---
type: concept
area: digital
areas: [digital]
source-ref: "ECE 270 lectures 10_05, 10_12, 10_17, 10_24, 10_26, 11_09 (Wakerly ch. 9, 12)"
tags: [digital-logic]
---

# Finite state machine

**Summary**: A clocked circuit with a state memory, next-state logic and output logic; Moore machines output from the state, Mealy machines from state and input.

## Structure
$$\text{next state} = F(\text{state},\ \text{input})$$
$$\text{output (Mealy)} = G(\text{state},\ \text{input})$$
$$\text{output (Moore)} = G(\text{state})$$
- Fig. 9-4 Mealy, Fig. 9-5 Moore, Fig. 9-6 pipelined output register. (source: 10_05.pdf, p. 11-14)
- The state memory is a bank of edge-triggered D flip-flops; see [[Latches and flip-flops]]. (source: 10_05.pdf, p. 9-10)
- Moore outputs change after the clock edge; Mealy outputs can change when inputs change; pipelined outputs are delayed one clock and glitch-free. (source: 10_05.pdf, p. 15)
- Clock: period, frequency, duty cycle; DDR uses both edges. See [[Timing diagram]]. (source: 10_05.pdf, p. 8)
- Tables 9-1 to 9-3 show state/output tables for the examples. (source: 10_05.pdf)

> [!definition] Moore vs Mealy
> Moore: output depends only on the state (seasons: winter snow, spring flowers). Mealy (more common): output depends on state and input, i.e. on the transition (spring break, commencement).
> (source: 10_05.pdf, p. 2-5, 11-12)

$$\text{next state} = F(\text{current state},\ \text{input})$$
$$\text{output (Mealy)} = G(\text{current state},\ \text{input})$$

> [!example] Four-state enable counter (p. 16)
> States A, B, C, D (Figs. 9-9, 9-10): EN = 0 holds, EN = 1 steps A to B to C to D to A. Mealy output MAX = 1 only on the D to A transition; Moore output MAXS = 1 in state D. With two D flip-flops (Fig. 9-8):
> $$Q_1^{+} Q_0^{+} = Q_1 Q_0 + 1 \ \text{ if } EN = 1$$
> $$D_0 = Q_0 \cdot EN' + Q_0' \cdot EN$$
> $$D_1 = Q_1 \cdot EN' + Q_1' Q_0 \cdot EN + Q_1 Q_0' \cdot EN$$
> (source: 10_05.pdf, p. 6-7, 16-20)

- Morning example: states Sleep, Breakfast, Sport, Lunch with inputs Alarm, Friend Call, Feel Hungry. An eight-state, three-flip-flop example (Table 9-3, Fig. 9-14) has inputs X, Y and outputs Z1, Z2. (source: 10_05.pdf, p. 2-5, 22-24)
- Building the detector table (Figs. 9-15, 9-16): INIT, then A0 and A1 (last A value), then OK (two equal A inputs) with Z = 1; nonminimal equivalent tables (OK00, OK11) are shown in Fig. 9-19, and the minimal Table 9-4 has five states, Z = 1 in OK0 and OK1. (source: 10_05.pdf, p. 25-26; 10_12.pdf, p. 19-25)

## Design steps (nine)
1. State and output tables, 2. minimize, 3. assign states, 4. transition and output tables, 5. choose flip-flops, 6. excitation table, 7. excitation equations, 8. output equations, 9. logic diagrams. (source: 10_05.pdf, p. 21)

## Examples
- Seasons and a morning routine illustrate Moore (output tied to state) versus Mealy (output tied to a transition). (source: 10_05.pdf, p. 2-7)
- Four-state enable counter (Figs. 9-9, 9-10), with next-state equations for D0 and D1 and outputs MAX and MAXS. (source: 10_05.pdf, p. 16-20)
- Detector with states INIT, A0, A1, OK0, OK1 (state assignments in Tables 9-5 and 9-6); adjacency diagram for choosing codes. (source: 10_12.pdf, p. 19-30)
- T-Bird tail lights (Tables 9-7, 9-8), with $LA = L1 + L2 + L3 + LR3$; traffic light (Sunnyvale); guessing game with output-coded state assignment; counting machine for multiples of 4. (source: 10_12.pdf, p. 19-34; 10_26.pdf, p. 13-14)
- Counters and ring counters are state machines with one cycle of states. See [[Counters and registers]].

## State minimization and encoding
- States merge when outputs match and, for every input, next states fall in the same group (by diagram and by table). (source: 10_17.pdf, p. 6-13)

> [!definition] Equivalent states
> Two states are equivalent if they give the same outputs and their next states for every input are equivalent; equivalent states can be merged.
> (source: 10_17.pdf, p. 6-13)

- Regular expressions describe input sequences: $\varepsilon$, $L_1$ or $L_2$, $L^{*}$, $L^{+}$; the pattern detector $0^{*}1^{+}0^{+}1(0\text{ or }1)^{*}$ is built as a state machine. (source: 10_17.pdf, p. 2-5)
- Encodings offered for five states: 3-bit simplest, decomposed, one-hot (5 bits), almost one-hot (4 bits). One-hot uses more flip-flops but simpler next-state logic. (source: 10_12.pdf, p. 26-28)
> [!definition] One-hot and almost one-hot
> One flip-flop per state (5 for INIT, A0, A1, OK0, OK1); almost one-hot drops the flip-flop for the reset state (4).
> (source: 10_12.pdf, Table 9-5)

- With n bits there are $2^n$ codes; choosing which k to use gives
$$C(2^n, k) = \frac{(2^n)!}{k!\,(2^n - k)!}$$
For 3 bits and 4 states $C(8,4) = 70$. Wiki note: this counts subsets of codes; assigning them to specific states multiplies by $4!$. (source: 10_17.pdf, p. 14)

> [!example] Pipelined output (p. 23)
> $$Z \leftarrow Zn \quad \text{at each clock edge}$$
> $Zn$ is decoded from $Snext$, so Z is registered, delayed one clock and glitch-free (Fig. 12-2).
> (source: 10_17.pdf, p. 22-25)
- Invalid machines: missing or conflicting transitions for some input. (source: 10_17.pdf)
- A pipelined output register delays an output by one clock and removes glitches. (source: 10_17.pdf, p. 23)
- USB state diagram shown as a real-world example. (source: 10_17.pdf)

## In Verilog
- Three parts: state register `always @(posedge CLOCK) Sreg <= Snext;`, a `case (Sreg)` next-state block, and a second block for outputs. See [[Verilog]]. (source: 10_12.pdf, p. 35-36)
- Synchronous reset checks RESET on the clock edge; asynchronous reset adds it to the sensitivity list. (source: 10_24.pdf, p. 6)

## Applications beyond hardware
> [!example] Not only hardware
> The same state, input and transition vocabulary describes robots, ticketing and ecological models, not just clocked circuits. (source: 11_09(1).pdf, p. 2-6)

> [!definition] Transition matrix view
> The state table is a matrix $M$ with one row per current state: $\text{out} = M\cdot\text{in}$ (the wiki's reading; the slides give only tables, no equations). (source: 11_09(1).pdf, p. 8)

- Robots, the Aibo pet, ticketing, ecology. A state table can be read as a matrix: $\text{out} = M\cdot\text{in}$, for example $M = ((0,1,1),(1,0,1),(0,0,1))$, in $= (0,1,0)$, out $= (1,0,0)$. The ecology rules are **[unverified]** because the slide render is hard to read. (source: 11_09(1).pdf, p. 2-8)

Wiki note: the slides treat regular expressions and state machines as equivalent; only the examples are shown, not the theorem. (source: 10_17.pdf, p. 2)

**Covered in**: ECE 270 10_05, 10_12, 10_17, 10_24, 10_26, 11_09 (ECE 27000/week 07/10_05.pdf, week 08/10_12.pdf, week 09/10_17.pdf, week 10/10_24.pdf, week 10/10_26.pdf, week 12/11_09(1).pdf)
**Sources**: `ECE 27000/week 07/10_05.pdf`, `ECE 27000/week 08/10_12.pdf`, `ECE 27000/week 09/10_17.pdf`, `ECE 27000/week 10/10_24.pdf`, `ECE 27000/week 10/10_26.pdf`, `ECE 27000/week 12/11_09(1).pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Sequential logic]]
- [[Latches and flip-flops]]
- [[Counters and registers]]
- [[Verilog]]
- [[Timing diagram]]
