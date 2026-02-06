# Campaign: Git Mastery (The Meta-Module)

**Vision**: The student learns Git by destroying and rebuilding the School's history.

## The Workflow for New Students

### 1. The Setup (Consumption)
The student clones the "Clean" version of the School.
```bash
git clone https://github.com/samir/school-of-first-principles.git
```

### 2. The Reset (Destruction)
The first task in `curriculum/units/00_meta/01_git_init/README.md` is:
> "To understand Git, you must become the Creator. Delete the `.git` folder."
```bash
rm -rf .git
```
*   **State**: The project is now just a pile of files. No history.

### 3. The Genesis (Creation)
The student initializes *their* repository.
```bash
git init
git add .
git commit -m "Initial commit: My School starts here"
```

### 4. The Branching (Workflow)
We teach the `main` vs `feature` workflow immediately.
*   **Task**: Create a branch for your solutions.
```bash
git checkout -b my-solutions
```
*   **Concept**: `main` is the textbook (Questions). `my-solutions` is the notebook (Answers).

## Implementation Steps for Us
1.  finish our current IPC Campaign.
2.  Clean up the repo (Archive solutions to a separate branch `solutions-ref`).
3.  Ensure `main` only contains the `curriculum/` and empty templates.
