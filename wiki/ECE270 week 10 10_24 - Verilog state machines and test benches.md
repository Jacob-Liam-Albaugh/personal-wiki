---
type: lecture
area: digital
areas: [digital]
course: ece270
lecture: week 10 10_24
source-ref: "ECE 27000/week 10/10_24.pdf, 26 slides (Wakerly ch. 12 figures plus instructor slides)"
tags: [digital-logic]
---

# ECE270 week 10 10_24 - Verilog state machines and test benches

**Summary**: Wakerly chapter 12: the Verilog structure of a Moore machine, adding a reset, writing a test bench with a task, then three complete Verilog machines (a counting machine, the T-Bird tail lights, and a traffic-light controller).

**File**: `ECE 27000/week 10/10_24.pdf`

---

## Topics
- **Verilog structure (p. 2-5)**: Fig. 12-1 Moore structure from the coding style: next-state `always @(A, B, Sreg)` with `case (Sreg)`, a state memory `always @(posedge CLOCK) Sreg <= Snext;` and an output `always @(Sreg)` block. Same detector problem as the previous lecture (Table 12-1, Fig. 12-2 pipelined outputs, module `VrSMex`). See [[ECE270 week 09 10_17 - State minimization and encoding]].
- **Add reset (p. 6)**: synchronous active-high reset: `always @(posedge CLOCK) if (RESET==1) Sreg <= INIT; else Sreg <= Snext;`. Asynchronous reset adds the reset to the sensitivity list: `always @(posedge CLOCK or posedge RESET)`.
- **Test bench steps (p. 7)**: (1) declare a module with no inputs or outputs; (2) instantiate the unit under test (UUT); (3) an `always` block for a free-running clock; (4) statements to initialize the UUT, apply test vectors each clock tick, and check outputs.
- **Test bench example (p. 8-9)**: `VrSMex_tbv` uses `` `timescale 1ns/100ps``, 10 ns clock with a small offset, `Aseq` and `Bseq` 30-bit constants shifted one bit per tick in a `for` loop, a 115 ns reset, and `$stop(1)` at the end. Fig. 12-3 shows the waveforms of Tclk, RST, A, B and Z over about 400 ns.
- **Self-checking test (p. 10)**: `VrSMex_tb` defines a `task checkZ` that applies inputs, waits, and prints an error with `$display` if Z differs from the expected value, then calls it step by step for each case (two 1s in a row, B=1 should hold Z=1, B=0 releases, and so on). Slide 12: separate test code from production code, treat the production code as a black box, no excessive print statements in production code; "if the internal cannot be observed by the test code, does that really matter?"
- **Counting machine (p. 13-15)**: design a clocked machine with inputs X and Y and output Z that is 1 if the number of 1 inputs since reset is a multiple of 4. Module `VronescntSM`: `reg [1:0] Q, Qnext;` synchronous reset; next state `if (X & Y) Qnext = Q + 2; else if (X | Y) Qnext = Q + 1; else Qnext = Q;`; output `if (Q==0) Z = 1; else Z = 0;`.
- **T-Bird tail lights (p. 16-22)**: Fig. 12-5 and 12-6 as in earlier lectures, Fig. 9-25 corrected diagram, Tables 9-7 and 9-8. Module `VrTbirdSM` has inputs CLOCK, RESET, LEFT, RIGHT, HAZ and outputs LA, LB, LC, RA, RB, RC; parameters IDLE=3'b000, L1=3'b001, L2=3'b011, L3=3'b010, R1=3'b101, R2=3'b111, R3=3'b110, LR3=3'b100. Asynchronous reset to IDLE; IDLE goes to LR3 if `HAZ | (LEFT & RIGHT)`, to R1 if RIGHT, to L1 if LEFT; the output block assigns the concatenation `{LC,LB,LA,RA,RB,RC}`, for example IDLE `6'b000000` and LR3 `6'b111111`; unused states give all off.
- **Traffic light (p. 23-26)**: Fig. 12-7 an intersection in Sunnyvale, California with north-south and east-west sensors and lights. Module `Vrsvale` has inputs CLOCK, RESET, NSCAR, EWCAR, TMSHORT, TMLONG and outputs for red, yellow, green per direction plus TMRESET; states NSGO=000, NSWAIT=001, NSWAIT2=010, NSDELAY=011, EWGO=100, EWWAIT=101, EWWAIT2=110, EWDELAY=111. In NSGO the machine stays while `~TMSHORT` (minimum 5 seconds), leaves when `TMLONG` (maximum 5 minutes), makes an east-west car wait if only it is present, and changes when cars arrive both ways or only a new north-south car; yellow lasts two ticks (WAIT, WAIT2), then a delay state with red both ways. The default (unused) state goes to NSDELAY as a "reset" state. Outputs are `assign` statements on `Sreg`, and `TMRESET` is 1 in NSWAIT2 or EWWAIT2.

## Key results
> [!definition] Synchronous vs asynchronous reset
> Synchronous: reset checked only on the clock edge.
> Asynchronous: reset also in the sensitivity list, acts at once.
> (source: 10_24.pdf, p. 6)

> [!example] Three-part Verilog machine
> State memory (`<=`, clocked), next-state logic (combinational `case`), output logic (combinational). Defaulting unused states to a safe state avoids latches and lockups.

**Connections**: Verilog constructs from [[ECE270 week 05 09_19 - Verilog behavior and test benches]]; the machines are those of [[ECE270 week 08 10_12 - State machine design and Verilog]]. Next: [[ECE270 week 10 10_26 - Verilog examples and two's complement]].

**Sources**: `ECE 27000/week 10/10_24.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Finite state machine]] · [[Verilog]] · [[Sequential logic]] · [[Timing diagram]]
