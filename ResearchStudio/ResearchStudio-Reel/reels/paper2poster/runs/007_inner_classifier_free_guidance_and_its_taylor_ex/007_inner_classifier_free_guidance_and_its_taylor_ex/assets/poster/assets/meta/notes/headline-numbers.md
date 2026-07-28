# Headline Numbers

Core claim: - Best balance: FID 15.28 / CLIP 26.11 at w = 2.0, v = 0.25, C = Call (vs CFG's 15.42 / 25.80). - Best FID from the middle-point sweep: 15.42 at m = 1.1.

Supporting detail: - On U-ViT, ICFG cuts FID from 34.23 → 24.69 at the 5k-step budget and reaches 7.92 vs CFG 8.10 at 80k steps. - Second-order ICFG adds only a few lines of code with no change to the training policy.

Narration: A few numbers to take away. The best fidelity-alignment balance on MS-COCO is an FID of fifteen point two eight and a CLIP score of twenty six point one one, beating classifier-free guidance on both. In the middle-point sweep, the best FID is fifteen point four two at m equal to one point one. On U-ViT, inner classifier-free guidance cuts FID substantially at low sampling budgets and edges out CFG at high budgets. And all of it comes from a few lines of code, with no change to training.
