"""
Configuration - All paths and constants.
"""

from pathlib import Path

# Resolve school root relative to this file
# scholar/ is inside src/, so we go up twice
SCHOOL_ROOT = Path(__file__).parent.parent.parent  # src/school/../../ = school root

# Core paths
DOMAINS_PATH = SCHOOL_ROOT / "domains"
TRACKS_PATH = SCHOOL_ROOT / "tracks"
LEARNER_STATE_PATH = SCHOOL_ROOT / "learner_state"
LEDGER_PATH = LEARNER_STATE_PATH / "ledger.yaml"
