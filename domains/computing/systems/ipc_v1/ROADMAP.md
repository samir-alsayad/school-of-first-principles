# Parallax Curriculum Roadmap
## The Journey from Signal Hacker to System Architect

You are currently on **Level 1**. Do not worry about the mountain yet; just focus on the next step. But know that the path exists.

### Phase 1: Mechanics (The "What")
- [x] **Mission 01: The Link (Simple)**
    - *Goal:* Manually send a signal to control the shell.
    - *Concept:* IPC, Signals, File Polling.
    - *Location:* `a02_parallax_link`

- [ ] **Mission 02: The Pulse (Deep Trace)**
    - *Goal:* Use `tail -f` to watch the Python Event Loop in real-time.
    - *Concept:* Event Loops, Logging, State.

### Phase 2: Architecture (The "How")
- [ ] **Mission 03: The Autopsy**
    - *Goal:* Map the 4,500 lines of code. Identify the "Kernel", "View", and "Controller".
    - *Concept:* Monoliths vs. Modules.

- [ ] **Mission 04: The Protocol**
    - *Goal:* Reverse-engineer the text protocol used between Python and FZF.
    - *Concept:* Serialization, Interfaces.

### Phase 3: Mastery (The "Why")
- [ ] **Mission 05: The Refactor (Capstone)**
    - *Goal:* Decouple `parallax` from `nexus-shell` by defining a clean Plugin Interface.
    - *Concept:* Dependency Injection, Software Architecture.
