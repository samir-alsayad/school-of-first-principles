# Atomic Unit: Polymorphism (The Wrappers)

**Goal**: Write one script that behaves differently based on how it is called.

## The Theory
In `nexus-shell`, many commands check `$0` (the name of the script).
If called as `nxs-kill`, it kills.
If called as `nxs-watch`, it watches.
But they are the *same file* (Symlink).

## The Mission
1.  Create `tool.py`.
2.  Check `sys.argv[0]`.
3.  If name contains "kill", act like a killer.
4.  If name contains "save", act like a saver.
5.  Create symlinks:
    *   `ln -s tool.py killer`
    *   `ln -s tool.py saver`

## Verification
Run `./killer`. Output: "I am killing".
Run `./saver`. Output: "I am saving".

---

## Understanding
*   [ ] What is a Symlink?
*   [ ] Why is `sys.argv[0]` useful here?
*   [ ] How does `parallax` use this for its CLI?

## My Journal
*   **Date**:
*   **Learnings**:
*   **Code (Tool)**:
    ```python
    # Paste your tool.py here
    ```
