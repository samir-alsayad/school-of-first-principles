# Reflection: a03_commit_plumbing

## The Mirror
*Professor: "History is just a chain of pointers to snapshots."*

1.  Why does your name and email appear in the commit object even though you didn't provide them to `commit-tree`? (Hint: `git config`).
2.  What happens to the 'History' if you delete a commit object but keep its child? (Dangling commits).
3.  If you commit the exact same tree twice with a 1-second delay, why are the hashes different?

## My Notes
- **The Discovery**: [How simplified is 'committing' now?]
- **The Gap**: [How do branches fit into this?]

## Verified By
- [ ] Invariant: Commit = Metadata + Tree Pointer + Parent Pointer.
- [ ] Invariant: Git Log is a traversal of Commit Parent pointers.
