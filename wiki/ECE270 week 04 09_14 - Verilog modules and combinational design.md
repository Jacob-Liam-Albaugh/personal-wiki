---
type: lecture
area: digital
areas: [digital]
course: ece270
lecture: week 04 09_14
source-ref: "ECE 27000/week 04/09_14.pdf, 29 slides (Wakerly ch. 5 tables 5-1 to 5-16)"
tags: [digital-logic]
---

# ECE270 week 04 09_14 - Verilog modules and combinational design

**Summary**: Verilog syntax tour from Wakerly chapter 5: module and port declarations, the four logic states, nets and variables, literals, vectors, operators, built-in gates and instance statements, and structural examples (alarm circuit, an inhibit gate, a XOR built from inhibit gates).

**File**: `ECE 27000/week 04/09_14.pdf`

---

## Topics
- **Module and ports (p. 2-5, 7)**: `module VrInhibit(X, Y, Z); input X, Y; output Z; assign Z = X & ~Y; endmodule` (p. 2). Table 5-1 module syntax; Table 5-2 input, output, inout declarations, with optional `[msb:lsb]` for vectors, one bit each otherwise. New ANSI-style syntax puts directions in the port list: `module VrInhibit(input X, Y, output Z);` (p. 7).
- **Four states (p. 5)**: `0` false, `1` true, `x` unknown, `z` high impedance (three-state logic).
- **Bitwise operators (p. 6, Table 5-3)**: `&` AND, `|` OR, `^` XOR, `~^` or `^~` XNOR, `~` NOT.
- **Nets (p. 8-9)**: Table 5-4 net types (`wire`, `tri`, `triand`, `trior`, `trireg`, `wand`, `wor`, `supply0`, `supply1`). A `wire` is a connection with no assumed function; `supply0` and `supply1` are logic 0 and 1. Table 5-5 gives `wire` and `tri` declarations.
- **Variables (p. 10-11)**: `reg` stores one or more bits and is not necessarily a flip-flop (covered later); `integer` stores a 32-bit two's-complement value (Table 5-6).
- **Literals (p. 12)**: form `n'Bddd`, n bits, base B (b, o, h, d), digits. Examples: `1'b0`, `8'h07`, `16'hF00D`, `4'b1zz`, `8'b01x11xx0`. A literal too wide for its size loses the leftmost bits.
- **Parameters and vectors (p. 13-14)**: Table 5-8 `parameter identifier = value;` and a decoder port example `Vr3to8deca`. Table 5-9: `reg [7:0] byte1;` etc.; `{}` concatenation and `n{}` replication, e.g. `{2'b00, 2'b11} = 4'b0011`.
- **Arithmetic and shift (p. 15, Table 5-10)**: `+ - * / % **`, logical shifts `<< >>`, arithmetic shifts `<<< >>>`. Signed numbers are tricky: `8'sb11111111` is -1 in two's complement. `$signed()` and `$unsigned()` convert types.
- **Reduction operators (p. 16)**: `&Zbus` is 1 if all bits are 1; `^byte` is 1 if an odd number of 1s, `x` if any bit is `x` or `z`.
- **Arrays (p. 17, Table 5-11)**: `reg [msb:lsb] id [start:end];`. Both `[7:0]` and `[0:255]` are allowed; follow one convention.
- **Logical and relational operators (p. 18, Table 5-12)**: `&& || !`, `== !=`, `> >= < <=`. A multi-bit value is false only if all bits are 0, so `4'b1011 && 4'b0100` is true but bitwise `4'b1011 & 4'b0100` is `4'b0000`.
- **Conditional operator (p. 19, Table 5-13)**: `logical-expression ? true-expression : false-expression`, nestable for a priority chain.
- **Case equality (p. 20, Table 5-14)**: `===` and `!==` compare bit by bit. Precedence warning: `W & X | Y & Z` equals `(W&X) | (Y&Z)`, while `W | X & Y | Z` is `W | (X&Y) | Z`. When in doubt, add parentheses.
- **Be careful (p. 21)**: logic vs arithmetic operations; signed vs unsigned numbers.
- **Compiler directives (p. 22)**: `` `include filename `` and `` `define identifier text ``.
- **Built-in gates (p. 23, Table 5-15)**: `and nand or nor xor xnor buf not bufif0 bufif1 notif0 notif1`.
- **Instances (p. 24, Table 5-16)**: `component-name instance-id (expr, ...)` positional, or named `.port(expr)`. Built-in gates must use the positional format; user modules may use either; named is more readable.
- **Structural examples (p. 25-29)**: `VrAlarmCkt` from Fig. 3-16 uses `or`, `and`, `not` instances and wires; the five statements are evaluated concurrently and may be reordered (it is incorrect to think U1 runs before U2). `VrInh` builds BUT-NOT from `not` and `and`. `VrSillyXOR` (Fig. 5-2) builds XOR from `VrInh` instances and `not`.

## Key results
> [!example] Alarm circuit in Verilog (p. 27)
> $$ALARM = PANIC + ENABLE \cdot EXITING' \cdot SECURE'$$
> $$SECURE = WINDOW \cdot DOOR \cdot GARAGE$$
> becomes five gate instances (U1 to U5) joined by wires `secure`, `notsecure`, `notexiting`, `otheralarm`.

> [!definition] Concurrency
> Verilog statements in a module describe hardware that all runs at once; order in the file carries no meaning for these statements.
> (source: 09_14.pdf, p. 27)

**Connections**: syntax introduced in [[ECE270 week 04 09_12 - Hazards, documentation and timing]]; the same circuit appears as a design example in [[ECE270 week 03 09_07 - Circuit analysis and Karnaugh maps]]. Next: [[ECE270 week 05 09_19 - Verilog behavior and test benches]].

**Sources**: `ECE 27000/week 04/09_14.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Verilog]] · [[Logic gate]] · [[Boolean algebra]] · [[Number systems and codes]]
