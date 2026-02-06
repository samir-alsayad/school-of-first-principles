# Mission: The Physics of Bits (Quantization)

## The Objective
"A weight is a number; a number is a container."
To understand quantization, we must see how we can squeeze a 16-bit float into a 4-bit integer without losing the "soul" of the model.

## The Logic
Quantization maps a high-precision range (e.g., -1.0 to 1.0) to a small set of discrete integers (e.g., 0 to 15 for 4-bit).

## The Challenge: `quant_sim.py`
1. Create a list of 10 random float weights between -1.0 and 1.0.
2. Implement a simple "Min-Max" quantization function to map these to the 0-15 range (4-bit).
3. "De-quantize" them back to floats.
4. Calculate the **Mean Squared Error (MSE)** between the original and de-quantized weights.

## Verification
- Prove that the 4-bit version retains the "shape" of the data but introduces "quantization noise."
