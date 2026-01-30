# Atomic Unit: The Protocol (Language)

**Prerequisites**: Sender & Receiver.
**Goal**: Give meanings to different signals.

## The Theory
We can handle multiple signals.
*   `SIGUSR1` could mean "Hello".
*   `SIGUSR2` could mean "Goodbye".

## The Mission
1.  **Modify Receiver**:
    *   Register a handler for `SIGUSR1` (Print "Hello").
    *   Register a handler for `SIGUSR2` (Print "Goodbye" and `exit()`).
2.  **Modify Sender**:
    *   Ask user: "1 for Hello, 2 for Goodbye".
    *   Send the corresponding signal.

## Verification
1.  Start Receiver.
2.  Start Sender.
3.  Press 1 -> Receiver says Hello.
4.  Press 2 -> Receiver says Goodbye and dies.

---

## Understanding
*   [ ] Why do we need different handler functions (or can we use one)?
*   [ ] What argument tells the handler *which* signal triggered it?
*   [ ] Why is `SIGKILL` special? (Can we catch it?)

## My Journal
*   **Date**:
*   **Learnings**:
*   **Code (Protocol)**:
    ```python
    # Paste your code here
    ```
