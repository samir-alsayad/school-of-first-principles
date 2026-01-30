# Concept Map

This document tracks the dependency graph of principles. Every experiment must hang off a known branch here.

## Legend
*   **[R]**: Root Concept (Assumption-less starting point)
*   **[D]**: Derived Concept (Requires prerequisites)

## The Tree

### 1. Information (Root)
*   **[R] Binary Representation**: How state is encoded (0/1).
    *   **[D] Integer Representation**: Binary to Decimal (Experiment: `...`)

### 2. Communication
*   **[R] Signal**: Information transfer over time.
    *   **[D] Socket**: The OS interface for signals. (Experiment: `01_distributed_adder`)
        *   **[D] Protocol**: Agreeing on meaning (TCP/IP).

### 3. Computation
*   **[D] Adder**: Combining states to create new state.
*   **[D] Function**: A machine that takes input, transforms it, and returns output (Scope).
*   **[D] Execution Model**: How instructions are processed.

### 6. Systems (Inter-Process)
*   **[D] IPC**: Signals (Poke) vs Sockets (Stream) vs Files (Shared State).
*   **[D] Environment**: The air the process breathes (Env Vars, Path).
*   **[D] Permissions**: Who owns the signal? (User/Group, rwx, Admin != Owner).

### 7. State (What is it?)
*   **[R] Variable**: A label for a value.
*   **[D] Lifecycle (Init vs Decl)**: When does it start existing?
    *   *Concept:* In C/Java, you can say "I will have a variable" (Declaration) before you give it value. In Python, they happen together.
*   **[D] Immutability**: Can it change? (Tuple vs List).
