---
type: concept
area: digital
areas: [digital]
source-ref: "ECE 270 lectures 09_12 to 11_07 (Wakerly ch. 5, 10, 12)"
tags: [digital-logic]
---

# Verilog

**Summary**: The hardware description language used in ECE 270: modules built from continuous assignments, gate instances and always blocks, simulated with test benches.

## Modules and ports
- A module has ports and concurrent statements: `module VrInhibit(X, Y, Z); input X, Y; output Z; assign Z = X & ~Y; endmodule`. One module per file, same name as the file. (source: 09_12.pdf, p. 24-28; 09_14.pdf, p. 2-7)
- ANSI-style port declarations put direction and type in the module header. (source: 09_14.pdf, p. 3-7)
- Four logic values: 0, 1, x (unknown), z (high impedance). (source: 09_14.pdf, p. 5)

## Data and operators
- `wire` is a connection; `reg` stores bits and is not necessarily a flip-flop; `integer` is 32-bit two's complement. The slides tabulate the net types. (source: 09_14.pdf, p. 8-11)
- Literals `n'Bddd`, for example `8'h07`, `4'b1zz`. (source: 09_14.pdf, p. 12)
- Parameters give constants such as a width `WID` (module `Maj` with parameter width); vectors `[n-1:0]`, concatenation `{}` and replication `{n{x}}`. (source: 09_14.pdf, p. 13-15)
- Arithmetic `+ - * / %`, shifts `<< >>`, bitwise `& | ^ ~`, logical `&& || !`, reduction `&Zbus`, relational, conditional `? :`, and case-equality `===` (compares x and z). Arrays are declared as `reg [7:0] mem [0:15]`. A multi-bit value is false only if all bits are 0. (source: 09_14.pdf, p. 6, 16-20)
- When precedence is unclear, add parentheses. (source: 09_14.pdf, p. 20)
- `` `include `` and `` `define `` are compiler directives. (source: 09_14.pdf)

## Three styles
- Structural: instantiate gates and modules, statements run concurrently in any order. Built-in gates are `and nand or nor xor xnor buf not` and tristate `bufif0 bufif1 notif0 notif1`; instances use positional or named port connections. Examples: `VrAlarmCkt`, `VrInh`, `VrSillyXOR`. (source: 09_14.pdf, p. 23-29)
- Dataflow: `assign net = expression;`; the right side re-evaluates whenever an operand changes. (source: 09_19.pdf, p. 6)
- Behavioral: `always @(...)` with `if`, `case`, `for`. (source: 09_19.pdf, p. 13-22)

> [!example] Prime detector in three styles
> `Vrprimed` (dataflow sum of products from the [[Karnaugh map]]) and `Vrprimec` (the conditional operator or a `case`) detect primes among 4-bit inputs; the structural version instantiates gates for the same equation. (source: 09_19.pdf, p. 6-12)

> [!example] Smallest Verilog module (p. 26)
> $$Z = X \cdot Y'$$
> written as `assign Z = X & ~Y;` in module `VrInhibit` (also called BUT-NOT). (source: 09_12.pdf, p. 26)

> [!example] Alarm circuit in Verilog (p. 27)
> $$ALARM = PANIC + ENABLE \cdot EXITING' \cdot SECURE'$$
> $$SECURE = WINDOW \cdot DOOR \cdot GARAGE$$
> becomes five gate instances (U1 to U5) joined by wires `secure`, `notsecure`, `notexiting`, `otheralarm`. (source: 09_14.pdf, p. 27)

> [!definition] Concurrency
> Verilog statements in a module describe hardware that all runs at once; order in the file carries no meaning for these statements.
> (source: 09_14.pdf, p. 27)

> [!example] Prime detector, conditional form (p. 10)
> $$F = N_3 \; ? \; (N_0 \;\&\; (N_1 \oplus N_2)) \; : \; (N_0 \;|\; (N_2' \;\&\; N_1))$$
> drawn as a 2-input multiplexer (Fig. 5-3); it equals the minimized sum of products for primes 2, 3, 5, 7, 11, 13. (source: 09_19.pdf, p. 10-12)

> [!definition] Blocking vs nonblocking (p. 15)
> Combinational `always`: use `=`. Sequential `always`: use `<=`. Never mix them in one block.
> (source: 09_19.pdf, p. 15)

## Rules for always blocks
- Blocking `=` for combinational logic, nonblocking `<=` for sequential logic; do not mix them in one block or drive a variable from two blocks. (source: 09_19.pdf, p. 15)
- For synthesis assign all outputs in all branches and prefer `case` to long `if-else`; an unassigned branch infers a latch. (source: 09_19.pdf, p. 32)
- Time and delays: `` `timescale ``, `#delay` and built-in tasks `$display`, `$monitor`, `$stop`, `$finish` are for simulation only. (source: 09_19.pdf, p. 23-26)

## Test benches
- A module with no ports, a unit under test, a clock block, and an `initial` block applying vectors (`Vrprime_tb1`, `Vrprime_tb2`). A `task` can check outputs and `$display` errors. (source: 09_19.pdf, p. 27-31; 10_24.pdf, p. 7-10)
- Practices: keep test code separate from production code, check results automatically rather than by eye, and exercise every case. (source: 10_24.pdf, p. 7-10)

## Design patterns
- State machine template `VrSMex`: state register `always @(posedge CLOCK) Sreg <= Snext;`, a next-state `case`, and an output `case`; a pipelined output (Fig. 12-2) adds an output register. See [[Finite state machine]]. (source: 10_12.pdf, p. 35-36; 10_24.pdf, p. 2-6)
> [!definition] Synchronous vs asynchronous reset
> Synchronous: `always @(posedge CLOCK) if (RESET==1) Sreg <= INIT; else Sreg <= Snext;` checks reset only on the clock edge. Asynchronous: `always @(posedge CLOCK or posedge RESET)` acts at once.
> (source: 10_24.pdf, p. 6)

> [!example] Verilog template for a Moore machine
> State register: `always @(posedge CLOCK) Sreg <= Snext;`
> Next state: `always @(A, B, Sreg) case (Sreg) ...`
> Output: `always @(Sreg) case (Sreg) ...`
> Three parts: state memory (`<=`, clocked), next-state logic and output logic (combinational). Defaulting unused states to a safe state avoids latches and lockups. `VrSMex` declares `reg [2:0] Sreg, Snext` with `parameter [2:0] INIT = 3'b000, A0 = 3'b001, A1 = 3'b010, OK0 = 3'b011, OK1 = 3'b100`; the output block sets `Z = 0` in INIT, A0, A1 and `Z = 1` in OK0, OK1. (source: 10_12.pdf, p. 35-36; 10_24.pdf, p. 2-5)

- Test bench `VrSMex_tbv`: `` `timescale 1ns/100ps``, 10 ns clock, 30-bit constants `Aseq` and `Bseq` shifted one bit per tick, a 115 ns reset, `$stop(1)` at the end (Fig. 12-3). Self-checking `VrSMex_tb` defines `task checkZ` that applies inputs, waits and `$display`s an error if Z differs from expected. (source: 10_24.pdf, p. 8-10)
- `VronescntSM` (Z=1 when the count of 1 inputs since reset is a multiple of 4): `reg [1:0] Q, Qnext;` next state `if (X & Y) Qnext = Q + 2; else if (X | Y) Qnext = Q + 1; else Qnext = Q;`, output `Z = (Q==0)`. (source: 10_24.pdf, p. 13-15)
- `VrTbirdSM`: parameters IDLE=3'b000, L1=3'b001, L2=3'b011, L3=3'b010, R1=3'b101, R2=3'b111, R3=3'b110, LR3=3'b100; asynchronous reset to IDLE; IDLE goes to LR3 if `HAZ | (LEFT & RIGHT)`, to R1 if RIGHT, to L1 if LEFT; outputs are the concatenation `{LC,LB,LA,RA,RB,RC}` (IDLE `6'b000000`, LR3 `6'b111111`). (source: 10_24.pdf, p. 16-22)
- `Vrsvale` traffic light (Sunnyvale): states NSGO=000, NSWAIT=001, NSWAIT2=010, NSDELAY=011, EWGO=100, EWWAIT=101, EWWAIT2=110, EWDELAY=111; stays in NSGO while `~TMSHORT` (5 s minimum), leaves on `TMLONG` (5 min maximum) or when cars wait the other way; yellow lasts two ticks, then a delay state with red both ways; unused states go to NSDELAY; `TMRESET` is 1 in NSWAIT2 or EWWAIT2. (source: 10_24.pdf, p. 23-26)
- Test benches `VrSMex_tbv` and `VrSMex_tb` (with `task checkZ`), and machines `VronescntSM`, `VrTbirdSM`, `Vrsvale` (traffic light), `Vrggameoc` (guessing game). (source: 10_24.pdf, p. 7-20)
- Counter `Vrcntr4u`; see [[Counters and registers]]. (source: 10_03.pdf, p. 12)
- `VrDlatch` and `VrDff`; see [[Latches and flip-flops]]. (source: 09_28(2).pdf, p. 25)
- Adder: `assign {COUT, S} = A + B + CIN;`; see [[Adders and arithmetic circuits]]. (source: 11_02.pdf, p. 16)
- Decoder, mux and priority encoder: see [[Decoder and multiplexer]].
- Two's complement examples in Verilog: see [[Number systems and codes]]. (source: 10_26.pdf)

**Covered in**: ECE 270 09_12, 09_14, 09_19, 09_21, 09_28, 10_03, 10_12, 10_24, 10_26, 11_02 (courses/ECE 270/week 04/09_12.pdf, week 04/09_14.pdf, week 05/09_19.pdf, week 05/09_21.pdf, week 06/09_28(2).pdf, week 07/10_03.pdf, week 08/10_12.pdf, week 10/10_24.pdf, week 10/10_26.pdf, week 11/11_02.pdf)
**Sources**: `courses/ECE 270/week 04/09_12.pdf`, `courses/ECE 270/week 04/09_14.pdf`, `courses/ECE 270/week 05/09_19.pdf`, `courses/ECE 270/week 05/09_21.pdf`, `courses/ECE 270/week 06/09_28(2).pdf`, `courses/ECE 270/week 07/10_03.pdf`, `courses/ECE 270/week 08/10_12.pdf`, `courses/ECE 270/week 10/10_24.pdf`, `courses/ECE 270/week 10/10_26.pdf`, `courses/ECE 270/week 11/11_02.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Logic gate]]
- [[Boolean algebra]]
- [[Karnaugh map]]
- [[Finite state machine]]
- [[Decoder and multiplexer]]
- [[Latches and flip-flops]]
- [[Adders and arithmetic circuits]]
- [[Counters and registers]]
- [[Number systems and codes]]
- [[Timing diagram]]
