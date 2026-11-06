---
type: lecture
area: digital
areas: [digital]
course: ece270
lecture: week 05 09_21
source-ref: "ECE 27000/week 05/09_21.pdf, 30 slides (Wakerly ch. 6 and 7 figures)"
tags: [digital-logic]
---

# ECE270 week 05 09_21 - Decoders, multiplexers and encoders

**Summary**: Combinational building blocks: binary decoders (2-to-4, 74x138, cascading), their Verilog models in three styles, binary and priority encoders, and multiplexers and demultiplexers with structural and behavioral Verilog.

**File**: `ECE 27000/week 05/09_21.pdf`

---

## Topics
- **Decoder (p. 2-5)**: Fig. 6-14, a decoder maps an input code word plus enable inputs to an output code word; n input bits select one of $2^n$ outputs (usually 0 to $2^n - 1$). Table 6-3 truth table for a 2-to-4 decoder: `EN = 0` gives all outputs 0 for any $A_1 A_0$; `EN = 1` makes exactly output $Y_{A_1A_0}$ high. Applications: Fig. 6-12 selects one of four USB ports; Fig. 6-13 memory decoding (see [[ECE270 week 05 09_19 - Verilog behavior and test benches]]).
- **Logic diagram (p. 6)**: Fig. 6-15, 2-to-4 decoder with two inverters and four 3-input ANDs sharing `EN`.
- **74x138 (p. 7-8)**: Fig. 6-16 symbol with enables G1, G2A_L, G2B_L, inputs A, B, C and active-low outputs Y0_L to Y7_L; Table 6-4 truth table (exactly one output low when enabled).
- **Cascading (p. 9)**: Fig. 6-19 builds a 5-to-32 decoder from 3-to-8 decoders. Reason (slide): it is electrically difficult to have any gate with many inputs or outputs, so use multiple levels.
- **Decoder in Verilog (p. 10-12)**: structural `Vr2to4dec_s` (two `not`, four `and`, Fig. 6-21); dataflow `Vr2to4dec_d` with conditional `assign Y0 = EN ? ({A1,A0}==2'b00) : 0;` and similar; behavioral `Vr2to4dec_b1` with `always @(A0, A1, EN)`, `if (EN==0)` and `case ({A1,A0})`. See [[Verilog]].
- **Encoder (p. 13)**: Fig. 6-24, a binary encoder has $2^n$ inputs and n outputs; the 8-to-3 encoder is three OR gates. Assumes exactly one input is active.
- **Multiplexer (p. 14-20)**: a MUX selects one of several signals (Fig. 6-25 as a multi-position switch; examples: disk, network, keyboard inputs). Implementations: decoder plus switches (Fig. 6-26), CMOS transmission gates (Fig. 6-27), decoder plus gates (Fig. 6-28), 4-input from gates (Fig. 6-29), 8-input 1-bit with output buffers to increase signal strength (Fig. 6-30, Table 6-6). Fig. 6-34 a mux driving a bus and a demultiplexer receiving it.
- **Mux in Verilog (p. 24-25)**: `Vrmux2in8b_d` uses nested conditional operators with `x` default; `Vrmux4in8b` uses `always` with `if (~EN_L == 1'b0)` then `case (S)` and `default: Y = 8'bx`.
- **Priority encoder (p. 26-29)**: Fig. 7-10 a request encoder for $2^n$ requestors reports which request is asserted; Fig. 7-11 generic 8-input priority encoder with outputs A2, A1, A0 and IDLE; the highest-priority asserted input wins. Intermediate terms H7 = I7, H6 = I6 I7', H5 = I5 I6' I7', ... H0 = I0 I1' ... I7'. Fig. 7-12 and Table 7-2: cascadable version with EI, GS, EO. `Vr8inprior3` uses a `for` loop that checks low priority first so higher priority overwrites.

## Key results
> [!definition] Binary decoder
> n inputs, $2^n$ outputs, one output asserted per input code when enabled.
> $$Y_i = EN \cdot (\text{input code} = i)$$
> (source: 09_21.pdf, p. 2-5)

> [!theorem] Priority encoder outputs (Wakerly eq. as on slide p. 27)
> $$A_2 = H_4 + H_5 + H_6 + H_7$$
> $$A_1 = H_2 + H_3 + H_6 + H_7$$
> $$A_0 = H_1 + H_3 + H_5 + H_7$$
> $$IDLE = (I_0 + I_1 + \dots + I_7)'$$

> [!example] Why loops give priority (p. 29)
> The loop starts at $j = 0$ and each true `I[j]` overwrites `A`; the last (highest) true index remains, which implements priority.

**Connections**: Verilog constructs from [[ECE270 week 05 09_19 - Verilog behavior and test benches]]. Next: [[ECE270 week 06 09_28 - Latches and flip-flops]].

**Sources**: `ECE 27000/week 05/09_21.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Decoder and multiplexer]] · [[Logic gate]] · [[Verilog]] · [[Boolean algebra]] · [[CMOS logic]]
