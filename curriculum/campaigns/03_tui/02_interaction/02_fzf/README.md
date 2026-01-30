# Atomic Unit: Interactive Filters (The Brain)

**Prerequisites**: `fzf` installed (`brew install fzf`).
**Goal**: Use `fzf` inside Python.

## The Theory
`fzf` acts as a filter.
Stdin -> FZF (User selects) -> Stdout.

To use it in Python, we need to Open a Pipe to the shell.
*   Tool: `subprocess.Popen`.

## The Mission
1.  Create `picker.py`.
2.  Define a list: `["Apple", "Banana", "Cherry"]`.
3.  Send this list to `fzf` via `subprocess`.
4.  Capture the output (what the user chose).
5.  Print "You chose: [Selection]".

## Verification
Run it. Select "Banana". Python prints "You chose: Banana".

---

## Understanding
*   [ ] What is `stdin` (Standard Input)?
*   [ ] Why do we need `encoding='utf-8'`?
*   [ ] What happens if the user presses ESC?

## My Journal
*   **Date**:
*   **Learnings**:
*   **Code (Picker)**:
    ```python
    # Paste your picker.py here
    ```
