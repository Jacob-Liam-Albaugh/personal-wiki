---
type: lecture
area: digital
areas: [digital]
course: ece270
lecture: week 08 10_12
source-ref: "ECE 27000/week 08/10_12.pdf, 36 slides (Wakerly ch. 9 figures plus USB slides)"
tags: [digital-logic]
---

# ECE270 week 08 10_12 - State machine design and Verilog

**Summary**: Opens with USB as a state-machine example, repeats the Moore/Mealy structure and the enable-counter example, then works the full design flow on a two-input detector (state table, state assignment, excitation table), the T-Bird tail lights, and a Verilog coding style for state machines.

**File**: `ECE 27000/week 08/10_12.pdf`

---

## Topics
- **USB (p. 2-3)**: up to 127 devices; cables up to 5 m, up to 30 m with hubs; USB 2.0 at 480 Mb/s, USB 3.0 at 4.8 Gb/s; a cable has +5 V, ground and a twisted data pair. Slide 3 shows a Cypress "USB 101" state diagram (Attached, Powered, Default, Address, Configured, Suspended). Author credited on the slide: Robert Murphy.
- **Recap of structure (p. 4-8)**: Fig. 9-4 Mealy, 9-5 Moore, 9-6 pipelined outputs, 9-7 timing, 9-8 the two-flip-flop machine with $Q_0^{*} = D_0$ and $Q_1^{*} = D_1$. See [[ECE270 week 07 10_05 - Finite state machines]].
- **Tables and diagrams (p. 9-14)**: Table 9-1 transition, state and state/output tables; Table 9-2 Moore table; Fig. 9-11 redrawn circuit; Fig. 9-9 and 9-10 state diagrams; Fig. 9-12 timing.
- **Design steps (p. 15)**: nine steps, from state and output tables to logic diagrams.
- **Eight-state machine (p. 16-18)**: Fig. 9-13, Table 9-3, Fig. 9-14.
- **Two-input detector (p. 19-24)**: Problem on slide 19: two inputs A and B, output Z is 1 if A had the same value at each of the two previous clock ticks, or B has been 1 since that was last true; otherwise 0. Fig. 9-15 timing. Fig. 9-16 and 9-17 grow the state table: INIT, A0, A1, then OK states split by the last A value (OK0, OK1). Fig. 9-18 timing and state sequence. Fig. 9-19 shows nonminimal state tables equivalent to the minimal one (extra states such as OK00, OK11).
- **Minimal table (p. 25)**: Table 9-4 has five states INIT, A0, A1, OK0, OK1; Z=1 in OK0 and OK1.
- **State assignment (p. 26-28)**: Table 9-5 offers four codes for the five states: simplest (3 bits, INIT=000, A0=001, A1=010, OK0=011, OK1=100), decomposed, one-hot (5 bits) and almost one-hot (4 bits). Fig. 9-20 adjacency diagram guides the choice so neighbouring states differ by one bit. Table 9-6 transition/excitation table for the decomposed assignment (INIT=000, A0=100, A1=101, OK0=110, OK1=111), giving $D_1 D_2 D_3$.
- **T-Bird tail lights (p. 29-34)**: Fig. 9-22 and 9-23 flashing sequences for left turn (LA, then LB, then LC) and right turn (RA, RB, RC); in hazard mode all lights are on or off. Fig. 9-24 initial state diagram with output equations such as $LA = L1 + L2 + L3 + LR3$; Fig. 9-25 corrected diagram. Table 9-7 assignment: IDLE=000, L1=001, L2=011, L3=010, R1=101, R2=111, R3=110, LR3=100. Table 9-8 lists transitions, with IDLE going to L1 on `LEFT * HAZ' * RIGHT'`, to R1 on `RIGHT * HAZ' * LEFT'`, to LR3 on `HAZ + LEFT * RIGHT`, and staying otherwise.
- **Verilog state machine (p. 35-36)**: Fig. 9-30 shows the style: a combinational next-state block, a D flip-flop state register and a combinational output block. Module `VrSMex(CLOCK, A, B, Z)` declares `reg [2:0] Sreg, Snext` with `parameter [2:0] INIT = 3'b000, A0 = 3'b001, A1 = 3'b010, OK0 = 3'b011, OK1 = 3'b100`; `always @(posedge CLOCK) Sreg <= Snext;` for the state memory; a `case (Sreg)` block for next-state logic; and a second `case (Sreg)` that sets `Z = 0` in INIT, A0, A1 and `Z = 1` in OK0, OK1. See [[Verilog]].

## Key results
> [!definition] One-hot and almost one-hot
> One flip-flop per state (5 for INIT, A0, A1, OK0, OK1); almost one-hot drops the flip-flop for the reset state (4).
> (source: 10_12.pdf, Table 9-5)

> [!example] Verilog template for a Moore machine
> State register: `always @(posedge CLOCK) Sreg <= Snext;`
> Next state: `always @(A, B, Sreg) case (Sreg) ...`
> Output: `always @(Sreg) case (Sreg) ...`

**Connections**: continues [[ECE270 week 07 10_05 - Finite state machines]]; uses `case` and `always` from [[ECE270 week 05 09_19 - Verilog behavior and test benches]]. Next: [[ECE270 week 09 10_17 - State minimization and encoding]].

**Sources**: `ECE 27000/week 08/10_12.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Finite state machine]] · [[Verilog]] · [[Latches and flip-flops]] · [[Sequential logic]] · [[Karnaugh map]]
