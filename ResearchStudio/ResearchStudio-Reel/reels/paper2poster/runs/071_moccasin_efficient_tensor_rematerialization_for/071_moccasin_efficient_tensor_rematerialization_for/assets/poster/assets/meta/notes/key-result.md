# Key Result

Core claim: Moccasin is up to an order of magnitude faster than Checkmate, especially on large graphs. On graphs G3 (n = 500) and G4 (n = 1000) Checkmate times out with no solution even at a 3-hour limit and exits with out-of-memory, while Moccasin converges to a low-duration-increase solution in under an hour.

Supporting detail: On G2 (n = 250) with a tight budget Checkmate finds no feasible solution within 30 minutes and takes 10 minutes at the loosest budget, whereas Moccasin finishes in a few seconds.

Narration: Across the board, Moccasin solves the rematerialization problem substantially faster than Checkmate, up to an order of magnitude on the larger graphs. On the smallest graph the two are comparable, but the gap widens quickly. For the graph with two hundred fifty nodes and a tight memory budget, Checkmate fails to find any feasible solution within thirty minutes, and at the loosest budget it takes ten minutes, while Moccasin finishes in seconds. For the five hundred and one thousand node graphs, Checkmate times out entirely, finding no solution even given three hours, and it exits with an out-of-memory error, whereas Moccasin converges to a good, low-duration-increase solution in under an hour.
