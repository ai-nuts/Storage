# Takeaway

Core claim: Turning a retrieval datastore into a pointer-and-cluster automaton lets a language model reuse retrieval across time steps, so it skips most costly nearest-neighbor searches while matching or beating perplexity.

Supporting detail: The construction is unsupervised, model-agnostic, and works across domains, generalizing token, chunk, and sequence retrieval within a single dynamic mechanism.

Narration: The lasting idea is that a retrieval datastore has structure worth exploiting. By linking consecutive entries with pointers and grouping similar ones into automaton states, RetoMaton lets a language model carry retrieval forward in time instead of searching from scratch at every token. It is unsupervised, works with any base model, transfers across domains, and unifies token, chunk, and sequence retrieval, all while cutting the dominant cost of retrieval-based language modeling.
