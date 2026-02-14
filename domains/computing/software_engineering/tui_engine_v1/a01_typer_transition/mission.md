# Mission: a01_typer_transition

## The Objective
Modern CLI tools need to be ergonomic and easily extensible. While `argparse` is standard, it becomes unwieldy as subcommands grow. In this mission, you will refactor the existing `school` CLI to use **Typer**. This is the first step in building our TUI engine, as Typer integrates perfectly with the rendering power of Rich.

---

## 🏗️ The Academy State
The current CLI lives in `src/school/cli.py` and uses a classic `argparse` setup. Your goal is to replace this with a Typer application while maintaining backward compatibility for the `status` command.

---

## 🛠️ The Tasks

### 1. The Prototype
Create a temporary experiment file `workbench/typer_lab.py` to test the Typer syntax.
```python
import typer

app = typer.Typer()

@app.command()
def status(
    scope: str = typer.Option("total", help="Scope of progress"),
    id: str = typer.Option(None, help="Specific module or campaign ID")
):
    print(f"Checking status for: {scope}")
    if id:
        print(f"Target ID: {id}")

if __name__ == "__main__":
    app()
```

### 2. The Refactor
Now, adapt `src/school/cli.py`. 
-   Import `typer`.
-   Initialize `app = typer.Typer(help="School CLI - The Sovereign Interface")`.
-   Migrate the `cmd_status` logic into an `@app.command()`.

> [!IMPORTANT]
> Keep the imports to `from .commands import cmd_status` but wrap the call in a Type-safe function.

### 3. Verification
Verify that the `school` command still works as expected:
```bash
# Ensure the entry point still works
PYTHONPATH=src python3 -m school status --scope total
```

---

## 🎯 Verification Criteria
- [ ] `school --help` shows a clean, automatically generated help menu.
- [ ] Running `school status` without arguments defaults to `total` scope.
- [ ] You can explain why Typer's use of **Type Hints** `(scope: str = ...)` is superior to the string-based configuration of `argparse`.
- [ ] The CLI now uses a standard entry point that we can easily extend with `read` and `browse` commands.
