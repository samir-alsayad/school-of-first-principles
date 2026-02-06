# Theory Atom: Model Selection Matrix

To build a sovereign Tutor Council on a single M-series machine (48GB RAM), we cannot simply load four massive models. We must practice **Role-Specific Optimization**.

## The Council Selection Logic

| Persona | Model Candidate | VRAM (Est) | Rationale |
| :--- | :--- | :--- | :--- |
| **The Helper** | `Qwen2.5-Coder-14B` (4bit) | ~8GB | Primary "tactical" copilot. Needs to be fast and high-accuracy for tool calls. |
| **The Proposer** | `Qwen2.5-Coder-32B` (4bit) | ~18GB | The "creative architect." Needs high parameter count for structural drafting of long documents. |
| **The Critic** | `Qwen3-Coder-30B` (8bit) | ~30GB | The "audit engine." Needs 8-bit precision to detect subtle "sloppiness" that 4-bit models might miss. |
| **The Optimizer**| `Devstral-24B` (4bit) | ~14GB | Specialized in strategic pathing and roadmapping. |

## Strategy: Sequential Brain Activation
Since we have 48GB RAM, we cannot have all models "Resident" simultaneously if they exceed the limit.
- **Active**: Only one "Expert" (Helper/Proposer/Critic/Optimizer) should be hot-loaded at a time during intense reasoning cycles.

## Verification Check
1. Why is the **Critic** assigned an 8-bit model while the **Proposer** uses 4-bit?
2. If the user is doing rapid-fire debugging, which Council model should be the focus of the inference buffer?
