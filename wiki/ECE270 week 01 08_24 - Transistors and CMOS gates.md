---
type: lecture
area: digital
areas: [digital]
course: ece270
lecture: week 01 08_24
source-ref: "ECE 27000/week 01/08_24.pdf, 43 slides (Wakerly ch. 1 and ch. 14 figures)"
tags: [digital-logic]
---

# ECE270 week 01 08_24 - Transistors and CMOS gates

**Summary**: Where logic gates come from physically. Integrated-circuit history and Moore's law, a quick circuits review (Kirchhoff, Ohm, resistors, power, capacitors, voltage divider), logic levels and noise margins, then MOS transistors as voltage-controlled switches and the [[CMOS logic]] inverter, NAND, NOR, AND and AND-OR-INVERT gates.

**File**: `ECE 27000/week 01/08_24.pdf`

---

## Topics
- **IC terms and history (p. 2-8)**: wafers and chips; SSI, MSI, LSI, VLSI, ULSI; transistor counts doubling about every two years (Moore's law); ENIAC (1945); first transistor (1947); DIP packages with 14, 20, 28 pins (Fig. 1-8).
- **Transistor as switch (p. 9-12, 22-24)**: [[MOSFET]] (metal-oxide-semiconductor field-effect transistor), n-type and p-type; together they form CMOS. A MOS transistor is a voltage-controlled resistance: raising $V_{gs}$ lowers $R_{ds}$ in an NMOS, the reverse in a PMOS. The gate looks like a capacitor, so no current flows into it. Slide note: CMOS replaced bipolar transistors because it uses less energy (p. 9). Physical structure of NMOS and PMOS on p. 24.
- **CMOS gates (p. 13-18, 25-39)**: inverter, 2-input NAND, 2-input NOR, 3-input NAND, 8-input NAND built as a tree, noninverting buffer, AND (NAND plus inverter), AND-OR-INVERT and OR-AND-INVERT (Figs. 14-16 to 14-19). Each gate is shown as a transistor circuit, a switch model, a function table with the on/off state of every transistor, and its logic symbol.
- **Circuits review (p. 17-21, 23)**: Kirchhoff's laws (KVL: voltage drops around a loop sum to zero; KCL: currents into a node sum to zero); Ohm's law; series and parallel resistance; power; capacitor; voltage divider.
- **Logic levels (p. 22-23)**: Fig. 14-1 outputs have a guard gap against inputs, the noise margin, with an invalid region between logic 0 and logic 1. Typical CMOS at 5.0 V: logic 0 up to 1.5 V, undefined from 1.5 to 3.5 V, logic 1 above 3.5 V (Fig. 14-2). Trend: lower supply voltage to cut power and heat, and allow fewer batteries.

## Key results
> [!definition] Circuit laws used in the lecture
> $$V = I R$$
> $$\frac{1}{R_{\text{parallel}}} = \frac{1}{R_1} + \dots + \frac{1}{R_n}$$
> $$\text{power} = IV = I^2 R = \frac{V^2}{R}$$
> $$Q = C V$$
> $$V_{\text{out}} = \frac{Z_2}{Z_1 + Z_2}\, V_{\text{in}}$$
> (source: 08_24.pdf, p. 17-21, 26)

- Inverter: PMOS (Q2) to $V_{DD}$ and NMOS (Q1) to ground, both gates tied to $V_{IN}$. Low input turns Q2 on and Q1 off, so $V_{OUT}$ is high; high input does the opposite (Figs. 14-6 to 14-8). Slides show both $V_{DD}=3.3$ V and $5.0$ V versions.
- NAND: NMOS in series, PMOS in parallel; output low only when both inputs are high (Fig. 14-9). NOR is the dual: PMOS in series, NMOS in parallel (Fig. 14-11).
- Slide note: NOR fan-in is typically limited to 4 and NAND to 6; NMOS is faster than PMOS (less resistance), so NAND is faster than NOR (p. 33). Wider gates are built as multi-level trees (Fig. 14-13).
- AND and OR need an extra inverter stage, so they are slower and bigger than NAND and NOR.

**Connections**: CMOS naturally gives inverting gates, which is why [[NAND and NOR universality]] matters in design. Gate behavior is abstracted in [[Logic gate]]; the algebra for combining them is [[Boolean algebra]]. Previous lecture: [[ECE270 week 01 08_22 - Intro and number systems]].

**Sources**: `ECE 27000/week 01/08_24.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[CMOS logic]] · [[MOSFET]] · [[Logic gate]] · [[Boolean algebra]] · [[NAND and NOR universality]]
- [[ECE270 week 01 08_22 - Intro and number systems]] · [[ECE270 week 02 08_29 - CMOS electrical behavior]]
