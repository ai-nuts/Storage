# Dataset / Benchmark

Core claim: The k-hop induction heads task: a synthetic sequential benchmark generalizing standard induction heads by chaining k bigram completions. Evaluated with context length N = 100, alphabet size |Σ| = 4, and hop counts k ∈ {0, …, 16}.

Supporting detail: It is a hard special case of pointer-chasing and related to the LEGO reasoning task; its k-fold composition structure is what forces a depth-vs-k trade-off that cleanly separates architectures.

Narration: To make everything concrete the authors design the k-hop induction heads task. Standard induction heads asks a model to complete a bigram by predicting the token that followed the last occurrence of the current token. The k-hop version chains this: use one completion to decide which bigram to complete next, k times over. That composition is exactly what makes the task an interesting stress test, because intuitively it looks like it needs k sequential steps, yet a parallel architecture can fold it into logarithmically many. They train and evaluate on sequences of length one hundred over a four-symbol alphabet, sweeping the hop count k from zero up to sixteen, in a multi-task setup where one model handles a randomly drawn k each time.
