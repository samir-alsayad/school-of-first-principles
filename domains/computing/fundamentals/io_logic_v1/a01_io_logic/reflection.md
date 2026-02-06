# Reflection: The Observable Effect
**Status**: [Verified]

## The Mirror
1. How do you prove that your code actually ran?
> By producing an observable effect (Input/Output).

2. If you write `1` in a file and run it, what happens? Why?
> Nothing happens (silence). Because writing `1` is just an expression, not a command to change the state of the screen.

## My Notes
- **The Observable Effect**: A program can calculate things properly (like `1 + 1`), but if it does not perform an I/O action (like `print`), the outside world will never know.
- **Expression vs. Action**: `1` is a value (an expression). `print(1)` is a command to change the state of the screen (a side effect).

## The Discovery
Running `print(1)` produced the output: `1`. Just writing `1` in the file and running it produced **silence**.

## The Gap
[How do we capture input from the user?]

## Evidence
[Verified in Archive/01_foundations_v1]
