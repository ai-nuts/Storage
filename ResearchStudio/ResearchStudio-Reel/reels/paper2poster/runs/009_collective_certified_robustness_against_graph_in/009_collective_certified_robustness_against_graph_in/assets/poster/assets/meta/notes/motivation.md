# Motivation

Core claim: A single perturbed graph must simultaneously fool an entire target set, so certifying nodes jointly should be far less conservative than certifying them one by one.

Supporting detail: The only prior collective scheme (Schuchardt et al., 2020) assumes a fixed receptive field and does not apply to GIA, which adds edges after injecting nodes and thereby expands the receptive field.

Narration: Here is the key insight. In the real world, an attacker cannot conjure a different graph for every node they want to fool. They inject one perturbed graph, and that single graph has to disrupt the entire set of target nodes at the same time. If we certify the whole target set jointly instead of one node at a time, the guarantee should be much stronger. Prior collective methods existed for edge-modification attacks, but they assume a fixed receptive field and simply do not carry over to injection attacks, which expand the receptive field by adding new edges.
