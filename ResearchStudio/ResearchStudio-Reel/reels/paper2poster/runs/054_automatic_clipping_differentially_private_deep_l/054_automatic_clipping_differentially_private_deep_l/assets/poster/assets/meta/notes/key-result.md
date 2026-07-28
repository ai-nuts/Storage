# Key Result

Core claim: Automatic clipping (AUTO-S) matches or beats state-of-the-art on every task without tuning R: e.g. GPT2 on E2E reaches BLEU 64.18 at epsilon=3 (vs 63.85 prior), and RoBERTa-base SST-2 reaches 92.32% vs 91.86%.

Supporting detail: On CIFAR10 with SimCLRv2, AUTO-S reaches 92.70% at epsilon=2; RoBERTa-large SST-2 hits 94.61% at epsilon=8; searching only the learning rate (not the (R, learning rate) grid) cuts tuning cost roughly 5x.

Narration: Across the board, automatic clipping matches or outperforms the state of the art, and it does so without ever tuning the threshold. For GPT2 text generation on E2E, AUTO-S reaches a BLEU score of sixty-four point one eight at epsilon three, edging past the prior best of sixty-three point eight five. For RoBERTa-base on SST-2, it reaches ninety-two point three two percent, above the prior ninety-one point eight six. On CIFAR-10 with a pretrained SimCLRv2 it hits ninety-two point seven percent at epsilon two. And because only the learning rate needs searching, the tuning cost drops by about five times.
