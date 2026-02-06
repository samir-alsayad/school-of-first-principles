# Repository Structure Guide

## 1. Central Design Rule

> **Folders represent *questions*, not *topics*.**

We do not organize by "Python", "Networking", or "Physics".
We organize by fundamental principles that manifest across all these domains.

## 2. Core Directories (The Questions)

### `representation/`
**Question:** *How is meaning represented?*
*   Unit separation (Number vs. String vs. Byte)
*   Encodings, Scales, Formats
*   *Example:* `representation/numbers/int_vs_str_vs_bytes/`

### `state/`
**Question:** *What can a system be?*
*   States, Transitions, Lifecycles
*   Finite State Machines (FSMs)
*   *Example:* A TCP connection (listening -> connected -> closed) is a pure state machine.

### `time/`
**Question:** *What does "after one another" mean?*
*   Blocking vs. Non-blocking
*   Ordering, Causality, Latency
*   *Example:* `recv()` blocking is a time phenomenon, not just a network feature.

### `information/`
**Question:** *What is information?*
*   Signal vs. Noise
*   Entropy, Redundancy
*   Lossless vs. Lossy
*   *Example:* Raw bytes without context are pure information carriers.

### `computation/`
**Question:** *What means "to calculate"?*
*   Functions, Transformations, Mappings
*   Limits of computation
*   *Example:* Addition is a mapping, not a CPU instruction.

### `systems/`
**Question:** *What happens when things interact?*
*   Boundaries, Resources, Protocols
*   Interactions between processes
*   *Example:* Ports, OS Processes, Resource constraints.

## 3. Support Directories

### `experiments/`
**Purpose:** Quick tests, scratchpad, unpolished ideas.
*   Once an experiment yields a clear principle, it is refined and moved to a Core Directory.

### `notes/`
**Purpose:** Pure text. Aha-moments, mental models, corrected assumptions.
*   The "Why" and the "So What".

### `meta/`
**Purpose:** Reflection on the learning process itself.
*   How we learn, how we use AI, the rules of this school.

## 4. The Experiment Structure
Every canonical experiment (in a Core Directory) should follow this structure:

```
[principle_name]/
├── README.md           # Question, Expectation, Setup
├── [code].py           # The minimal code to probe the system
└── observations.md     # What happened, what was false, what remains
```
