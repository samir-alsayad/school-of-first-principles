# Experiment 02: Persistence (The Heartbeat)

## The Code
We created a process that refuses to die using `while True` and `time.sleep(1)`.

## Learnings
### The "Missing Parentheses" Mystery
One key discovery was the difference between:
*   `os.getpid`: The **Function Object** (The Machine itself). Output: `<built-in function getpid>`.
*   `os.getpid()`: The **Function Call** (Running the Machine). Output: `66584`.

If you forget the `()`, Python treats the function like a variable (a noun), not an action (a verb).

### User's Explanation
> "I created a process that runs infinitely without ending, and prints its own pid each second. I used the time module to implement a 1 second pause after printing the pid each time the loop runs. While True runs infinitely as fast as it can, without ending unless I ctrl c or something, because we are declaring it so, we are declaring True as not a variable but a *constant*. While checks if something is true, and runs an iteration until it isnt, therefore while true allowes the loop to iterate infinitely.

### Q&A
**Q: Why did you have to be careful to implement a rest period in the while true loop?**
A: If I didnt implement a rest period in the while True loop, the process would run as fast as the os allows it. (This is called a "Busy Wait" and kills the battery).
