---
type: lecture
area: digital
areas: [digital]
course: ece270
lecture: week 07 10_05
source-ref: "ECE 27000/week 07/10_05.pdf, 26 slides (Wakerly ch. 9 figures plus instructor slides)"
tags: [digital-logic]
---

# ECE270 week 07 10_05 - Finite state machines

**Summary**: Introduces clocked state machines: Moore vs Mealy, the clock signal, the D flip-flop as state memory, the next-state and output structure, a worked 2-flip-flop counter with enable, and the nine design steps.

**File**: `ECE 27000/week 07/10_05.pdf`

---

## Topics
- **Applications (p. 2-5)**: seasons cycle Spring, Summer, Autumn, Winter. A Moore machine puts the output on the state (Winter snow, Spring flowers, Summer travel, Autumn leaves); a Mealy machine puts it on the transition (spring break, commencement, school year start, Thanksgiving). Instructor table: Moore = output by states; Mealy (more common) = output by transitions. A morning example has states Sleep, Breakfast, Sport, Lunch with inputs Alarm, Friend Call, Feel Hungry.
- **State diagrams (p. 6-7)**: Fig. 9-9 Mealy and Fig. 9-10 Moore diagrams of a 4-state machine A, B, C, D. With EN=0 the state holds; EN=1 steps A to B to C to D to A. Mealy output MAX=1 only on the D to A transition (EN=1); Moore output MAXS=1 in state D.
- **Clock (p. 8)**: Fig. 9-1 active-high and active-low clocks; period, frequency $1/t_{per}$, duty cycle $t_H/t_{per}$. Clock speed up to 4 GHz inside chips and up to 500 MHz on a PCB between chips.
- **D flip-flop (p. 9-10)**: Fig. 9-2 positive-edge D flip-flop with function table (rising edge copies D to Q; otherwise Q holds); Fig. 9-3 waveforms. DDR (double data rate) uses both edges, common in memory interfaces. See [[Latches and flip-flops]].
- **Structure (p. 11-14)**: Fig. 9-4 Mealy: next-state logic F, state memory, output logic G.
  $$\text{next state} = F(\text{current state},\ \text{input})$$
  $$\text{output (Mealy)} = G(\text{current state},\ \text{input})$$
  Fig. 9-5 Moore: $\text{output} = G(\text{current state})$. Fig. 9-6 adds an output pipeline register to a Mealy machine.
- **Timing (p. 15)**: Fig. 9-7 compares Moore, pipelined and Mealy output timing against the clock. Mealy outputs can change when inputs change; Moore outputs change after the clock edge.
- **Implementation (p. 16-20)**: Fig. 9-8 builds the 4-state machine from two D flip-flops with
  $$D_0 = Q_0 \cdot EN' + Q_0' \cdot EN$$
  $$D_1 = Q_1 \cdot EN' + Q_1' Q_0 \cdot EN + Q_1 Q_0' \cdot EN$$
  and MAX from an AND gate on the state and EN. Table 9-1 gives the transition table (a), state table (b) and state/output table (c); Table 9-2 the Moore state/output table. Fig. 9-11 is the same circuit redrawn; Fig. 9-12 its timing diagram (states A, A, B, C, C, C, D, D, D, A, A).
- **Design steps (p. 21)**: (1) determine state and output tables; (2) minimize states and outputs; (3) assign states; (4) write transition and output tables; (5) choose flip-flops (usually edge-triggered D); (6) construct the excitation table; (7) derive excitation equations; (8) write output equations; (9) draw logic diagrams.
- **Eight-state example (p. 22-24)**: Fig. 13 uses three flip-flops, inputs X and Y, outputs Z1 and Z2; Table 9-3 transition/output and state/output tables for states A to H; Fig. 9-14 state diagram.
- **Building a state table (p. 25-26)**: Fig. 9-15 timing for a machine that sets Z when two equal A inputs occur (with B=1 variants). Fig. 9-16 shows the table evolving: initial state INIT, then A0 (got a 0 on A), A1 (got a 1 on A), then OK (two equal A inputs) with Z=1.

## Key results
> [!definition] Moore vs Mealy
> Moore: output depends only on the state.
> Mealy: output depends on state and input.
> (source: 10_05.pdf, p. 4, 11-12)

> [!example] Four-state enable counter (p. 16)
> $$Q_1^{+} Q_0^{+} = Q_1 Q_0 + 1 \ \text{ if } EN = 1$$
> The state holds when EN = 0. Equations as read from the slide.

**Connections**: state memory is the flip-flop of [[ECE270 week 06 09_28 - Latches and flip-flops]]; counters in [[ECE270 week 07 10_03 - Counters and shift registers]] are special state machines. Next: [[ECE270 week 08 10_12 - State machine design and Verilog]].

**Sources**: `ECE 27000/week 07/10_05.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Finite state machine]] · [[Latches and flip-flops]] · [[Sequential logic]] · [[Timing diagram]] · [[Karnaugh map]] · [[Boolean algebra]]
