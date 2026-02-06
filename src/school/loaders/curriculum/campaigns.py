"""
Campaign loader - Scans /projects for campaign.yaml files.
"""

import sys
import yaml
from typing import Dict, List

from ...config import TRACKS_PATH, SCHOOL_ROOT


def scan_campaigns() -> Dict[str, List[str]]:
    """
    Scan all campaign.yaml files in /tracks.
    Returns: {campaign_id: [assignment_ids]}
    
    Strict validation: exits if projects path doesn't exist.
    """
    campaigns = {}
    
    if not TRACKS_PATH.exists():
        print(f"[FATAL] Tracks path does not exist: {TRACKS_PATH}")
        print(f"[HINT] Expected school root: {SCHOOL_ROOT}")
        print("[HINT] Create /tracks directory or check SCHOOL_ROOT.")
        sys.exit(1)
    
    for campaign_yaml in TRACKS_PATH.rglob("campaign.yaml"):
        try:
            with open(campaign_yaml) as f:
                manifest = yaml.safe_load(f)
            
            campaign_id = manifest.get("id")
            assignments = manifest.get("assignments", [])
            
            if campaign_id:
                campaigns[campaign_id] = assignments
                print(f"[OK] Loaded campaign: {campaign_id} ({len(assignments)} assignments)")
        except Exception as e:
            print(f"[ERR] Failed to load {campaign_yaml}: {e}")
    
    if not campaigns:
        print("[WARN] No campaigns found. Create campaign.yaml files in /tracks.")
    
    return campaigns
