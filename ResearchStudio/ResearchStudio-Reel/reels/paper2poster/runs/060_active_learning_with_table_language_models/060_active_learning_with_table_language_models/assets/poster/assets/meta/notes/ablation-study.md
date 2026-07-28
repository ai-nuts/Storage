# Ablation Study

Core claim: Comparing MNLP, MNLP+, BADGE, and Rand isolates the effect of diversity: built-in batch diversity (BADGE) helps, while forced maximum table diversity (MNLP+) is detrimental, dropping well below the random baseline.

Supporting detail: A table-diversity metric (number of distinct tables sampled per iteration) shows MNLP fixates on few tables, MNLP+ spreads across as many tables as the budget allows, and BADGE sits in between, balancing table diversity against cell uncertainty.

Narration: The four acquisition functions effectively ablate diversity, and the lesson is that the right amount matters enormously. BADGE's built-in batch diversity helps, but MNLP-plus's forced maximum diversity hurts, falling below even random. Tracking how many distinct tables each method draws from explains why: MNLP fixates on a few tables, MNLP-plus spreads across as many as possible, and BADGE lands in between. The goal isn't maximum diversity but a careful trade-off with per-cell uncertainty.
