---
type: lecture
area: digital
areas: [digital]
course: ece270
lecture: week 05 09_19
source-ref: "ECE 27000/week 05/09_19.pdf, 34 slides (Wakerly ch. 5 and 6 figures plus instructor slides)"
tags: [digital-logic]
---

# ECE270 week 05 09_19 - Verilog behavior and test benches

**Summary**: Continues Verilog: structural examples, continuous assignment, the 4-bit prime detector written three ways, procedural code (`always`, blocking vs nonblocking, `if`, `case`, loops, functions, tasks), simulated time, test benches, and a first look at decoders in chapter 6.

**File**: `ECE 27000/week 05/09_19.pdf`

---

## Topics
- **Keep it clean (p. 2)**: photos of a tidy breadboard and a tangle of wires (provided by teaching assistant Erik Duxstad); keep design and implementation clean.
- **Structural recap (p. 3-4)**: `VrInh` (BUT-NOT) and `VrSillyXOR` (Fig. 5-2) from the previous lecture.
- **Parameters and Maj (p. 5)**: module `Maj(OUT, I0, I1, I2)` with `parameter WID = 1`, vector ports `[WID-1:0]`, wires `I0I1`, `I1I2`, `I0I2`, three AND gates and an OR gate; the same function as one `assign OUT = I0 & I1 | I0 & I2 | I1 & I2;`.
- **Continuous assignment (p. 6, Table 5-17)**: `assign net = expression;`, also for a bit, a range, or a concatenation. With no delay it takes no simulated time. Do not create loops such as `assign Y = X; assign X = Y;`.
- **4-bit prime detector (p. 7-9)**: truth table for $N[3:0]$ with output true for 2, 3, 5, 7, 11, 13. The textbook treats 1 as prime (flagged on the slide, p. 7), the lecture says 1 is not prime. The K-map is redrawn and the term $N_3'N_2'N_1$ circled (p. 8); Fig. 3-24 appears again (p. 9). Two Verilog styles: `Vrprimed` with a sum-of-products `assign` and `Vrprimec` with the conditional operator `N[3] ? (...) : (...)`, drawn as a 2-input multiplexer (Fig. 5-3, p. 10-12).
- **Comment advice (p. 11)**: write comments before code; interviewers read code.
- **Always blocks (p. 13, Table 5-18)**: `always @(a or b)`, `always @(a, b)`, `always @(*)` (every signal that may change; be careful), `always @(posedge clk)`, `always @(negedge clk)`, and plain `always`.
- **Procedural assignment (p. 14, Table 5-19)**: blocking `=` and nonblocking `<=`.
- **Programming rules (p. 15)**: use blocking assignments in always blocks for combinational logic; use nonblocking for sequential logic (Wakerly section 10.3.2); do not mix them in one always block; do not assign the same variable in two always blocks.
- **Statements (p. 16-22)**: `begin ... end` with optional block name (Table 5-20), `if`, `else` (5-21), `case ... default ... endcase` (5-22), `for` (5-23), `repeat`, `while`, `forever` (5-24), `function` (5-25, no recursion), `task` (5-26, no return type, usually not synthesizable).
- **Built-in tasks (p. 23)**: `$display`, `$write`, `$monitor`, `$monitoroff`, `$fflush`, `$time`, `$random` (32-bit signed), `$stop`.
- **Time (p. 24-26)**: `#` delay specifier and `` `timescale time-unit / time-precision``. Example `` `timescale 1 ns / 100 ps`` with `assign #2 ...` and `assign #3.5 F = ...` in `Vrprimedly`. Verilog keeps an event list and a sensitivity matrix; with no delay everything happens at the same simulated time, then time advances.
- **Test benches (p. 27-31)**: `initial` runs once at time zero (Table 5-27). `Vrprime_tb1` declares `reg [3:0] Num; wire Prime;`, instantiates `Vrprimed UUT (.N(Num), .F(Prime));` and loops `for (i = 0; i <= 15; i = i+1) #10 Num = i;`. `Vrprime_tb2` adds `$write` and `$display` of "Yes" or "No" using `===` tests. Fig. 5-4 shows the waveform for 0 to 15 over 150 ns; Table 5-28 shows the first output lines (Num 0 No, 1 Yes, 2 Yes, 3 Yes, 4 No, 5 Yes; Wiki note: row for 0 and 1 as printed on the slide).
- **Synthesizable descriptions (p. 32)**: replace if-else by case; assign all outputs in all conditions; loops can be problematic.
- **Decoders preview (p. 33-34)**: Fig. 6-12 a decoder selects one of four USB ports from a 2-bit select; Fig. 6-13 memory-module decoding with a 40-bit address bus (up to 1 TB), 4 GB installed so only 32 bits needed, upper bits must be 0, a 2-to-4 decoder picks a 1 GB module and a 3-to-8 decoder picks byte enables.

## Key results
> [!definition] Blocking vs nonblocking (p. 15)
> Combinational `always`: use `=`.
> Sequential `always`: use `<=`.
> Never mix them in one block.

> [!example] Prime detector, conditional form (p. 10)
> $$F = N_3 \; ? \; (N_0 \;\&\; (N_1 \oplus N_2)) \; : \; (N_0 \;|\; (N_2' \;\&\; N_1))$$
> as read from the slide; it equals the minimized sum of products for primes 2, 3, 5, 7, 11, 13.

**Connections**: syntax from [[ECE270 week 04 09_14 - Verilog modules and combinational design]]; the K-map is from [[ECE270 week 03 09_07 - Circuit analysis and Karnaugh maps]]. Continues in [[ECE270 week 05 09_21 - Decoders, multiplexers and encoders]].

**Sources**: `ECE 27000/week 05/09_19.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Verilog]] · [[Karnaugh map]] · [[Decoder and multiplexer]] · [[Timing diagram]] · [[Logic gate]]
