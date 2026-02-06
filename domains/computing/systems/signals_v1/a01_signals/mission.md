# Mission: Signals (Inter-Process Talk)

## The Objective
How does a user tell a running agent to "Stop" or "Reload" without touching its code? We use **Signals**. 

## The Logic
The Operating System can send "Pokes" to a process. 
- `SIGINT` (Ctrl+C)
- `SIGTERM` (Please die)
- `SIGUSR1` (User Defined 1)

Python's `signal` module allows us to "Catch" these pokes and run functions.

## The Challenge: `radio.py` & `poke.py`
1. **The Radio (`radio.py`)**: Create a script that catches `SIGUSR1` and prints `"Signal Received! Switching Frequencies..."`.
2. **The Poke (`poke.py`)**: Create a script that takes a PID as an argument and sends `SIGUSR1` to it using `os.kill(pid, signal.SIGUSR1)`.

## Verification
1. Run `python3 radio.py` and get its PID.
2. Run `python3 poke.py [PID]`.
3. Watch the Radio react!
