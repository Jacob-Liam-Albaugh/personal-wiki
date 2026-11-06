---
type: concept
area: digital
areas: [digital]
source-ref: "ECE 270 lectures 09_12 to 11_02 (Wakerly ch. 5, 10, 12)"
tags: [digital-logic]
---

# Verilog

**Summary**: The hardware description language used in ECE 270: modules built from continuous assignments, gate instances and always blocks, simulated with test benches.

## Modules and ports
- A module has ports and concurrent statements: `module VrInhibit(X, Y, Z); input X, Y; output Z; assign Z = X & ~Y; endmodule`. One module per file, same name as the file. (source: 09_12.pdf, p. 24-28; 09_14.pdf, p. 2-7)
- Four logic values: 0, 1, x (unknown), z (high impedance). (source: 09_14.pdf, p. 5)

## Data and operators
- `wire` is a connection; `reg` stores bits and is not necessarily a flip-flop; `integer` is 32-bit two's complement. (source: 09_14.pdf, p. 8-11)
- Literals `n'Bddd`, for example `8'h07`, `4'b1zz`. (source: 09_14.pdf, p. 12)
- Bitwise `& | ^ ~`, logical `&& || !`, reduction `&Zbus`, concatenation `{}`, conditional `? :`. A multi-bit value is false only if all bits are 0. (source: 09_14.pdf, p. 6, 16-20)
- When precedence is unclear, add parentheses. (source: 09_14.pdf, p. 20)

## Three styles
- Structural: instantiate gates and modules, statements run concurrently in any order. (source: 09_14.pdf, p. 24-29)
- Dataflow: `assign net = expression;`. (source: 09_19.pdf, p. 6)
- Behavioral: `always @(...)` with `if`, `case`, `for`. (source: 09_19.pdf, p. 13-22)

## Rules for always blocks
- Blocking `=` for combinational logic, nonblocking `<=` for sequential logic; do not mix them in one block or drive a variable from two blocks. (source: 09_19.pdf, p. 15)
- For synthesis assign all outputs in all branches and prefer `case` to long `if-else`. (source: 09_19.pdf, p. 32)

## Test benches
- A module with no ports, a unit under test, a clock block, and an `initial` block applying vectors. A `task` can check outputs and `$display` errors. (source: 09_19.pdf, p. 27-31; 10_24.pdf, p. 7-10)

## Design patterns
- State machine: state register, next-state `case`, output `case`; see [[Finite state machine]]. (source: 10_12.pdf, p. 35-36)
- Adder: `assign {COUT, S} = A + B + CIN;`; see [[Adders and arithmetic circuits]]. (source: 11_02.pdf, p. 16)
- Decoder and multiplexer: see [[Decoder and multiplexer]].

## Where it appears
[[ECE270 week 04 09_14 - Verilog modules and combinational design]], [[ECE270 week 05 09_19 - Verilog behavior and test benches]], [[ECE270 week 08 10_12 - State machine design and Verilog]], [[ECE270 week 10 10_24 - Verilog state machines and test benches]], [[ECE270 week 11 11_02 - Adders, ALUs and shifters]], [[ECE270 week 12 11_07 - Shifters, multipliers and division]].

**Sources**: `ECE 27000/week 04/09_12.pdf`, `ECE 27000/week 04/09_14.pdf`, `ECE 27000/week 05/09_19.pdf`, `ECE 27000/week 08/10_12.pdf`, `ECE 27000/week 10/10_24.pdf`, `ECE 27000/week 11/11_02.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Logic gate]]
- [[Boolean algebra]]
- [[Finite state machine]]
- [[Decoder and multiplexer]]
- [[Latches and flip-flops]]
- [[Adders and arithmetic circuits]]
- [[Timing diagram]]
- [[ECE270 week 04 09_14 - Verilog modules and combinational design]]
- [[ECE270 week 05 09_19 - Verilog behavior and test benches]]
