# Legacy Migration Map (v1 -> Domain)

**Objective**: Map the flat list of `_legacy_v1` campaigns to the new 5-Domain Taxonomy.
**Logic**: Legacy content goes to `domains/{domain}/archive/{campaign_name}` to avoid cluttering active campaigns.

| Legacy Campaign | Target Domain | Target Path (Archive) | Reasoning |
| :--- | :--- | :--- | :--- |
| `01_foundations` | **Computing** | `domains/computing/archive/01_foundations_v1` | Python, Git, and Shell basics. |
| `02_systems` | **Computing** | `domains/computing/archive/02_systems_v1` | System architecture patterns. |
| `03_tui` | **Computing** | `domains/computing/archive/03_tui_v1` | Interface handling logic. |
| `04_arch` | **Computing** | `domains/computing/archive/04_arch_v1` | Old architectural drafts. |
| `05_inference_engine` | **Intelligence** | `domains/intelligence/archive/05_inference_v1` | LLM and Local model logic. |
| `06_agentic_brain` | **Intelligence** | `domains/intelligence/archive/06_agentic_brain_v1` | RLM and Memory structures. |
| `07_security_shell` | **Computing** | `domains/computing/archive/07_security_v1` | Early sandboxing ideas (pre-Warden). |
| `08_sovereign_architect` | **Computing** | `domains/computing/archive/08_architect_v1` | Meta-structure planning. |
| `09_tutor_council` | **Intelligence** | `domains/intelligence/archive/09_tutor_council_v1` | Early persona definitions. |
| `10_model_codex` | **Intelligence** | `domains/intelligence/archive/10_model_codex_v1` | Model cards and specs. |
| `11_feedback_loop` | **Intelligence** | `domains/intelligence/archive/11_feedback_loop_v1` | Reinforcement learning loops. |

## Execution Plan
1.  **Create Archive Folders**:
    - `domains/computing/archive`
    - `domains/intelligence/archive`
2.  **Move**:
    - Move directories from `Docs/archive/legacy_v1/v1/` to their respective targets.
3.  **Delete**:
    - Remove `Docs/archive/legacy_v1` once empty.
