# Theory Atom: The AutoEvolver Kernel

The **AutoEvolver** is the orchestrator that manages the transition from "Doing" to "Learning." It implements the **Outer Loop** of the meta-evolutionary process.

## Tournament-Style Evolution
The kernel doesn't just "guess" a better architecture; it runs a rigorous tournament:
1. **Initial Evaluation**: Run the base system on `EVOLVE_TASK_BATCH_X` tasks (default: 20).
2. **Candidate Generation**: Spawn `EVOLVE_GENERATED_M` candidates (default: 3) with varying "Creativity Indexes."
3. **Pareto Scoring**: Evaluating candidates based on Accuracy vs. Token Consumption vs. Latency.
4. **Final Selection**: The "Survivor" with the highest **Scalarized Score** becomes the new base.

## The Scalarized Score Heuristic
Look at `AutoEvolver._pareto_select_top`. The selection isn't just about being "smart." 
Tie-breaking weights:
- **Accuracy**: 0.6
- **Token Efficiency**: 0.25
- **Latency (Execution Time)**: 0.15

## Critical Code Point: `run()`
The `AutoEvolver.run()` method handles checkpointing. If an evolution round fails (e.g., due to an API timeout), it saves its state to `evolve_state.json`, allowing you to resume precisely where it left off.

## Study Task
In `MemEvolve/core/auto_evolver.py`, find the `dominates` function. How does it define "Dominance" between two memory genotypes?
