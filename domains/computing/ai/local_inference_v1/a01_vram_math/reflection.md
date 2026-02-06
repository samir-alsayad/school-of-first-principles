# Reflection: VRAM Math
**Status**: [Verified]

## The Mirror
1. Why does a 32B model take ~16GB at 4-bit but ~64GB at 16-bit?
> Because 4-bit uses 4 bits per weight (0.5 bytes), while 16-bit uses 2 bytes. The reduction is 4x.

2. What happens if the model is 100MB larger than your VRAM?
> On Unified Memory (Mac), it swaps to RAM, causing a massive performance drop (token/s). On dedicated GPUs, it usually crashes with OOM (Out of Memory).

## My Notes
- **Unified Memory**: The Mac's greatest strength for AI is that the CPU and GPU share the same pool of fast RAM.
- **Quantization is Lossy**: Reducing bits saves space but slowly degrades "intelligence" (perplexity).

## The Discovery
Found that adding a constant buffer isn't enough for long-context models; the KV-cache grows linearly with sequence length.

## Evidence
[Verified in Archive/05_inference_v1]
