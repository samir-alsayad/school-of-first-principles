# Atomic Unit: The Sender (The Finger)

**Prerequisites**: Function Calls (`os.getpid`), Signals Concept.
**Goal**: Write a script that can control another process remotely.

## The Theory
To "kill" a process in Unix means to send it a signal.
The Python function `os.kill(pid, signum)` is the remote control.
*   `pid`: The Target (Who?)
*   `signum`: The Message (What?)

## The Mission
1.  **Ground Zero**: Start empty.
2.  **Input**: Ask the user for the `Target PID` (using `input()`).
3.  **Action**: Use `os.kill` to send `signal.SIGUSR1` to that PID.
4.  **Feedback**: Print "Signal Sent!".

## Verification
1.  Start your `receiver.py` in Terminal A (It prints its PID).
2.  Start `sender.py` in Terminal B.
3.  Enter the PID.
4.  **Win Condition**: Receiver says "Received Signal!", Sender says "Signal Sent!".

---

## Understanding
*   [ ] Why do we need the PID of the target?
*   [ ] Does `os.kill` always kill the process?
*   [ ] What happens if you send a signal to a PID that doesn't exist? (Try it!)

## My Journal
*   **Date**:
*   **Learnings**:
*   **Code (Sender)**:
    ```python
    # Paste your sender.py here
    ```
