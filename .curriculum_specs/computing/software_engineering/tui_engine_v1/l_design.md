# Pedagogical Design: TUI Engine Evolution (v1)

## 1. Cognitive Dependencies (Invariants)
- **Structure before Style**: A beautiful TUI is useless if the underlying CLI commands aren't robust.
- **Source of Truth (SoT)**: The TUI must reflect precisely what is in the YAML/MD files, never inventing data.
- **User Agency**: The TUI should empower the user to act, not just consume information.

## 2. Topic Sequence

| Step | Mission | Objective | Cognitive Milestone |
| :--- | :--- | :--- | :--- |
| **a01** | **The Data-First CLI** | `school list` & `school path` | Thinking in Data Providers. |
| **a02** | **Nexus Station Setup** | Creating `nexus-shell/modules/academy` | Understanding modular expansion. |
| **a03** | **The Mission Selector** | Integrating `fzf` as a Navigator | Mastering UI Composition. |
| **a04** | **The Render Bridge** | Connecting School -> `nexus-view` | Bridging logic and presentation. |
| **a05** | **Parallax Nerves** | IPC via `ACADEMY_EVENT` | Building a reactive nervous system. |
| **a06** | **The Academy Layout** | Creating the `academy.json` composition | Designing the Sovereign Workspace. |

## 3. Pedagogical Invariants
- Student must build the TUI components using the actual code of the `school` CLI (Dogfooding).
- No external heavy TUI frameworks (like Textual) allowed until the basics of `rich` are mastered.

## 4. Evaluation Criteria
- **Rendering Test**: "Does the `school read` command handle nested Markdown tables correctly?"
- **State Test**: "Does the TUI correctly mark missions as 'Complete' based on the ledger?"
