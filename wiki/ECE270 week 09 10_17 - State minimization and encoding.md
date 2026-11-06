---
type: lecture
area: digital
areas: [digital]
course: ece270
lecture: week 09 10_17
source-ref: "ECE 27000/week 09/10_17.pdf, 25 slides (instructor slides plus Wakerly ch. 9 and 12 figures)"
tags: [digital-logic]
---

# ECE270 week 09 10_17 - State minimization and encoding

**Summary**: Links state machines to regular expressions, shows how to detect a pattern with a Moore machine, how to merge equivalent states (by diagram and by table), how many ways there are to encode states, then reviews the T-Bird and detector examples and the Verilog state machine structure, including pipelined outputs.

**File**: `ECE 27000/week 09/10_17.pdf`

---

## Topics
- **Regular expressions (p. 2)**: state machines and regular expressions are "equivalent". Over an alphabet such as {0, 1}: $\epsilon$ is the terminal symbol; `L1 or L2` is an option; `L1 L2` is concatenation; `L*` repeats 0 or more times; `L+` repeats 1 or more times. Examples: `0`, `001`, `0*`, `1+0`, `1+01*`.
- **Pattern detector (p. 3-4)**: a machine for `0*1+0+1(0 or 1)*` has states S1 to S4; S1 loops on 0 and moves to S2 on 1; S2 loops on 1 and moves to S3 on 0; S3 loops on 0 and moves to S4 on 1; S4 loops on 0 and 1. As a Moore machine the output is 1 only in S4. State table: S1 (0: S1, 1: S2), S2 (S3, S2), S3 (S3, S4), S4 (S4, S4).
- **Problematic machines (p. 5)**: a state with two different next states for the same input, or with no next state for some input, is not a valid deterministic machine.
- **Merging equivalent states by diagram (p. 6-9)**: an example (credited on the slide to a wustl.edu course page) with states S0 to S4 and 3-bit input labels 100, 010, 001. States with the same output and the same transitions into the same groups merge: first {S0, S1, S3} vs {S2, S4}, then split further until the groups are consistent, leaving S0, then {S1, S3}, then {S2, S4}.
- **Merging by state table (p. 10-13)**: table with states A to F and input x. Rows with different outputs cannot merge, so A and B stay apart. Start with groups {A, C, E} (output 1 when x=1) and {B, D, F} (output 0 when x=1), then refine when next states fall in different groups: {A, C, E}, {B, D}, {F}, then {A, C}, {E}, {B, D}, {F}.
- **Encoding states (p. 14)**: with n bits there are $2^n$ codes; choosing which k to use gives
  $$C(2^n, k) = \frac{(2^n)!}{k!\,(2^n - k)!}$$
  For 3 bits and 4 states, $C(8, 4) = 70$ (the slide counts subsets of codes, not their assignments to states).
- **T-Bird recap (p. 15-19)**: Fig. 9-22 to 9-25, Table 9-7 and Table 9-8; state assignment IDLE=000, L1=001, L2=011, L3=010, R1=101, R2=111, R3=110, LR3=100. See [[ECE270 week 08 10_12 - State machine design and Verilog]].
- **Detector recap (p. 20-21)**: the two-input problem (output Z is 1 if A matched its value at the two previous ticks, or B has been 1 since then); Table 12-1 state and output table for INIT, A0, A1, OK0, OK1.
- **Verilog structure (p. 22-25)**: Fig. 9-30 Moore structure from the Verilog style; Fig. 12-2 a variant with pipelined outputs, where the output logic reads `Snext` and an output register `always @(posedge CLOCK) Z <= Zn;` delays the output by one clock; and the full module `VrSMex`. See [[Verilog]].

## Key results
> [!definition] Equivalent states
> Two states can merge if they give the same outputs and, for every input, go to states in the same group.
> (source: 10_17.pdf, p. 10-13)

> [!example] Pipelined output (p. 23)
> $$Z \leftarrow Zn \quad \text{at each clock edge}$$
> $Zn$ is decoded from $Snext$, so Z is registered and glitch-free.

> [!warning] Counting codes
> Wiki note: the slide's $C(8,4) = 70$ counts which four of the eight 3-bit codes are used. Assigning them to specific states multiplies this by $4!$.

**Connections**: builds on [[ECE270 week 07 10_05 - Finite state machines]] and [[ECE270 week 08 10_12 - State machine design and Verilog]]. Next: [[ECE270 week 10 10_24 - Verilog state machines and test benches]].

**Sources**: `ECE 27000/week 09/10_17.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Finite state machine]] · [[Verilog]] · [[Sequential logic]] · [[Latches and flip-flops]]
