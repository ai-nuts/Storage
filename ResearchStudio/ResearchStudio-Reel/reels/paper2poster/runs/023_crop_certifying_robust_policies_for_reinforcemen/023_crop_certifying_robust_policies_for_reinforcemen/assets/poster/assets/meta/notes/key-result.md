# Key Result

Core claim: CROP certifies and ranks the nine methods: RadialRL is consistently the most certifiably robust on Freeway, while SA-MDP (CVX) is most robust on Pong, and the certified rankings largely match empirical robustness observations.

Supporting detail: All methods exhibit periodic patterns in the per-state certified radius on Pong, tied to "confident states" such as when the ball approaches the paddle.

Narration: The certifications reveal clear and consistent winners. On Freeway, RadialRL achieves the highest certified radius across every smoothing level, because it explicitly optimizes against worst-case perturbations. On Pong, SA-MDP with the convex relaxation is the most certifiably robust. Encouragingly, these certified rankings largely agree with what people had observed empirically, which builds confidence in the certificates. The analysis also surfaces new structure: on Pong every method shows a periodic pattern in its certified radius over time, with robustness peaking at confident states such as when the ball flies toward the paddle, an insight that could guide future robust training.
