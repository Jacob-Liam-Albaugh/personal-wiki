---
type: concept
area: digital
areas: [digital]
source-ref: "ECE 270 lectures 08_22, 08_29, 09_12, 09_19, 09_28, 10_03, 10_05, 10_24 (Wakerly ch. 4, 10, 14)"
tags: [digital-logic]
---

# Timing diagram

**Summary**: A plot of signals against time that shows causality, delays, setup and hold, and clocked behavior.

## What it shows
- An output changing a little after its inputs (Fig. 1-5 example). (source: 08_22.pdf, p. 27)
- Causality, propagation delay, rise time (LOW to HIGH), fall time (HIGH to LOW), and minimum and maximum delay (Fig. 4-19). (source: 09_12.pdf, p. 15-17)
- Data signals on a bus with setup, hold and an unknown region (Fig. 4-20). (source: 09_12.pdf, p. 16)
- Slide note: treat rise and fall as symmetric when drawing. (source: 09_12.pdf, p. 17)

## Delay measures
- $t_{pHL}$ and $t_{pLH}$ are taken between 50% points; rise and fall times between $V_{ILmax}$ and $V_{IHmin}$. See [[Static timing and propagation delay]]. (source: 08_29.pdf, p. 21-27)

## Sequential circuits
- Clock: period, frequency $1/t_{per}$, duty cycle $t_H/t_{per}$. (source: 10_05.pdf, p. 8)
- Latch and flip-flop parameters: $t_{pLH(CQ)}$, $t_{pHL(CQ)}$, setup, hold, minimum pulse width. (source: 09_28(2).pdf, p. 10-20)
- State machine output timing differs for Moore, pipelined and Mealy outputs (Fig. 9-7). (source: 10_05.pdf, p. 15)
- Counter decoding glitches are visible in the waveforms (Fig. 11-9); see [[Hazards]]. (source: 10_03.pdf, p. 10)
- Hazard timing diagram: signals $ZP$, $XZP$ and $YZ$ show the glitch on $F$. (source: 09_07.pdf, p. 24)

## Simulation waveforms
- Verilog test benches produce waveforms such as Fig. 5-4 (prime detector, 09_19.pdf p. 30) and Fig. 12-3 (state machine simulation, 10_24.pdf p. 9). See [[Verilog]].

**Covered in**: ECE 270 08_22, 08_29, 09_07, 09_12, 09_19, 09_28, 10_03, 10_05, 10_24 (ECE 27000/week 01/08_22.pdf, week 02/08_29.pdf, week 03/09_07.pdf, week 04/09_12.pdf, week 05/09_19.pdf, week 06/09_28(2).pdf, week 07/10_03.pdf, week 07/10_05.pdf, week 10/10_24.pdf)
**Sources**: `ECE 27000/week 01/08_22.pdf`, `ECE 27000/week 02/08_29.pdf`, `ECE 27000/week 03/09_07.pdf`, `ECE 27000/week 04/09_12.pdf`, `ECE 27000/week 05/09_19.pdf`, `ECE 27000/week 06/09_28(2).pdf`, `ECE 27000/week 07/10_03.pdf`, `ECE 27000/week 07/10_05.pdf`, `ECE 27000/week 10/10_24.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Static timing and propagation delay]]
- [[Hazards]]
- [[Latches and flip-flops]]
- [[Finite state machine]]
- [[Verilog]]
