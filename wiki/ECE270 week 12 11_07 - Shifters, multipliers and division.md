---
type: lecture
area: digital
areas: [digital]
course: ece270
lecture: week 12 11_07
source-ref: "ECE 27000/week 12/11_07.pdf, 16 slides (Wakerly ch. 8 figures plus instructor slides)"
tags: [digital-logic]
---

# ECE270 week 12 11_07 - Shifters, multipliers and division

**Summary**: Shift versus rotate and the four shift terms, the barrel shifter (multiplexer based, with a Verilog version covering six shift types), then the 8 by 8 combinational multiplier and the variables of the division algorithm.

**File**: `ECE 27000/week 12/11_07.pdf`

---

## Topics
- **Shift versus rotate (p. 2)**: shift left by 1 multiplies by 2 and shift right by 1 divides by 2; zeros enter at the vacated end and the bits shifted out are discarded. Rotate wraps the bits that leave one end back into the other end. Slide note: "need to be careful about sign bits".
- **Counter wheel (p. 3)**: Fig. 2-3 again (4-bit two's complement), annotated with "shift left ok" where the result stays in range and "shift left" and "shift right" arrows beside the wheel. See [[ECE270 week 11 10_31 - Binary arithmetic, codes and adders]].
- **Terminology (p. 4)**: (1) shift, (2) rotate (circular shift), (3) logical shift (the left-most bit is not treated as a sign), (4) arithmetic shift (the left-most bit is treated as a sign).
- **Barrel shifter, first design (p. 5-6)**: Fig. 8-17 builds a 16-bit shifter from sixteen 16-input, 1-bit-wide multiplexers (select S[3:0]), each output bit picking one input bit; Fig. 8-18 is the symbol of a 2-input, 16-bit-wide multiplexer used in the next design.
- **Barrel shifter, staged design (p. 7-8)**: Fig. 8-19 left circular shift using four 2-input 16-bit-wide multiplexers in series. Stage $k$ either passes its input or rotates it left by $2^k$ places, selected by bit $S_k$, so the total shift is the number written on S[3:0]. Fig. 8-20 shows one bit of a 2-input multiplexer built from transmission gates (see [[CMOS logic]]).
- **Shift types (p. 9)**: Table 8-2 gives name, 3-bit code C, Verilog function and note.
  - Left rotate, Lrotate, 000, Vrol, wrap-around
  - Right rotate, Rrotate, 001, Vror, wrap-around
  - Left logical, Llogical, 010, Vsll, 0 into LSB
  - Right logical, Rlogical, 011, Vslr, 0 into MSB
  - Left arithmetic, Larith, 100, Vsla, 0 into LSB
  - Right arithmetic, Rarith, 101, Vsra, replicate MSB
- **Verilog barrel shifter (p. 10)**: module `Vrbarrel16(DIN, S, C, DOUT)` with a 16-bit data input, a 4-bit shift amount S (0 to 15) and a 3-bit mode C. Parameters name the six codes. Functions such as `Vrol` loop `N = S` times with `TMPD = {TMPD[14:0], TMPD[15]}`, and `Vror` with `TMPD = {TMPD[0], TMPD[15:1]}`. The body is `always @ (DIN or S or C) case (C)` with one `DOUT = Vrol(DIN,S)` style line per code and `default: DOUT = DIN;`.
- **Components (p. 11)**: Fig. 8-21 the barrel shifter as a rotate block `ROLR16`, a `FIXUP` for left shifts and a `FIXUP` for right shifts (the fixups force the wrapped-around bits to 0 or to the sign), with select S[3:0] and mode C[2:0] driving "other logic".
- **Multiplier partial products (p. 12)**: Fig. 8-22 an 8 by 8 multiplication as eight rows of partial products $y_j x_i$, each shifted one place, added to give $p_{15}$ down to $p_0$. This is the same shift-and-add as the $11 \times 13$ example of the earlier lecture.
- **Combinational multiplier (p. 13-15)**: Fig. 8-23 arranges the additions as rows of adders (an array multiplier); Fig. 8-24 reroutes the interconnections for a faster version (each row's carries go to the next row instead of rippling along the row); Fig. 8-25 gives the Verilog variable names (`PCS`, `PCC`, `RAS`, `RAC` for partial sum and carry signals).
- **Division variables (p. 16)**: Fig. 8-26 uses DVND (dividend), DVSR (divisor), QUOT (quotient) and REM (remainder), with a $2n$-bit working register `RDIV` whose upper half is compared against DVSR; each step shifts left, subtracts, and records a quotient bit (the diagram shows DIFF = RDIV upper half minus DVSR).

## Key results
> [!definition] Logical versus arithmetic shift
> A logical shift fills with 0 and ignores the sign; an arithmetic right shift replicates the MSB so the sign survives (Table 8-2, Rarith "replicate MSB").
> (source: 11_07.pdf, p. 4, 9)

> [!example] Staged barrel shifter
> $$\text{shift} = 8 S_3 + 4 S_2 + 2 S_1 + S_0$$
> Four 2-input multiplexer stages, shifting by 8, 4, 2 and 1, cover every amount from 0 to 15. Wiki note: this reading of Fig. 8-19 follows from the figure's four stages labelled S0 to S3 and the one-bit offsets in the signal names; the slides do not state the formula.

> [!warning] Arithmetic left shift
> Shift left multiplies by 2 only if the result still fits; otherwise it overflows, as in the two's complement overflow rule. Slide 3 marks the "shift left ok" region on the wheel.

**Connections**: multiplication by shift-and-add appears in [[ECE270 week 11 10_31 - Binary arithmetic, codes and adders]]; adders in [[ECE270 week 11 11_02 - Adders, ALUs and shifters]]; multiplexers in [[ECE270 week 05 09_21 - Decoders, multiplexers and encoders]]. Next: [[ECE270 week 12 11_09 - State machine applications]].

**Sources**: `ECE 27000/week 12/11_07.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Adders and arithmetic circuits]] · [[Decoder and multiplexer]] · [[Number systems and codes]] · [[Verilog]]
