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
- Sum is 1 when an odd number of inputs are 1; carry when at least two are (read from the Table 2-3 rows; the slides show only the table). (source: 10_26.pdf, p. 15-18)
- Half adder: half sum $HS = A \oplus B$, carry-out $CO = A B$. Fig. 8-1 gives the gate-level full adder, its symbol and an alternate symbol suitable for cascading. (source: 10_31.pdf, p. 21-22)
- Subtractor: an adder with the B input inverted and $c_{in} = 1$ (Fig. 8-3). As a standalone full subtractor:
$$D = A \oplus B \oplus B_{IN}$$
$$B_{OUT} = A' B + A' B_{IN} + B B_{IN}$$
(source: 10_31.pdf, p. 24)

## Ripple adder
- Fig. 8-2: four full adders with carry chain $c_0 \to c_1 \to c_2 \to c_3 \to c_4$ and sums $s_0$ to $s_3$. The carry must ripple through the stages, so delay grows linearly with n. (source: 10_31.pdf, p. 23)
$$t_{ADD} = t_{ABCout} + (n-2)\, t_{CinCout} + t_{CinS}$$

## Carry lookahead
> [!definition] Generate and propagate
> $$g_i = a_i b_i$$
> $$p_i = a_i + b_i \quad\text{(or } p_i = a_i \oplus b_i\text{)}$$
> A stage generates a carry by itself when both inputs are 1, and propagates an incoming carry when either input is 1.
> (source: 11_02.pdf, p. 6-7)

- One lookahead stage (Fig. 8-4): the half sum $hs_i$ and the carry $c_i$ from the lookahead logic feed an XOR, $s_i = hs_i \oplus c_i$. (source: 11_02.pdf, p. 6)
- Carry recurrence $c_{i+1} = g_i + p_i c_i$; unrolling removes the ripple, so each carry is a two-level function of the inputs and $c_0$:
$$c_1 = g_0 + p_0 c_0$$
$$c_2 = g_1 + p_1 g_0 + p_1 p_0 c_0$$
$$c_3 = g_2 + p_2 g_1 + p_2 p_1 g_0 + p_2 p_1 p_0 c_0$$
$$c_4 = g_3 + p_3 g_2 + p_3 p_2 g_1 + p_3 p_2 p_1 g_0 + p_3 p_2 p_1 p_0 c_0$$
(source: 11_02.pdf, p. 7)
- Half sum identity: $hs_i = a_i \oplus b_i = (a_i + b_i)(a_i b_i)' = p_i g_i'$, so the sum can be formed from OR and AND signals the lookahead already needs. (source: 11_02.pdf, p. 9)
- Wiki note: the unrolled terms grow with bit position (the $c_4$ line already has five product terms), which is why the slides move to 4-bit groups and then prefix trees. The slides give no delay or area numbers, so no speedup is claimed here.
- 74x283 4-bit binary adder with internal lookahead (Figs. 8-5, 8-6: inputs C0, A0-A3, B0-B3; outputs S0-S3, C4). (source: 11_02.pdf, p. 8, 10)
- 16-bit adders from 4-bit groups: four 74x283 in a group-ripple adder (C4, C12, C16 ripple between chips, Fig. 8-7), or a lookahead carry circuit over group generate $G_g$ and group propagate $P_g$ so group carries do not ripple (Fig. 8-8). Hierarchy (Fig. 8-11): four `VrNbitGCLAdder` blocks plus one `Vr4iLACckt` lookahead circuit with outputs Gs, Ps and COUT. (source: 11_02.pdf, p. 11-12, 22)
- Parallel-prefix adders (Fig. 8-12): pre-computation of $g_i, p_i$, a prefix tree, then post-computation of the sums with XORs. Fig. 8-13 the GPN cell combining two neighbouring (G, P) pairs, full and pruned at the boundaries. Kogge-Stone (Fig. 8-14: few levels, many wires) versus Brent-Kung (Fig. 8-15: fewer cells, more levels), both 16-bit. (source: 11_02.pdf, p. 23-26)
- FPGA carry chain: CARRY4 element, a hardwired 4-bit carry chain fed by lookup tables (Fig. 8-16). (source: 11_02.pdf, p. 27)

## ALU
Table 8-1, functions by select inputs S2 S1 S0 (legacy parts 74x381, 74x382 and lookahead unit 74x182, Fig. 8-9). (source: 11_02.pdf, p. 13-14)
- 000: F = 0000
- 001: F = B minus A minus 1 plus CIN
- 010: F = A minus B minus 1 plus CIN
- 011: F = A plus B plus CIN
- 100: F = A xor B
- 101: F = A or B
- 110: F = A and B
- 111: F = 1111

## Shift and rotate
- Shift left by 1 multiplies by 2 and shift right by 1 divides by 2; zeros enter at the vacated end and bits shifted out are discarded. Rotate (circular shift) wraps the bits that leave one end into the other end. Care is needed with sign bits. (source: 11_02.pdf, p. 28; 11_07.pdf, p. 2)
- Terms: (1) shift, (2) rotate, (3) logical shift (the left-most bit is not a sign), (4) arithmetic shift (the left-most bit is a sign). An arithmetic right shift replicates the MSB so the sign survives. (source: 11_07.pdf, p. 4, 9)
- Counter wheel (Fig. 2-3) annotated with "shift left ok" where the result stays in range; an arithmetic left shift overflows otherwise, as in the two's complement overflow rule (see [[Number systems and codes]]). (source: 11_07.pdf, p. 3)

## Barrel shifter
- First design (Fig. 8-17): a 16-bit left circular shifter from sixteen 16-input, 1-bit-wide multiplexers with select S[3:0]. Fig. 8-18 is the symbol of a 2-input, 16-bit-wide multiplexer. (source: 11_02.pdf, p. 29-30; 11_07.pdf, p. 5-6)
- Staged design (Fig. 8-19): four 2-input 16-bit multiplexers in series; stage $k$ either passes its input or rotates it left by $2^k$ places, selected by $S_k$. Fig. 8-20 shows one multiplexer bit built from transmission gates (see [[CMOS logic]]). (source: 11_07.pdf, p. 7-8)
$$\text{shift} = 8 S_3 + 4 S_2 + 2 S_1 + S_0$$
(Wiki note: this formula follows from the four stages S0 to S3 in Fig. 8-19; the slides do not state it.)
- Table 8-2, shift types: name, 3-bit code C, Verilog function, note. (source: 11_07.pdf, p. 9)
  - Left rotate, Lrotate, 000, Vrol, wrap-around
  - Right rotate, Rrotate, 001, Vror, wrap-around
  - Left logical, Llogical, 010, Vsll, 0 into LSB
  - Right logical, Rlogical, 011, Vslr, 0 into MSB
  - Left arithmetic, Larith, 100, Vsla, 0 into LSB
  - Right arithmetic, Rarith, 101, Vsra, replicate MSB
- Fig. 8-21 components: a rotate block `ROLR16`, a `FIXUP` for left shifts and a `FIXUP` for right shifts (they force wrapped-around bits to 0 or to the sign), with S[3:0] and C[2:0] driving other logic. (source: 11_07.pdf, p. 11)

## Multiply and divide
- Partial products: an 8 by 8 multiplication is eight rows $y_j x_i$, each shifted one place, added to give $p_{15}$ to $p_0$ (Fig. 8-22); the same shift-and-add as $11 \times 13 = 143$. (source: 11_07.pdf, p. 12)
- Combinational (array) multiplier: rows of adders (Fig. 8-23); Fig. 8-24 reroutes the interconnections so each row's carries go to the next row instead of rippling along it, giving a faster version; Fig. 8-25 gives the Verilog names `PCS`, `PCC`, `RAS`, `RAC` for partial sum and carry signals. (source: 11_07.pdf, p. 13-15)
- Division variables (Fig. 8-26): DVND (dividend), DVSR (divisor), QUOT, REM; a $2n$-bit working register `RDIV` whose upper half is compared against DVSR; each step shifts left, subtracts (DIFF = upper half minus DVSR) and records a quotient bit. (source: 11_07.pdf, p. 16)

## In Verilog
- One-line adder; the synthesis tool picks the structure:
```verilog
module VrNbitadder(A, B, CIN, S, COUT);  // parameter N = 64
  assign {COUT, S} = A + B + CIN;
```
(source: 11_02.pdf, p. 16)
- ALU `VrNbitALU(S, A, B, CIN, F, G_L, P_L)`, `parameter N = 8`: an `always @(*)` block computes generate `G[i] = (A[i]^(S==3'd1)) & (B[i]^(S==3'd2))` and propagate `P[i]` with OR in place of AND, accumulates group G and P in a loop (`GG = G[i] | (GG & P[i])`, `GP = GP & P[i]`), sets `G_L = ~GG; P_L = ~GP`, and a `case (S)` selects F as in Table 8-1. (source: 11_02.pdf, p. 15)
- Selectable addition: `Vraddersh` with `if (SEL) S = A + B; else S = C + D;` synthesizes to two adders and a 2-input mux (Fig. 8-10a); one adder with muxes on its inputs is Fig. 8-10b; `Vradderse` writes `assign S = (SEL) ? A + B : C + D;`. (source: 11_02.pdf, p. 17-19)
- Barrel shifter `Vrbarrel16(DIN, S, C, DOUT)`: 16-bit data, 4-bit shift amount S (0 to 15), 3-bit mode C with parameters naming the six codes. Functions loop `N = S` times, e.g. `Vrol` with `TMPD = {TMPD[14:0], TMPD[15]}` and `Vror` with `TMPD = {TMPD[0], TMPD[15:1]}`; the body is `always @ (DIN or S or C) case (C)` with one `DOUT = Vrol(DIN,S)`-style line per code and `default: DOUT = DIN;`. (source: 11_07.pdf, p. 10)
- Adder/ALU test bench `VrNbitgcladd_tb`: instantiates `VrNbitALU_e #(.N(N))` with `.S(3'b011)`; a `task checkadd` computes expected sum `xpectS = A+B+CIN`, group generate `xpectG = ((A+B) >= 2**N)` and propagate `xpectP` (a 1 in every bit of A|B) and prints `$display("ERROR: ...")` on a mismatch; an `initial` block loops over all `ci`, `ai`, `bi`, applies each vector, waits `#10`, calls `checkadd`, prints the error count and calls `$stop(1)`. See [[Verilog]]. (source: 11_02.pdf, p. 20-21)

**Covered in**: ECE 270 10_26, 10_31, 11_02, 11_07 (ECE 27000/week 10/10_26.pdf, week 11/10_31.pdf, week 11/11_02.pdf, week 12/11_07.pdf)
**Sources**: `ECE 27000/week 10/10_26.pdf`, `ECE 27000/week 11/10_31.pdf`, `ECE 27000/week 11/11_02.pdf`, `ECE 27000/week 12/11_07.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Number systems and codes]]
- [[Logic gate]]
- [[Decoder and multiplexer]]
- [[Static timing and propagation delay]]
- [[Verilog]]
