# Takeaway

Core claim: For active learning with tabular language models, cell-level acquisition with built-in batch diversity (BADGE) can hit full-training performance with far fewer expert labels, but forcing maximum table diversity backfires: balancing diversity against uncertainty is the key.

Supporting detail: This is the first study of active learning for tabular language models, leaving open questions about computational efficiency and the burden that table-diverse acquisition places on human annotators.

Narration: The lasting message: active learning really can slash the expert-labeling cost of tabular language models, but only if diversity is handled with care. Cell-level acquisition with built-in batch diversity, like BADGE, reaches full-training performance using a fraction of the labels, while bluntly maximizing table diversity backfires. Balance diversity against uncertainty rather than maximize either alone. As the first work here, it flags two frontiers: acquisition compute cost, and annotator cognitive load.
