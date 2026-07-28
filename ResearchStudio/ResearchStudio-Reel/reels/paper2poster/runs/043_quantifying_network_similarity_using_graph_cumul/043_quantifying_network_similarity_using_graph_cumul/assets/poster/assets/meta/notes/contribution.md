# Contribution

Core claim: The paper introduces a simple two-sample test for networks built on graph cumulants and shows, via theory, simulation, and real data, that it has substantially greater statistical power than the analogous graph-moment test at identical computational complexity.

Supporting detail: It demonstrates that the cumulant test statistic closely follows a known chi-squared null distribution even for very few graphs per sample, enabling analytic control of false-positive rates, and that it remains applicable even when only a single graph is observed per sample.

Narration: The paper's central contribution is a simple, drop-in two-sample test for networks that swaps graph moments for graph cumulants. Using theory, controlled simulation, and real biological networks, the authors show this swap consistently increases statistical power without changing the computational cost. They further show that the cumulant test statistic tracks a known chi-squared distribution remarkably well, even with only a handful of graphs, so false-positive rates can be controlled analytically. Strikingly, the cumulant test even works when just one graph is observed per sample, a regime where the moment test is undefined.
