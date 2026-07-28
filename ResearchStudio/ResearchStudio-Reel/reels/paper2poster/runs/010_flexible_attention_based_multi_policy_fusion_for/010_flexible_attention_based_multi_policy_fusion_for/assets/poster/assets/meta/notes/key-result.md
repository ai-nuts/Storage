# Key Result

Core claim: Given a sub-optimal knowledge set, KIAN is the only method that succeeds across all environments and shows the best sample efficiency, with its advantage growing as tasks become harder. It also transfers best in zero-shot simple-to-complex and complex-to-simple generalization.

Supporting detail: KIAN produces lower-variance results than the baselines (BC, RL, RL+BC, KoGuN, A2T) and remains stable in most environments; A2T barely succeeds in continuous control because it ignores entropy imbalance.

Narration: Across both benchmark suites, KIAN was the only method to succeed in every environment when starting from sub-optimal external knowledge, and its sample-efficiency advantage grew as tasks became more complex. In zero-shot generalization, where a policy trained on one task is tested on a different one, KIAN outperformed all baselines in most transfers and did so with noticeably smaller variance. On the hardest simple-to-complex grid task, KIAN reached a reward of about 0.93 while the strongest baseline stalled near 0.53. In continuous control, competing methods that ignore the exploration issue collapse, whereas KIAN keeps learning efficiently.
