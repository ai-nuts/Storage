# Dataset / Benchmark

Core claim: Synthetic experiments use pairs of two-community Stochastic Block Models, one heterogeneous (parameter ε_h) and one assortative (parameter ε_a), matched in edge density, with n = 128 and n = 256 nodes. Real experiments use genetic-interaction networks from the FunCoup repository (Persson et al., 2021).

Supporting detail: Real networks compared include Arabidopsis (~1.3×10⁴ nodes, 7.9×10⁵ edges) versus Mouse (~1.4×10⁴ nodes, 9.2×10⁵ edges), and Human (~1.6×10⁴ nodes, 13.9×10⁵ edges) versus Rat (~1.1×10⁴ nodes, 9.0×10⁵ edges), each adjusted to equal edge density so that low-order tests cannot trivially separate them.

Narration: To compare the tests fairly, the authors first run a controlled competition on synthetic data. They pit a heterogeneous stochastic block model, which has an uneven degree distribution but no communities, against an assortative one, which has communities but even degrees, holding edge density fixed so the two are genuinely hard to tell apart. They vary graph size from one hundred twenty-eight to two hundred fifty-six nodes and the number of graphs per sample. They then move to real data: genetic-interaction networks of Arabidopsis, mouse, human, and rat from the FunCoup repository, again matched in edge density so that separating them demands higher-order structure.
