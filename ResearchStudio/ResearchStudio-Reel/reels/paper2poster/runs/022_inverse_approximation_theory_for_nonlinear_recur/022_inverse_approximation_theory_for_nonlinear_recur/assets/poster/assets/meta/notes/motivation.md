# Motivation

Core claim: In machine learning most approximation results are forward theorems that bound achievable error; the reverse question, what a target must look like to be efficiently and stably learnable, is under-explored and far more revealing of architectural limits.

Supporting detail: A prior Bernstein-type result showed linear-RNN-approximable targets must have exponentially decaying memory, but its linear-only scope left open whether nonlinearity removes the limitation.

Narration: Approximation theory offers two complementary kinds of statements. Forward, or Jackson-type, theorems tell you how well a model can approximate a sufficiently regular target. Inverse, or Bernstein-type, theorems run the other direction: they assume a target can be efficiently approximated and then deduce what regularity the target must have. Inverse theorems are precisely the tool for exposing fundamental limitations of an architecture. Earlier work proved such a result for linear RNNs, showing that efficiently approximable linear targets must have exponentially decaying memory. The pressing question was whether adding nonlinearity, which greatly increases model capacity, would break this so-called curse of memory. This paper was motivated to settle that.
