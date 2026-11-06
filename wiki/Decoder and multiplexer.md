---
type: concept
area: digital
areas: [digital]
source-ref: "ECE 270 lectures 09_21, 11_07 (Wakerly ch. 6, 7)"
tags: [digital-logic]
---

# Decoder and multiplexer

**Summary**: Decoders select one of $2^n$ outputs from an n-bit code; multiplexers select one of several inputs; encoders and priority encoders do the reverse of a decoder.

## Decoder
- n inputs and $2^n$ outputs, one asserted when enabled (Fig. 6-14, Table 6-3; logic in Fig. 6-15).
$$Y_i = EN \cdot (\text{input code} = i)$$
> [!definition] Binary decoder
> n inputs, $2^n$ outputs, one output asserted per input code when enabled. The 2-to-4 decoder is two inverters and four 3-input ANDs sharing EN (Fig. 6-15); with EN = 0 all outputs are 0.
> (source: 09_21.pdf, p. 2-6)

- Cascading: it is electrically difficult to have a gate with many inputs or outputs, so wide decoders use several levels (Fig. 6-19). The 8-to-3 binary encoder is three OR gates (Fig. 6-24). (source: 09_21.pdf, p. 9, 13)
- Applications: choose one of four USB ports, pick a memory module from an address (Figs. 6-12, 6-13). (source: 09_21.pdf, p. 2-5)
- Memory decoding example: a 40-bit address reaches 1 TB; 4 GB uses 32 of the bits, and the upper address bits drive 2-to-4 and 3-to-8 decoders that choose a chip. Wiki note: the slide arithmetic is summarized, not reproduced. (source: 09_21.pdf, p. 4-6)
- 74x138 3-to-8 decoder with enables G1, G2A_L, G2B_L and active-low outputs (Table 6-4); a 5-to-32 decoder uses several of them (Fig. 6-19). (source: 09_21.pdf, p. 7-9)

## Encoder
- Binary encoder: $2^n$ inputs, n outputs, assumes exactly one active input. (source: 09_21.pdf, p. 13)
- Priority encoder: highest asserted request wins. Inputs H7..H0 produce a binary code A2, A1, A0 plus IDLE (Table 7-2 style). (source: 09_21.pdf, p. 26-29)
$$A_2 = H_4 + H_5 + H_6 + H_7$$
$$IDLE = (I_0 + I_1 + \dots + I_7)'$$
- Intermediate terms $H_7 = I_7$, $H_6 = I_6 I_7'$, $H_5 = I_5 I_6' I_7'$, ..., $H_0 = I_0 I_1' \cdots I_7'$; the outputs are
$$A_2 = H_4 + H_5 + H_6 + H_7$$
$$A_1 = H_2 + H_3 + H_6 + H_7$$
$$A_0 = H_1 + H_3 + H_5 + H_7$$
(source: 09_21.pdf, p. 27)

> [!example] Why loops give priority (p. 29)
> In `Vr8inprior3` the `for` loop starts at $j = 0$ and each true `I[j]` overwrites `A`; the last (highest) true index remains, which implements priority.
> (source: 09_21.pdf, p. 29)
- Cascadable priority encoder (Fig. 7-12): enable input EI, group signal GS and enable output EO let several chips form a wider encoder. (source: 09_21.pdf, p. 28-29)

## Multiplexer
- Selects one of several signals; built from a decoder plus switches, transmission gates, gates, or trees (Figs. 6-26 to 6-30). Output buffers raise signal strength. (source: 09_21.pdf, p. 14-20)
- A bus can be driven by a mux and received by a demultiplexer (Fig. 6-34). (source: 09_21.pdf)
- Barrel shifters are built from multiplexers. See [[Adders and arithmetic circuits]]. (source: 11_07.pdf, p. 5-8)

## In Verilog
- Structural (`Vr2to4dec_s`), dataflow (`Vr2to4dec_d`, `assign Y0 = EN ? ... : 0;`) and behavioral (`Vr2to4dec_b1`, `case ({A1,A0})`) decoders; 8-bit 2-input mux `Vrmux2in8b_d` and 4-input `Vrmux4in8b` with `case (S)` and `default: Y = 8'bx`; priority encoder `Vr8inprior3`. See [[Verilog]]. (source: 09_21.pdf, p. 10-12, 21-25)

**Covered in**: ECE 270 09_21, 11_07 (ECE 27000/week 05/09_21.pdf, week 12/11_07.pdf)
**Sources**: `ECE 27000/week 05/09_21.pdf`, `ECE 27000/week 12/11_07.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Logic gate]]
- [[Verilog]]
- [[Counters and registers]]
- [[Adders and arithmetic circuits]]
