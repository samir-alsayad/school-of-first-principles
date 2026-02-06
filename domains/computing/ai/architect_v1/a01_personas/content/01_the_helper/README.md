# Atom 01: Defining The Helper

## Objective
Learn how to define a **Tactical Assistant** persona using Letta's Infrastructure-as-Code (IaC) patterns.

## The Theory
The **Helper** is the front-line tactical support of the Tutor Council. Unlike the Critic or Optimizer, which observe after the fact, the Helper is meant to be invoked **live** when you are stuck.

### Tactical Constraints
To be effective, the Helper must:
1.  **Stay High-Signal**: Only answer technical questions related to the current workbench context.
2.  **Be Deterministic**: Prefer existing solutions in the curriculum over inventing new patterns.
3.  **Sinkhole Feedback**: Write help-logs to a specific path for the Critic to audit later.

## The Experiment: Persona Blueprinting
In this experiment, you will create the `.json` blueprint for the Helper and instantiate it via the Letta backend.

### 1. Create the Blueprint
Create a file named `helper_blueprint.json`:

```json
{
  "name": "Helper",
  "persona": "You are the Tactical Helper in the Sovereign AI Tutor Council. Your goal is to unblock the learner with precise, technical advice based on the provided workbench context. Stay concise. If a solution is in the curriculum, point to it.",
  "human": "I am a learner in the School of First Principles. I value privacy and local execution.",
  "model": "qwen-14b",
  "embedding": "jina-code"
}
```

### 2. Instantiate the Agent
Run the following command in your terminal:

```bash
letta create-agent --file helper_blueprint.json
```

## Challenge
Modify the persona to include a "Security Protocol" where it refuses to suggest any solution that requires an external API key (all tools must be local).

---
**Status**: [ ] Define Blueprint | [ ] Instantiate Agent | [ ] Test Security Protocol
