# Learning Requirements: Git Mastery (v1)

## 1. Learning Goals (User Stories)
- **As a Student**, I want to understand that Git is a **content-addressable filesystem**, not just a "version control tool," so that I can predict its behavior in complex states.
- **As a Student**, I want to master the **three trees** (Working Directory, Index, HEAD) to eliminate "git add ." as a reflex.
- **As a Student**, I want to understand **Branching as a Pointer**, so that merges, rebases, and resets lose their "magic."
- **As a Student**, I want to recover "lost" work using the **Reflog**, so that I never fear destructive operations.

## 2. Success Criteria
- [ ] **Feynman Test**: Explain the difference between `git reset --hard` and `git reset --soft` to someone who has never used Git.
- [ ] **State Test**: Successfully resolve a complex merge conflict manually using an editor.
- [ ] **Topology Test**: Diagram a rebase vs a merge and explain the trade-offs.
- [ ] **Sovereignty Test**: Restore a deleted branch using only the hash found in the reflog.

## 3. Scope
- **Core**: Content hashing (SHA-1), Objects (Blob, Tree, Commit), Refs.
- **Plumbing**: `hash-object`, `cat-file`, `ls-files`.
- **Porcelain**: `add`, `commit`, `branch`, `checkout`, `reset`, `rebase`, `merge`.
- **Safety**: `stash`, `reflog`.
