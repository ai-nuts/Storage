# Dataset / Benchmark

Core claim: Evaluated on three domains of increasing complexity: the normal-form game rock-paper-scissors, the spatiotemporal partially-observed game running-with-scissors, and the large-scale 2-vs-2 MuJoCo Football Game-of-Skills.

Supporting detail: Running-with-scissors gives each player only a 4×4 first-person grid view and requires inferring the opponent's hidden inventory; MuJoCo Football couples continuous motor control with team coordination and latent strategic cycles.

Narration: "NeuPL is validated across three domains chosen to span the difficulty spectrum. Rock-paper-scissors is the classic purely cyclic normal-form game, where the learned population can be visualized directly on the strategy simplex. Running-with-scissors lifts this into a spatiotemporal, partially observed setting: players move on a grid, collect rock, paper, and scissors resources, and must infer a hidden opponent inventory from a narrow first-person view. Finally, MuJoCo Football is a large-scale Game-of-Skills where two-versus-two teams must simultaneously master continuous motor control and coordinated team play, a regime where handcrafted PSRO truncation is especially fragile."
