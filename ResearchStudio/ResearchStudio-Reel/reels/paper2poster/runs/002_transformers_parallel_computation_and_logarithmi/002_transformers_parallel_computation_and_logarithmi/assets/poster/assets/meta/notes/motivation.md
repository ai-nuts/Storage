# Motivation

Core claim: Unlike recurrent models that process inputs serially, transformers let all tokens interact simultaneously through query-key inner products. This paper identifies that parallelism as the key distinguishing property and formalizes it.

Supporting detail: Massively Parallel Computation (MPC), the theoretical model behind MapReduce-style distributed systems, is the natural formal language for describing what a small number of self-attention layers can compute.

Narration: The authors' insight is that self-attention is fundamentally a parallel operation. Every pair of tokens can interact in one layer through the inner product between their query and key embeddings, whereas a recurrent network must thread information through the sequence one step at a time. That parallelism looks a lot like the Massively Parallel Computation model, or MPC, the abstraction that theorists use to reason about MapReduce and other distributed systems, where many machines each hold a little data and exchange messages in synchronous rounds. The paper's bet is that if you can make the connection between attention layers and MPC rounds precise, you get a single lens that explains both what transformers can do and what they cannot.
