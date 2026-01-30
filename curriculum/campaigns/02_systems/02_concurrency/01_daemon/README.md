# Atomic Unit: The Daemon (The Service)

**Goal**: Run a script in the background, detached from the terminal.

## The Theory
Standard scripts die when you close the terminal.
Daemons "double fork" to detach.

## The Mission (Simplified)
1.  Run your `persistence.py` from Unit 2.
2.  But run it with `nohup python persistence.py &`.
3.  Close the terminal.
4.  Open a new terminal.
5.  Find it with `ps aux | grep persistence`.
6.  Kill it.

## Verification
Prove that closing the terminal didn't kill the process.

---

## Understanding
*   [ ] What does `&` do in the shell?
*   [ ] What does `nohup` mean? (No Hang Up).
*   [ ] Why is this important for a server?

## My Journal
*   **Date**:
*   **Learnings**:
*   **Code (Daemon Command)**:
    ```bash
    # Paste the command you used to start it
    ```
