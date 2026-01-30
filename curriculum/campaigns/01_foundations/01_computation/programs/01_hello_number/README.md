# Experiment 01: The Observable Effect

**One New Idea:** A program must produce an observable effect to be useful. (Input/Output).

## Prerequisites
*   None. (This is the Root).

## Hypotheses / Question
How do I prove that my code actually ran?

## Prediction
**STOP.** Before running inputs:
*   If we write `1` in a file, does the computer show `1`?

No!
*   If we write `print(1)`, what happens?

Yes!

## The Experiment
We will create a file `main.py` with a single instruction to "print" a number to the screen.

## Observations
*   Running `print(1)` produced the output: `1`.
*   (Hypothetically) Just writing `1` in the file and running it would produce **silence** (no output).

## Conclusions & Learned Principles
*   **The Observable Effect**: A program can calculate things properly (like `1 + 1`), but if it does not perform an I/O action (like `print`), the outside world will never know.
*   **Expression vs. Action**: `1` is a value (an expression). `print(1)` is a command to change the state of the screen (a side effect).
