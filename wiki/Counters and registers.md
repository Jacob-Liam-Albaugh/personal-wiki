---
type: concept
area: digital
areas: [digital]
source-ref: "ECE 270 lecture 10_03 (Wakerly ch. 11)"
tags: [digital-logic]
---

# Counters and registers

**Summary**: Counters step through a cycle of states; registers store several bits and, as shift registers, move them serially.

## Counters
- A counter is a state machine with one cycle of states; an n-bit binary counter counts $0$ to $2^n - 1$ and wraps. (source: 10_03.pdf, p. 2)
- Ripple counter: only the first stage sees the clock; saves energy but slow. (source: 10_03.pdf, p. 3)
- Synchronous counters: serial enable (long AND chain) versus parallel enable (shorter path). (source: 10_03.pdf, p. 4-5)
- CNTR4U inputs CLR, LD, ENT, ENP; ENT and ENP both 1 counts up. (source: 10_03.pdf, p. 6-8)
$$Q^{+} = Q + 1 \pmod{2^n}$$
- Decoded counter outputs glitch; register them. See [[Hazards]]. (source: 10_03.pdf, p. 9-11)

## Shift registers
- Serial-in or parallel-in, serial-out or parallel-out forms (Figs. 11-12 to 11-15). (source: 10_03.pdf, p. 14-18)
- Universal shift register: hold, shift right, shift left, load. (source: 10_03.pdf, p. 19-20)
- Ring counter: a single 1 circulates; the simple version has unused cycles; a self-correcting version returns every illegal state to the main cycle. (source: 10_03.pdf, p. 21-26)
- Shift in arithmetic: shift left multiplies by 2, rotate wraps bits; see [[Adders and arithmetic circuits]]. (source: 11_07.pdf, p. 2)

## In Verilog
- `Vrcntr4u`: `always @(posedge CLK)` with clear, load, count, hold branches. See [[Verilog]]. (source: 10_03.pdf, p. 12)

## Where it appears
[[ECE270 week 07 10_03 - Counters and shift registers]], [[ECE270 week 07 10_05 - Finite state machines]], [[ECE270 week 12 11_07 - Shifters, multipliers and division]].

**Sources**: `ECE 27000/week 07/10_03.pdf`, `ECE 27000/week 12/11_07.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Latches and flip-flops]]
- [[Finite state machine]]
- [[Sequential logic]]
- [[Decoder and multiplexer]]
- [[Hazards]]
- [[ECE270 week 07 10_03 - Counters and shift registers]]
