---
type: lecture
area: digital
areas: [digital]
course: ece270
lecture: week 04 09_12
source-ref: "ECE 27000/week 04/09_12.pdf, 28 slides (Wakerly ch. 3-5 figures plus instructor slides)"
tags: [digital-logic]
---

# ECE270 week 04 09_12 - Hazards, documentation and timing

**Summary**: Finishes timing hazards (static-1, static-0, dynamic) and the K-map fix for static-1, then moves to chapter 4: how to document a design, gate symbols, propagation delay and the factors that change it, and design-flow vocabulary. Ends with the first Verilog slides (module syntax).

**File**: `ECE 27000/week 04/09_12.pdf`

---

## Topics
- **Static hazards (p. 2-5)**: a static-1 hazard is a pair of input combinations that differ in one variable and both give 1, yet a momentary 0 can occur during the transition. A static-0 hazard is the same with outputs 0 and a momentary 1. Fig. 3-26 uses $F = XZ' + YZ$ with $X=Y=1$ and $Z$ changing; the inverter delay makes $XZ'$ fall before $YZ$ rises. In an AND-OR circuit a static-0 hazard needs a variable and its complement feeding the same AND gate, which is usually a mistake (Fig. 3-27).
- **Removing the hazard (p. 5-6)**: add the consensus term, one more product that covers the two adjacent K-map groups (Fig. 3-28, 3-29): $F = XZ' + YZ + XY$. See [[Karnaugh map]].
- **Dynamic hazard (p. 6)**: Fig. 3-31, output makes three or more transitions where one is expected, because of paths with different delays.
- **Describing designs (p. 7-9)**: specification, block diagram, logic description, HDL, schematic, logic diagram, timing diagram, circuit description with assumptions, test plan. Explain why before how. Slide jokes: undocumented work gets you fired or never promoted. Use the right level of abstraction; show interfaces first (Fig. 4-2: do not draw 32 separate lines).
- **Gate symbols (p. 10-12)**: Fig. 4-3 shapes (AND, OR, buffer, NAND, NOR, inverter, bubbles). A buffer strengthens a signal (low lower, high higher). Fig. 4-4 shows equivalent symbols under generalized DeMorgan. See [[Logic gate]].
- **Unused inputs (p. 13)**: Fig. 4-9, tie unused inputs to constant 0 or 1 appropriate to the gate.
- **Timing diagrams (p. 15-17)**: Fig. 4-19 causality, propagation delay, rise time (LOW to HIGH) and fall time (HIGH to LOW), minimum and maximum delay. Fig. 4-20 data signals on a bus with setup, hold, unknown region. Slide note: treat rise and fall as symmetric. See [[Timing diagram]].
- **Factors affecting delay (p. 17)**: supply voltage (higher is faster), temperature (higher is slower), output load, input slew, asymmetric LOW-to-HIGH and HIGH-to-LOW, speed of light (about 0.3 m per ns), manufacturing variation, signal paths, transmission-line effects, noise. Solution: margin of safety.
- **Product binning (p. 18)**: the same part sold fast (expensive), typical, slow (cheap), or discarded. Design Automation Conference shown as industry context (p. 14).
- **Delay tables (p. 19-21)**: Tables 4-2 (SSI) and 4-3 (MSI) give propagation delay in ns for 74AC at 5.0 V and 74HC at 2.0 V and 4.5 V, typical and maximum at 25 C and 85 C. Wiki note: numbers were not transcribed because the render is too small to read reliably.
- **Terms (p. 22-24)**: timing closure (analyze, meet constraint, revise, repeat), RTL, layout and placement, routing, verification (functional and timing), fitting, netlist. HDL and IP reuse are trends; hardware design is like writing code.
- **Verilog start (p. 24-28)**: Fig. 5-1 modules, one module or modules instantiating others hierarchically. Behavioral model versus structural model; instantiate a module to create hardware (like objects); one module per file with the same name; C++ style comments. Example module `VrInhibit` with `assign Z = X & ~Y;`. Verilog is case sensitive; use meaningful names. Table 5-1 gives module declaration syntax: input, output, inout, net, variable, parameter, function, task declarations, then concurrent statements. See [[Verilog]].

## Key results
> [!definition] Static hazards
> Static-1: output should stay 1 but glitches to 0.
> Static-0: output should stay 0 but glitches to 1.
> (source: 09_12.pdf, p. 2)

> [!example] Fix for the Fig. 3-26 circuit
> Original:
> $$F = XZ' + YZ$$
> With the extra covering term:
> $$F = XZ' + YZ + XY$$
> (source: 09_12.pdf, p. 5)

> [!example] Smallest Verilog module (p. 26)
> $$Z = X \cdot Y'$$
> written as `assign Z = X & ~Y;` in module `VrInhibit` (also called BUT-NOT).

**Connections**: hazards follow from gate delays ([[ECE270 week 02 08_29 - CMOS electrical behavior]]) and from minimization ([[ECE270 week 03 09_07 - Circuit analysis and Karnaugh maps]]). Verilog continues in [[ECE270 week 04 09_14 - Verilog modules and combinational design]].

**Sources**: `ECE 27000/week 04/09_12.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Hazards]] · [[Timing diagram]] · [[Karnaugh map]] · [[Logic gate]] · [[Verilog]] · [[Boolean algebra]]
