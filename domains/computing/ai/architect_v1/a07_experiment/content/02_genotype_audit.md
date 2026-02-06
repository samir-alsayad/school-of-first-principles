# Experiment Atom: The Genotype Audit

After an evolution cycle completes, you must audit the "Genotype" to understand what structurally changed.

## The Audit Protocol
1. Open the newly generated provider file.
2. Compare its `retrieve` method to the previous version.
3. Locate the `diff` in the `config.json`.

## Questions to Answer
- Did the evolution increase the complexity of the **Retrieval** logic (e.g., adding a reranker)?
- Did it reduce the **Encoding** window to save tokens?
- Is the new Genotype "Smarter" or just "Cheaper"?

## Reflection
Submit a summary of the architectural shift to your **Optimizer** for a strategic review of the new path.
