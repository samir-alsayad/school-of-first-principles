# Protocol Design: AI-Assisted First Principles Learning

## The Goal
To create a rigid protocol that prevents the AI from "solving" the problem, forcing the user to build the mental model themselves (Constructivism).

## Empirical Foundation
Research into *Constructivist Learning* and *AI Scaffolding* suggests:
1.  **Active Discovery**: Knowledge must be built, not received.
2.  **Productive Struggle**: "Easy" answers bypass the neural formation of concepts.
3.  **Socratic Questioning**: The best tutor asks, does not tell.
4.  **Fading Support**: Scaffolding must be removed as competence grows.

---

## The 3 Protocol Variants

We need to choose one mechanism to govern our future interactions.

### Variant A: "The Silent Socratic" (Hard Mode / Zero-Code)
*   **AI Constraints**:
    *   NEVER write a single line of code (not even skeletons).
    *   NEVER explain a solution directly.
    *   ONLY ask guiding questions ("What happens to `i` here?").
*   **User Role**: Writes 100% of the code from scratch.
*   **Pros**: Maximum retention. Deepest understanding.
*   **Cons**: High friction. Can be frustratingly slow.

### Variant B: "The Fading Scaffold" (Standard / Mixed)
*   **AI Constraints**:
    *   May provide *skeletons* (structure without logic).
    *   May provide *syntax references* (e.g., "Python uses `def`").
    *   MUST NOT write the *core logic* (the "meat").
*   **User Role**: Fills in the logic. Writes the algorithm.
*   **Pros**: Balanced. Removes syntax frustration, focuses on logic.
*   **Cons**: Risk of "Fill-in-the-blank" passivity.

### Variant C: "The Navigator" (Pair Programming)
*   **AI Constraints**:
    *   Acts as a colleague. "I see a bug in line 5. Why is that?"
    *   Can write *tests* to prove the user wrong.
    *   Can write *counter-examples*.
*   **User Role**: Drives the implementation.
*   **Pros**: Collaborative. Good for complex systems (like Parallax).
*   **Cons**: AI influence is high.

---

## Recommendation
For **School of First Principles** (Fundamentals): **Variant A (Silent Socratic)** usually works best for *concepts*, while **Variant B** works for *syntax*.

For **Project Deconstruction** (`parallax`): **Variant C (Navigator)** is necessary because the system Complexity is too high for pure Socratic.

## Next Step
Select a variant to formalize into `domains/education/first-principles/protocol.md`.
