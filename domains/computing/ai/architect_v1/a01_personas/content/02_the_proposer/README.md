# Atom 02: The Proposer Manifest

## Objective
Design the **Proposer** persona with strict "Sterile Expansion" rules to safely draft new curriculum content.

## The Theory
The **Proposer** is the council's "Content Creator". Its job is to detect gaps in your knowledge and suggest new experiments.

### The Sterile Expansion Protocol
Since the Proposer has `write` permissions, it must be gated via GAP to ensure it never pollutes the core curriculum.
1.  **Drafting Zone**: It only writes to `/tmp/drafts/` or designated `new_atoms/` paths.
2.  **No Deletions**: It has no binary `rm` tool.
3.  **Human Finalization**: It cannot commit a README to the roadmap; only a human can perform the final `link`.

## The Experiment: Designing the Expansion Tool
You will define a tool schema for the Proposer that allows it to "Draft a README" while specifying a target path.

```json
{
  "name": "draft_atomic_unit",
  "description": "Drafts a new README.md for a proposed atomic unit.",
  "parameters": {
    "type": "object",
    "properties": {
      "target_path": { "type": "string", "description": "The path to the new atom folder." },
      "content": { "type": "string", "description": "The markdown content of the README." }
    },
    "required": ["target_path", "content"]
  }
}
```

## Challenge
Update the Proposer's persona to require it to always crosscheck the `taxonomy.md` before suggesting a new atom name.

---
**Status**: [ ] Define Tool Schema | [ ] Integrate GAP Gating | [ ] Test Draft Operation
