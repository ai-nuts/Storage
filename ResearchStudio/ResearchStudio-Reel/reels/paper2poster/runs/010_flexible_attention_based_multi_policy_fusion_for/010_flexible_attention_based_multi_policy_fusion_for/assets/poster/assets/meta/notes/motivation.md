# Motivation

Core claim: To approach human-like efficiency, an agent must treat external policies as a modular, reorderable set, so knowledge can be transferred to new tasks and expanded without relearning the whole model.

Supporting detail: Prior approaches such as KoGuN and A2T tie policy fusion to fixed input orderings or per-policy parameters, so adding or removing a policy forces architectural changes or retraining.

Narration: The authors summarize five properties of efficient, flexible human learning: being knowledge-acquirable, sample-efficient, generalizable, compositional, and incremental. Existing knowledge-guided reinforcement learning methods satisfy some of these but stumble on flexibility. When their fusion mechanism depends on the number or ordering of external policies, rearranging the knowledge set or swapping one policy for another means rebuilding or retraining large parts of the model. The motivation here is to design an actor whose structure lets knowledge policies be freely rearranged, added, or replaced, so a single trained agent can carry its skills into new tasks.
