# Theory Atom: Temperature & Entropy

> [!NOTE]
> This is a **Theory Atom**. Its goal is conceptual mastery. No code execution is required. Read the synthesis, internalize the mechanic, and proceed to the verification questions.

## The Mechanic: Thermal Noise in Thought
Imagine the model's prediction as a landscape of hills. Each hill is a word. The highest hill is the most likely word.

**Temperature (T)** is the heat you apply to this landscape:
- **T = 0**: The landscape freezes. Only the absolute highest hill remains. The model is deterministic. 1+1 will always be 2.
- **T = 1**: The landscape is natural. The model picks words based on their actual predicted probabilities.
- **T > 1**: The landscape melts. Low hills become as tall as high hills. The model becomes chaotic, "drunk," and eventually loses all coherence.

## The Strategic Choice
| Task Type | Recommended Temp | Rationale |
| :--- | :--- | :--- |
| **Logic / Math** | `0.0` | Eliminates "guessing." We want the highest probability of truth. |
| **Code Generation** | `0.2` | Minimal variance to handle syntax strictly, but allows for slight "creative" architectural choices. |
| **Creative Writing** | `0.8` | Encourages flair and unexpected word associations. |
| **Brainstorming** | `1.0+` | Forces the model to look at low-probability "wildcard" ideas. |

## Verification Check
1. Why does setting `Temperature=0` make the `Top-P` setting irrelevant?
2. If a model is stuck in a repetitive loop (echoing the same sentence), would increasing or decreasing temperature help break the loop?
