# Motivation

Core claim: Prior in-context methods like DATER hard-decompose a table into a sub-table, which can discard useful cells and lock in errors when the wrong sub-table is selected.

Supporting detail: Explicitly removing table content is brittle; a soft relevance-weighting scheme keeps all information available while still de-emphasizing noise.

Narration: A natural way to reduce noise is to shrink the table before answering, and methods like DATER do this by decomposing the table into a smaller sub-table. The trouble is that hard decomposition is unforgiving: if the wrong sub-table is extracted, useful information is permanently lost and the reasoner answers incorrectly with no way to recover. CABINET argues for a softer approach that weighs relevant parts higher without ever explicitly removing content, so the answering model retains access to the whole table while being steered toward what matters.
