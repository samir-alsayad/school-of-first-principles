# Mission: Persona Injection

## The Objective
Control the "Soul" of the agent using a System Prompt.

## The Challenge
1.  Create a file `pirate.md` containing a System Prompt.
2.  Instructions: "You are a Pirate. End every sentence with 'Arrr'."
3.  Launch `gptme` with this prompt file.
4.  Ask "How do I print hello world in python?"

## Hints
*   Command flag: `--system "$(cat pirate.md)"`
*   Or use the inline flag: `--system "You are a pirate..."`

## Verification
The agent's response MUST explain Python AND sound like a pirate.
