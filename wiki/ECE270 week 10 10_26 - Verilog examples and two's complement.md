---
type: lecture
area: digital
areas: [digital]
course: ece270
lecture: week 10 10_26
source-ref: "ECE 27000/week 10/10_26.pdf, 29 slides (Wakerly ch. 12 and ch. 2 figures plus instructor slides)"
tags: [digital-logic]
---

# ECE270 week 10 10_26 - Verilog examples and two's complement

**Summary**: Finishes the chapter 12 Verilog state machine examples (T-Bird, traffic light, a pushbutton guessing game) and then returns to chapter 2 binary arithmetic: full adder and subtractor tables, signed number formats, and two's complement.

**File**: `ECE 27000/week 10/10_26.pdf`

---

## Topics
- **T-Bird and traffic light recap (p. 2-12)**: Fig. 12-5, 12-6, 9-25, Tables 9-7 and 9-8, then modules `VrTbirdSM` and `Vrsvale` as in [[ECE270 week 10 10_24 - Verilog state machines and test benches]].
- **Guessing game (p. 13-14)**: four pushbutton inputs G1 to G4, four LED outputs L1 to L4, and an ERR output. In normal operation the L outputs show a 1-out-of-4 pattern rotated one position per clock tick (about 4 Hz). A guess is a pressed and held debounced button; ERR is asserted if the pressed Gi does not match the lit LED; play stops until the input is negated, then resumes. Module `Vrggameoc` uses a 5-bit state register whose bits are the outputs: S1=5'b10000, S2=5'b01000, S3=5'b00100, S4=5'b00010, SOK=5'b00000, SERR=5'b00001. In S1, any of G2, G3, G4 goes to SERR; G1 alone goes to SOK; no input goes to S2 (similarly for S2 to S4). SOK and SERR return to S1 when no Gi is asserted. Output logic is `assign {L1,L2,L3,L4,ERR} = Sreg;` (output coded state assignment).
- **Chapter 2 binary arithmetic (p. 15-18)**: Table 2-3 shows the full adder (inputs x, y, c_in; outputs s, c_out) and full subtractor (x, y, b_in; d, b_out) truth tables, annotated with arithmetic such as $1+1+1 = 11$. Fig. 2-1 adds $190 + 141 = 331$ and $173 + 44 = 217$ in binary with carries. Fig. 2-2 subtracts $229 - 46 = 183$ and $210 - 109 = 101$ with borrows rippling through columns.
- **Expectation (p. 19)**: understand the process; no need to be a "human computer"; know how to calculate 2's complement; do not memorize the tables.
- **Table 2-4, 4-bit numbers (p. 20-24)**: columns two's complement, ones' complement, signed magnitude and excess-$2^{m-1}$ (the last is "ignore for now"). Signed magnitude adds a sign bit (MSB) to the magnitude. Ones' complement of a negative number: flip each bit (1 to 0, 0 to 1). Two's complement: take the ones' complement and add 1. A negative number has MSB = 1. Slide note: two's complement is used more widely because adders are simpler.
- **Practice problems (p. 27)**: $17 \to 00010001 \to 11101110 + 1 = 11101111 = -17$; $119 \to 01110111 \to 10001001 = -119$; $0 \to 00000000$ (complement 11111111, plus 1 carries out and gives 00000000); $-99 = 10011101 \to 01100011 = 99$; $-127 = 10000001 \to 01111111 = 127$; $-128 = 10000000 \to 10000000 = -128$ (negating $-128$ overflows).
- **Addition (p. 28-29)**: $3 + 4 = 7$ (0011 + 0100 = 0111); $-2 + (-6) = -8$ (1110 + 1010 = 1 1000, carry discarded); $6 + (-3) = 3$ (0110 + 1101 = 1 0011); $4 + (-7) = -3$ (0100 + 1001 = 1101).

## Key results
> [!definition] Two's complement negation
> $$-x = \overline{x} + 1$$
> where the overline is a bitwise inversion; the MSB of a negative number is 1.
> (source: 10_26.pdf, Table 2-4 slides)

> [!example] Full adder
> $$s = x \oplus y \oplus c_{in}$$
> $$c_{out} = x y + x c_{in} + y c_{in}$$
> Wiki note: these closed forms follow from the Table 2-3 rows (sum is 1 when an odd number of inputs are 1; carry when at least two are); the slides show only the table.

> [!warning] Overflow of the most negative value
> In n bits, $-2^{n-1}$ negates to itself (slide 27, $-128$).

**Connections**: number systems first appeared in [[ECE270 week 01 08_22 - Intro and number systems]]. Next: [[ECE270 week 11 10_31 - Binary arithmetic, codes and adders]].

**Sources**: `ECE 27000/week 10/10_26.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Number systems and codes]] · [[Finite state machine]] · [[Verilog]] · [[Logic gate]]
