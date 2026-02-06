# Protocol: The Atomic Assignment

## Philosophy
The School operates on the principle of **Atomic Units of Work**.
An assignment must never be overwhelming. It must teach exactly one concept or achieve one concrete verification step.

## Campaign Architecture
Projects are strictly divided into two types of Campaigns:
1.  **Theory Campaigns**: Focus on specifications, philosophy, and architectural design (The "Classroom").
    *   *Output*: Markdown files (`VISION.md`, `PROTOCOL.md`), Rulesets.
2.  **Foundry Campaigns**: Focus on concrete implementation and tool building (The "Lab").
    *   *Output*: Code, CLIs, Executables.

## Registration Protocol
1.  **Project Registry**: The root `structure.yaml` registers all active Campaigns.
2.  **Campaign Registry**: Each Campaign MUST have its own internal registrar (e.g., `structure.yaml` or explicit module list) to track its specific Modules.
3.  **No Ghost Work**: If it is not registered, it does not exist.

## The Rule of Splitting
IF an assignment requires more than one major mental context switch, OR more than 3 distinct verification steps, THEN it must be split.

## The Format
Every registered module MUST consist of:
1.  **Mission (`mission.md`)**: The Objective, The Challenge, Hints, Verification.
2.  **Reflection (`reflection.md`)**: The Mirror, The Gap, Evidence.
3.  **Status Metadata**: strictly `**Status**: [Pending/Verified]`.

## Registry
All work must be registered in the project's `structure.yaml` before execution begins.
