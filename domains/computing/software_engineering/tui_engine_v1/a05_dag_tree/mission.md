# Mission: a05_dag_tree

## The Objective
The Academy is a graph of many modules. In this mission, you will learn how to visualize this hierarchy using the `rich.tree.Tree` object. You will build the foundation for an interactive "Evolution Map" that shows what you have mastered and what you have unlocked.

---

## 🏗️ The Setup
You will use the data from `scan_modules()` and `scan_campaigns()` in your CLI loaders.

---

## 🛠️ The Tasks

### 1. The Tree Root
Create a script `workbench/tree_lab.py`.
```python
from rich.tree import Tree
from rich.console import Console

console = Console()
tree = Tree("[bold]Academy Knowledge Graph[/bold]")
```

### 2. Branching Out
Iterate through your loaded modules and add them as branches to the tree.
Add assignments as leaves under each module.
```python
computing = tree.add("Computing")
fundamentals = computing.add("Fundamentals")
fundamentals.add("Git Mastery")
```

### 3. State Awareness (The Ledger)
Use the `ledger.yaml` to color-code the tree:
- **Completed**: [bold green]
- **Unlocked/Next**: [bold white]
- **Locked**: [dim white]

---

## 🎯 Verification Criteria
- [ ] You can explain why `rich.tree` is better for hierarchical data than a flat list.
- [ ] Your tree correctly reflects your current progress from `ledger.yaml`.
- [ ] The output is clean and provides a "High-Level View" of your entire school state.
