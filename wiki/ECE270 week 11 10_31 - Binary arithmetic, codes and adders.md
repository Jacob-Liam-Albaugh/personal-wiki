---
type: lecture
area: digital
areas: [digital]
course: ece270
lecture: week 11 10_31
source-ref: "ECE 27000/week 11/10_31.pdf, 24 slides (Wakerly ch. 2 and ch. 8 figures plus instructor slides)"
tags: [digital-logic]
---

# ECE270 week 11 10_31 - Binary arithmetic, codes and adders

**Summary**: Two's complement addition, overflow, subtraction as addition, multiplication and division, BCD and other codes, ASCII, then the hardware: the full adder, the 4-bit ripple adder, and a subtractor built from adders.

**File**: `ECE 27000/week 11/10_31.pdf`

---

## Topics
- **Signed formats recap (p. 2-8)**: Table 2-4 again, built up step by step. Signed magnitude adds a sign bit; ones' complement flips every bit; two's complement adds 1 to the ones' complement; a negative number has MSB 1. Excess-$2^{m-1}$ is "ignore for now". Practice problems convert 17, 119, 0, -99, -127, -128 (see [[ECE270 week 10 10_26 - Verilog examples and two's complement]]).
- **Addition (p. 9-10)**: examples $3+4$, $-2+(-6)$, $6+(-3)$, $4+(-7)$. Fig. 2-3 is a counter wheel for 4-bit two's complement: adding moves clockwise, subtracting counterclockwise, and -8 and +7 are adjacent across the dashed gap.
- **Overflow (p. 11)**: $-3 + (-6) = 1101 + 1010 = 1\,0111$ reads as $+7$; $+5 + 6 = 1011$ reads as $-5$; $-8 + (-8) = 1\,0000$ reads as $0$; $+7 + 7 = 1110$ reads as $-2$. Rule on the slide: overflow occurs if the addends' sign bits are the same but differ from the sum's sign bit; equivalently the carries into and out of the MSB differ (slide text is garbled; Table 2-5 states the carry rule).
- **Subtraction (p. 12)**: subtracting means adding the complement with $c_{in} = 1$. Examples: $4 - 3 = 0100 + 1100 + 1 \to 0001$; $3 - 4 \to 1111$ ($-1$); $3 - (-4) \to 0111$ ($+7$); $-3 - (-4) \to 0001$ ($+1$).
- **Unsigned counter wheel (p. 13)**: Fig. 2-4, modular counting of 4-bit unsigned numbers 0 to 15.
- **Summary of rules (p. 14)**: Table 2-5 gives addition, negation and subtraction rules for unsigned, signed magnitude, two's complement and ones' complement. Two's complement: add ignoring the carry out of the MSB; negate by complementing and adding 1; subtract by complementing the subtrahend and adding with an initial carry of 1. Ones' complement: add and, if there is a carry out of the MSB, add 1 to the result (end-around carry).
- **Multiplication and division (p. 15-16)**: $11 \times 13 = 143$ as $1011 \times 1101 = 10001111$ using shifted multiplicands; Table 2-6 long division $217 / 11 = 19$ remainder $8$, as $11011001 / 1011 = 10011$ remainder $1000$.
- **Decimal codes (p. 17-18)**: Table 2-7 lists BCD (8421), 2421, excess-3, biquinary and 1-out-of-10 for digits 0 to 9, plus the unused code words. BCD addition: add the 4-bit codes and, if the sum exceeds 9 or carries out, add 0110 as a correction. Examples: $5 + 9 = 1110 \to + 0110 = 1\,0100$ (that is 14 as 1 and 4); $4 + 5 = 1001$ (no correction); $8 + 8 \to 1\,0110$; $9 + 9 \to 1\,1000$.
- **ASCII (p. 19-20)**: Table 2-9 (ANSI X3.4-1968) with control characters, and a hex/decimal/character listing from 0x00 NULL to 0x7F DEL; for example 0x20 is space.
- **Full adder (p. 21-22)**: Fig. 8-1 gate-level diagram, symbol and an alternate symbol suitable for cascading. The half adder gives HS = A xor B and carry-out CO = A B.
  $$S = A \oplus B \oplus C_{IN}$$
  $$C_{OUT} = A B + A C_{IN} + B C_{IN}$$
- **Ripple adder (p. 23)**: Fig. 8-2, four full adders with the carry chain $c_0 \to c_1 \to c_2 \to c_3 \to c_4$ and sums $s_0$ to $s_3$. Delay
  $$t_{ADD} = t_{ABCout} + (n-2)\, t_{CinCout} + t_{CinS}$$
- **Subtractor (p. 24)**: Fig. 8-3 builds a full subtractor and ripple subtractor from full adders with inverters on the B inputs.
  $$D = A \oplus B \oplus B_{IN}$$
  $$B_{OUT} = A' B + A' B_{IN} + B B_{IN}$$

## Key results
> [!definition] Two's complement overflow
> Overflow occurs when two operands of the same sign give a result of the opposite sign.
> (source: 10_31.pdf, p. 11)

> [!example] Ripple adder delay
> The carry has to ripple through $n-1$ full adders, so adder delay grows linearly with n.

> [!definition] BCD correction
> If a BCD digit sum is greater than 9, add 0110 and carry into the next digit.
> (source: 10_31.pdf, p. 18)

**Connections**: sign formats from [[ECE270 week 10 10_26 - Verilog examples and two's complement]]; adders use the gates of [[ECE270 week 02 08_31 - Boolean algebra and canonical forms]]. Next: [[ECE270 week 11 11_02 - Adders, ALUs and shifters]].

**Sources**: `ECE 27000/week 11/10_31.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Adders and arithmetic circuits]] · [[Number systems and codes]] · [[Logic gate]] · [[Boolean algebra]] · [[Verilog]]
