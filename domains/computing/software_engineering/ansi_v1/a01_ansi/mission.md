# Atomic Unit: ANSI Escape Codes (The Paint)

**Goal**: Make the terminal colorful.

## The Theory
 Terminals are text streams. How do they do color?
 They listen for special sequences starting with `Escape` (`\033` or `\x1b`).
 *   `\033[31m` = Red Text.
 *   `\033[0m` = Reset Attributes.

## The Mission
1.  Create `colors.py`.
2.  Print "This is RED" in actual red.
3.  Print "This is BOLD" in bold (`\033[1m`).
4.  **Important**: Always reset (`\033[0m`) at the end, or your terminal stays red!

## Verification
Run the script. If your terminal looks like a rainbow, you win.

---

## Understanding
*   [ ] What happens if you forget `\033[0m`?
*   [ ] Is this specific to Python or does it work in `bash` too? (Try `echo -e "\033[31mHello"`)
*   [ ] How would you make text Green? (Research the code).

## My Journal
*   **Date**:
*   **Learnings**:
*   **Code (Colors)**:
    ```python
    # Paste your colors.py here
    ```
