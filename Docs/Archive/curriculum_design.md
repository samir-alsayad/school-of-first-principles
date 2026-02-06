# Curriculum Design Strategy

## 1. The Core Philosophy
We do not "teach topics". We **reconstruct understanding** from the bottom up.
Every assignment must isolate **ONE First Principle** and prove it through a **Constraint**.

## 2. The Atomic Assignment Structure
To generate a valid assignment for you, I must construct it with these 4 parts:

### A. The Concept & The Anchor
*   **Concept**: What is the abstract principle? (e.g., "Positional Notation")
*   **Anchor**: Where does this sit in the `concept_map.md`? (e.g., `Representation -> Number Systems`)

### B. The Constraint (The Handicap)
*   **Rule**: You cannot use the "Easy Button" (e.g., `no int()`).
*   **Why**: Constraints force you to built the mental model of *how* the easy button works.

### C. The Prediction Gap
*   Before coding, you must predict an outcome that feels counter-intuitive or requires calculation.
*   *Example:* "What is `10 ** (3-0)` vs `10 ** (3-1)`?"

### D. The Verification Loop
*   Code runs -> Output is captured.
*   **Learnings**: You explain *why* it worked.

---

## 3. Project Deconstruction Protocol (For your Projects)
When you show me a complex project, I will not explain the code. I will:

1.  **Scan for Concepts**: Identify every "Black Box" in the code (e.g., `async`, `class`, `socket`, `decorator`).
2.  **Check the Map**: Compare against `meta/concept_map.md`.
    *   *Known?* -> Ignored.
    *   *Unknown?* -> **Flagged**.
3.  **Generate Dependency Tree**: Create a linear path of Micro-Experiments needed to understand the project.

**Example:**
*Input:* A Python Web Server with `asyncio`.
*Strategy:*
1.  Flag `async/await` -> Create Experiment: "Blocking vs Non-Blocking Time".
2.  Flag `HTTP Headers` -> Create Experiment: "Sending text via Sockets".
3.  **Goal**: You rebuild the mental model of the server, one experiment at a time.
