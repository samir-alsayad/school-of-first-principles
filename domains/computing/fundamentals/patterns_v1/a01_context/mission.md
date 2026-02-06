# Mission: Context Managers (The Safe Safe)

## The Objective
In C, you `fopen()` and pray you remember `fclose()`.
In Python, we use the `with` statement to guarantee cleanup.

## The Challenge
Create `safe_read.py` that:
1.  Uses `with open('test.txt', 'w')` to WRITE a file.
2.  Uses `with open('test.txt', 'r')` to READ it back.
3.  Prints the content.

## Constraints
*   Do NOT use `file.close()` explicitly.
*   The code must rely on the context manager to close the file.

## Verification
Run `python3 safe_read.py`.
It should work without errors.
(Bonus: Try causing an error inside the `with` block and observe that the file is still closed properly).
