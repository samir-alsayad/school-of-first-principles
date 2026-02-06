# Mission: Sync Gates (HALT and PROCEED)

## The Objective
Autonomy is not total freedom; it is a series of signed permissions. Every major change requires a "Human High-Five." In this mission, we implement the core **Sync Gates** of GAP: HALT and PROCEED.

## The Logic
A Sync Gate is a junction where the agent must stop and wait for a signal from the Supervisor.
- **HALT**: The agent suspends execution and presents its plan.
- **PROCEED**: The Supervisor validates the plan and signals the agent to continue.

## The Challenge: `sync_gate.py`
1. Create a script that simulates an agent performing a task.
2. After the "Draft" phase, use the `input()` function to ask the supervisor: `"Review Plan. Proceed? (y/n): "`
3. If input is `"y"`, print `"PROCEED: Executing plan..."`.
4. If input is `"n"`, print `"HALT: Agent suspended. Awaiting refinement."` and exit.

## Verification
- Run the script.
- Test both the `y` and `n` paths.
- Observe how the session is physically unable to continue without user interaction.
