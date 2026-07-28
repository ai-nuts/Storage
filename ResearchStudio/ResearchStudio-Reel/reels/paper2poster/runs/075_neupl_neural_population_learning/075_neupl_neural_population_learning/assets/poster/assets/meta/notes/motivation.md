# Motivation

Core claim: Population size and per-iteration training budget are handcrafted knobs in prior work; NeuPL instead lets the meta-game solver decide the effective population size while sharing skills across policies.

Supporting detail: Empirical successes like StarCraft leagues used close to a thousand agents at enormous cost, motivating a far more sample- and skill-efficient alternative.

Narration: "The need for a population of strategies is rooted in game theory: in a purely cyclic game like rock-paper-scissors a single strategy is meaningless, since improving against one opponent means losing to another. Prior frameworks handle this by training policies one at a time and discarding the shared knowledge between them. NeuPL's insight is that these policies overlap enormously — they share perception, memory, and motor skills — so training them independently is wasteful. If a single model could hold the whole population and condition its behaviour on which opponents it faces, early skills learned against weak opponents would directly bootstrap the discovery of exploiters to much stronger ones."
