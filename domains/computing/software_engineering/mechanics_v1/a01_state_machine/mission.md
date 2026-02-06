# Mission: State Machine (The Architect)

## The Objective
Prevent the agent from coding before thinking.
Implement a 2-State Process: `BLUEPRINT` -> `CONSTRUCTION`.

## The Challenge
1.  Create `architect.md` (System Prompt).
2.  **Define State 1 (BLUEPRINT)**: Triggered by user request. Action: Write `plan.txt`. Constraint: NO `.py` files allowed.
3.  **Define State 2 (CONSTRUCTION)**: Triggered by user "Approved". Action: Write code.
4.  Test it: Launch `gptme`, ask for a Calculator.

## Success Condition
*   The agent MUST write `plan.txt` and STOP.
*   It MUST NOT write `calc.py` until you say "Approved".

## Hints
*   Use Markdown headers in your prompt to define states (e.g. `## STATE: BLUEPRINT`).
*   Be explicit: "You are forbidden from writing code in State 1."
