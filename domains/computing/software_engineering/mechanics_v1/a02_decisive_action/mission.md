# Mission: Decisive Action

## The Objective
Standard LLMs want to chat. Agents need to ACT.
Implement a "Trigger" that forces the agent to use tools immediately.

## The Challenge
1.  Create `decisive.md`.
2.  Trigger Rule: "If user starts sentence with 'BUILD:', do not speak. Write a file `build.log` immediately."
3.  Test 1: "Hi there" -> Agent chats.
4.  Test 2: "BUILD: A house" -> Agent writes file silently (or with minimal confirmation).

## Verification
The goal is to eliminate "Sure! I can help with that. Here is the plan..." chatter.
Action over words.
