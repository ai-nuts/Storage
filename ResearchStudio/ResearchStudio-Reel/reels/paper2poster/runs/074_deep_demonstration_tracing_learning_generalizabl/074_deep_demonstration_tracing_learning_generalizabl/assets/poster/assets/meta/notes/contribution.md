# Contribution

Core claim: The paper (1) advances the OSIL setting with a strong gap between demonstration collection and deployment, backed by a new demo-navigation benchmark; (2) proposes a demonstration transformer architecture that traces demonstrations; and (3) casts OSIL as context-based meta-RL, with a theoretical condition for imitating from one trajectory.

Supporting detail: It introduces Valet Parking Assist in Maze (VPAM) as a benchmark suite and shows DDT scales log-linearly with data and model size.

Narration: The paper makes three main contributions. First, it advances the one-shot imitation setting by deliberately introducing a large difference between when the demonstration is collected and when the policy is deployed, and it supports this with a new demonstration-navigation benchmark. Second, it proposes a demonstration transformer architecture that encourages the policy to trace the demonstration, following the three-stage identify, analyze, and trace process. Third, it addresses one-shot imitation as a context-based meta-reinforcement-learning problem, and it theoretically analyzes the conditions under which an imitator can succeed from just a single trajectory.
