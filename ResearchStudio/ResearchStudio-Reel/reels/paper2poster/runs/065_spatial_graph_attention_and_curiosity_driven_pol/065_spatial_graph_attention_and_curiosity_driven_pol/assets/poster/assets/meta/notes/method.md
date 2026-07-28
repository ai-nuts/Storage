# Method

Core claim: Molecule generation is a Markov decision process: at each step the CReM chemical library proposes valid fragment-swap candidates, and an attentional policy selects the next molecule. States are embedded by sGAT, which attends over node/edge attributes and adds a spatial convolution on a sparsified inverse distance matrix. The policy is trained with PPO/A2C, and a random network distillation module supplies innovation rewards for exploration.

Supporting detail: Transition dynamics are deterministic (action equals selecting the next state), the trajectory length is fixed to keep episodes short and enable parallel docking, and early sGAT layers can be pre-trained via supervised learning and frozen during RL.

Narration: DGAPN casts molecule generation as a Markov decision process. At each step, the CReM library proposes valid molecules reachable by swapping one fragment, guaranteeing synthesizable candidates. Spatial Graph Attention embeds each candidate, combining attention over atom and bond attributes with a spatial convolution from a sparsified inverse distance matrix, so chemistry and geometry both inform the representation. An attentional policy scores candidates and samples the next molecule, trained with PPO. Finally, random network distillation supplies an innovation reward whose error rewards exploring novel states.
