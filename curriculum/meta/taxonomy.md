# School Taxonomy

To ensure consistency, we use the following hierarchy:

## 1. The School (The Repository)
*   **Definition**: The entire `school-of-first-principles` project.
*   **Goal**: From Zero to System Architect.

## 2. Campaign (The Phase)
*   **Definition**: A massive thematic block.
*   **Examples**: "Systems", "TUI", "Architecture".
*   **Folder**: `curriculum/units/02_systems/`.

## 3. Module (The Subject)
*   **Definition**: A specific skill set within a Campaign.
*   **Examples**: "IPC" (Inter-Process Communication), "Daemons", "ANSI Colors".
*   **Structure**: Usually contains 3-5 Atomic Units.

## 4. Atomic Unit (The Step)
*   **Definition**: A single, indivisible concept that can be learned in one sitting.
*   **Rule**: Must be "Ground Zero" compatible (start from scratch).
*   **Examples**: "Identity (PID)", "Persistence (Loop)", "Receiver (Signal)".
*   **Folder**: `curriculum/units/02_systems/04_sender/`.

## 5. Experiment (The Action)
*   **Definition**: The act of implementing a Unit in the `workbench/`.
*   **Artifact**: The user's code (e.g., `sender.py`).

---
**Hierarchy:**
`School` > `Campaign` > `Module` > `Unit` > `Experiment`
