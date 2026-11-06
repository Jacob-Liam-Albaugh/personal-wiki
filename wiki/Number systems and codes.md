---
type: concept
area: digital
areas: [digital]
source-ref: "ECE 270 lectures 08_22, 10_26, 10_31 (Wakerly ch. 2)"
tags: [digital-logic]
---

# Number systems and codes

**Summary**: Positional number systems, radix conversion, signed number formats (signed magnitude, ones' and two's complement), overflow, and character and decimal codes.

## Bits and analog versus digital
- Analog quantities are continuous (temperature, hair length); digital quantities are discrete (number of dogs, enrollment), and discrete values must not be connected by a line. (source: 08_22.pdf, p. 19-20)
- A bit is 0 or 1. Table 1-1 lists physical states for 0 and 1: relay open/closed, TTL 0-0.8 V versus 2.0-5.0 V, capacitor discharged/charged, light off/on, magnetic flux direction, pit/no pit. 0 = low = false, 1 = high = true. (source: 08_22.pdf, p. 21-22)

## Positional notation
> [!definition] Positional number
> A digit string $d_{p-1} \dots d_0 . d_{-1} \dots d_{-n}$ in radix $r$ has value
> $$\sum_{i=-n}^{p-1} d_i\, r^i$$
> (source: 08_22.pdf, p. 28)

- Radix r; MSD is leftmost, LSD rightmost; in binary, MSB and LSB. $273_{10} = 2^8 + 2^4 + 1 = 100010001_2$; $101.001_2 = 4 + 1 + 0.125 = 5.125_{10}$. (source: 08_22.pdf, p. 28-30)
- Why binary suffices: for any positive $n$ there is $k$ with $2^k = n$ (e.g. $k=2$ for 4, $-1$ for 0.5, 2.807... for 7). Any base 2, 3, 4, ... works but base 1 does not, since $1^k = 1$. (source: 08_22.pdf, p. 31)
- Table 2-1 lists binary, decimal, octal and hex side by side; 8 bits = 1 byte = 2 hex digits; C writes hex with a `0x` prefix. (source: 08_22.pdf, p. 32)
- Conversions (Table 2-2): binary to octal/hex by grouping 3 or 4 bits (substitution); to decimal by summation; decimal to another radix by repeated division, remainders giving the LSD first. $108_{10} = 1101100_2 = 154_8 = 6C_{16}$. (source: 08_22.pdf, p. 33-35)

## Binary addition and subtraction by hand
- Table 2-3 gives the full adder (inputs x, y, c_in; outputs s, c_out) and full subtractor (x, y, b_in; d, b_out) truth tables, annotated with arithmetic such as $1+1+1 = 11$. (source: 10_26.pdf, p. 15-18)
- Fig. 2-1 adds $190 + 141 = 331$ and $173 + 44 = 217$ in binary with carries; Fig. 2-2 subtracts $229 - 46 = 183$ and $210 - 109 = 101$ with borrows rippling through the columns. The expectation is to understand the process, not to be a "human computer" or memorize the tables. (source: 10_26.pdf, p. 15-19)
- The hardware version of these tables is in [[Adders and arithmetic circuits]].

## Signed formats (Table 2-4)
- Signed magnitude: a sign bit (the MSB) plus the magnitude.
- Ones' complement: flip every bit (1 to 0, 0 to 1).
- Two's complement: take the ones' complement and add 1; negative numbers have MSB 1; used most because adders are simpler.
- Excess-$2^{m-1}$: "ignore for now".
(source: 10_26.pdf, p. 20-24; 10_31.pdf, p. 2-8)

$$-x = \overline{x} + 1$$
(the overline is bitwise inversion). Full adder in lowercase: $s = x \oplus y \oplus c_{in}$ and $c_{out} = x y + x c_{in} + y c_{in}$ (sum is 1 for an odd number of 1 inputs, carry for at least two; derived from Table 2-3, which the slides show only as a table). Ripple addition passes the carry through $n-1$ full adders, so delay grows linearly with n. Negating the most negative value gives itself ($-128$ in 8 bits). (source: 10_26.pdf, p. 27)

> [!example] Two's complement practice (8 bits)
> - $17 \to 00010001 \to 11101110 + 1 = 11101111 = -17$
> - $119 \to 01110111 \to 10001001 = -119$
> - $0 \to 00000000$; complement $11111111$, plus 1 carries out and gives $00000000$
> - $-99 = 10011101 \to 01100011 = 99$
> - $-127 = 10000001 \to 01111111 = 127$
> - $-128 = 10000000 \to 10000000 = -128$ (negating $-128$ overflows)
>
> (source: 10_26.pdf, p. 27)

## Arithmetic
- Add two's complement numbers and discard the carry out of the MSB. Subtract by complementing the subtrahend and adding with $c_{in} = 1$. (source: 10_31.pdf, p. 9-14)
- Fig. 2-3 is a counter wheel for 4-bit two's complement: adding moves clockwise, subtracting counterclockwise, and $-8$ and $+7$ are adjacent across the dashed gap. Fig. 2-4 is the unsigned wheel, modular counting 0 to 15. (source: 10_31.pdf, p. 9-13)

> [!example] Two's complement addition and subtraction (4 bits)
> - $3 + 4 = 7$ (0011 + 0100 = 0111)
> - $-2 + (-6) = -8$ (1110 + 1010 = 1 1000, carry discarded)
> - $6 + (-3) = 3$ (0110 + 1101 = 1 0011)
> - $4 + (-7) = -3$ (0100 + 1001 = 1101)
> - $4 - 3 = 0100 + 1100 + 1 \to 0001$; $3 - 4 \to 1111$ ($-1$); $3 - (-4) \to 0111$ ($+7$); $-3 - (-4) \to 0001$ ($+1$)
>
> (source: 10_26.pdf, p. 28-29; 10_31.pdf, p. 9-12)

> [!definition] Two's complement overflow
> Overflow occurs when the addends' sign bits are the same but differ from the sum's sign bit; equivalently the carries into and out of the MSB differ (the slide text is garbled; Table 2-5 states the carry rule).
> Examples: $-3 + (-6) = 1101 + 1010 = 1\,0111$ reads as $+7$; $+5 + 6 = 1011$ reads as $-5$; $-8 + (-8) = 1\,0000$ reads as $0$; $+7 + 7 = 1110$ reads as $-2$.
> (source: 10_31.pdf, p. 11)

- Table 2-5 summarizes addition, negation and subtraction for unsigned, signed magnitude, two's complement and ones' complement. Ones' complement: add and, if there is a carry out of the MSB, add 1 to the result (end-around carry). (source: 10_31.pdf, p. 14)
- Multiplication by shift-and-add: $11 \times 13 = 143$ as $1011 \times 1101 = 10001111$ using shifted multiplicands. Table 2-6 long division: $217 / 11 = 19$ remainder $8$, as $11011001 / 1011 = 10011$ remainder $1000$. (source: 10_31.pdf, p. 15-16)

## Codes
- Decimal codes (Table 2-7): BCD 8421, 2421, excess-3, biquinary, 1-out-of-10, plus the unused code words. (source: 10_31.pdf, p. 17-18)

> [!definition] BCD correction
> Add the 4-bit codes; if the digit sum is greater than 9 or carries out, add 0110 and carry into the next digit.
> Examples: $5 + 9 = 1110 \to + 0110 = 1\,0100$ (14 as 1 and 4); $4 + 5 = 1001$ (no correction); $8 + 8 \to 1\,0110$; $9 + 9 \to 1\,1000$.
> (source: 10_31.pdf, p. 18)

- ASCII (Table 2-9, ANSI X3.4-1968): control characters plus a hex/decimal/character listing from 0x00 NULL to 0x7F DEL; for example 0x20 is space. (source: 10_31.pdf, p. 19-20)

## Logic-circuit warm-up from the first lecture
> [!example] Truth table and circuit (Table 1-2, Fig. 1-5)
> $F$ is 1 for $XYZ = 001$, $110$, $111$. Realized as $F = XY + X'Y'Z$ with two ANDs, two inverters and an OR. A [[Timing diagram]] shows $F$ changing a little after its inputs. (source: 08_22.pdf, p. 22-27)

The first lecture also motivated digital design with a Dance Dance Revolution scoring circuit (four XOR-like pad comparisons combined with AND; Gasser, Lu, Koh, IEEE FIE 2010) and Moore's law (storage cost fell to about one billionth from 1970 to 2022). (source: 08_22.pdf, p. 4-18)

**Covered in**: ECE 270 08_22, 10_26, 10_31 (courses/ECE 270/week 01/08_22.pdf, courses/ECE 270/week 10/10_26.pdf, courses/ECE 270/week 11/10_31.pdf); the course follows Wakerly, *Digital Design Principles and Practices*, 5th ed.
**Sources**: `courses/ECE 270/week 01/08_22.pdf`, `courses/ECE 270/week 10/10_26.pdf`, `courses/ECE 270/week 11/10_31.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Adders and arithmetic circuits]]
- [[Logic gate]]
- [[Boolean algebra]]
- [[Verilog]]
