# Reflection: The Physics of Bits
**Status**: [Verified]

## The Mirror
1. Is 4-bit quantization just rounding?
> Not quite. It involves scaling the weights into a specific range before mapping them to integers.

2. Why is "Intelligence" preserved even at 4-bits?
> Large weights (outliers) matter most in neural networks. Modern quantization (like GGUF or EXL2) protects these sensitive weights while being aggressive with the rest.

## My Notes
- **MSE (Mean Squared Error)**: This is our measure of "Loss." The lower the MSE, the better the quantization.
- **GGUF**: The standard format for local inference that supports varied quantization levels.

## The Discovery
Even at 2-bits, some models remain coherent but "hallucinate" more frequently due to high noise. 4-bit is the "Golden Ratio" for local balance.

## Evidence
[Verified in Archive/05_inference_v1]
