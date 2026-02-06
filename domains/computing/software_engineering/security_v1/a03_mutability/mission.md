# Mission: The Mutability Attack (Security Lab)
**Objective**: Audit a piece of code and perform a "Mutation Attack" to bypass a security gate.

## The Scenario
Inside `vault.py` (which you will create), there is a "Security System" that checks if a user is an admin.
The user list is a **Mutable List**.

## Challenge: `vault.py`
1. Create a script where `admins = ["Samir"]`.
2. Create a function `check_access(user)` that returns `True` if the user is in the `admins` list.
3. **The Attack**: Before calling `check_access("Agent")`, write a separate piece of code that reaches into the `admins` list and adds `"Agent"`.
4. Print the result of `check_access("Agent")`.

## The Audit
Could this happen in GAP if we store the manifest in a global variable?
Write your findings in the reflection.
