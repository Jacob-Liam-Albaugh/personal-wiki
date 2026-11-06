---
type: concept
area: digital
areas: [digital]
source-ref: "ECE 270 lectures 10_26, 10_31, 11_02, 11_07 (Wakerly ch. 2, 8)"
tags: [digital-logic]
---

# Adders and arithmetic circuits

**Summary**: Combinational circuits for arithmetic: full adder, ripple and lookahead adders, subtractor, ALU, shifters, multiplier and the division variables.

## Full adder
$$S = A \oplus B \oplus C_{IN}$$
$$C_{OUT} = A B + A C_{IN} + B C_{IN}$$
- Half sum $HS = A \oplus B$, carry-out $CO = A B$. (source: 10_31.pdf, p. 21-22)
- A subtractor is an adder with the B input inverted and $c_{in} = 1$ (Fig. 8-3). (source: 10_31.pdf, p. 24)

## Ripple and lookahead
- Ripple: the carry passes through every stage. (source: 10_31.pdf, p. 23)
- Lookahead: generate $g_i = a_i b_i$, propagate $p_i = a_i + b_i$.
$$c_{i+1} = g_i + p_i c_i$$
(source: 11_02.pdf, p. 6-7)
- 74x283 4-bit adder with lookahead; 16-bit group-ripple and group-lookahead adders (Figs. 8-5 to 8-8). (source: 11_02.pdf, p. 8-12)
- Parallel-prefix adders: Kogge-Stone (few levels) and Brent-Kung (fewer cells). (source: 11_02.pdf, p. 23-26)

## ALU
- Table 8-1 selects among 0, B-A, A-B, A+B, xor, or, and, all ones. (source: 11_02.pdf, p. 13-15)

## Shifters
- Barrel shifter from multiplexers with six shift types (Table 8-2). (source: 11_07.pdf, p. 5-11)

## Multiply and divide
- Partial products added in an array (Figs. 8-22 to 8-25); division variables DVND, DVSR, QUOT, REM (Fig. 8-26). (source: 11_07.pdf, p. 12-16)

## In Verilog
- `assign {COUT, S} = A + B + CIN;` (source: 11_02.pdf, p. 16)

## Where it appears
[[ECE270 week 10 10_26 - Verilog examples and two's complement]], [[ECE270 week 11 10_31 - Binary arithmetic, codes and adders]], [[ECE270 week 11 11_02 - Adders, ALUs and shifters]], [[ECE270 week 12 11_07 - Shifters, multipliers and division]].

**Sources**: `ECE 27000/week 10/10_26.pdf`, `ECE 27000/week 11/10_31.pdf`, `ECE 27000/week 11/11_02.pdf`, `ECE 27000/week 12/11_07.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Number systems and codes]]
- [[Logic gate]]
- [[Decoder and multiplexer]]
- [[Static timing and propagation delay]]
- [[Verilog]]
- [[ECE270 week 11 10_31 - Binary arithmetic, codes and adders]]
- [[ECE270 week 11 11_02 - Adders, ALUs and shifters]]
- [[ECE270 week 12 11_07 - Shifters, multipliers and division]]
