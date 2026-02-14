# Learning Design: Parallax Socket Transition

## Pedagogical Architecture

### Concept Map
```mermaid
graph TD
    A["Shell Process (ZSH)"] -->|Prerequisite| B["OS Signals (SIGUSR1)"]
    B -->|Current State| C["Parallax v1 (Signal-Driven)"]
    C -->|Gap: Latency/Scale| D["Parallax v2 (Socket-Driven)"]
    D -->|Enables| E["Continuous Assistant Feedback (MiniCPM-o)"]
    F["Python AsyncIO"] -->|Enables| G["Unix Socket Server"]
    G -->|Bridge| D
```

## The Socratic Strategy
**Approach:** Bottom-up Construction (The "Pulse").
We will start by breaking the "Signal" bridge intentionally. The Student will observe the friction of lost messages under high frequency. We then introduce the "Always-On" line.

### Pedagogical Invariants (Dependencies)
*Just as code has invariants, understanding has dependencies.*

**Invariant 1:**
*For any* Student to understand **Persistent Connection**, they MUST first experience the **Statelessness** of Signal/File polling.
**Validates: Objective 1**

**Invariant 2:**
*For any* implementation of a Shell Listener, the Student MUST understand the difference between **Sourcing a file** (Security Risk) and **Parsing a Command** (Sovereign Control).
**Validates: Objective 2**

## Verification Method
**Theory Check:** Explain the "Clogged Doorbell" metaphor versus the "Phone Queue."
**Practical Check:** Move the existing `px-link` logic from `TRAPUSR1` into a persistent `nc -U` loop (or Python shim).
