---
type: lecture
area: digital
areas: [digital]
course: ece270
lecture: week 02 08_29
source-ref: "ECE 27000/week 02/08_29.pdf, 29 slides (Wakerly ch. 14 figures)"
tags: [digital-logic]
---

# ECE270 week 02 08_29 - CMOS electrical behavior

**Summary**: The analog side of digital gates: data-sheet parameters, the inverter transfer curve, noise margins, a resistive (Thevenin) model of a CMOS output driving a load, sink and source current, unused inputs, electrostatic discharge, and transition times from RC behavior. Continues [[CMOS logic]] from the previous lecture.

**File**: `ECE 27000/week 02/08_29.pdf`

---

## Topics
- **Data sheets (p. 2-3)**: test circuits and waveforms for HC-series logic (Fig. 14-20); the 54/74HC00 quad NAND data sheet (Table 14-1) lists $V_{IH}$, $V_{IL}$, $V_{OH}$, $V_{OL}$, input and output currents, quiescent supply current, and switching characteristics such as propagation delay $t_{PD}$.
- **Transfer characteristic and noise margin (p. 4-6)**: $V_{OUT}$ versus $V_{IN}$ of an inverter is a sharp S-curve (Fig. 14-21). A slide asks which of two curves (steep versus shallow) is more resilient to noise; the steep one, since it restores a clean level. HC-series levels: HIGH above $0.7\,V_{CC}$, LOW below $0.3\,V_{CC}$, "abnormal" between; the gaps between output and input thresholds are the high-state and low-state DC noise margins (Fig. 14-22).
- **Resistive model of an output (p. 7-12)**: a CMOS output is a resistor $R_p$ to $V_{CC}$ and $R_n$ to ground, one of them large (over 1 M$\Omega$) and the other small (about 100-200 $\Omega$). A resistive load is replaced by its Thevenin equivalent (Figs. 14-23 to 14-25; a Thevenin refresher with a 28 V / 7 V two-battery circuit, p. 10-11). With a 1 kohm and 2 kohm load, $R_{Th} = 667\ \Omega$ and $V_{Th} = 3.33$ V. Results: LOW output 0.43 V, HIGH output 4.61 V.
- **Sink and source current (p. 12-14)**: $I_{OLmax}$ is the current the output can sink while staying LOW, $I_{OHmax}$ the current it can source while staying HIGH (Fig. 14-26). Table 14-2: for a CMOS load the limits are 0.02 mA at 0.1 V (LOW) and -0.02 mA at 4.4 V (HIGH); for a TTL load 4.0 mA at 0.33 V and -4.0 mA at 3.84 V. Fig. 14-27 estimates 5.0 mA sunk or 2.5 mA sourced into the example load.
- **Nonideal inputs (p. 15-17)**: with $V_{IN}$ at 1.5 V or 3.5 V both transistors partly conduct, so output levels degrade (3.98 V and 0.93 V in the example) and current is wasted ($I_{wasted}$) from $V_{CC}$ to ground.
- **Unused inputs (p. 18)**: tie them to another input, pull a NAND input up through a resistor, or pull a NOR input down (Fig. 14-31); floating inputs are not allowed.
- **Electrostatic discharge (p. 19-20)**: $Q = CV$; wrist straps and static-shielding bags protect gate oxides.
- **Transition times (p. 21-27)**: ideal zero-time versus real rise time $t_r$ and fall time $t_f$ (Fig. 14-32), measured between $V_{ILmax}$ and $V_{IHmin}$. The output load is modeled as $R_L$ and $C_L$ (Fig. 14-33). A HIGH-to-LOW fall goes through $R_n$ discharging $C_L$ (100 pF example); a LOW-to-HIGH rise goes through $R_p$ (Figs. 14-34 to 14-37). Propagation delays $t_{pHL}$ and $t_{pLH}$ are measured between 50% points (Fig. 14-38). Worst-case timing uses the logic-level boundary points (Fig. 14-39). Slide note: rise and fall times are not symmetric.

## Key results
> [!definition] RC response used for transition times
> $$V_{out} = \frac{Q}{C} = \frac{1}{C}\int i\,dt$$
> $$\frac{di}{dt} = -\frac{1}{RC}\, i$$
> $$i = e^{-t/(RC)}$$
> (source: 08_29.pdf, p. 21; slide normalizes the initial current to 1)

> [!definition] Noise margins
> From Fig. 14-22 the high-state margin is $V_{OHmin} - V_{IHmin}$ and the low-state margin is $V_{ILmax} - V_{OLmax}$.
> (source: 08_29.pdf, p. 6; the formulas are read off the figure labels)

**Connections**: these delays are why a [[Timing diagram]] shows edges slightly after input changes, and why [[Static timing and propagation delay]] limits clock speed in later sequential-circuit lectures.

**Sources**: `ECE 27000/week 02/08_29.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[CMOS logic]] · [[MOSFET]] · [[Logic gate]] · [[Timing diagram]]
- [[ECE270 week 01 08_24 - Transistors and CMOS gates]]
