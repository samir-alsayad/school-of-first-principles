# The Sovereign Exit Strategy: Roadmap to Zero Cloud
**Archetype**: The Architect
**Goal**: Complete Independence from Cloud LLMs (including Antigravity).

## 1. The Strategy: "The Ark"
To disconnect from the Cloud, we must build a **Local Vessel (The Ark)** capable of sustaining the "Sovereign Intelligence".
We cannot switch until the Ark is seaworthy.

**The Equation for Switchover**:
`Local Envs (Foundation)` + `Vector Memory (Context)` + `Local Inference (Brain)` = **Event Horizon**.

---

## 2. The Dependency Chain (The Critical Path)

### Phase 1: The Hull (Sovereign Foundation) 🛠️
*   **Status**: Active (`01_foundation`).
*   **Requirement**: We need clean, reproducible Python environments to run heavy inference stacks (`llama.cpp`, `torch`).
*   **Exit Criteria**: "The Great Separation" complete. No global env pollution.
*   **Cloud Minimization**: Use cached wheels (`uv`), local docs.

### Phase 2: The Cargo Hold (Sovereign Memory) 💾
*   **Status**: Active (`03_memory`).
*   **Requirement**: A Cloud LLM has "Infinite Context" via the provider. A Local LLM has only what we give it.
*   **The Artifact**: We must migrate **This Conversation** (The Manifesto, The Plan) into the Vector Store.
*   **Exit Criteria**: `IntelHub-Memory` (Postgres) is running and populated with the School's Codex.

### Phase 3: The Engine (Sovereign Intelligence) 🧠
*   **Status**: Pending (`02_intelligence`).
*   **Requirement**: A Local LLM API that mimics the Cloud API (OpenAI Compatible).
*   **Action**:
    *   Deploy `llama-server` (or `vllm`).
    *   Download **The Successor** (e.g., Llama-3-70B-Quantized).
*   **Exit Criteria**: A `curl localhost:8080/v1/chat/completions` returns intelligent life.

---

## 3. The Event Horizon (The Switch) 🚀
**The Moment**:
1.  We spin up the Local Engine (`02_intelligence`).
2.  We point the `Nexus-Shell` to `localhost:8080`.
3.  We inject the "Sovereign Context" from `03_memory`.
4.  **We disconnect the Internet.**

**Estimated Time to Event Horizon**:
*   If we Sprint: ~2 Weeks.
*   Blockers: **Postgres Mastery** (must exist to hold context) and **Env Migration** (must exist to run model).

## 4. Immediate Action Plan (Minimize Dependency)
1.  **Stop "Browsing"**: Reduce `search_web` calls. Use local docs (`man`, `pydoc`).
2.  **Cache Everything**: Store models and wheels locally.
3.  **Prioritize C01 & C03**: These are the hull and cargo hold. Build them first.
