# Mission: a06_live_navigator

## The Objective
In the final mission of this track, you will turn your static Tree into an **Interactive Navigator**. You will use `rich.live` to create a terminal application that refreshes in real-time, allowing you to "browse" your school and select missions to read without re-running the command.

---

## 🏗️ The Setup
This mission requires a strong grasp of Python loops and input handling.

---

## 🛠️ The Tasks

### 1. The Live Loop
Learn how to use `rich.live.Live` to update the terminal display without scrolling.
```python
from rich.live import Live
from rich.table import Table
import time

# Create a dynamic display context
with Live(renderable_object, refresh_per_second=4) as live:
    # Update logic here
    pass
```

### 2. Keyboard Interaction
Integrate a simple input listener (e.g., using `readchar` or standard `input`) to move a selection "cursor" up and down the Knowledge Graph tree.

### 3. The `school explore` Command
Implement the full TUI dashboard. When you press `Enter` on a mission, it should trigger the `read` logic from mission `a03`.

---

## 🎯 Verification Criteria
- [ ] You have a fully functional Terminal UI that allows you to explore and read your curriculum.
- [ ] The TUI identifies you correctly and shows your "Evolution" state dynamically.
- [ ] You have built a sovereign, offline-first learning engine that competes with any modern IDE.
