# Headline Numbers

Core claim: - Zero-shot generalization, Empty-Random-5x5 trained then tested at 16x16: KIAN 0.93 vs best baseline 0.53 (KoGuN). - Zero-shot Pick-and-Place, 10x goal range: KIAN 0.72 vs best baseline 0.30 (RL+BC). - Complex-to-simple transfer, DoorKey-8x8 to Reach: KIAN 1.00 vs 0.80 for RL/RL+BC. - Evaluated on 2 benchmark suites, 5 baselines, 10 random seeds with 95% confidence intervals.

Supporting detail: KIAN is the only method to succeed in all tested environments given a sub-optimal initial knowledge set.

Narration: A few numbers capture the gains. In zero-shot simple-to-complex transfer on the Empty-Random grid, KIAN scored about 0.93 at the sixteen-by-sixteen size while the best competing method reached only 0.53. On the Pick-and-Place task tested at a ten-times-larger goal range, KIAN reached 0.72 against 0.30 for the strongest baseline. In complex-to-simple transfer from DoorKey eight-by-eight to Reach, KIAN achieved a perfect 1.0 versus 0.80 for the reinforcement-learning baselines. All of this is measured across two benchmark suites, five baselines, and ten random seeds with ninety-five percent confidence intervals, and KIAN is the only method that succeeds everywhere.
