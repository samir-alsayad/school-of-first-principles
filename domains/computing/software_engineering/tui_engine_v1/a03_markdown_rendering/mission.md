# Mission: a03_markdown_rendering

## The Objective
This is the core of your "Markdown Documentation Engine." In this mission, you will implement the ability to render `.md` files directly in the terminal using Rich's `Markdown` class. This is what will make the Academy usable 100% offline without an external viewer.

---

## 🏗️ The Setup
You will need a path to a real mission file (e.g., `domains/computing/fundamentals/git_mastery_v1/a01_blob_objects/mission.md`).

---

## 🛠️ The Tasks

### 1. The Reader Prototype
Create a script `workbench/read_lab.py` to test rendering.
```python
from rich.console import Console
from rich.markdown import Markdown

console = Console()

with open("domains/computing/fundamentals/git_mastery_v1/a01_blob_objects/mission.md", "r") as f:
    md = Markdown(f.read())
    console.print(md)
```

### 2. The `school read` Command
Add a new command to your Typer app in `src/school/cli.py`:
- **Command**: `read`
- **Argument**: `mission_id` (e.g., `git_mastery_v1.a01`)
- **Logic**: It must resolve the ID to a file path, read the file, and print it using Rich.

### 3. The Path Resolver
Implement a simple logic to find the mission file based on the ID. (Hint: Look at how `scan_modules` works in your loaders).

---

## 🎯 Verification Criteria
- [ ] Running `school read <mission_id>` displays the mission with full formatting (headers, bold text, code blocks).
- [ ] Tables within the Markdown are rendered as clean terminal tables.
- [ ] You can navigate the school content entirely through the CLI.
