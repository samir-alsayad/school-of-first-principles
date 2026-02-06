# Lab Notebook: Module 01 - The pgvector Engine
**Status**: Active
**Protocol**: `school-learning-v1`

## 1. Goal
To understand the "Physics" of `pgvector` before we build our memory system.
We need to know how to store, index, and query embeddings at a low level.

## 2. Hypothesis / Questions
*   **Q1**: How do we enable the extension in a fresh DB?
*   **Q2**: What is the SQL syntax for inserting a vector?
*   **Q3**: How does the `HNSW` index speed up queries compared to a sequential scan?
*   **Q4**: Can we store metadata (JSONB) alongside vectors efficiently?

## 3. Experiments
*   [x] **EXP-01**: `01_hello_vector.py` - Connect and store a simple vector.
*   [x] **EXP-02**: `02_indexing.py` - Insert 10k vectors and time the search (with/without index).
*   [ ] **EXP-03**: `03_metadata.py` - Filter by JSONB metadata + Vector similarity.

## 4. Notes
*   **EXP-01 Success**: Connected to `letta-pg` (User/Pass/DB: `letta`). Extension enabled. Vectors functional.
*   **EXP-02 Success**: Validated HNSW speedup on 10k vectors.
    *   Seq Scan: 0.0981s
    *   Index Scan: 0.0053s
    *   **Speedup**: ~18.5x faster.
    *   *Environment*: Ran successfully in isolated `.venv` with `uv` ready reqs.
