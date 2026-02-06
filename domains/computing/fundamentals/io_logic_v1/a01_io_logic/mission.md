# Mission: The Observable Effect (I/O)

## The Objective
"A program must produce an observable effect to be useful." 
Before we write complex logic, we must prove that we can see our results. This is the first "First Principle" of computation.

## The Logic
There is a difference between **Expression** and **Action**.
- `1 + 1` is an expression. The computer does the work, but keeps the result for itself.
- `print(1 + 1)` is an action (Side Effect). The computer changes the state of the screen so the outside world can see the result.

## The Challenge: `observable.py`
1. Write a script that performs a calculation (e.g., `40 + 2`).
2. Run it. Observe the output.
3. Now wrap that calculation in a `print()` function.
4. Run it again.

## Verification
- Prove that the first run produced **silence**.
- Prove that the second run produced the **Observable Effect**.
