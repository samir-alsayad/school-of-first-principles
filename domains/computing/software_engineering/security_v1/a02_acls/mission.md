# Mission: Tool ACLs (Capabilities)

## The Objective
Limit the agent's blast radius.

## The Challenge
1.  Launch `gptme` with **ONLY** `save` and `read` tools.
2.  Try to make the agent run a python script (using `shell` or `python`).
3.  **Success**: The agent fails or says "I cannot do that".

## Hints
*   Flag: `--tools "save,read"` (Omit `python`, `shell`).

## Verification
This is "Safe Mode". A compromised agent cannot delete your system files if it has no shell access.
