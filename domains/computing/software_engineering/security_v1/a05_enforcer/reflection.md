# Reflection: Enforcer Logic
**Status**: [Verified]

## The Mirror
1. Why do we call this "Fail-Shut"?
> Because if any part of the validation fails or is uncertain, the default action is to shut down the process rather than allowing it to continue.

2. Does the Enforcer care about the *intent* of the agent?
> No. The Enforcer only cares about the *action* (the path being touched) and whether it matches the whitelist.

## My Notes
The `ACLEnforcer` is the brain of the GAP proxy. It parses the **Embedded ACL Block** in a plan and builds a "Whitelisted Permissions Set". It handles broad wildcards (e.g., `tests/*.py`) by validating them before any tool-call is made.

## The Discovery
I proven that simple string matching isn't enough—we need to handle absolute vs physical paths to prevent "Double-Dot" (`../`) escapes.

## The Gap
[How do we extend this to network access or tool-specific permissions?]

## Evidence
[Verified in Archive/07_security_v1]
