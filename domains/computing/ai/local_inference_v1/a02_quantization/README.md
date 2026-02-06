# Atom: Bits & Quantization

The first principle of local inference is that **precision is a choice.**

## The Principle
Weights start as 16-bit floats (fp16). By compressing them to 4-bit (int4), we trade a tiny amount of accuracy for a 4x reduction in memory footprint. This is the difference between a model being "impossible" and "running on your laptop."

## Learning Objectives
- Differentiate between weight quantization and activation quantization.
- Understand the role of "scales" and "zeros" in dequantization.

## The Experiment
Run `bits_check.py` to compare the memory footprint of a 7B model at different precisions.
