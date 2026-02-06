# Atomic Unit 5.1.2.05: The RLM Explorer (Recursive Exploration)

> "Don't read the whole book if you only need one chapter. RLM reads only what matters."

## 🔬 The Principle
Small models (like LFM2-2.6B) have tiny context windows. To help them navigate large codebases, we use **Recursive-LLM (rlm)** patterns.
The agent first lists the directory, then "dives" into one file, then "looks" at specific lines, instead of trying to ingest the whole folder at once.

## 🎯 Learning Objectives
1.  The `ls` -> `view` -> `edit` loop.
2.  Building a mental map of a project without full ingestion.
3.  Why "Recursive Search" is the secret to getting small models to perform like large ones.

## 🛠 Project Link
Study the RLM integration: [IntelHub/lab/agent_factory/rlm](file:///Users/Shared/Projects/IntelHub/lab/agent_factory/evolution_work)
