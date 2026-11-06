---
type: concept
area: digital
areas: [digital]
source-ref: "ECE 270 lectures 08_31, 09_28, 10_03, 10_05, 10_17 (Wakerly ch. 9, 10)"
tags: [digital-logic]
---

# Sequential logic

**Summary**: Logic whose output depends on past inputs as well as current ones, so it has memory; in ECE 270 this means clocked circuits built from flip-flops.

## Combinational versus sequential
- Combinational output depends only on current inputs (chess, go). Sequential output depends on inputs and previous output (Monopoly), so outputs feed back. (source: 08_31.pdf, p. 3-4)
- Adding a clock block coordinates the other blocks; the clock is a square wave (0 to 5 V in the example). (source: 09_28(2).pdf, p. 2-5)

## Memory elements
- Bistable element: two inverters feeding each other, with two stable points and one metastable point. (source: 09_28(2).pdf, p. 6-9)
- S-R latch, D latch, edge-triggered D flip-flop; see [[Latches and flip-flops]].

## Building blocks
- Counters and shift registers; see [[Counters and registers]].
- State machines with Moore and Mealy outputs; see [[Finite state machine]].
- A pipelined output register delays an output by one clock and removes glitches. (source: 10_17.pdf, p. 23; 10_03.pdf, p. 10)

## Timing
- Setup and hold times must be met, or the flip-flop can go metastable. (source: 09_28(2).pdf, p. 8-9, 17-20)
- Clock speed up to 4 GHz inside chips and 500 MHz between chips on a PCB. (source: 10_05.pdf, p. 8)
- See [[Static timing and propagation delay]] and [[Timing diagram]].

**Covered in**: ECE 270 08_31, 09_28, 10_03, 10_05, 10_17 (ECE 27000/week 02/08_31.pdf, week 06/09_28(2).pdf, week 07/10_03.pdf, week 07/10_05.pdf, week 09/10_17.pdf)
**Sources**: `ECE 27000/week 02/08_31.pdf`, `ECE 27000/week 06/09_28(2).pdf`, `ECE 27000/week 07/10_03.pdf`, `ECE 27000/week 07/10_05.pdf`, `ECE 27000/week 09/10_17.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Latches and flip-flops]]
- [[Counters and registers]]
- [[Finite state machine]]
- [[Timing diagram]]
- [[Static timing and propagation delay]]
