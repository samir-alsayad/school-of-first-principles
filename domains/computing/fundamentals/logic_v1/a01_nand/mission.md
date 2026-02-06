# Mission: The Universal Atom (NAND)

## The Objective
"I cannot create what I do not understand."
Before we use Python's `if` statements or `+` operators, we must understand how they are built from electricity and logic. 

Every computer in the world is built from millions of tiny switches called **NAND gates**.

## The Logic
A NAND gate (Not-AND) has two inputs and one output. 
It follows this rule: **The output is 0 ONLY if both inputs are 1.** 

| A | B | Output (NAND) |
|---|---|---|
| 0 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

## The Challenge: `logic_foundry.py`
1. Create a function `nand(a, b)` that simulates a single NAND gate.
2. **The "Sealed Envelope" Discovery**: Use ONLY your `nand` function to build a `not_gate(a)`.
   - *Hint*: What happens if you pass the same input to both sides of a NAND?
3. Build an `and_gate(a, b)` using your `nand` and your new `not_gate`.

## Verification
- Run your script. 
- Prove that `not_gate(1)` returns `0`.
- Prove that `and_gate(1, 1)` returns `1`.
