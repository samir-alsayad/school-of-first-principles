# Experiment 04: The Transformation Machine

**One New Idea:** Code can be encapsulated. A Function is a machine that takes **Input**, does work, and returns **Output**.

## Prerequisites
*   [x] Experiment 03 (Positional Notation)
*   [ ] Concept: "Scope" (What happens in the function, stays in the function).

## Hypotheses / Question
In `01_positional_notation`, if we wanted to convert *two* numbers, we would have to copy-paste the whole code.
**Hypothesis:** We can create a "Magic Box" that does the conversion for ANY string we throw at it.

## The Theory (Concepts)

### 1. The Machine Definition (`def`)
In Python, we define a machine with `def name(input):`.
*   Everything indented under `def` belongs to the machine.
*   It does not run until you call it.

### 2. The Input Port (Parameters)
When you write `def parse(text):`, the variable `text` is created **only inside** the function.
*   It doesn't matter what the value was named outside (`input_string`, `s`, `raw`).
*   Inside the function, it is always called `text`.

### 3. The Output Port (`return`)
*   `print()` just shows pixels on the screen. It is for humans.
*   `return` sends the **data** back to the program.
*   If you don't `return`, the function sends back `None` (void).

### 4. The One-Way Mirror (Scope)
*   **Inside can see Outside**: The function can read global constants (like `CHAR_TO_INT`).
*   **Outside CANNOT see Inside**: Variables created in the function (`total_sum`) die when the function ends. You cannot print them outside.

## The Experiment
1.  Create `main.py`.
2.  Define a function `def parse_int(text):`.

## Verification
### Actual Output
<!-- Paste results here -->
/Users/Shared/Projects🔒 
❯ /Users/samir/.pyenv/versions/3.12.3/bin/python /Users/Shared/Projects/school-of-first-principles/computation/functions/01_input_output/main.py
223

### My Learnings
<!-- Answer these questions to prove your understanding:
1. **The Ghost**: Why does `total_len` not exist outside the function? (What is Scope?)
2. **The Output**: Why is `return result` different from `print(result)`? What did `+ 100` prove?
3. **The Contract**: what happens if you change `number_string` to `text` inside the function? Does the outside world care? 
-->
