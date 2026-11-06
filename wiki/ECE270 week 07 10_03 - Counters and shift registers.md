---
type: lecture
area: digital
areas: [digital]
course: ece270
lecture: week 07 10_03
source-ref: "ECE 27000/week 07/10_03.pdf, 26 slides (Wakerly ch. 11 figures plus instructor slides)"
tags: [digital-logic]
---

# ECE270 week 07 10_03 - Counters and shift registers

**Summary**: Counters (ripple, synchronous with serial or parallel enable, the CNTR4U part and its Verilog), decoding glitches and how a register removes them, and shift registers (serial and parallel variants, the universal SHRG4U, ring counters).

**File**: `ECE 27000/week 07/10_03.pdf`

---

## Topics
- **Counter as a state machine (p. 2)**: Fig. 11-1, a single cycle of states S1, S2, ..., Sm; an n-bit binary counter counts $0, 1, \dots, 2^n - 1$ and wraps.
- **Ripple counter (p. 3)**: Fig. 11-2, 4-bit ripple counter of T flip-flops where only the first has the clock. Saves dynamic energy but is too slow and rarely used.
- **Synchronous counters (p. 4-5)**: Fig. 11-3 with serial enable logic has a long propagation path through the AND chain; Fig. 11-4 with parallel enable logic has a shorter path. Fig. 11-5 is the logic diagram of the CNTR4U 4-bit synchronous binary counter; slide notes D flip-flops are more common in FPGAs.
- **CNTR4U function (p. 6-8)**: Table 11-1 state table with inputs CLR, LD, ENT, ENP. CLR=1 clears; LD=1 loads D3..D0; with ENT and ENP both 1 it counts up; otherwise it holds. Fig. 11-6 free-running connections; Fig. 11-7 waveforms of a divide-by-16 counter showing QA toggling at half the clock rate, QB at a quarter, and RCO high at count 15.
- **Decoding a counter (p. 9-11)**: Fig. 11-8 a modulo-8 counter plus 3-to-8 decoder; Fig. 11-9 timing shows decoding glitches on outputs S0_L..S7_L when several counter bits change together; Fig. 11-10 fixes this by registering decoder outputs in an 8-bit register clocked by the same clock, giving glitch-free outputs RS0_L..RS7_L.
- **Verilog counter (p. 12)**: `Vrcntr4u` with `always @(posedge CLK)`: `if (CLR) Q <= 4'd0; else if (LD) Q <= D; else if (ENT && ENP) Q <= Q + 1; else Q <= Q;` and a combinational `RCO` block (`if (ENT && (Q == 4'd15)) RCO = 1`), the slide marks the comment text "not necessary" for the else holding branch. Fig. 11-11 simulation timing diagram for a test bench with variants (binary, decade, excess-3, up/down).
- **Shift register purpose (p. 14)**: parallel data in and out, serial data in and out, 1-bit cells moving the MSB toward the LSB.
- **Shift register structures (p. 15-18)**: serial-in serial-out (Fig. 11-12), serial-in parallel-out (Fig. 11-13), parallel-in serial-out with LOAD/SHIFT gating (Fig. 11-14), parallel-in parallel-out (Fig. 11-15).
- **Universal shift register (p. 19-20)**: SHRG4U logic diagram and symbol (Fig. 11-16). Table 11-2: CLR=1 clear; (S1,S0)=00 hold; 01 shift right (QA takes RIN); 10 shift left (QD takes LIN); 11 load A, B, C, D.
- **Ring counters (p. 21-26)**: Fig. 11-17 simplest 4-bit ring counter with single circulating 1 using SHRG4U shifting left and Q3 fed back; Fig. 11-18 timing (states S1 to S4 repeating); Fig. 11-19 state diagram has the main cycle 0001, 0010, 0100, 1000 plus unused cycles (0000, 1111, 0101/1010, and others) that never rejoin. Fig. 11-20 and 11-21 add a NOR-style gate to make it self-correcting: every unused state eventually leads to the main cycle.

## Key results
> [!definition] Synchronous binary counter
> $$Q^{+} = Q + 1 \pmod{2^n}\quad \text{when enabled}$$
> All flip-flops share one clock; enable logic decides which toggle.
> (source: 10_03.pdf, Fig. 11-3 to 11-5, Table 11-1)

> [!failure] Decoding glitches (p. 10)
> Outputs decoded combinationally from a counter can glitch when more than one counter bit changes. Register the decoded outputs to remove the glitches.

> [!definition] Ring counter
> A shift register whose last output feeds its first input with a single 1; period equals the number of bits. A self-correcting design maps every illegal state back to the legal cycle.

**Connections**: built on flip-flops from [[ECE270 week 06 09_28 - Latches and flip-flops]]; decoders from [[ECE270 week 05 09_21 - Decoders, multiplexers and encoders]]; the glitch issue echoes [[ECE270 week 04 09_12 - Hazards, documentation and timing]]. Next: [[ECE270 week 07 10_05 - Finite state machines]].

**Sources**: `ECE 27000/week 07/10_03.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Counters and registers]] · [[Latches and flip-flops]] · [[Finite state machine]] · [[Sequential logic]] · [[Verilog]] · [[Timing diagram]]
