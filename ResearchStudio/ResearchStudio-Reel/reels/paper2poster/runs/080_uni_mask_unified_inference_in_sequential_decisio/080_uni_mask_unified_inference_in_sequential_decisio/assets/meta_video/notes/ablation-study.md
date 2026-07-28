# Ablation Study

Core claim: Comparing the four training regimes isolates fine-tuning as the key ingredient, and comparing single-task Uni[MASK] against Decision-GPT isolates BERT-style versus GPT-style backbones.

Supporting detail: At context length 10, BERT-style Uni[MASK] models degrade and are outperformed by the GPT-based Decision-GPT, exposing a difficulty of BERT-like architectures with longer-sequence generation; feeding only the first RTG token beat feeding it at every timestep.

Narration: The training-regime comparison isolates the effect of each ingredient and shows fine-tuning is the decisive one for good performance in the more complex Maze2D environment. A second, controlled comparison pits single-task Uni-MASK against the Decision-GPT baseline, where the only real difference is a BERT-style versus a GPT-style backbone. Here the picture is nuanced: BERT works well at a short context length of five, but at length ten the BERT-style Uni-MASK models degrade and are outbeaten by the GPT-based Decision-GPT, revealing a known difficulty of BERT-like architectures with longer-sequence generation.
