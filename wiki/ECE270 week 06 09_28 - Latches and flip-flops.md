---
type: lecture
area: digital
areas: [digital]
course: ece270
lecture: week 06 09_28
source-ref: "ECE 27000/week 06/09_28(2).pdf, 28 slides (Wakerly ch. 10 figures plus instructor slides)"
tags: [digital-logic]
---

# ECE270 week 06 09_28 - Latches and flip-flops

**Summary**: Starts sequential logic. A clock coordinates blocks; two cross-coupled inverters form a bistable element with a metastable point; from it come the S-R latch, D latch, edge-triggered D flip-flop, T flip-flop, and their Verilog models.

**File**: `ECE 27000/week 06/09_28(2).pdf`

---

## Topics
- **Combinational vs sequential (p. 2-5)**: unlabeled block diagrams; adding a CLOCK block coordinates the others. The clock is a square wave between 0 V and 5 V with a time period (p. 4). Sequential circuits are chains of blocks all driven by the clock (p. 5). See [[Sequential logic]].
- **Bistable element (p. 6-9)**: Fig. 10-1, two inverters feeding each other give outputs Q and Q_L. Fig. 10-2 transfer functions show two stable points and one metastable point; Fig. 10-3 is a ball-and-hill analogy (stable in either valley, metastable on top). See [[Latches and flip-flops]].
- **S-R latch with NOR gates (p. 10-12)**: Fig. 10-4 function table: S=0,R=0 holds the last Q; S=0,R=1 gives Q=0, QN=1; S=1,R=0 gives Q=1, QN=0; S=1,R=1 gives Q=0 and QN=0, so QN is not always Q'. Fig. 10-5 typical operation, including S and R asserted together. Fig. 10-6 symbols (bubble-to-bubble preferred; a symbol with double negation is incorrect). Fig. 10-7 timing parameters: $t_{pLH(SQ)}$, $t_{pHL(RQ)}$ and minimum pulse width $t_{pw(min)}$.
- **S-R latch with NAND gates and gated version (p. 13)**: Fig. 10-8 with function table of D, EN, CLK.
- **D latch (p. 14-16)**: Fig. 10-9 NAND design, G=1 passes D to Q, G=0 holds the last value. Fig. 10-10 behavior for various inputs; Fig. 10-11 timing parameters $t_{pLH(GQ)}$, $t_{pHL(DQ)}$ with setup and hold times.
- **Edge-triggered D flip-flop (p. 17-20)**: Fig. 10-12, a positive-edge-triggered D flip-flop built from two D latches (master QM and slave) with the clock inverted for the master. Fig. 10-13 functional behavior (Q changes only at the rising edge); Fig. 10-14 timing with $t_{pLH(CQ)}$, $t_{pHL(CQ)}$, setup and hold. Fig. 10-15 negative-edge-triggered version.
- **Preset, clear, enable (p. 21-22)**: Fig. 10-16 D flip-flop with preset (PR_L) and clear (CLR_L) from NAND gates; Fig. 10-17 with enable EN.
- **T flip-flop (p. 23-27)**: T means toggle (Fig. 10-18). Fig. 10-19 builds T from D plus feedback, with an XOR for the enable version; Fig. 10-20 T flip-flop with enable.
- **Verilog (p. 25)**: `VrDlatch`: `always @(D or G) if (G==1) Q <= D;`. `VrDff`: `always @(posedge CLK) Q <= D;` with `output reg Q`. See [[Verilog]].
- **Library parts (p. 28)**: Table 10-1 lists latches and positive-edge flip-flops in Xilinx ISE 8.1, 7-Series and LSI Logic names (for example LDCE, FDC, FDCE, FTC), with variants for async clear/preset and clock enable.

## Key results
> [!definition] D flip-flop
> $$Q^{+} = D \text{ at the active clock edge}$$
> Q holds its value otherwise. Master and slave D latches give edge triggering.
> (source: 09_28(2).pdf, Fig. 10-12, 10-13)

> [!definition] T flip-flop
> $$Q^{+} = Q \oplus T$$
> Wiki note: this is the standard T behavior implied by Fig. 10-19(a) (D tied to Q xor T); the slide itself shows the circuit and waveform.

> [!failure] Metastability
> The bistable element has a third, unstable equilibrium. An input that violates setup or hold time can leave Q there for an unbounded time (p. 8-9, Fig. 10-2, 10-3).

**Connections**: uses gates from [[ECE270 week 05 09_21 - Decoders, multiplexers and encoders]] and propagation delay ideas from [[ECE270 week 02 08_29 - CMOS electrical behavior]]. Next: [[ECE270 week 07 10_03 - Counters and shift registers]].

**Sources**: `ECE 27000/week 06/09_28(2).pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Latches and flip-flops]] · [[Sequential logic]] · [[Finite state machine]] · [[Timing diagram]] · [[Verilog]] · [[Logic gate]]
