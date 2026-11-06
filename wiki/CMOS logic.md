---
type: concept
area: digital
areas: [digital]
source-ref: "ECE 270 lectures 08_24, 08_29 (Wakerly ch. 14)"
tags: [digital-logic]
---

# CMOS logic

**Summary**: Logic built from complementary pairs of NMOS and PMOS transistors; the pull-up and pull-down networks are duals, so gates are inverting. Also covers the analog side of gates: logic levels, noise margin, output resistance, load current and RC transition times.

## IC background
- Wafers and chips; SSI, MSI, LSI, VLSI, ULSI; transistor counts doubling about every two years (Moore's law); ENIAC (1945); first transistor (1947); DIP packages with 14, 20, 28 pins (Fig. 1-8). (source: 08_24.pdf, p. 2-8)
- Trend: lower supply voltage to cut power and heat, and allow fewer batteries. (source: 08_24.pdf, p. 23)

## Gates
- Inverter: PMOS (Q2) to $V_{DD}$ and NMOS (Q1) to ground, both gates tied to $V_{IN}$. Low in turns Q2 on and Q1 off, so $V_{OUT}$ is high; high in does the opposite (Figs. 14-6 to 14-8). Slides show both $V_{DD}=3.3$ V and $5.0$ V versions. (source: 08_24.pdf, p. 13-15)
- NAND: NMOS in series, PMOS in parallel; output low only when both inputs are high (Fig. 14-9). NOR is the dual: PMOS in series, NMOS in parallel (Fig. 14-11). 3-input NAND and an 8-input NAND built as a tree are also shown. (source: 08_24.pdf, p. 25-33)
- AND is NAND plus inverter (and OR is NOR plus inverter), so they are slower and bigger than NAND and NOR; the noninverting buffer is two inverters; AND-OR-INVERT and OR-AND-INVERT are single compound gates (Figs. 14-16 to 14-19). Each gate is shown as a transistor circuit, a switch model, a function table of which transistors are on, and a logic symbol. (source: 08_24.pdf, p. 13-39)
- Fan-in notes: NOR about 4, NAND about 6; NMOS is faster than PMOS (less resistance), so NAND beats NOR. Wider gates are multi-level trees (Fig. 14-13). (source: 08_24.pdf, p. 33)
- CMOS naturally gives inverting gates, which is why [[NAND and NOR universality]] matters in design.

## Circuit laws used
> [!definition] Circuit laws used in the lectures
> $$V = I R$$
> $$\frac{1}{R_{\text{parallel}}} = \frac{1}{R_1} + \dots + \frac{1}{R_n}$$
> $$\text{power} = IV = I^2 R = \frac{V^2}{R}$$
> $$Q = C V$$
> $$V_{\text{out}} = \frac{Z_2}{Z_1 + Z_2}\, V_{\text{in}}$$
> (source: 08_24.pdf, p. 17-21, 26)

Kirchhoff: KVL says voltage drops around a loop sum to zero; KCL says currents into a node sum to zero. Also reviewed: series and parallel resistance, power, capacitor, voltage divider. (source: 08_24.pdf, p. 17-21, 23)

## Logic levels and noise margin
- Outputs have a guard gap against inputs, the noise margin, with an invalid region between logic 0 and logic 1 (Fig. 14-1). Typical 5.0 V CMOS: logic 0 up to 1.5 V, undefined 1.5 to 3.5 V, logic 1 above 3.5 V (Fig. 14-2). (source: 08_24.pdf, p. 22-23)
- HC series: HIGH above $0.7\,V_{CC}$, LOW below $0.3\,V_{CC}$, "abnormal" between (Fig. 14-22). (source: 08_29.pdf, p. 4-6)
- The inverter transfer curve $V_{OUT}$ versus $V_{IN}$ is a sharp S-curve (Fig. 14-21); the steeper curve is more resilient to noise since it restores a clean level. (source: 08_29.pdf, p. 4-6)

> [!definition] Noise margins
> From Fig. 14-22 the high-state margin is $V_{OHmin} - V_{IHmin}$ and the low-state margin is $V_{ILmax} - V_{OLmax}$.
> (source: 08_29.pdf, p. 6; the formulas are read off the figure labels)

- Data sheets: test circuits and waveforms for HC-series logic (Fig. 14-20); the 54/74HC00 quad NAND (Table 14-1) lists $V_{IH}$, $V_{IL}$, $V_{OH}$, $V_{OL}$, input and output currents, quiescent supply current and switching characteristics such as $t_{PD}$. (source: 08_29.pdf, p. 2-3)

## Electrical behavior
- Resistive model of an output: a resistor $R_p$ to $V_{CC}$ and $R_n$ to ground, one large (over 1 M$\Omega$) and the other small (about 100-200 $\Omega$). A resistive load is replaced by its Thevenin equivalent (Figs. 14-23 to 14-25; refresher with a 28 V / 7 V two-battery circuit). (source: 08_29.pdf, p. 7-12)

> [!example] Output with a resistive load
> A 1 kohm and 2 kohm load give $R_{Th} = 667\ \Omega$ and $V_{Th} = 3.33$ V. Results: LOW output 0.43 V, HIGH output 4.61 V. (source: 08_29.pdf, p. 10-12)

- Sink and source current: $I_{OLmax}$ is the current the output can sink while staying LOW, $I_{OHmax}$ the current it can source while staying HIGH (Fig. 14-26). Table 14-2: for a CMOS load 0.02 mA at 0.1 V (LOW) and -0.02 mA at 4.4 V (HIGH); for a TTL load 4.0 mA at 0.33 V and -4.0 mA at 3.84 V. Fig. 14-27 estimates 5.0 mA sunk or 2.5 mA sourced into the example load. (source: 08_29.pdf, p. 12-14)
- Nonideal inputs: with $V_{IN}$ at 1.5 V or 3.5 V both transistors partly conduct, so output levels degrade (3.98 V and 0.93 V in the example) and current $I_{wasted}$ flows from $V_{CC}$ to ground. (source: 08_29.pdf, p. 15-17)
- Unused inputs: tie to another input, pull a NAND input up through a resistor, or pull a NOR input down (Fig. 14-31); floating inputs are not allowed. (source: 08_29.pdf, p. 18)
- Electrostatic discharge: see [[MOSFET]].

## Transition times
- Ideal zero-time versus real rise time $t_r$ and fall time $t_f$ (Fig. 14-32), measured between $V_{ILmax}$ and $V_{IHmin}$. Output load as $R_L$ and $C_L$ (Fig. 14-33). A HIGH-to-LOW fall goes through $R_n$ discharging $C_L$ (100 pF example); a LOW-to-HIGH rise goes through $R_p$ (Figs. 14-34 to 14-37). Rise and fall times are not symmetric. (source: 08_29.pdf, p. 21-27)

> [!definition] RC response used for transition times
> $$V_{out} = \frac{Q}{C} = \frac{1}{C}\int i\,dt$$
> $$\frac{di}{dt} = -\frac{1}{RC}\, i$$
> $$i = e^{-t/(RC)}$$
> (source: 08_29.pdf, p. 21; slide normalizes the initial current to 1)

- Propagation delays $t_{pHL}$ and $t_{pLH}$ are measured between 50% points (Fig. 14-38); worst-case timing uses the logic-level boundary points (Fig. 14-39). See [[Static timing and propagation delay]] and [[Timing diagram]].

## Other uses
- A 2-input multiplexer bit can be built from transmission gates (Fig. 8-20, Fig. 6-27). See [[Decoder and multiplexer]]. (source: 11_07.pdf, p. 8; 09_21.pdf, p. 14-20)

**Covered in**: ECE 270 08_24, 08_29 (ECE 27000/week 01/08_24.pdf, week 02/08_29.pdf)
**Sources**: `ECE 27000/week 01/08_24.pdf`, `ECE 27000/week 02/08_29.pdf`, `ECE 27000/week 05/09_21.pdf`, `ECE 27000/week 12/11_07.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[MOSFET]]
- [[Logic gate]]
- [[Static timing and propagation delay]]
- [[NAND and NOR universality]]
