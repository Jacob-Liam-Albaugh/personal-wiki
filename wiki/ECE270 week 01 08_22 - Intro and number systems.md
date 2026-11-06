---
type: lecture
area: digital
areas: [digital]
course: ece270
lecture: week 01 08_22
source-ref: "ECE 27000/week 01/08_22.pdf, 35 slides"
tags: [digital-logic]
---

# ECE270 week 01 08_22 - Intro and number systems

**Summary**: First lecture of ECE 270 (Introduction to Digital System Design, Yung-Hsiang Lu, Purdue, Fall 2022). It motivates digital design (Dance Dance Revolution scoring circuit, Moore's law), separates analog from digital, introduces bits, truth tables and the first [[Logic gate]]s, and starts positional number systems (binary, octal, hex).

**File**: `ECE 27000/week 01/08_22.pdf`

---

## Topics
- **Course framing (p. 1-9)**: instructor intro, Brightspace and Piazza resources, a short talk on why cheating hurts the cheater (p. 7-9). The course follows Wakerly, *Digital Design Principles and Practices* (see the syllabus note below).
- **Motivation (p. 4-6)**: a Dance Dance Revolution machine scores only if all four arrow directions match. The slide shows the circuit: each pad/pin pair goes through an XOR-like comparison, the four results are combined with AND, and the output goes to the score pin (source: 08_22.pdf, p. 5-6; the circuit is from Gasser, Lu, Koh, IEEE FIE 2010).
- **Electronics get cheaper (p. 10-18)**: housing-price charts versus memory price, Moore's law ("storage cost fell to about one billionth from 1970 to 2022", p. 15), mobile phones 1973-2007, Purdue semiconductor degree program news.
- **Analog vs digital (p. 19-20)**: continuous quantities (temperature, hair length) versus discrete (number of dogs, enrollment). Discrete values must not be connected by a line.
- **Bits (p. 21-22)**: a bit is 0 or 1. Table 1-1 lists physical states for 0 and 1 (relay open/closed, TTL 0-0.8 V vs 2.0-5.0 V, capacitor discharged/charged, light off/on, magnetic flux direction, pit/no pit). 0 = low = false, 1 = high = true.
- **Logic circuits (p. 22-27)**: black-box 3-input, 1-output circuit; truth table (Table 1-2); AND, OR, NOT, then NAND, NOR; a circuit for the table $F = X Y + X' Y' Z$; a [[Timing diagram]] showing $F$ changing a little after its inputs.
- **Number systems (p. 28-35)**: positional notation with base (radix) $r$.

## Key results
> [!definition] Positional number
> A digit string $d_{p-1} \dots d_0 . d_{-1} \dots d_{-n}$ in radix $r$ has value
> $$\sum_{i=-n}^{p-1} d_i\, r^i$$
> (source: 08_22.pdf, p. 28)

- MSD is leftmost, LSD rightmost; in binary, MSB and LSB.
- Example: $273_{10} = 2^8 + 2^4 + 1 = 100010001_2$ (p. 29).
- Example: $101.001_2 = 4 + 1 + 0.125 = 5.125_{10}$ (p. 30).
- Why binary suffices: for any positive $n$ there is $k$ with $2^k = n$ (e.g. $k=2$ for 4, $-1$ for 0.5, 2.807... for 7). Any base 2, 3, 4, ... works but base 1 does not, since $1^k = 1$ (p. 31).
- Table 2-1: binary, decimal, octal, hex side by side; 8 bits = 1 byte = 2 hex digits; C writes hex with a `0x` prefix (p. 32).
- Table 2-2 conversions (p. 33-35): binary to octal/hex by grouping 3 or 4 bits (substitution); to decimal by summation; decimal to another radix by repeated division, remainders giving LSD first. Example: $108_{10} = 1101100_2 = 154_8 = 6C_{16}$.

## Examples
> [!example] Truth table and circuit (Table 1-2, Fig. 1-5)
> $F$ is 1 for $XYZ = 001$, $110$, $111$. Realized as $F = XY + X'Y'Z$ with two ANDs, two inverters and an OR (p. 23, 26).

**Connections**: the gates and truth tables here are formalized in [[Boolean algebra]]; later lectures turn them into minimized circuits ([[ECE270 week 02 08_31 - Boolean algebra and canonical forms]]) and coded hardware ([[Verilog]]).

Syllabus note: the course syllabus (`ECE 27000/zz_Syllabus.pdf`) gives grading by homework, 3 of 4 exams and 12 of 13 labs, and the Wakerly 5th edition textbook. It has no page of its own.

**Sources**: `ECE 27000/week 01/08_22.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Boolean algebra]] · [[Logic gate]] · [[Timing diagram]] · [[Number systems and codes]]
- [[ECE270 week 01 08_24 - Transistors and CMOS gates]] 
