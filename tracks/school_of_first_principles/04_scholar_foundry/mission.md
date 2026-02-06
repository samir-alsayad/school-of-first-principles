# Mission: Level 0 - The Scholar
## The Objective
Build your own progression tracker.
Your mission is to create a Python CLI tool (`scholar.py`) that reads the `ledger.yaml` database and validates the completion status of your curriculum modules.

## The Challenge
Create a file `scholar.py` that:
1.  Reads `ledger.yaml` to load your student profile.
2.  Implementing a `status` command that prints your Character Sheet (Name, Level, XP, Inventory Loop).
3.  Implementing a `verify` command that:
    *   Iterates through your Inventory.
    *   Opens the `reflection.md` for each item.
    *   Checks if the line `**Status**: [Verified]` exists.
    *   If verified, marks it in the ledger and awards XP.

## Hints
*   Use `pyyaml` library (install via `pip install pyyaml` if needed) to read the database.
*   Use `argparse` for the CLI commands (`status`, `verify`).
*   Example verification pattern: `if "**Status**: [Verified]" in line:`

## Verification
Run: `python3 scholar.py status`
Expected Output:
```
Student: Samir | Level: 0 | XP: 000
Inventory:
[x] io_logic (Verified)
[ ] variables (Pending)
[ ] sync_gates (Locked)
```
