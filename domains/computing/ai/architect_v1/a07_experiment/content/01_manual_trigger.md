# Experiment Atom: Manual Trigger (trigger_evolve.py)

In this experiment, you will take the reins of the evolution loop. Instead of waiting for the Gateway to decide when to evolve, you will force a cycle manually.

## Goal
Force a **Helper** agent to evolve after a failed task attempt.

## The Setup
1. Identify a task where the agent struggled (e.g., a "tech debt" log).
2. Use the **Evolve CLI** from the AI_CORE workspace:
```bash
# Navigate to the Flash-Searcher environment
cd /Users/Shared/AI_CORE/MemEvolve/Flash-Searcher-main/

# Trigger a manual analysis
python evolve_cli.py analyze /Users/Shared/Projects/IntelHub/lab/logs/failed_task/ --provider agent_kb
```

## Phase 2: Manual Generation
Once analyzed, force the Architect to propose a new genotype:
```bash
python evolve_cli.py generate --creativity 0.8
```

## Success Criteria
Confirm that a new provider file (e.g., `helper_evolved_v1_provider.py`) has been created.
