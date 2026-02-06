# Campaign 11: The Feedback Loop (MemEvolve)

Mastering the recursive evolution of agent memory.

## The Compiler Narrative
Standard memory systems are static—they record experiences but never change *how* they remember. **MemEvolve** introduces the **Adaptive Learner** paradigm: an agent that not only accumulates experience but refines its own memory architecture (Encode, Store, Retrieve, Manage) through a Diagnose-and-Design loop.

In this campaign, you will move from understanding the theoretical meta-evolutionary paper to manually triggering evolution cycles and auditing the resulting "Genotype" shifts in your Tutor Council.

## Modules

### M01: The Meta-Evolutionary Paper (Theory)
Deep dive into the **MemEvolve** research. Understanding biological analogies: from "Skillful Learners" to "Adaptive Learners."
- **Atoms**:
    - [The Design Space (E, S, R, M)](01_theory/01_design_space.md)
    - [Diagnose-and-Design Logic](01_theory/02_diagnose_design.md)

### M02: Codebase Mastery (In-process)
Navigating the `Flash-Searcher` and `EvolveLab` substrates.
- **Atoms**:
    - [Registry & Implementations](02_code/01_registry.md)
    - [The AutoEvolver Kernel](02_code/02_kernel.md)

### M03: Manual Triggers (Experiment)
Taking control of the feedback loop. Breaking the automated stream to force deterministic evolution.
- **Atoms**:
    - [trigger_evolve.py](03_experiment/01_manual_trigger.md) - Using the CLI to evolve a specific Council expert.
    - [The Genotype Audit](03_experiment/02_genotype_audit.md) - Confirming architectural shifts.

## Compiler Focus
**Mastering the "Why" and "How" of Memory Adaptation.**
