# Atomic Experiment: The Receiver (Signals)

**Concept:** Processes are deaf. To make them listen, we need to wire up a **Signal Handler**.

## The Project Context
We are building a "Silent Wire" (IPC System).
Step 1 (Identity) & Step 2 (Persistence) are done & archived.
Step 3 (The Receiver) starts from scratch.

## The Theory
A **Signal** is a software interrupt.
By default, signals like `SIGTERM` or `SIGINT` (Ctrl+C) kill the process.
We can catch them!

### The Toolbox
1.  **The Module**: `import signal`
2.  **The Handler Function**:
    You need a function that Python calls when the phone rings.
    ```python
    def my_handler(signum, frame):
        print("I got a signal!")
    ```
    *   `signum`: The number of the signal (e.g., 30 for SIGUSR1).
    *   `frame`: Where was the code when it was interrupted? (We ignore this for now).

### 3. The Wiring (The Pattern)
    You connect the Signal (Event) to the Handler (Function).

#### Example: Catching Ctrl+C (SIGINT)
This is how you would prevent a script from stopping when you press `Ctrl+C`.
**Study this pattern. You will need to adapt it for SIGUSR1.**

```python
import signal
import sys

# 1. Define the Handler
def my_shutdown_handler(signum, frame):
    print("\nNice try! But I refuse to stop via Ctrl+C.")
    # If we wanted to stop, we would call sys.exit(0) here.

# 2. Wire it up
# When 'SIGINT' happens -> Call 'my_shutdown_handler'
signal.signal(signal.SIGINT, my_shutdown_handler)
```

## The Mission
Write `receiver.py` from scratch. Adapting the pattern above.

1.  **Imports**: `os`, `time`, `signal`.
2.  **Define Handler**: A function that prints "Received Signal!".
3.  **Setup**:
    *   Print PID.
    *   Wire up `signal.SIGUSR1` to your handler.
4.  **The Loop**: (Re-write your infinite loop from the last lesson).

## Verification
1.  Run `receiver.py`.
2.  Open new Terminal.
3.  `kill -SIGUSR1 <PID>`
4.  Success = It prints "Received Signal!" and **keeps running**.
