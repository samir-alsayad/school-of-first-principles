# Mission: Enforcer Logic (Intent Validation)

## The Objective
"The enforcer doesn't trust the agent's words; it trusts the agent's YAML."
In GAP, we use an **Enforcer** to check every plan before it is executed. If the agent tries to touch a file that isn't in its ACL (Access Control List), the Enforcer kills the session.

## The Logic
The `ACLEnforcer` follows the **Fail-Shut** philosophy. 
If a permission isn't explicitly granted, it is denied. This is the only way to safely run untrusted code.

## The Challenge: `acl_validator.py`
1. Create a script that has a list of `ALLOWED_PATHS = ["src/main.py", "README.md"]`.
2. Create a function `validate_access(attempted_path)` that checks if the path is in the allowed list.
3. **The Test**: Simulate an agent trying to call `validate_access("/etc/passwd")`.
4. The script must raise an error: `"SECURITY BREACH: Access to /etc/passwd is forbidden!"`

## Verification
- Run your validator.
- Prove that it blocks the forbidden path but allows `src/main.py`.
