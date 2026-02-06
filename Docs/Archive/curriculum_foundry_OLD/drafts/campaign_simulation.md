# Simulation: Campaign 14 - Hugging Face Scout
**Archetype Integration Test**

 This simulation demonstrates the **Deferred Design Pattern** across the 4 stages of a Grand Campaign.

---

## Phase 1: The Surveyor (Discovery) 🔭
*   **Gate I (Charter)**: "I want to find the best local models."
*   **Action**: The Agent scans Hugging Face Trends, Reddit (LocalLlama), and Arxiv.
*   **Deliverable**: `surveys/model_codex.md`.
    *   *List*: Llama-3, Mistral, Gemma, Phi-2.
    *   *Metadata*: Parameters, License, Quantization availability.
*   **Status**: We know *what* exists. We don't know if they are good.

## Phase 2: The Analyst (Evaluation) 🧐
*   **Context**: "How do I judge these?"
*   **Action**: Agent reseraches "MMLU vs. ARC", "GGUF vs. EXL2", "Perplexity".
*   **Deliverable**: `analysis/evaluation_framework.md`.
    *   *Heuristic*: "Prefer EXL2 for speed, GGUF for compatibility."
    *   *Heuristic*: "Ignore benchmarks older than 3 months."
*   **Status**: We know *how* to judge. We still can't build a tool.

## Phase 3: The Initiate (Skill) 🥋
*   **Context**: "I need to query the HF API to automate this."
*   **Action**:
    *   *Module A*: "HF Hub API Basics" (Learn `huggingface_hub`).
    *   *Module B*: "Scraping Model Cards" (Learn `BeautifulSoup`).
*   **Deliverable**: `labs/api_experiments/` (Python scripts).
*   **Status**: Skills Acquired. NOW we can design.

## Phase 4: The Architect (Construction) 🏗️
*   **Gate III (Design)**:
    *   **Intent**: "Build a CLI that alerts me to new 7B models with >70 MMLU."
    *   **Spec**: EARS Syntax.
    *   **Casting Guide**: "Create `nexus-shell/tools/hf-watchdog.py`."
*   **Gate IV (Delivery)**:
    *   **Action**: Agent writes code in Foundry.
    *   **Cast**: User manually moves `hf-watchdog.py` to Nexus-Shell.

---
**Result**: A clean, production tool built on a foundation of deep understanding.
