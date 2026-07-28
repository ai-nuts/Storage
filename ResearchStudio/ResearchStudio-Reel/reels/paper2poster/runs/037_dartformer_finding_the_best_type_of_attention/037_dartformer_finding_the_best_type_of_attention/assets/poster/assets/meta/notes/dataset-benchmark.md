# Dataset / Benchmark

Core claim: Three tasks from Long Range Arena (LRA): byte-level binary text classification on IMDb (1k sequence length), ListOps 10-way classification (2k), and byte-level document matching (4k).

Supporting detail: Nine candidate attention mechanisms are searched: Bigbird, Linear Transformer, Linformer, Local, Longformer, Performer, Reformer, Sparse Transformer, and Synthesizer. Hyperparameters largely follow LRA; each homogeneous model is trained three times and averaged.

Narration: All experiments run on three tasks drawn from the Long Range Arena benchmark, chosen to stress long-sequence modeling. These are byte-level binary text classification on IMDb with sequences of one thousand tokens, ListOps ten-way classification with two-thousand-token sequences, and byte-level document matching with four-thousand-token sequences. The search considers nine candidate attention mechanisms, including Bigbird, Linear Transformer, Linformer, Local attention, Longformer, Performer, Reformer, Sparse Transformer, and Synthesizer, with hyperparameters largely matching the original Long Range Arena setup.
