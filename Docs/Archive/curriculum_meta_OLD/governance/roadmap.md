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

## Level 5: Sovereign Intelligence

### [Campaign 05: The Inference Engine (MLX)](campaigns/05_inference_engine/README.md)
*Mastering local GPU/NPU performance.*
- [ ] [M01: Hardware Physics](campaigns/05_inference_engine/01_hardware_physics/)
    - [ ] [VRAM Math](campaigns/05_inference_engine/01_hardware_physics/01_vram_math/)
    - [ ] [Bits & Quantization](campaigns/05_inference_engine/01_hardware_physics/01_bits/)
    - [ ] [MLX Basics](campaigns/05_inference_engine/01_hardware_physics/02_mlx_basics/)
- [ ] [M02: Storage Optimization](campaigns/05_inference_engine/02_storage_optimization/)
    - [ ] [KV State Management](campaigns/05_inference_engine/02_storage_optimization/01_kv_state/)
    - [ ] [KV Quantization](campaigns/05_inference_engine/02_storage_optimization/01_kv_quant/)
- [ ] [M03: Acceleration Loops](campaigns/05_inference_engine/03_acceleration_loops/)
    - [ ] [Drafting Loops](campaigns/05_inference_engine/03_acceleration_loops/01_drafting/)
    - [ ] [Verification Pass](campaigns/05_inference_engine/03_acceleration_loops/01_verification/)

### [Campaign 06: Blackbox: The Agentic Brain (Letta)](campaigns/06_agentic_brain/README.md)
*Building agents that think and remember.*
- [ ] [M01: Understanding RLM (Theory)](campaigns/06_agentic_brain/01_understanding_rlm_paper/)
    - [ ] [Recursive Logic](campaigns/06_agentic_brain/01_understanding_rlm_paper/01_recursive_logic/)
- [ ] [M02: Using RLM (Codebase)](campaigns/06_agentic_brain/02_using_rlm_codebase/)
    - [ ] [RLM Explorer](campaigns/06_agentic_brain/02_using_rlm_codebase/01_rlm_explorer/)
- [ ] [M03: Stateful Memory Kernels](campaigns/06_agentic_brain/03_stateful_memory_kernels/)
    - [ ] [Letta Health](campaigns/06_agentic_brain/03_stateful_memory_kernels/01_letta_health/)
    - [ ] [Tool Blueprints](campaigns/06_agentic_brain/03_stateful_memory_kernels/02_tool_schema/)
    - [ ] [Archival Search](campaigns/06_agentic_brain/03_stateful_memory_kernels/03_archival_search/)
- [ ] [M04: Memory Evolution (MemEvolve)](campaigns/06_agentic_brain/04_memory_evolution_memevolve/)
- [ ] [M05: The Evolution Loop](campaigns/06_agentic_brain/04_evolution_loop/)
    - [ ] [Trajectory Auditing](campaigns/06_agentic_brain/04_evolution_loop/01_trajectory_log/)
    - [ ] [Gold Exam Verification](campaigns/06_agentic_brain/04_evolution_loop/02_gold_exam/)

### [Campaign 07: The Security Shell (GAP)](campaigns/07_security_shell/README.md)
*Fearless execution through deterministic isolation.*
- [ ] [M01: Sterile Containment](campaigns/07_security_shell/01_sterile_containment/)
    - [ ] [Session Isolation](campaigns/07_security_shell/01_sterile_containment/01_session_path/)
- [ ] [M02: ACL Protocols](campaigns/07_security_shell/02_acl_protocols/)
    - [ ] [Enforcer Logic](campaigns/07_security_shell/02_acl_protocols/01_enforcer_logic/)
- [ ] [M03: Human Sync Logic](campaigns/07_security_shell/03_human_sync_logic/)
    - [ ] [Sync Gates](campaigns/07_security_shell/03_human_sync_logic/01_sync_gates/)

### [Campaign 08: The Sovereign Architect (Product)](campaigns/08_sovereign_architect/README.md)
*Owning the full production stack.*
- [ ] [M01: TUI Orchestration](campaigns/08_sovereign_architect/01_orchestration/)
    - [ ] [Nexus Intro](campaigns/08_sovereign_architect/01_orchestration/01_nexus_intro/)
    - [ ] [Thought Hoisting](campaigns/08_sovereign_architect/01_orchestration/02_thought_hoisting/)
- [ ] [M02: Feature Sealing](campaigns/08_sovereign_architect/02_feature_sealing/)
    - [ ] [Synthesis Gate](campaigns/08_sovereign_architect/02_feature_sealing/01_synthesis/)
    - [ ] [Parallax Gates](campaigns/08_sovereign_architect/01_orchestration/02_gate_coordination/)
- [ ] [M03: Project Finalization](campaigns/08_sovereign_architect/03_project_finalization/)
    - [ ] [State Finalization](campaigns/08_sovereign_architect/03_project_finalization/01_state_finalization/)

### [Campaign 09: The Tutor Council (Stateful Pedagogy)](campaigns/09_tutor_council/README.md)
*Live pedagogical layer over the workbench.*
- [ ] [M01: The Council Personas](campaigns/09_tutor_council/01_council_personas/)
    - [ ] [The Helper](campaigns/09_tutor_council/01_council_personas/01_the_helper/)
    - [ ] [The Proposer](campaigns/09_tutor_council/01_council_personas/02_the_proposer/)
    - [ ] [The Critic](campaigns/09_tutor_council/01_council_personas/03_the_critic/)
    - [ ] [The Optimizer](campaigns/09_tutor_council/01_council_personas/04_the_optimizer/)
- [ ] [M02: Council Coordination](campaigns/09_tutor_council/02_council_coordination/)
    - [ ] [Shared Context](campaigns/09_tutor_council/02_council_coordination/01_shared_context/)
    - [ ] [Feedback Loops](campaigns/09_tutor_council/02_council_coordination/02_feedback_loops/)
### [Campaign 10: The Model Codex (Selection)](campaigns/10_model_codex/README.md)
*Mastering model archetypes and context steering.*
- [ ] [M01: The Model Zoo](campaigns/10_model_codex/01_model_zoo/)
- [ ] [M02: Prompt Engineering (First Principles)](campaigns/10_model_codex/02_prompt_engineering/)

### [Campaign 11: The Feedback Loop (Evolution)](campaigns/11_feedback_loop/README.md)
*Designing agents that learn from their own errors.*
- [ ] [M01: Bilevel Optimization](campaigns/11_feedback_loop/01_theory/)
- [ ] [M02: Auto-Evolution](campaigns/11_feedback_loop/02_auto_evolution/)

### [Campaign 12: Postgres Mastery (Persistence)](campaigns/12_postgres_mastery/README.md)
*Deep-dive into the school's persistence engine.*
- [ ] [M01: The PGVector Engine](campaigns/12_postgres_mastery/01_pgvector/)
- [ ] [M02: Relational Schemas for Agents](campaigns/12_postgres_mastery/02_schemas/)
- [ ] [M03: High-Performance Search](campaigns/12_postgres_mastery/03_search_optimization/)

---

## 🚀 Future Campaigns (The High Level Roadmap)

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
