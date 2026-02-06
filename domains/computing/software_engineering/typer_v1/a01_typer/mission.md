# Mission: Typer (The Modern CLI)

## The Objective
`sys.argv` is painful for complex tools.
`Typer` handles arguments, help menus, and type conversion automatically.

## The Challenge
Create `cli.py` that:
1.  Imports `typer`.
2.  Creates a generic `app = typer.Typer()`.
3.  Defines a command `hello(name: str)` that prints "Hello {name}".
4.  Runs the app.

## Requirements
*   Install: `pip install "typer[all]"`
*   Boilerplate: `if __name__ == "__main__": app()`

## Verification
1.  Run `python3 cli.py --help` -> Expect a generated help menu.
2.  Run `python3 cli.py hello "Neo"` -> Expect "Hello Neo".
