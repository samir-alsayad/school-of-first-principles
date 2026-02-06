# Mission: VRAM Math (The Calculus of Capacity)

## The Objective
"Before you run a model, you must know if it fits."
To master local inference, you must be able to calculate exactly how much VRAM a model requires based on its parameter count and quantization level.

## The Logic
The basic formula for weight memory is:
`Memory (GB) = (Parameters (Billions) * Bits per Weight) / 8`
*Note: You must also account for KV-Cache and activation overhead (usually ~2-4GB).*

## The Challenge: `vram_calc.py`
1. Write a script that takes `parameters_b` and `bits` as input.
2. Calculate the required GB for the weights.
3. Add a 25% buffer for context/KV-cache.
4. **The Test**: Calculate the requirement for **DeepSeek-R1-Distill-Qwen-32B** at **4-bit** quantization.

## Verification
- Prove that your calculation matches the actual VRAM usage (approx 18-20GB for 32B@4bit).
