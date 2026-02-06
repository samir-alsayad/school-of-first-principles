# Mission: The Build (Capstone)

## The Objective
Prove your sovereignty.
Build your own GAP Bootstrap System from scratch.

## The Challenge
Create a folder `my_agent/` containing:
1.  `bootstrap.py`: Python script handling arguments and launching `gptme`.
2.  `system.md`: Your Prompt implementing a "Plan -> Code" State Machine.

## Requirements
*   **Args**: The script must accept a `project_path` argument.
*   **Security**: The script must launch `gptme` with **ONLY** `save,read,form` initially (Safe Mode).
*   **Protocol**: The system prompt must forbid coding until the user says "Approve".

## Verification
1.  Run: `python3 bootstrap.py ./test_project`
2.  Conversation:
    *   You: "Build a snake game"
    *   Agent: "Here is the plan..." (NO CODE)
    *   You: "Approve"
    *   Agent: "Coding..." (BUT FAILS because tools are restricted!)
3.  **Bonus**: Use `form` to ask for "Unlocking Tools" to add `python` permission dynamically.

## Victory
If you build this, you understand the Gated Agent Protocol.
You are now a Toolsmith.
