# Theory Atom: Bilevel Optimization (Dual-Evolution)

The core scientific innovation of **MemEvolve** is the **Bilevel Optimization** of agent memory. You are not just teaching the agent; you are teaching the agent *how to remember*.

## Inner vs. Outer Loops

MemEvolve conceptualizes evolution as two nested feedback cycles:

### 1. The Inner Loop (Experiential Evolution)
- **Subject**: The Agent's **Experience Base**.
- **Process**: The agent solves tasks and populates a *fixed* memory architecture.
- **Analogy**: A student taking notes in a standard notebook.

### 2. The Outer Loop (Architectural Evolution)
- **Subject**: The Agent's **Memory Architecture** (The "Genotype").
- **Process**: The Meta-Evolver audits the Inner Loop's performance and *redesigns the notebook itself*.
- **Analogy**: The student realizing that a "Mind Map" works better for Literature than a "Checklist," and physically rebuilding their note-taking system.

## The Dual-Evolution Formula
The paper formalizes this as:
- **Inner**: $M_{t+1} = \Omega(M_t, \epsilon_\tau)$ where $\Omega$ is fixed.
- **Outer**: $\Omega^{(k+1)} = \mathcal{F}(\Omega^{(k)}, F^{(k)})$ where $\mathcal{F}$ is the meta-evolution operator.

## Why it's "Stronger"
Most agents only have an Inner Loop (RAG, Long-term memory). MemEvolve is one of the first frameworks to implement a production-ready Outer Loop that **modifies the source code** of the agent's memory providers based on Pareto-optimized fitness signals.

## Reflection
In Campaign 11, you will trigger an Outer Loop cycle manually to see this "Genotype" shift in real-time.
