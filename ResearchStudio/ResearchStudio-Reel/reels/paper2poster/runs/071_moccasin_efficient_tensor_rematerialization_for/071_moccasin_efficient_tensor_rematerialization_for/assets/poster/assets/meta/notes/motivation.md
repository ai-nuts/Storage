# Motivation

Core claim: Prior state-of-the-art (Checkmate) formulates rematerialization as a MILP with O(n²) Boolean variables, which does not scale to graphs with hundreds of nodes and thousands of edges.

Supporting detail: On-device training and tighter latency targets increase pressure on local memory, so a solver must handle large graphs within an acceptable compile time.

Narration: The leading prior method, Checkmate, casts rematerialization as a mixed-integer linear program. It is expressive, but its number of Boolean decision variables grows with the square of the number of nodes in the graph. That quadratic growth becomes a wall: for graphs with a few hundred nodes and a few thousand edges, Checkmate either times out or runs out of memory during the solve. Because the trend toward on-device training and stricter latency targets keeps enlarging these graphs, we need a formulation whose complexity grows much more slowly, so realistic graphs can be solved within an acceptable compile time.
