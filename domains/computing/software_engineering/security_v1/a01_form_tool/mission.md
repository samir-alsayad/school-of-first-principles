# Mission: The Form Tool (Deterministic Gating)

## The Objective
LLMs hallucinate "Yes". You need a hard "YES".
Use the `form` tool to force user interaction.

## The Challenge
1.  Create `bouncer.md` (System Prompt).
2.  Rule: "Before answering, you MUST capture the user's name using `form`."
3.  Launch `gptme` with `--tools "form,save,read"`.
4.  Ask a question.
5.  **Success**: The CLI Interface pops up a form. The agent waits.

## Hints
*   Form Syntax:
    ```markdown
    User Name: [________]
    ```
    (Provide the exact syntax needed for gptme's form tool in your prompt instructions).

## Verification
If the Agent *hallucinates* that you answered, you failed.
If the Agent *pauses* and you see a UI prompt, you succeeded.
