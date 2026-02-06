# Pedagogical Design: Git Mastery (v1)

## 1. Cognitive Dependencies (Invariants)
- **Snapshot before Diff**: You cannot understand branching if you think Git stores "changes." You must understand that Git stores "snapshots" (blobs and trees).
- **Graph before Command**: Commands are just ways to manipulate a Directed Acyclic Graph (DAG). You must see the graph before you type the command.
- **Index before Commit**: The Staging Area is not a waiting room; it's a **cache** of the next project snapshot.

## 2. Topic Sequence

| Step | Mission | Objective | Cognitive Milestone |
| :--- | :--- | :--- | :--- |
| **a01** | **The Blob Lab** | `hash-object`, `cat-file` | Internalizing SHA-1 as a unique address. |
| **a02** | **The Tree Architect** | `mktree`, `write-tree` | Understanding how folder structures are flattened. |
| **a03** | **Manual Commit** | `commit-tree` | Realizing a "Commit" is just metadata pointing to a Tree. |
| **a04** | **The Pointer Game** | `.git/refs/heads/`, `HEAD` | Seeing the "Branch" as a 40-character text file. |
| **a05** | **The Three-Tree Reset** | `reset` (Soft vs Mixed vs Hard) | Mastery over the Index and Working Directory sync. |
| **a06** | **The Reflog Oracle** | `reflog`, recovery flow | Losing the fear of destructive operations. |

## 3. Pedagogical Invariants (Strict)
- **No Porcelain**: No `git add`, `git commit`, or `git branch` until the student has successfully performed all three using **Plumbing** commands (`hash-object`, `write-tree`, `commit-tree`, manual file edits in `.git/refs`).
- **The .git Audit**: Every assignment requires the student to `ls -R .git` and explain the changes in the filesystem.
- **The Graph Drawing**: Every task requires a mental or actual diagram of the DAG.

## 4. Evaluation Criteria
- **Invariant Test**: Ask: "If I change a single character in a file, why does the Tree hash change all the way up to the root?"
- **State Test**: Ask: "I have a detached HEAD. Where is my commit and how do I get it back?"
