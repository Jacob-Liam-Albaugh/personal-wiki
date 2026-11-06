---
type: lecture
area: digital
areas: [digital]
course: ece270
lecture: week 12 11_09
source-ref: "ECE 27000/week 12/11_09(1).pdf, 8 slides (instructor slides)"
tags: [digital-logic]
---

# ECE270 week 12 11_09 - State machine applications

**Summary**: A short closing deck on where state machines are used beyond circuits: robots, a ticket-selling system, an ecology model, and the idea that a state machine can be written as a matrix acting on an input vector.

**File**: `ECE 27000/week 12/11_09(1).pdf`

---

## Topics
- **Where state machines are used (p. 2)**: "Very widely". Example: a seven-state strategy for a swarm of miniature robots transporting tall objects (Search Object, Move to Object, Close In on Object, Scan and Align, Push Object, Move Around Object, Evade), with transitions such as "object is near", "goal not seen", "lost contact" and timer events. Credited on the slide to Chen, Gauci and Gross, May 2013.
- **A simple controller (p. 3)**: a robot dog (Aibo) soccer behaviour as a state diagram: Walking To Unseen Ball, Head Scan For Ball, Turning For Ball, Walking To Seen Ball, Chin Pinch Turn, Kicking, Recover From Kick, with transitions such as "ball is seen" and "ball kicked". Source credited to a txstate.edu page.
- **Ticket selling system (p. 4)**: UML-style states Available, Locked, Sold. Lock moves Available to Locked; unlock or a timeout returns to Available; buy moves Locked to Sold; "assign to subscription" and "exchange" are further transitions involving Sold. Template credited to visual-paradigm.com.
- **Ecology model (p. 5-6)**: a cycle of Grass Growth, Rabbit Growth, Coyote Growth, Rabbit Decline. The next slide encodes the state as a vector [grass, rabbit, coyote] where 0 means decline and 1 means growth. States such as [0,0,0], [1,0,0], [1,1,0], [0,1,1] and [1,0,1] are connected by rain and drought transitions.
- **State machine and matrix (p. 7)**: a two-state machine S1, S2 with arrows S1 to S2 and S2 to S1, written as a table with current states as rows and next states as columns:
  - S1 row: S1 = 0, S2 = 1
  - S2 row: S1 = 1, S2 = 0
- **State transitions and inputs (p. 8)**: a three-state table whose columns are the inputs x, y, z. An input column vector is combined with the table to give an output column vector. Rows: S1 = (0, 1, 1), S2 = (1, 0, 1), S3 = (0, 0, 1). With input (x, y, z) = (0, 1, 0) the result is (1, 0, 0).

## Key results
> [!definition] Transition matrix view
> The table is a matrix $M$ with one row per current state.
> $$\text{out} = M \cdot \text{in}$$
> For the slide's example, $M = ((0,1,1),(1,0,1),(0,0,1))$ and in $= (0,1,0)$ give out $= (1,0,0)$.
> (source: 11_09(1).pdf, p. 8)

> [!example] Not only hardware
> The same state, input and transition vocabulary describes robots, ticketing and ecological models, not just clocked circuits.
> (source: 11_09(1).pdf, p. 2-6)

> [!warning] Reading the matrix slides
> Wiki note: the slides give only the tables and no equations, so the matrix reading above is the wiki's interpretation of the arrangement. The ecology transition rules (which of rain or drought applies at each arrow) are not fully legible at the montage resolution **[unverified]**.

**Connections**: formal machines are in [[ECE270 week 07 10_05 - Finite state machines]] and [[ECE270 week 08 10_12 - State machine design and Verilog]]. Previous: [[ECE270 week 12 11_07 - Shifters, multipliers and division]]. This is the last lecture in the set.

**Sources**: `ECE 27000/week 12/11_09(1).pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Finite state machine]] · [[Sequential logic]] · [[Logic gate]]
