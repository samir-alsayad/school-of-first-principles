# The Hybrid Structure: "The Cognitive Mirror"

## The Psychological Evidence
We base this design on **Cognitive Load Theory (Sweller)**.

1.  **minimize Extraneous Load**: Searching through deep folders (`school/computation/functions/experiments/...`) wastes mental energy that should be used for learning.
2.  **Working Memory vs. Long-Term Memory**:
    *   **Working Memory** is small and fast. It needs focused context.
    *   **Long-Term Memory** is huge and structured. It needs taxonomy.

## The Hybrid Solution
We mirror the brain's architecture.

### 1. `workbench/` (The Working Memory)
*   **Concept**: The active state. **Only ONE experiment** lives here at a time.
*   **Rule**: "Low Friction". No deep folders. Flat structure.
*   *Example:* `workbench/main.py`, `workbench/README.md`.

### 2. `library/` (The Long-Term Memory)
*   **Concept**: The archive. When an experiment is marked DONE, it moves here.
*   **Rule**: "High Structure". Organized by First Principles.
*   *Example:* `library/computation/functions/01_input_output/`.

### 3. `curriculum/` (The Executive Function)
*   **Concept**: The Plan. Tell us what to load into the Workbench next.
*   **Rule**: Linear progression.
*   *Example:* `curriculum/roadmap.md`.

---

## Migration Plan
1.  Create `workbench/`, `library/`, `curriculum/`.
2.  Move `computation/`, `systems/` into `library/`.
3.  Move meta-files into `curriculum/` or keep in root.
4.  **Workflow**:
    *   Agent creates `workbench/README.md` (Gate II).
    *   User codes in `workbench/` (Gate III).
    *   After Verification (Gate IV), we `mv workbench/* library/...`.

**This solves the conflict:** You get the focus of the "Lab" and the order of the "Tree".
