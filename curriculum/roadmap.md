# The Learning Roadmap

> "From First Principles to System Architect."

This document tracks the path from "User" to "Creator of Parallax".

---

## 🟢 Level 1: The Shell Foundation (Basics)
**Goal:** Understanding the environment we live in.
*   [ ] **1.1 The File System**: `ls`, `cd`, `pwd`, Absolute vs Relative Paths.
*   [ ] **1.2 Permissions**: The Guard (`chmod`, `chown`, User/Group/Other, Octal vs Symbolic).
    *   *Scan:* `install.sh` usually needs `chmod +x`.
*   [ ] **1.3 Environment Variables**: `export`, `PATH`, `$HOME`. "The Air we breathe".
    *   *Scan:* `.nexus-shell.zsh` (sourcing, exports).
*   [ ] **1.4 Piping & Redirection**: `|`, `>`, `2>`, `stdin/stdout/stderr`.
    *   *Scan:* `core/boot/dispatch.sh` (logs).

## 🟡 Level 2: Systems & Inter-Process Communication (IPC)
**Goal:** Making programs talk to each other (The "Silent Wire").
*   [ ] **2.1 Signals**: The Poke (`SIGUSR1`, `SIGINT`, `trap`).
    *   *Context:* How `parallax` wakes up shells.
    *   *Experiment:* `systems/ipc/01_signal_vs_socket`.
*   [ ] **2.2 Sockets**: The Stream (Unix Domain Sockets).
    *   *Context:* `core/bus/event_server.py` (The Nexus Event Bus).
*   [ ] **2.3 State Persistence**: Files vs Memory.
    *   *Context:* `/tmp/px-session-*.meta` (Parallax State) vs Daemon RAM.
*   [ ] **2.4 Process Management**: `PID`, `fork`, `exec`, `wait`.
    *   *Context:* `core/api/nxs-kill.sh`, `core/boot/launcher.sh`.

## 🟠 Level 3: TUI & Interaction (The Frontend)
**Goal:** Building UIs in the Terminal.
*   [ ] **3.1 ANSI Escape Codes**: Colors, Cursor Movement.
    *   *Context:* `core/boot/theme.sh`.
*   [ ] **3.2 Interactive Filters (FZF)**: The "Rubber Duck" of UIs.
    *   *Context:* `modules/parallax/bin/parallax` (using `--bind` for events).
*   [ ] **3.3 TUI Libraries**: `gum`, `glow`.
    *   *Context:* `modules/gum/install.sh`.

## 🔴 Level 4: Architecture (The Engineer)
**Goal:** Designing complex systems.
*   [ ] **4.1 Polymorphism in Scripts**: Making generic wrappers.
    *   *Context:* `core/boot/shell_hooks.zsh`.
*   [ ] **4.2 The Daemon Pattern**: Long-running background services.
    *   *Context:* `core/bridge/render_daemon.sh`.
*   [ ] **4.3 Event-Driven Architecture**: Bus, Subscribers, Events.
    *   *Context:* `core/bus/event_server.py`.

---

## � Future Campaigns (The High Level Roadmap)

### Phase 2: Capstone Project (Mini-Parallax)
*   **Goal**: Build a **Session Manager**.
*   **Components**: Daemon (Service) + Client (TUI) + State (File).
*   **Status**: Locked 🔒.

### Phase 3: Advanced Systems (The Nexus Core)
*   **Topics**: Sockets (Streams), Hooks (Shell Integration), TMUX API.
*   **Status**: Locked 🔒.

### Phase 4: Contribution
*   **Goal**: Write a plugin/fix for `nexus-shell`.
*   **Status**: Locked 🔒.

---

## �🔵 Active Modules (The Syllabus)

### Module 01: Foundations (Done)
*   [x] **Representation**: Number Systems (Bin/Dec/Hex).
*   [x] **State**: Immutability (Tuple vs List).
*   [x] **Computation**: Functions & Scope (`parse_int`).

### Module 02: Systems (Active)
*   [ ] **IPC**: The Silent Wire (Signal vs Receiver). `workbench/`.
