# Learning Requirements: TUI Engine Evolution (v1)

## 1. Learning Goals (User Stories)
- **As a Developer**, I want to migrate a legacy `argparse` CLI to **Typer** to handle complex subcommands elegantly.
- **As a Learner**, I want a terminal-based **Markdown Engine** using **Rich** so that I can read my curriculum without leaving the shell.
- **As a Sovereign User**, I want an **Interactive Explorer** to browse my Knowledge Graph offline.

## 2. Success Criteria
- [ ] **Typer Test**: All existing `school` commands are functional under the new Typer registry.
- [ ] **Rich Test**: A command `school read <id>` renders a mission with colors, panels, and syntax highlighting.
- [ ] **TUI Test**: A command `school browse` shows a navigable tree of the available modules.
- [ ] **Offline Test**: The engine works perfectly without any internet connection or AI server.

## 3. Scope
- **Frameworks**: Typer, Rich.
- **Concepts**: Terminal UI (TUI), Layouts, Panels, Syntax Highlighting, TUI Tree Navigation.
