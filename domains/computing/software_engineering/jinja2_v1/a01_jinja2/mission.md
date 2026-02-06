# Mission: Jinja2 (The Templater)

## The Objective
System Prompts are dynamic. We need to inject variables (e.g., User Name, Project Path).
Jinja2 is the industry standard for Python templating.

## The Challenge
1.  Create `prompt.j2` (Template file):
    ```markdown
    You are {{ role }}.
    Your mission is to {{ goal }}.
    ```
2.  Create `render.py`:
    *   Imports `jinja2`.
    *   Creates a `Template` from the file string.
    *   Renders it with `role="Architect"` and `goal="Build a Pyramid"`.
    *   Prints the result.

## Verification
Output:
```
You are Architect.
Your mission is to Build a Pyramid.
```
