# Mission: Process IDs (The Machine's Identity)

## The Objective
Understand that every running program on a computer is a **Process**, and every process has a unique number called a **PID**. This is the first step to understanding how an agent (like gptme) actually "lives" in your system.

## The Logic
When you run a Python script, the Operating System creates a process. To the OS, your name doesn't matter—only your PID. 

In Python, we use the `os` module to talk to the kernel and ask: *"Who am I?"*

## The Challenge: `identity.py`
1. Create a script that imports `os`.
2. Use `os.getpid()` to find the process ID.
3. Print: `"Hello, I am a process! My PID is: [PID]"`
4. **The Observation**: Run the script 3 times. Does the PID stay the same?

## Verification
- Run `python3 identity.py`.
- Compare the numbers.
