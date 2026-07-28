# Ablation Study

Core claim: The grammar-reduction study (Q1) shows G(L3), the intermediate grammar, and the reduced r-G(L3) reach comparable MAE on QM9 R², confirming reduction preserves expressiveness, while over-reducing (removing rules) degrades MAE — validating each rule's contribution.

Supporting detail: Removing rules also reveals each operation's weight in the model, guiding principled pruning when full 3-WL expressiveness is not required for a task.

Narration: The most instructive experiment is the grammar-reduction ablation. The authors compare the full grammar, an intermediate one, and the reduced grammar r-G-of-L-three on the QM9 R-squared target. Their errors are essentially the same, which confirms that reduction throws away redundancy without touching expressive power. But when you push past the reduced grammar and start deleting essential rules, performance degrades in a measurable way. That degradation is actually useful information: it tells you how much each operation contributes, so you can prune the model deliberately when a task does not demand the full 3-W-L strength.
