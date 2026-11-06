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
> [!definition] Static hazards
> Static-1: output should stay 1 but glitches to 0 (two input combinations differ in one variable and both give 1, yet the output can dip to 0 during the change).
> Static-0: output should stay 0 but glitches to 1.
> (source: 09_12.pdf, p. 2)

- A logically correct circuit can glitch because gate delays differ: one path through an inverter is slower, so $F$ glitches when $Z$ changes (09_07.pdf p. 24, diagram with $ZP$, $XZP$, $YZ$; slide label "Timing Hazard"). (source: 09_07.pdf, p. 24-25)
- Dynamic hazard: three or more transitions where one is expected (output changes 1-0-1-0 instead of 1-0), from paths of different delay, e.g. slow and slower OR gates (Fig. 3-31). (source: 09_07.pdf, p. 25; 09_12.pdf, p. 6)

## Example
> [!example] Fix for the Fig. 3-26 circuit
> $F = XZ' + YZ$ with $X = Y = 1$ and Z changing. The inverter delay makes $XZ'$ fall before $YZ$ rises.
> $$F = XZ' + YZ$$
> Add the consensus term:
> $$F = XZ' + YZ + XY$$
> (source: 09_12.pdf, p. 2-5)

## Rules
- In an AND-OR circuit a static-0 hazard needs a variable and its complement into one AND gate, usually a design mistake (Fig. 3-27). (source: 09_12.pdf, p. 4)
- The extra term covers the two adjacent groups on the [[Karnaugh map]] (Figs. 3-28, 3-29). (source: 09_12.pdf, p. 5-6)

## Sequential circuits
> [!failure] Decoding glitches (p. 10)
> Outputs decoded combinationally from a counter can glitch when more than one counter bit changes. Register the decoded outputs to remove the glitches (Figs. 11-9, 11-10).
> (source: 10_03.pdf, p. 9-11)

**Covered in**: ECE 270 09_07, 09_12, 10_03 (courses/ECE 270/week 03/09_07.pdf, week 04/09_12.pdf, week 07/10_03.pdf)
**Sources**: `courses/ECE 270/week 03/09_07.pdf`, `courses/ECE 270/week 04/09_12.pdf`, `courses/ECE 270/week 07/10_03.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Karnaugh map]]
- [[Static timing and propagation delay]]
- [[Timing diagram]]
- [[Counters and registers]]
