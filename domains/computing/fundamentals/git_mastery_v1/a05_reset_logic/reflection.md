# Reflection: a05_reset_logic

## The Mirror
*Professor: "Resetting is just choosing a different 'Now'."*

1.  If I do a `git reset --hard` by accident, are my commits actually deleted?
2.  Which reset type would I use if I want to combine 3 small commits into one giant one? (Hint: Squash).
3.  Why is the Index (Staging Area) so important in the `reset` logic?

## My Notes
- **The Discovery**: [Which reset type do you find most useful?]
- **The Gap**: [Is 'rebase' just a fancy reset?]

## Verified By
- [ ] Invariant: --soft = HEAD only.
- [ ] Invariant: --mixed = HEAD + Index.
- [ ] Invariant: --hard = HEAD + Index + Working Directory.
