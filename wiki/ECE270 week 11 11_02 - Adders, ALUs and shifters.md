---
type: lecture
area: digital
areas: [digital]
course: ece270
lecture: week 11 11_02
source-ref: "ECE 27000/week 11/11_02.pdf, 30 slides (Wakerly ch. 8 figures plus instructor slides)"
tags: [digital-logic]
---

# ECE270 week 11 11_02 - Adders, ALUs and shifters

**Summary**: Chapter 8 arithmetic hardware. Repeats the full adder, ripple adder and subtractor, then speeds up addition with carry lookahead (generate and propagate), builds 16-bit adders from 4-bit groups, introduces the ALU, writes adders in Verilog, and ends with parallel-prefix adders, shift versus rotate and barrel shifters.

**File**: `ECE 27000/week 11/11_02.pdf`

---

## Topics
- **Recap (p. 2-5)**: Fig. 8-1 full adder with $HS = A \oplus B$ and $CO = A B$; Fig. 8-2 4-bit ripple adder; Fig. 8-3 subtractor from adders. See [[ECE270 week 11 10_31 - Binary arithmetic, codes and adders]].
- **Carry lookahead stage (p. 6)**: Fig. 8-4 one stage of a carry-lookahead adder. The half sum $hs_i$ and the carry $c_i$ come from the lookahead logic and feed an XOR to give $s_i$. Slide note: if both $a_i$ and $b_i$ are 1, there is definitely a carry.
  $$g_i = a_i b_i$$
  $$s_i = hs_i \oplus c_i$$
- **Generate and propagate (p. 7)**: two forms of propagate, and the carry recurrence.
  $$p_i = a_i \oplus b_i \quad\text{or}\quad p_i = a_i + b_i$$
  $$c_{i+1} = g_i + p_i c_i$$
  Unrolling gives each carry as a two-level function of the inputs and $c_0$:
  $$c_1 = g_0 + p_0 c_0$$
  $$c_2 = g_1 + p_1 g_0 + p_1 p_0 c_0$$
  $$c_3 = g_2 + p_2 g_1 + p_2 p_1 g_0 + p_2 p_1 p_0 c_0$$
  $$c_4 = g_3 + p_3 g_2 + p_3 p_2 g_1 + p_3 p_2 p_1 g_0 + p_3 p_2 p_1 p_0 c_0$$
- **Half sum identity (p. 9)**: step by step, $hs_i = a_i \oplus b_i = (a_i + b_i)(a_i b_i)' = p_i g_i'$, so the sum can be formed from OR and AND signals the lookahead already needs.
- **74x283 (p. 8, 10)**: Fig. 8-5 symbol of the 4-bit binary adder with internal carry lookahead (inputs C0, A0-A3, B0-B3; outputs S0-S3, C4) and Fig. 8-6 its logic diagram.
- **16-bit adders from 4-bit groups (p. 11-12)**: Fig. 8-7 chains four 74x283 in a group-ripple adder (C4, C12 and C16 ripple between chips). Fig. 8-8 adds a lookahead carry circuit over the groups using group generate $G_g$ and group propagate $P_g$ signals, so the group carries do not ripple.
- **ALU (p. 13-14)**: Fig. 8-9 legacy ALU symbols 74x381, 74x382 and the lookahead unit 74x182; slide note: ALU means arithmetic logic unit. Table 8-1 functions by select inputs S2 S1 S0:
  - 000: F = 0000
  - 001: F = B minus A minus 1 plus CIN
  - 010: F = A minus B minus 1 plus CIN
  - 011: F = A plus B plus CIN
  - 100: F = A xor B
  - 101: F = A or B
  - 110: F = A and B
  - 111: F = 1111
- **Verilog ALU (p. 15)**: module `VrNbitALU(S, A, B, CIN, F, G_L, P_L)` with `parameter N = 8`. An `always @(*)` block computes generate `G[i] = (A[i]^(S==3'd1)) & (B[i]^(S==3'd2))` and propagate `P[i]` with OR in place of AND, accumulates group $G$ and $P$ in a loop (`GG = G[i] | (GG & P[i])`, `GP = GP & P[i]`), sets `G_L = ~GG; P_L = ~GP`, and a `case (S)` selects F as in Table 8-1.
- **Adder in Verilog (p. 16)**: module `VrNbitadder(A, B, CIN, S, COUT)` with `parameter N = 64` and one statement:
  `assign {COUT, S} = A + B + CIN;`
- **Selectable addition (p. 17-19)**: `Vraddersh` uses `always @(SEL, A, B, C, D)` with `if (SEL) S = A + B; else S = C + D;`, which Fig. 8-10(a) shows as two adders and a 2-input mux. Fig. 8-10(b) is one adder with muxes on the inputs. `Vradderse` writes the same selection as `assign S = (SEL) ? A + B : C + D;`.
- **Test bench for the adder/ALU (p. 20-21)**: module `VrNbitgcladd_tb` instantiates `VrNbitALU_e #(.N(N))` with `.S(3'b011)`. A `task checkadd` computes the expected sum `xpectS = A+B+CIN`, expected group generate `xpectG = ((A+B) >= 2**N)` and propagate `xpectP` (a 1 in every bit of A|B), and prints `$display("ERROR: ...")` on a mismatch. An `initial` block loops over all `ci`, `ai`, `bi`, applies each vector, waits `#10`, calls `checkadd`, then prints the error count and calls `$stop(1)`.
- **Hierarchy (p. 22)**: Fig. 8-11 a 16-bit group-carry-lookahead adder built from four `VrNbitGCLAdder` blocks (A[3:0] to A[15:12]) plus one `Vr4iLACckt` lookahead circuit with outputs Gs, Ps and COUT.
- **Parallel-prefix adder (p. 23-26)**: Fig. 8-12 general structure in three stages: pre-computation of initial prefixes ($g_i$, $p_i$), a carry lookahead (prefix) tree, and post-computation of sum bits with XORs. Fig. 8-13 the GPN reduction circuit that combines two neighbouring (G, P) pairs, in full and pruned at the boundaries. Fig. 8-14 prefix graph of a 16-bit Kogge-Stone adder (few levels, many wires); Fig. 8-15 prefix graph of a 16-bit Brent-Kung adder (fewer cells, more levels).
- **FPGA carry chain (p. 27)**: Fig. 8-16 the CARRY4 logic element, a hardwired 4-bit carry chain fed by lookup tables.
- **Shift versus rotate (p. 28)**: shift left by 1 multiplies by 2 and shift right by 1 divides by 2, with zeros entering at the vacated end; rotate wraps the bits that fall off back around to the other end.
- **Barrel shifter (p. 29-30)**: Fig. 8-17 a 16-bit barrel shifter made from sixteen 16-input, 1-bit-wide multiplexers, wired for left circular shifts, with select S[3:0]; Fig. 8-18 symbol for a 2-input, 16-bit-wide multiplexer (inputs A, B, select S, output Y).

## Key results
> [!definition] Generate and propagate
> $$g_i = a_i b_i$$
> $$p_i = a_i + b_i$$
> A stage generates a carry by itself when both inputs are 1, and propagates an incoming carry when either input is 1.
> (source: 11_02.pdf, p. 6-7)

> [!example] Carry recurrence
> $$c_{i+1} = g_i + p_i c_i$$
> Substituting repeatedly removes the ripple: each carry is a two-level function of $g$, $p$ and $c_0$.
> (source: 11_02.pdf, p. 7)

> [!warning] Cost of lookahead
> Wiki note: the unrolled carry terms grow with the bit position (the $c_4$ line already has five product terms), which is why the slides move to 4-bit groups and then prefix trees. The slides show the structure but give no delay or area numbers, so no speedup is claimed here.

> [!example] One-line adder
> `assign {COUT, S} = A + B + CIN;` leaves the choice of adder structure to the synthesis tool.
> (source: 11_02.pdf, p. 16)

**Connections**: ripple adder and subtractor from [[ECE270 week 11 10_31 - Binary arithmetic, codes and adders]]; multiplexers from [[ECE270 week 05 09_21 - Decoders, multiplexers and encoders]]; Verilog operators and `always` blocks from [[ECE270 week 05 09_19 - Verilog behavior and test benches]]. Next: [[ECE270 week 12 11_07 - Shifters, multipliers and division]].

**Sources**: `ECE 27000/week 11/11_02.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Adders and arithmetic circuits]] · [[Number systems and codes]] · [[Logic gate]] · [[Decoder and multiplexer]] · [[Verilog]]
