# Contribution

Core claim: The paper proposes Knowledge-Grounded RL (KGRL), a paradigm for fusing multiple knowledge policies, and KIAN, an actor architecture that enables free knowledge rearrangement via embedding-based attentive action prediction. It also identifies and resolves entropy imbalance in maximum-entropy KGRL.

Supporting detail: It formalizes knowledge-acquirable, generalizable, compositional, and incremental agents, and shows KIAN's key-based design decouples each policy from the rest so the knowledge set can be updated without relearning KIAN.

Narration: The paper makes three main contributions. First, it defines Knowledge-Grounded Reinforcement Learning, a paradigm that fuses an inner, self-learned policy with multiple external knowledge policies. Second, it introduces the Knowledge-Inclusive Attention Network, KIAN, whose embedding-based attention lets knowledge policies be freely rearranged, added, or replaced without touching the rest of the network. Third, it uncovers a problem called entropy imbalance that arises when maximizing entropy for exploration, proves when it happens, and proposes modified policy distributions that fix it. Together these give an agent that is efficient, generalizable, and truly modular in its use of knowledge.
