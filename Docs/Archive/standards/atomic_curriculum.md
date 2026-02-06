# Atomic Curriculum Standard (v1.0)

This standard defines the structure for the **School of First Principles**. It prioritizes progressive complexity and sovereign understanding.

## 1. The "Atom" (Teaching Unit)
An Atom focuses on **exactly one** new concept.
- **Goal**: Minimize mental load.
- **Structure (The Triple-Doc)**:
    - `codex.md`: The "What" and "Why" (Technical background). **Immutable**.
    - `reflection.md`: The User's Journal. **Iterative**. Questions provided by the Agent, answers provided by the User.
    - `response.md`: The Tutor's Feedback. **Iterative**. The Agent analyzes the reflection and provides deep dives or corrections.
    - `discovery.py/sh`: The Proof of Work.

## 2. The "Assembly Gate" (Integration Unit)
- **Lineage**: The Gate explicitly lists previously completed Atoms it depends on.
- **Action**: The User "pulls" the code from an Atom's discovery file into the **Foundry** to begin assembly.

## 3. The "Foundry" (The Forge)
Each Campaign has a `foundry/` directory. This is the "Production Sandbox" where Atoms are combined into the final system. Deliverables in the Foundry are the only code allowed to exit the "School" and enter the "Sovereign Machine."

## 4. The "Assembly Module"
Unlike a standard module which teaches atoms, an Assembly Module connects multiple completed campaigns into a new global system. Use this for complex integrations like "The Sovereign Handover."

## 5. The "Socratic Backstop" (Pedagogy)
The Teacher (AI) SHALL NOT provide direct code solutions for Atoms by default. 
- **Method**: Hinting, questioning, and referencing the Codex.
- **Goal**: Ensure the "Aha!" moment happens in the Sovereign's mind, not the AI's.

## 6. The "Cast" (Deployment)
"Casting" is the formal action where a validated Foundry deliverable is moved into the `/Users/Shared/Projects/` production architecture.
- **Invariant**: Only code that has passed through an Assembly Gate can be cast.
- **Tool**: `nxs-cast` (The Casting Script).

## 7. The "School Council" (Identity)
- **Librarian**: Curates cross-campaign context and prerequisites.
- **Tutor**: Guides the user through Atoms (Socratic mode).
- **Critic**: Reviews Foundry code and advises on optimization/trajectories.
- **Smith**: Drafts the initial blueprints/placeholders in the Foundry.

## 8. The "Reflective Gate" (Access Control)
Progress to the next Atom or Assembly Gate is locked until the User provides a verified **Reflection**, containing:
- **The Mirror**: Q&A on the core concept.
- **My Notes**: Freform observations.
- **The Discovery**: What was actually learned (The "Aha!").
- **The Gap**: What is still confusing.
- **The Evidence**: Shell output or logs proving execution.
### Proposed Structure for `05_sovereign_user`:
- **Module 01: Local Anchoring**
    - [Atom] 01.1: Binary Discovery (`psql` & `PATH`)
    - [Atom] 01.2: Database Genesis (Users & Rights)
    - [Atom] 01.3: The Vector Key (`pgvector` compilation)
    - [Gate] 01.4: **Bridging Letta** (Connecting the Intelligence Duo)
- **Module 02: Sentry Jail**
    - [Atom] 02.1: Signal Trapping
    - [Atom] 02.2: Process Isolation
    - [Gate] 02.3: **The Jailer** (Native Security Layer)
