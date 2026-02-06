# Mission: Rich (The UI)

## The Objective
Terminal output shouldn't be boring black and white text.
`Rich` makes it beautiful (Colors, Tables, Spinners).
GAP uses this for the "Matrix" aesthetic.

## The Challenge
Create `dashboard.py` that:
1.  Imports `rich` (`pip install rich`).
2.  Prints "[bold red]Alert![/bold red] System Critical".
3.  Creates and prints a `Table` showing "Agent Status".
    *   Columns: "Agent", "Status"
    *   Row: "Smith", "Online"

## Hints
*   `from rich import print`
*   `from rich.table import Table`

## Verification
Run it. Enjoy the colors.
