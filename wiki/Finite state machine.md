---
type: concept
area: digital
areas: [digital]
source-ref: "ECE 270 lectures 10_05, 10_12, 10_17, 10_24, 11_09 (Wakerly ch. 9, 12)"
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
- Moore outputs change after the clock edge; Mealy outputs can change when inputs change. (source: 10_05.pdf, p. 15)

## Design steps (nine)
1. State and output tables, 2. minimize, 3. assign states, 4. transition and output tables, 5. choose flip-flops, 6. excitation table, 7. excitation equations, 8. output equations, 9. logic diagrams. (source: 10_05.pdf, p. 21)

## State minimization and encoding
- States merge when outputs match and, for every input, next states fall in the same group. (source: 10_17.pdf, p. 6-13)
- Encodings offered for five states: 3-bit simplest, decomposed, one-hot (5 bits), almost one-hot (4 bits). (source: 10_12.pdf, p. 26-28)
- With n bits there are $2^n$ codes; choosing k of them gives $C(2^n, k)$ subsets. (source: 10_17.pdf, p. 14)

## In Verilog
- Three parts: state register `always @(posedge CLOCK) Sreg <= Snext;`, a `case (Sreg)` next-state block, and a second block for outputs. See [[Verilog]]. (source: 10_12.pdf, p. 35-36)
- Synchronous reset checks RESET on the clock edge; asynchronous reset adds it to the sensitivity list. (source: 10_24.pdf, p. 6)

## Examples in the lectures
- Seasons, morning routine, 4-state enable counter, two-input detector, T-Bird tail lights, traffic light, guessing game. (source: 10_05.pdf, p. 2-7; 10_12.pdf, p. 19-34; 10_26.pdf, p. 13-14)
- Counters and ring counters are state machines with one cycle of states. See [[Counters and registers]].
- Beyond hardware: robots, ticketing, ecology; a table can be read as a matrix. (source: 11_09(1).pdf, p. 2-8)

Wiki note: the slides treat regular expressions and state machines as equivalent; only the examples are shown, not the theorem. (source: 10_17.pdf, p. 2)

**Sources**: `ECE 27000/week 07/10_05.pdf`, `ECE 27000/week 08/10_12.pdf`, `ECE 27000/week 09/10_17.pdf`, `ECE 27000/week 10/10_24.pdf`, `ECE 27000/week 12/11_09(1).pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Sequential logic]]
- [[Latches and flip-flops]]
- [[Counters and registers]]
- [[Verilog]]
- [[Timing diagram]]
- [[ECE270 week 07 10_05 - Finite state machines]]
- [[ECE270 week 08 10_12 - State machine design and Verilog]]
- [[ECE270 week 09 10_17 - State minimization and encoding]]
- [[ECE270 week 10 10_24 - Verilog state machines and test benches]]
- [[ECE270 week 12 11_09 - State machine applications]]
