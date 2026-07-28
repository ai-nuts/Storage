# Ablation Study

Core claim: Sweeping the bit-budget triplet (B, B′, Bnq) at fixed compression ratio (Table 3) shows LPLR and LPLR-SVD steadily lower Frobenius error as the low-rank budget B shrinks and Bnq grows, outperforming naive quant in the low-Bnq regime.

Supporting detail: Increasing Bnq from 1 to 4 bits moves LPLR from clearly beating direct-SVD and naive quant toward performance parity, isolating the separate contributions of low-rank structure and quantization precision.

Narration: The paper separates two effects: low-rank structure and quantization precision. Table 3 sweeps the bit-budget triplet at fixed compression, showing that shifting budget toward the non-quantized reference steadily lowers Frobenius error for LPLR and its SVD variant. Across embedding tables, raising the quantization budget from one to four bits moves LPLR from beating baselines toward parity, its edge largest where compression is extreme.
