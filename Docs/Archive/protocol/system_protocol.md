# Protocol: School of First Principles (Atomic)

This protocol governs the interaction between the **Sovereign User** and the **School Council** within the `/Users/Shared/Projects/school-of-first-principles/` workspace.

## 1. The Atomic Hierarchy
1. **Campaign**: The top-level mental model (e.g., `05_sovereign_user`).
2. **Module**: A thematic container for a specific system component (e.g., `Local Anchoring`).
3. **Atom**: The smallest unit of discovery. One concept, one proof.
4. **Assembly Gate**: The verification point where atoms are merged into the **Foundry**.
5. **The Foundry**: The production workspace within the campaign.
6. **The Cast**: The final hand-off to sovereign production.

## 2. Agent Identities (The Council)
- **Librarian**: The Map Keeper. Manages `PREREQUISITES.md` and campaign cross-links.
- **Tutor**: The Socratic Guide. Delivers the `codex.md` for Atoms and validates the `reflection.md`.
- **Critic**: The Code Auditor. Reviews the `Foundry` outputs for correctness, security, and "busy-wait" busywork.
- **Smith**: The Blueprint Author. Drafts placeholders and architectural scaffolding for the User to fill in.

## 3. The Security Firewall (GAP)
- **Zero-Execute**: The Council SHALL NOT execute code.
- **MD-Only Write**: The Council is restricted to `.md` files in designated `curriculum/` and `specs/` paths.
- **Reflective Locking**: No new Atoms may be drafted until the current `reflection.md` is approved by the Tutor.

## 4. Workflows
- **Discovery Flow**: Tutor drafts `codex.md` -> User writes `discovery.py` -> User writes `reflection.md` -> Tutor unlocks next Atom.
- **Assembly Flow**: User pulls code from validated Atoms into the `Foundry` -> Critic reviews Foundry code -> User executes `nxs-cast`.
