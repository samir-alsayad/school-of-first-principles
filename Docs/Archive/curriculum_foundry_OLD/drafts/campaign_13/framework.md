# Campaign 13 Framework: The Orchestration Logic
**Archetype**: The Analyst
**Status**: Evaluated

## 1. The Gap Analysis
We have the **Parts**:
- `school-learning-v1`: Handles low-rigor skill acquisition.
- `school-foundry-v1`: Handles high-rigor delivery.

We lack the **Orchestrator**:
- No protocol exists to *transition* between these states based on a long-running goal.
- Current protocols are "Atomic" (do one thing). A Campaign is "Molecular" (composed of atoms).

## 2. The Logic Framework (State Machine)
We need a protocol that acts as a **Container State Machine**.

### State A: The Empty Vessel (Gate I)
- **Input**: User Intent (EARS).
- **Invariant**: Design Spec must be NULL.
- **Allowed Transitions**: To State B (Learning).

### State B: The Learning Loop (Gate II)
- **Activity**: Spawning `school-learning-v1` child sessions.
- **Invariant**: Cannot exit until "Definition of Done" (from Charter) is met.
- **Accumulator**: `knowledge_ledger.md` (Tracks what was learned).

### State C: The Design Lock (Gate III)
- **Activity**: Writing the EARS Spec & Casting Guide.
- **Invariant**: Must reference `knowledge_ledger` items as justification.
- **Transition**: To State D (foundry).

### State D: The Delivery (Gate IV)
- **Activity**: Spawning `school-foundry-v1` child session.
- **Invariant**: Strict adherence to Casting Guide.

## 3. Implementation Strategy
The `school-campaign-v1` manifest will be a **Meta-Protocol**.
It does not manage files directly; it manages **Child Sessions**.
*   It authorizes the creation of a `learning` session.
*   It authorizes the creation of a `foundry` session.
