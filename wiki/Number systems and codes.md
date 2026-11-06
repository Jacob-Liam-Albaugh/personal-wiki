---
type: concept
area: digital
areas: [digital]
source-ref: "ECE 270 lectures 08_22, 10_26, 10_31 (Wakerly ch. 2)"
tags: [digital-logic]
---

# Number systems and codes

**Summary**: Positional number systems, radix conversion, signed number formats (signed magnitude, ones' and two's complement), and character and decimal codes.

## Positional notation
$$\sum_{i=-n}^{p-1} d_i\, r^i$$
- Radix r, MSD leftmost. $273_{10} = 100010001_2$; $101.001_2 = 5.125_{10}$. (source: 08_22.pdf, p. 28-30)
- Binary, octal, hex: group 3 or 4 bits; decimal to other radix by repeated division. $108_{10} = 1101100_2 = 154_8 = 6C_{16}$. (source: 08_22.pdf, p. 32-35)

## Signed formats (Table 2-4)
- Signed magnitude: sign bit plus magnitude.
- Ones' complement: flip every bit.
- Two's complement: flip, then add 1; negative numbers have MSB 1; used most because adders are simpler.
- Excess-$2^{m-1}$: "ignore for now".
(source: 10_26.pdf, p. 20-24; 10_31.pdf)

$$-x = \overline{x} + 1$$
(the overline is bitwise inversion). Negating the most negative value gives itself ($-128$ in 8 bits). (source: 10_26.pdf, p. 27)

## Arithmetic
- Add two's complement numbers and discard the carry out. Subtract by adding the complement with $c_{in} = 1$. (source: 10_31.pdf, p. 9-14)
- Overflow when the addends share a sign that differs from the sum's sign. Examples: $5+6 \to 1011 = -5$; $7+7 \to 1110 = -2$. (source: 10_31.pdf, p. 11)
- Multiplication by shift-and-add ($11 \times 13 = 143$), long division (217 / 11 = 19 remainder 8). (source: 10_31.pdf, p. 15-16)

## Codes
- Decimal codes (Table 2-7): BCD 8421, 2421, excess-3, biquinary, 1-out-of-10. BCD sums above 9 take a +0110 correction. (source: 10_31.pdf, p. 17-18)
- ASCII (Table 2-9, ANSI X3.4-1968). (source: 10_31.pdf, p. 19-20)

## Where it appears
[[ECE270 week 01 08_22 - Intro and number systems]], [[ECE270 week 10 10_26 - Verilog examples and two's complement]], [[ECE270 week 11 10_31 - Binary arithmetic, codes and adders]].

**Sources**: `ECE 27000/week 01/08_22.pdf`, `ECE 27000/week 10/10_26.pdf`, `ECE 27000/week 11/10_31.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Adders and arithmetic circuits]]
- [[Logic gate]]
- [[Verilog]]
- [[ECE270 week 01 08_22 - Intro and number systems]]
- [[ECE270 week 10 10_26 - Verilog examples and two's complement]]
- [[ECE270 week 11 10_31 - Binary arithmetic, codes and adders]]
