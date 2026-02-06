# Mission: Nested Functions (The Secret Room)

## The Objective
In C, functions are defined at the top level. You cannot put a function inside another function.
In Python, functions are "Objects". You can define a function inside a function.
This is the **First Step** to understanding Decorators.

## The Logic
```python
def outer():
    def inner():           # Nested inside!
        print("I'm inside")
    inner()                # Call it from within outer
```

## The Challenge
Create `nest.py` that:
1.  Defines a function `parent()`.
2.  Inside `parent`, defines a function `child()`.
3.  Inside `child`, prints "Junior is here".
4.  The `parent` function should call `child()`.
5.  Call `parent()` at the bottom.

## Verification
Output: `Junior is here`
(Wait for the next mission to see why this is useful!).
