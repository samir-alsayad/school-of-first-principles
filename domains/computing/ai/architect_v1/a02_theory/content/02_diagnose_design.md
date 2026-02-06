# Theory Atom: Diagnose-and-Design Logic

In this atom, you will learn the "Brain" of the meta-evolutionary process: how MemEvolve identifies its own weaknesses and proposes architectural fixes through **Contrastive Learning**.

## The Dual-Evolution Loop

MemEvolve operates in two nested cycles:
1. **Inner Loop (Experiential)**: The agent solves tasks and builds its memory base (M) using fixed rules.
2. **Outer Loop (Architectural)**: The **Meta-Evolver** (AutoEvolver) audits the logs of the Inner Loop to find bottlenecks and redesigns the memory system (Ω) itself.

## The 4-Phase Transition

When you trigger an evolution cycle, the system moves through these deterministic stages (as implemented in `MemoryEvolver`):

| Phase | Core Class | Agent Role | Output |
| :--- | :--- | :--- | :--- |
| **1. Analyze** | `PhaseAnalyzer` | **The Auditor** | A `defect_profile` identifying why the agent failed (e.g., "Retrieved successful trajectories that were irrelevant"). |
| **2. Generate** | `PhaseGenerator` | **The Architect** | A new "Genotype" (JSON config) that tweaks the code of the memory modules (E, S, R, M). |
| **3. Create** | `MemorySystemCreator` | **The Builder** | Production-ready `.py` files in `EvolveLab/providers/` and entry updates in `memory_types.py`. |
| **4. Validate** | `PhaseValidator` | **The Tester** | Static checks and "dry-runs" to ensure the new code actually executes without crashes. |

## The Science of Contrastive Diagnosis
Why "Diagnose-and-Design"? Unlike basic "Self-Reflection," the `PhaseAnalyzer` uses **Contrastive Learning**. It evaluates **Successful** vs. **Failed** trajectories side-by-side to determine which memory retrieval sparked the divergence. If the Auditor sees that the agent keeps retrieving similar but irrelevant facts, the Architect might decide to evolve the Retrieval module from simple `Top-K` to a `Clustered-Reranking` approach.

## Next Step
In the experiment atom, you will use a manual trigger to force this transition and audit the resulting code diff.
