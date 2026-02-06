# Reflection: Persistence
**Status**: [Verified]

## The Mirror
1. Why does the loop need a `time.sleep()`? What happens to your CPU usage if you remove it?
> If I didnt implement a rest period in the while True loop, the process would run as fast as the os allows it. (This is called a "Busy Wait" and kills the battery).

2. If you close your terminal window, does the process stay alive?
> No, unless it is "daemonized" or put in the background, closing the shell usually kills its child processes.

## My Notes
I created a process that runs infinitely without ending, and prints its own pid each second. I used the time module to implement a 1 second pause after printing the pid each time the loop runs. While True runs infinitely as fast as it can, without ending unless I ctrl c or something, because we are declaring it so, we are declaring True as not a variable but a constant. While checks if something is true, and runs an iteration until it isnt, therefore while true allowes the loop to iterate infinitely.

## The Discovery
One key discovery was the difference between `os.getpid` (the function object) and `os.getpid()` (running the machine). If you forget the `()`, Python treats the function like a variable, not an action.

## The Gap
[If a process is infinite, how do we send it new orders without killing it?]

## Evidence
[Verified in Archive/02_systems_v1]
