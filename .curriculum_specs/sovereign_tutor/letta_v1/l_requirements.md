# Learning Requirements: The Sovereign Tutor (Letta Integration)

## Introduction
The Student feels a "tremendous resistance" because current learning flows are too fast and lack persistence. The goal is to build a **Stateful Tutor Agent** that tracks the Student's "Mastery Tiers" across sessions, ensuring that no concept is left un-mastered and the pace adapts to the Student's internal state.

## Conceptual Glossary
- **Stateful Memory**: The ability for an agent to remember details from previous conversations and file edits.
- **Context Window vs. Archival Memory**: Understanding what the agent is thinking *now* vs what it has stored *forever*.
- **The Knowledge Graph**: A map of what the Student knows (Tier 1-10).

## Learning Objectives

### Objective 1: Memory Architecture (Letta)
**Student Story:** As a Sovereign Student, I want to understand how Letta stores my progress, so that I don't feel like I'm starting from scratch every time I open the terminal.

#### Verification Criteria (Acceptance of Knowledge)
1. The Student SHALL be able to explain the difference between Core Memory and Archival Memory in Letta.
2. The Student SHALL be able to point to where their personal progress data is stored on their disk.
3. The Student SHALL implement a "Memory Sync" that saves their `reflection.md` scores into the Letta agent's brain.

### Objective 2: Socratic Adaptation
**Student Story:** As a Student facing resistance, I want the agent to detect my frustration and slow down automatically, so that I can focus on First Principles.

#### Verification Criteria
1. The Student SHALL define the "Resistance Invariants" (what triggers a slow-down).
2. The Student SHALL design the protocol for the agent to check: "Do you truly understand [X], or are we just typing?"
