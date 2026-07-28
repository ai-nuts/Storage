# Headline Numbers

Core claim: On CIFAR-10 with 60% cue data, CBFT keeps accuracy nearly constant across No-Cue, With-Cue, and Randomized-Cue tests (74.1 / 71.5 / 73.4%), whereas fine-tuning collapses from 98.7% with cue to 17.5% on randomized cue, evidence of cue reliance.

Supporting detail: Across CIFAR-10, CIFAR-100 and Dominoes (mean of three seeds), only CBFT drives Randomized-Image accuracy toward chance (e.g. 8.75% on CIFAR-10), confirming it stops predicting from the cue.

Narration: The numbers make the effect concrete. On CIFAR-10 with sixty percent cued data, Connectivity-Based Fine-Tuning achieves seventy-four percent accuracy without the cue, seventy-two percent with the cue, and seventy-three percent when the cue is randomized, essentially invariant to the cue. A standard fine-tuning baseline, by contrast, hits ninety-nine percent with the cue but drops to just seventeen percent when the cue is randomized, revealing heavy reliance on the spurious feature. And when the underlying image is randomized, CBFT falls near chance, around nine percent, showing it no longer predicts from the cue at all.
