# The Environment Codex: The Surveyor's Map
**Module**: 02_env_migration
**Status**: Generated via `01_audit_global.py`

## 1. The Global State (sovereign_core_env)
*   **Path**: `/Users/compute/sovereign_core_env`
*   **Status**: 🟢 **CLEAN** (Surprisingly).
*   **Installed Packages**:
    *   `numpy==2.4.1`
    *   `pgvector==0.4.2`
    *   `psycopg2-binary==2.9.11`
*   **Verdict**: This is not a "Giga Env" yet. It is just a workspace root.
*   **Action**: **LOCK IT**. Do not install anything else here.

## 2. The Project Inventory (The Hit List)
Scanned `/Users/Shared/Projects`.

### ✅ Sovereign (Has Manifest)
Projects that are already compliant or close to it.
*   `Gated Agent Protocol` (`pyproject.toml`)
*   `IntelHub/canon/recursive-llm` (`pyproject.toml`)
*   `IntelHub/mini-swe-agent` (`pyproject.toml`)
*   `Inference_LLM_Lab` (`requirements.txt`)
*   `school-of-first-principles/curriculum.../module_01_pgvector` (`requirements.txt`)

### ⚠️ Shadow Zones (Nested venvs / Mess)
Projects that show signs of unmanaged environments (venvs inside source tree).
*   `IntelHub/lab/agent_factory` (Contains nested `venv` directories).
*   `IntelHub/runtime/letta` (Contains `letta-env`).

### 🚨 The Dependency Gap (Deep Scan Results)
**Target**: `IntelHub`
*   **Used Imports**: 108 (Refined from 3,484 false positives)
*   **Declared**: 0
*   **Verdict**: **Parasite**, but manageable.
*   **Key Dependencies**: `openai`, `anthropic`, `pydantic`, `numpy`, `pandas`.

### 🔗 Internal Sibling Linkage (Local Projects)
**Warning**: These are NOT on PyPI. They must be installed via `pip install -e`.
*   `rlm` (Found in `IntelHub/canon/recursive-llm/rlm`)
*   `minisweagent` (Found in `IntelHub/mini-swe-agent/src/minisweagent`)

### 📂 Renaming Impact (Path Integrity)
*   **Observation**: `nexus-shell` and `Nexus` are still referenced in 50+ files despite renames.
*   **Risk**: Logic breakage during execution.

## 3. The Migration Plan
1.  **Global Lock**: Treat `sovereign_core_env` as Read-Only.
2.  **IntelHub Quarantine**:
    *   *Action*: Apply `rescue_requirements.txt` (108 packages).
    *   *Command*: `uv pip install -r rescue_requirements.txt` in a fresh `.venv`.
3.  **Linkage Phase**: Perform editable installs of `rlm` and `minisweagent`.
4.  **Repair Phase**: Run a global search-and-replace for old folder names to restore path integrity.
5.  **Standardization**: Ensure `Inference_LLM_Lab` and others use the **Standard Protocol** (`uv` or `.venv` at root).
