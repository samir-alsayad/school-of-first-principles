# Reflection: a04_refs_and_heads

## The Mirror
*Professor: "A branch is a name, not a place."*

1.  If I delete the `.git/refs/heads/master` file, do I delete the commits?
2.  What is a "Detached HEAD"? (Hint: What if `.git/HEAD` contains a hash instead of a `ref:`?)
3.  Why does Git use a symbolic ref for HEAD instead of just storing the hash of the current commit?

## My Notes
- **The Discovery**: [How did your fear of 'branches' change?]
- **The Gap**: [Is 'merging' still magical?]

## Verified By
- [ ] Invariant: Branch = Text file containing a Commit Hash.
- [ ] Invariant: HEAD = Pointer to a Branch or a Commit.
