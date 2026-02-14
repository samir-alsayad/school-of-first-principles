# Mission: a03_state_sync

## The Objective
This is the most critical mission for the **Agentic Academy**. You will learn how to build a **Letta Tool** that allows an agent to read and write to the local filesystem. Specifically, you will build a bridge that synchronizes the `ledger.yaml` (your truth) with the agent's **Core Memory** (its "Now").

---

## 🏗️ The Setup
Continue using your **Chronos** agent.
You will need a working `ledger.yaml` in your project root.

---

## 🛠️ The Tasks

### 1. The Tool Blueprint
In Letta, tools are Python functions. Create a file called `sync_tools.py` in your workbench:

```python
import yaml
import os

def read_ledger():
    """
    Reads the Academy ledger from the local filesystem.
    Returns: The content of ledger.yaml as a dictionary.
    """
    path = os.path.abspath("learner_state/ledger.yaml")
    if not os.path.exists(path):
        return {"error": "Ledger not found"}
    
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def write_ledger(data):
    """
    Writes updated progress to the Academy ledger.
    Args:
        data (dict): The full ledger dictionary to save.
    """
    path = os.path.abspath("learner_state/ledger.yaml")
    with open(path, 'w') as f:
        yaml.safe_dump(data, f)
    return "Ledger updated successfully."
```

### 2. Registering the Tools
Use the Letta CLI to add these tools to your server and then attach them to your agent.

```bash
letta tool create --file sync_tools.py
letta agent add-tool --agent Chronos --tool read_ledger
letta agent add-tool --agent Chronos --tool write_ledger
```

### 3. The Active Sync
Chat with Chronos and give it an order:
*"Chronos, read my local ledger and tell me my current XP. Then, add a manual log entry saying 'Letta Mastery Initiated' and save it back."*

> [!IMPORTANT]
> Chronos should now be able to "feel" your filesystem. It will read the YAML, parse it, reason about it, and then write the update back to your disk.

---

## 🎯 Verification Criteria
- [ ] You can explain why we use `os.path.abspath` instead of relative paths in Letta tools. (Hint: Letta runs in a sandbox/separate process).
- [ ] The `ledger.yaml` file in your filesystem reflects the changes made by the AI agent.
- [ ] The agent correctly identified your XP from the YAML.
- [ ] You have bridged the gap between "AI Thought" and "Physical State."
