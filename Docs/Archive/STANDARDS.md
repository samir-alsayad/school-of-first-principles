# The Sovereign Standards (v1.0)
**Status**: Canonical
**Supersedes**: `atomic_curriculum_standard.md`, `school_protocol.md`

## 1. The Triple-Doc Protocol (Iterative Learning)
Every **Atom** must support infinite-turn dialogue. We do not overwrite history; we append to it.

### A. Codex (Immutable)
*   **File**: `codex.md`
*   **Purpose**: The Source of Truth. The Lesson.
*   **Write Access**: **Agent Only** (Librarian/Tutor).

### B. Reflection (The Journal)
*   **File**: `reflection.md`
*   **Purpose**: The User's understanding.
*   **Structure**:
    ```markdown
    # Turn 1
    ## The Mirror (Q&A)
    ...
    ## My Notes
    ...
    ## The Evidence
    ...
    
    # Turn 2
    ## Re-Evaluation
    ...
    ```
*   **Write Access**: **User Only**.

### C. Response (The Feedback)
*   **File**: `response.md`
*   **Purpose**: The Tutor's synthesis and validation.
*   **Structure**:
    ```markdown
    # Turn 1
    ## Diagnosis
    ...
    
    # Turn 2
    ## Verdict
    ...
    ```
*   **Write Access**: **Agent Only**.

## 2. The Atomic Structure
Every learning unit must contain:
1.  **Directory**: `XX_atom_name/`
2.  **Triple-Doc**: `codex.md`, `reflection.md`, `response.md`
3.  **Proof**: `discovery.sh` or `.py` (The executable verification).

## 3. The Foundry
*   **Location**: `modules/XX_module/foundry/`
*   **Rule**: No code leaves the School (moves to `Projects/`) without passing through the Foundry and being "Cast" by the Critic.
*   **Security**: Foundry code is assumed **Unsafe** until verified.

## 5. The Geography (File System Standards)
We maintain a strict separation between **Governance** (The Rules) and **Execution** (The Work).

- **`Docs/`**: The Constitution. Contains `TAXONOMY.md`, `STANDARDS.md`. (The School's general laws).
- **`curriculum/`**: The User's specific instance.
    - **`ROADMAP.md`**: The User's personal trajectory.
    - **`campaigns/`**: The active content folders.
- **`meta/`**: Archives and drafts.
