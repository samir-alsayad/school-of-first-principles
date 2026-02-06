"""
Ledger loader - Loads learner progress from ledger.yaml.
"""

import yaml
from typing import Set

from ...config import LEDGER_PATH, LEARNER_STATE_PATH


def load_ledger() -> Set[str]:
    """
    Load completed assignment IDs from ledger.yaml.
    Returns: set of completed assignment IDs
    
    Creates learner_state directory if it doesn't exist.
    """
    if not LEDGER_PATH.exists():
        print(f"[WARN] Ledger does not exist: {LEDGER_PATH}")
        print("[INFO] Creating empty learner_state directory...")
        LEARNER_STATE_PATH.mkdir(parents=True, exist_ok=True)
        return set()
    
    try:
        with open(LEDGER_PATH) as f:
            ledger = yaml.safe_load(f) or {}
        
        completed = set(ledger.get("completed", {}).keys())
        print(f"[OK] Loaded ledger: {len(completed)} completed assignments")
        return completed
    except Exception as e:
        print(f"[ERR] Failed to load ledger: {e}")
        return set()
