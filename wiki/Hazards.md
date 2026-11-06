---
type: concept
area: digital
areas: [digital]
source-ref: "ECE 270 lectures 09_07, 09_12, 10_03 (Wakerly ch. 3, 11)"
tags: [digital-logic]
---

# Hazards

**Summary**: Momentary wrong outputs caused by unequal gate delays: static-1, static-0 and dynamic hazards, and the glitches seen when decoding counters.

## Definitions
- Static-1 hazard: two input combinations differ in one variable and both give 1, yet the output can dip to 0 during the change. Static-0 is the same with 0 and a spike to 1. (source: 09_12.pdf, p. 2)
- Dynamic hazard: three or more transitions where one is expected, from paths of different delay (Fig. 3-31). (source: 09_07.pdf, p. 25; 09_12.pdf, p. 6)

## Example
Fig. 3-26: $F = XZ' + YZ$ with $X = Y = 1$ and Z falling. The inverter delay makes $XZ'$ rise late and $YZ$ fall early.
$$F = XZ' + YZ$$
Add the consensus term:
$$F = XZ' + YZ + XY$$
(source: 09_12.pdf, p. 2-5)

## Rules
- In an AND-OR circuit a static-0 hazard needs a variable and its complement into one AND gate, usually a design mistake (Fig. 3-27). (source: 09_12.pdf, p. 4)
- The extra term covers the two adjacent groups on the [[Karnaugh map]] (Figs. 3-28, 3-29). (source: 09_12.pdf, p. 5-6)

## Sequential circuits
- A decoder on counter outputs glitches when several bits change together; register the decoded outputs (Figs. 11-9, 11-10). (source: 10_03.pdf, p. 9-11)

## Where it appears
[[ECE270 week 03 09_07 - Circuit analysis and Karnaugh maps]], [[ECE270 week 04 09_12 - Hazards, documentation and timing]], [[ECE270 week 07 10_03 - Counters and shift registers]].

**Sources**: `ECE 27000/week 03/09_07.pdf`, `ECE 27000/week 04/09_12.pdf`, `ECE 27000/week 07/10_03.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Karnaugh map]]
- [[Static timing and propagation delay]]
- [[Timing diagram]]
- [[Counters and registers]]
- [[ECE270 week 04 09_12 - Hazards, documentation and timing]]
