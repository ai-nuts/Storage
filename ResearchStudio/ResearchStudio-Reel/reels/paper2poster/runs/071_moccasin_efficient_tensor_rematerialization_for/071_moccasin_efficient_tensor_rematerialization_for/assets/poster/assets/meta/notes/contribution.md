# Contribution

Core claim: Moccasin, a constraint programming formulation with only O(n) integer variables (versus Checkmate's O(n²) Boolean variables), that solves the rematerialization scheduling problem up to an order of magnitude faster on large graphs.

Supporting detail: A retention-interval representation of tensor lifetimes, memory and precedence constraints modeled with CP cumulative and reservoir constraints, and an optional topological-ordering restriction that further shrinks the search space.

Narration: The paper's main contribution is Moccasin, a constraint programming formulation of tensor rematerialization. Its central idea is to represent each node's decisions as a small number of retention intervals, defined by the start and end event of the tensor's lifetime, which reduces the count of discrete variables from quadratic to linear in the number of nodes. On top of this, the authors show how to encode the nonlinear memory and precedence constraints using standard CP building blocks, the cumulative and reservoir constraints, and they add an optional variant that enforces an input topological ordering to further reduce the search space. The payoff is up to an order-of-magnitude speedup over prior work on large graphs.
