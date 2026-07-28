# Headline Numbers

Core claim: - Integer/Boolean variables: O(n) for Moccasin vs O(n²) for Checkmate. - Up to 10× (an order of magnitude) faster solve time on large graphs. - Total duration increase consistently under 5% for the solutions Moccasin finds.

Supporting detail: - Scales to graphs with hundreds of nodes and thousands of edges (e.g. n = 1000, m = 5875) where Checkmate times out / runs out of memory. - Interval budget Cv = 2 used in all experiments.

Narration: A few numbers capture the impact. Moccasin needs only a linear number of integer variables in the graph size, compared to a quadratic number of Boolean variables for the prior state of the art. This translates into solve times up to an order of magnitude, roughly ten times, faster on large graphs. And the solutions it finds are high quality: the total duration increase from rematerialization stays consistently below five percent. Crucially, Moccasin scales to graphs with up to one thousand nodes and nearly six thousand edges, a regime where the competing method simply times out or runs out of memory.
