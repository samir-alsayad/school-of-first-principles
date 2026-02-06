# Mission: Persistence (The Infinite Machine)

## The Objective
An agent isn't just a script that runs and dies. It's a "Life Form" that stays awake, waiting for instructions. To build this, we need the **Infinite Loop**.

## The Logic
Normally, a script runs from line 1 to the end and exits. 
A **Persistent Process** uses `while True:` to stay in memory. 

## The Challenge: `persistent_machine.py`
1. Use the code you moved from the archive.
2. Modify it so that it prints its PID and the current time every 2 seconds.
3. **The Observation**: Open a *new* terminal. Use the command `ps aux | grep python` to find your process.

## Verification
- Run the script.
- Find it in the process list of your operating system.
- Kill it using `Ctrl+C` or the `kill [PID]` command.
