# Reflection: a02_tree_objects

## The Mirror
*Professor: "A directory is just a file that lists other files."*

1.  If I have two identical folders (different names, identical contents), does Git create one or two Tree objects?
2.  Why is the Tree hash deterministic? (Same content + same filenames = same hash).
3.  How does Git know if a file is an executable (script) or a regular text file? (Look at the 'mode' bits in the tree).

## My Notes
- **The Discovery**: [How did your view of 'folders' change?]
- **The Gap**: [What is confusing about tree vs blob?]

## Verified By
- [ ] Invariant: Tree = List of (Mode, Type, Hash, Name).
- [ ] Invariant: Renaming a file changes the Tree Hash, but not the Blob Hash.
