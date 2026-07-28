# Takeaway

Core claim: A cheap DARTS-like search with a masked-validation-drop metric reliably finds the single best attention for a task, but combining multiple attention types yields Transformers that beat the average homogeneous model yet never the best one.

Supporting detail: The finding challenges the assumption that diverse attention biases compound; for these long-range NLP tasks, picking one well-suited attention beats mixing many.

Narration: For a given task it is often unclear which attention will do best, and DARTFormer offers a cheap, reliable recipe: train a single-layer mixed-attention Transformer and use masked validation accuracy drop to pick the winner, keeping in mind that very low drop scores are a warning that the choice may be unreliable. The deeper lesson is a cautionary one for the field. Combining diverse attention mechanisms does beat the average single choice, but it never beats the best single choice, which suggests the different attentions do not simply add complementary biases the way common intuition assumes.
