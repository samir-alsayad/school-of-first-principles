# Mission: a02_rich_foundations

## The Objective
A TUI is more than just text; it is a visual space. In this mission, you will learn the core building blocks of the **Rich** library. You will learn how to use the `Console` and `Panel` primitives to create structured, styled output that makes your CLI feel like a premium application.

---

## 🏗️ The Setup
Continue from your Typer-refactored CLI.
Create a test script `workbench/rich_lab.py`.

---

## 🛠️ The Tasks

### 1. The Console Object
The `Console` is the gateway to terminal magic.
```python
from rich.console import Console
from rich.panel import Panel

console = Console()
console.print("[bold green]TUI Engine Initiated[/bold green]")
```

### 2. Thinking in Panels
Wrap your output in a **Panel**. This creates a visual boundary for your content.
```python
panel = Panel(
    "Welcome to the School of First Principles.",
    title="[bold yellow]Academy Status[/bold yellow]",
    subtitle="v0.2.0",
    border_style="blue"
)
console.print(panel)
```

### 3. Integrating with the CLI
Update your `src/school/commands/status.py` (or the logic in `cli.py`) to use `rich.console` for printing headers instead of standard `print`.

---

## 🎯 Verification Criteria
- [ ] Your `school status` command now outputs a beautiful, colored header wrapped in a Rich Panel.
- [ ] You can explain why we prefer `console.print()` over the built-in `print()`.
- [ ] You understand how to apply conditional styling (e.g., green for [OK], red for errors).
