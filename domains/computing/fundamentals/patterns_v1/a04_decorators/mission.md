# Mission: Decorators (The Wrapper)

## The Objective
Modify a function's behavior without changing its code.
This is used in GAP for `@check_permission` gates.

## The Challenge
Create `gated.py` that:
1.  Defines a decorator `secure` that prints "Checking Security..." before running the function.
2.  Defines a function `launch_nuke()` decorated with `@secure`.
3.  Calls `launch_nuke()`.

## Hints
*   A decorator is a function that takes a function and returns a wrapper function.
    ```python
    def secure(func):
        def wrapper():
            print("Checking...")
            func()
        return wrapper
    ```

## Verification
Output should be:
```
Checking Security...
Nuke Launched!
```
