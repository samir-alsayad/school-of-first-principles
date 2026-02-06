# Mission: Argument Parsing 101 (The Interface)
## The Objective
Master the art of receiving commands.
Your mission is to write a script that accepts CLI arguments using Python's `argparse` library. This is the "Ears" of the Scholar Tool.

## The Challenge
Create `lab_args.py` that:
1.  Accepts a required argument `--name` (string).
2.  Accepts an optional argument `--level` (integer, default=1).
3.  Prints "Hello [name], Level [level]".

## Hints
*   `import argparse`
*   `parser = argparse.ArgumentParser()`
*   `parser.add_argument(...)`
*   `args = parser.parse_args()`
*   Remember: `required=True` forces the user to provide input.

## Verification
Run: `python3 lab_args.py --name "Samir" --level 5`
Expected Output:
```
Hello Samir, Level 5
```
