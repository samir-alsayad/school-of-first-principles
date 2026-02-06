# Mission: Argument Parsing 102 (Advanced Scopes)
## The Objective
Master hierarchical command logic.
Your mission is to upgrade your argument parsing to handle different "Modes" or "Scopes". This mimics how the Scholar CLI will ask about Total vs Project vs Campaign progress.

## The Challenge
Create `lab_scope.py` that:
1.  Accepts a `--scope` argument restricted to: `['total', 'project', 'campaign']` (default: `total`).
2.  Accepts an optional `--id` argument (string).
3.  Logic (Dummy Data):
    *   If scope=`total`: Print "Total Level: 5, XP: 5000"
    *   If scope=`project`:
        *   If `--id` is missing, error: "Project ID required."
        *   Else: Print "Project [id] Level: 2"
    *   If scope=`campaign`:
        *   If `--id` is missing, error: "Campaign ID required."
        *   Else: Print "Campaign [id] XP: 400"

## Hints
*   `choices=['a', 'b']` in `add_argument` forces validation.
*   Check `args.scope` first, then decide if you need to check explicit logic for `args.id`.

## Verification
Run: `python3 lab_scope.py --scope campaign --id "specs"`
Output: `Campaign specs XP: 400`
Run: `python3 lab_scope.py --scope project`
Output: `Error: Project ID required.`
