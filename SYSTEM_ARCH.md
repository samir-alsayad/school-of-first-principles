# System Architecture: The School of First Principles

This document defines the structural and security integration between the **Sovereign Machine** and the **School Council**.

## 1. The Security Layer (GAP)
The School operates as a **Sovereign Domain** within the Gated Agent Protocol (GAP).
- **Domain Identity**: `sovereign/school-of-first-principles`
- **Inheritance**: Extends `core/instructional` (The Blueprint for Pedagogical Work).
- **Inheritance Logic**:
    - **Inherits**: Standard Instructional Gates (Draft -> Review -> Publish).
    - **Inherits**: Standard Roles (Author, Reviewer).
    - **Overrides**: Adds `Reflective Locking` and specific `school-of-first-principles` paths.
- **Enforcement**: ACLEnforcer blocks all execution and restricts writes to authorized `.md` paths.

## 2. The Atomic Data Flow
We utilize an **Atomic Curriculum** strategy to ensure high-fidelity knowledge transfer:

```mermaid
graph TD
    subgraph "The School (Authorized Context)"
        A[Campaign 05: Sovereign User] --> B[Module: Local Anchoring]
        B --> C1[Atom: Binary Discovery]
        B --> C2[Atom: DB Genesis]
        B --> C3[Atom: Vector Key]
        C1 & C2 & C3 --> D[Assembly Gate: Anchoring Letta]
    end

    subgraph "The Foundry (Drafting Area)"
        D --> E[Foundry: local_bridge.py]
    end

    subgraph "The Sovereign Machine (Production)"
        E --> F{The Cast}
        F --> G[Production: /Users/Shared/Projects/...]
    end

    style G fill:#f9f,stroke:#333,stroke-width:4px
```

## 3. The Council Matrix
The School is staffed by specialized agent identities, each governed by specific GAP roles:

| Council Role | GAP Role | Responsibility |
| :--- | :--- | :--- |
| **Librarian** | `archivist` | Memory linkage & Prerequisite mapping. |
| **Tutor** | `instructor` | Socratic guidance & Reflective Gate validation. |
| **Critic** | `reviewer` | Foundry code audit & security checking. |
| **Smith** | `drafter` | Initial blueprint generation (MD-only). |

## 4. Operational Invariants
1. **Zero-Execution**: AI agents are physically blocked from running shell commands.
2. **Reflective Locking**: Progress requires human-written `reflection.md`.
3. **Manual Casting**: Only the Sovereign (User) can move code from the Foundry to Production.
