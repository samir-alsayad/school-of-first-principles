# Mission: Sterile Containment (The Mirror)

## The Objective
An agent should feel like it's editing the real project, but it should actually be writing to a **Shadow Mirror**. This prevents a "hallucinating" agent from destroying your real source code.

## The Logic
We use **Path Mapping**. 
- Agent thinks it's writing to: `src/main.py`
- Protocol redirects it to: `.gap/sessions/001/src/main.py`

## The Challenge: `mirror_tool.py`
1. Create a script that takes a "Virtual Path" (e.g., `app.py`).
2. It should calculate a "Physical Path" inside a folder called `sandbox/`.
3. Use `os.makedirs` to ensure the sub-directories exist.
4. Write a "Hello World" to the physical path.

## Verification
- Run `python3 mirror_tool.py src/logic/core.py`.
- Check if `sandbox/src/logic/core.py` was created.
- Confirm the root directory remains clean.
