# Headline Numbers

Core claim: - Up to 12x memory reduction versus Adam fine-tuning (OPT-13B); same memory as inference. - Trains a 30B model on one 80GB A100 GPU, versus only 2.7B for backprop. - Within ~1% of fine-tuning on 7 of 11 OPT-13B tasks. - Up to 2x fewer GPU-hours than Adam fine-tuning at 30B scale.

Supporting detail: Scales tested up to 66B; beats BBTv2 by up to 11% absolute.

Narration: A few numbers capture the impact. MeZO delivers up to a twelvefold reduction in memory compared with Adam fine-tuning on OPT-thirteen-billion, using no more memory than inference. On a single eighty-gigabyte A100, it trains a thirty-billion-parameter model where backpropagation fits only two-point-seven billion. It matches fine-tuning within about one percent on seven of eleven tasks, and it roughly halves the GPU-hours needed at the thirty-billion scale.
