---
type: concept
area: digital
areas: [digital]
source-ref: "ECE 270 lectures 10_03, 11_07 (Wakerly ch. 11)"
tags: [digital-logic]
---

# Counters and registers

**Summary**: Counters step through a cycle of states; registers store several bits and, as shift registers, move them serially.

## Counters
- A counter is a state machine with one cycle of states; an n-bit binary counter counts $0$ to $2^n - 1$ and wraps. Variants: binary, decade, excess-3, up/down. (source: 10_03.pdf, p. 2)
- Ripple counter: only the first stage sees the clock; saves energy but slow. (source: 10_03.pdf, p. 3)
- Synchronous counters: serial enable (long AND chain) versus parallel enable (shorter path). (source: 10_03.pdf, p. 4-5)
- CNTR4U (Table 11-1) inputs CLR, LD, ENT, ENP; ENT and ENP both 1 counts up; RCO goes high at count 15. Divide-by-16 waveforms show the lowest bit at half the clock rate and so on. (source: 10_03.pdf, p. 6-8)
> [!definition] Synchronous binary counter
> $$Q^{+} = Q + 1 \pmod{2^n}\quad \text{when enabled}$$
> All flip-flops share one clock; enable logic decides which toggle. Fig. 11-3 serial enable has a long AND chain; Fig. 11-4 parallel enable is shorter.
> (source: 10_03.pdf, Fig. 11-3 to 11-5, Table 11-1)
- Decoded counter outputs glitch because several bits change at once; register the decoded outputs (Figs. 11-9, 11-10). See [[Hazards]]. (source: 10_03.pdf, p. 9-11)

## Shift registers
- Serial-in or parallel-in, serial-out or parallel-out forms (Figs. 11-12 to 11-15). (source: 10_03.pdf, p. 14-18)
- Universal shift register SHRG4U (Table 11-2): S1S0 = 00 hold, 01 shift right, 10 shift left, 11 parallel load. (source: 10_03.pdf, p. 19-20)
- Ring counter: a single 1 circulates; the simple version has unused cycles; a self-correcting version returns every illegal state to the main cycle. (source: 10_03.pdf, p. 21-26)
- Shift in arithmetic: shift left multiplies by 2, rotate wraps bits; see [[Adders and arithmetic circuits]]. (source: 11_07.pdf, p. 2)

## In Verilog
- `Vrcntr4u`: `always @(posedge CLK)` with clear, load, count, hold branches. See [[Verilog]]. (source: 10_03.pdf, p. 12)

**Covered in**: ECE 270 10_03, 11_07 (ECE 27000/week 07/10_03.pdf, week 12/11_07.pdf)
**Sources**: `ECE 27000/week 07/10_03.pdf`, `ECE 27000/week 12/11_07.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Latches and flip-flops]]
- [[Finite state machine]]
- [[Sequential logic]]
- [[Decoder and multiplexer]]
- [[Hazards]]
