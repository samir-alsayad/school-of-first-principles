# Atom 03: The Critic's Audit

## Objective
Build the **Critic** persona to audit terminal logs for "Sloppiness" and "Technical Debt".

## The Theory
The **Critic** is an observer. It doesn't help you code; it tells you where you took shortcuts.

### Audit Focal Points
The Critic looks for specific "Smells" in your `.gap/sessions/` logs:
1.  **Missing Verification**: You ran a script but didn't check the output.
2.  **Brute Force**: You retried the same command 5 times without changing your logic.
3.  **Path Pollution**: You wrote a temporary file to the project root instead of `/tmp`.

## The Experiment: Log Parsing logic
In this lab, you will write a simple python script to simulate the Critic's audit of a session log.

```python
import json

def audit_log(log_path):
    with open(log_path, 'r') as f:
        events = json.load(f)
    
    for event in events:
        if event['type'] == 'command' and event['exit_code'] != 0:
            print(f"[CRITIC] Error detected in: {event['command']}")
            # Logic for sloppiness check goes here...

# Test with a dummy session log
audit_log('.gap/sessions/latest/events.json')
```

## Challenge
Instruct the Critic to find any instance where an LLM was asked to "write code" but no "run command" was observed immediately following the edit.

---
**Status**: [ ] Define Audit Logic | [ ] Connect to Log Stream | [ ] Run Sloppiness Check
