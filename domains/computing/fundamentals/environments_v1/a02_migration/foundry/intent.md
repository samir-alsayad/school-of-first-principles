# Module 02: The Great Separation (Environment Migration)
# Campaign: 01_foundation (The Machine)
# Gate I: Intent (Charter)
# Status: DRAFT

## 1. Context
The User is currently running a "Giga Environment" (`sovereign_core_env`) that serves 20+ projects.
This creates dependency conflicts and pollution.
We need to migrate all projects to **Isolated Environments** (`.venv`).

## 2. Requirements (EARS)
id: mod-02-env-migration-charter
requirements:
  - **REQ-01**: The System SHALL categorize all 20 projects by dependency complexity (Surveyor).
  - **REQ-02**: The System SHALL enforce a "No Global Python" rule for all new work.
  - **REQ-03**: The Protocol SHALL require a `requirements.txt` and `.venv` for every active project.
  - **REQ-04**: The Global Environment SHALL be deprecated and eventually removed.

## 3. The Network Effect
*   **Target**: [School Ecosystem]
    *   *Deliverable*: Clean, reproducible builds for all modules.

## 4. Design Spec (Deferred)
<!-- DEFERRED: We need to survey the 20 projects first. -->
