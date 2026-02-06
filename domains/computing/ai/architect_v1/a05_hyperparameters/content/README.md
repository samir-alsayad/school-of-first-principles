# M02: The Control Knobs (Hyperparameters)

Mastering an LLM is like playing a specialized synthesizer. You are not just sending text; you are shaping the probability distribution of the model's next token. This module explores the mathematical "knobs" that control the stochasticity and focus of the engine.

## The Theory of Stochasticity
At its core, an LLM is a probability engine. It predicts the most likely next token. Hyperparameters allow us to warp that probability field.

## The Narrative Atoms

### [01: Temperature & Entropy](01_temperature/)
*The heat of the engine.*
- **Concept**: How "Temperature" flattens the probability curve.
- **Mastery**: Understanding when to use `0.0` (math/code) vs `0.8+` (creative writing).

### [02: The Sampling Filters](02_sampling/)
*Focusing the beam.*
- **Concept**: Top-P (Nucleus), Top-K, and the new **Min-P** (the smartest filter).
- **Mastery**: Learning why Min-P is superior for preserving high-logic reasoning while pruning junk.

### [03: Frequency & Presence Penalties](03_penalties/)
*Combatting Echoes.*
- **Concept**: How penalties discourage repetition.
- **Mastery**: Tuning penalties for long-form generation to prevent "looped thought" logic errors.
