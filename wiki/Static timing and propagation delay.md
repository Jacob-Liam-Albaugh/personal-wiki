---
type: concept
area: digital
areas: [digital]
source-ref: "ECE 270 lectures 08_29, 09_12, 09_28, 10_31, 11_02"
tags: [digital-logic]
---

# Static timing and propagation delay

**Summary**: How gate delays, rise and fall times and setup and hold times bound how fast a design can run; the ECE 270 slides treat it through examples, not a full method.

## Gate delay
- $t_{pLH}$ and $t_{pHL}$ between 50% points; output load as $R_L$ and $C_L$ (Figs. 14-33 to 14-39). Rise and fall are not symmetric. (source: 08_29.pdf, p. 21-27)
- Factors: supply voltage (higher is faster), temperature (higher is slower), load, input slew, manufacturing variation, signal paths, noise. Remedy: a margin of safety. (source: 09_12.pdf, p. 17)
- Product binning sells the same part as fast, typical or slow. (source: 09_12.pdf, p. 18)

## Delay tables
- Tables 4-2 and 4-3 list typical and maximum delays for 74AC and 74HC parts at 25 C and 85 C. (source: 09_12.pdf, p. 19-21)

## Flip-flop timing
- Setup, hold and clock-to-output delays $t_{pLH(CQ)}$, $t_{pHL(CQ)}$ (Fig. 10-14). (source: 09_28(2).pdf, p. 17-20)

## Design flow terms
- Timing closure: analyze, meet the constraint, revise, repeat; also RTL, placement, routing, verification and netlist. (source: 09_12.pdf, p. 22-24)

## Arithmetic delay
$$t_{ADD} = t_{ABCout} + (n-2)\, t_{CinCout} + t_{CinS}$$
A ripple adder's delay grows linearly with n; carry lookahead and prefix adders shorten the carry path. (source: 10_31.pdf, p. 23; 11_02.pdf, p. 6-26)

## Where it appears
[[ECE270 week 02 08_29 - CMOS electrical behavior]], [[ECE270 week 04 09_12 - Hazards, documentation and timing]], [[ECE270 week 06 09_28 - Latches and flip-flops]], [[ECE270 week 11 10_31 - Binary arithmetic, codes and adders]], [[ECE270 week 11 11_02 - Adders, ALUs and shifters]].

Wiki note: the minimum clock period is set by the clock-to-output delay, the longest combinational path and the setup time; the slides show the ingredients but do not state this formula **[unverified]**.

**Sources**: `ECE 27000/week 02/08_29.pdf`, `ECE 27000/week 04/09_12.pdf`, `ECE 27000/week 06/09_28(2).pdf`, `ECE 27000/week 11/10_31.pdf`, `ECE 27000/week 11/11_02.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Timing diagram]]
- [[Hazards]]
- [[CMOS logic]]
- [[Latches and flip-flops]]
- [[Adders and arithmetic circuits]]
- [[ECE270 week 02 08_29 - CMOS electrical behavior]]
