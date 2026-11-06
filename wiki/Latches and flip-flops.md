---
type: concept
area: digital
areas: [digital]
source-ref: "ECE 270 lecture 09_28 (Wakerly ch. 10)"
tags: [digital-logic]
---

# Latches and flip-flops

**Summary**: The 1-bit memory elements of sequential logic: the bistable pair, S-R and D latches, and the edge-triggered D and T flip-flops.

## Bistable element
- Two inverters feeding each other; two stable states and one metastable state (Figs. 10-1 to 10-3). (source: 09_28(2).pdf, p. 6-9)

## Latches
- S-R latch (NOR): S=R=0 holds; S=1,R=0 sets Q=1; S=0,R=1 clears; S=R=1 gives Q = QN = 0. (source: 09_28(2).pdf, p. 10-12)
- D latch: G=1 passes D to Q, G=0 holds. Setup and hold times around G. (source: 09_28(2).pdf, p. 14-16)

## Flip-flops
- Positive-edge D flip-flop from a master and a slave D latch with inverted clock; Q changes only at the rising edge. (source: 09_28(2).pdf, p. 17-20)
$$Q^{+} = D \text{ at the active edge}$$
- Preset and clear (PR_L, CLR_L) and enable (EN). (source: 09_28(2).pdf, p. 21-22)
- T flip-flop toggles (Fig. 10-18). Wiki note: standard behavior is
$$Q^{+} = Q \oplus T$$
which Fig. 10-19 realizes with a D flip-flop and XOR.

## Metastability
- A setup or hold violation can leave the output at the unstable equilibrium for an unbounded time. (source: 09_28(2).pdf, p. 8-9)

## In Verilog
- `VrDlatch`: `always @(D or G) if (G==1) Q <= D;`; `VrDff`: `always @(posedge CLK) Q <= D;`. See [[Verilog]]. (source: 09_28(2).pdf, p. 25)

## Where it appears
[[ECE270 week 06 09_28 - Latches and flip-flops]], [[ECE270 week 07 10_03 - Counters and shift registers]], [[ECE270 week 07 10_05 - Finite state machines]].

**Sources**: `ECE 27000/week 06/09_28(2).pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Sequential logic]]
- [[Counters and registers]]
- [[Finite state machine]]
- [[Timing diagram]]
- [[Static timing and propagation delay]]
- [[ECE270 week 06 09_28 - Latches and flip-flops]]
