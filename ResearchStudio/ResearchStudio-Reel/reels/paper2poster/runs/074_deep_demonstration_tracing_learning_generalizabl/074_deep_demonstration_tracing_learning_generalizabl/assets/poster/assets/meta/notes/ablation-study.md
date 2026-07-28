# Ablation Study

Core claim: Replacing the demonstration transformer with a standard transformer (DDT using transformer) significantly lowers asymptotic performance, and removing the OSIL reward (DDT w/o OSIL reward, learning only from the ending reward) sharply reduces learning efficiency — showing both components are essential.

Supporting detail: Both ablations are run on multi-map imitation without obstacles and tested on unseen maps (Fig. 8a).

Narration: To confirm each component matters, the authors ablate two pieces. First, they swap the demonstration transformer for a standard transformer; this significantly reduces the final asymptotic performance, underscoring that the tailored architecture, not just attention in general, is what drives DDT's imitation ability. Second, they remove the OSIL reward and train with only the sparse ending reward; this sharply slows learning, because the OSIL reward supplies a dense, informative signal that lets the agent closely follow the demonstration early in training. Together the ablations show the demonstration transformer and the OSIL reward each play a distinct and necessary role.
