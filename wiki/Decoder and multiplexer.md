---
type: concept
area: digital
areas: [digital]
source-ref: "ECE 270 lecture 09_21 (Wakerly ch. 6, 7)"
tags: [digital-logic]
---

# Decoder and multiplexer

**Summary**: Decoders select one of $2^n$ outputs from an n-bit code; multiplexers select one of several inputs; encoders and priority encoders do the reverse of a decoder.

## Decoder
- n inputs and $2^n$ outputs, one asserted when enabled (Fig. 6-14, Table 6-3).
$$Y_i = EN \cdot (\text{input code} = i)$$
- Applications: choose one of four USB ports, pick a memory module from an address (Figs. 6-12, 6-13). (source: 09_21.pdf, p. 2-5)
- 74x138 3-to-8 decoder with enables G1, G2A_L, G2B_L and active-low outputs; a 5-to-32 decoder uses several of them (Fig. 6-19). (source: 09_21.pdf, p. 7-9)

## Encoder
- Binary encoder: $2^n$ inputs, n outputs, assumes exactly one active input. (source: 09_21.pdf, p. 13)
- Priority encoder: highest asserted request wins. (source: 09_21.pdf, p. 26-29)
$$A_2 = H_4 + H_5 + H_6 + H_7$$
$$IDLE = (I_0 + I_1 + \dots + I_7)'$$

## Multiplexer
- Selects one of several signals; built from a decoder plus switches, transmission gates, gates, or trees (Figs. 6-26 to 6-30). Output buffers raise signal strength. (source: 09_21.pdf, p. 14-20)
- A bus can be driven by a mux and received by a demultiplexer (Fig. 6-34). (source: 09_21.pdf)
- Barrel shifters are built from multiplexers. See [[Adders and arithmetic circuits]]. (source: 11_07.pdf, p. 5-8)

## In Verilog
- Structural, dataflow (`assign Y0 = EN ? ... : 0;`) and behavioral (`case ({A1,A0})`) decoders; mux with `case (S)` and `default: Y = 8'bx`. See [[Verilog]]. (source: 09_21.pdf, p. 10-12, 24-25)

## Where it appears
[[ECE270 week 05 09_21 - Decoders, multiplexers and encoders]], [[ECE270 week 07 10_03 - Counters and shift registers]], [[ECE270 week 12 11_07 - Shifters, multipliers and division]].

**Sources**: `ECE 27000/week 05/09_21.pdf`, `ECE 27000/week 12/11_07.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Logic gate]]
- [[Verilog]]
- [[Counters and registers]]
- [[Adders and arithmetic circuits]]
- [[ECE270 week 05 09_21 - Decoders, multiplexers and encoders]]
