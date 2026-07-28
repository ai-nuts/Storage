# Contribution

Core claim: The first collective certified robustness scheme for GNNs against graph injection attacks. It formulates certification as a binary integer quadratic constrained linear program (BQCLP) and introduces a customized linearization that relaxes it to an efficiently solvable linear program.

Supporting detail: The scheme is almost model-agnostic, applying to any message-passing GNN, and delivers large certified-ratio gains with minimal computational overhead.

Narration: This paper delivers the first collective certified robustness scheme for graph neural networks against injection attacks. The authors cast certification as a worst-case optimization problem, a binary integer quadratic constrained linear program, and then introduce a customized linearization that relaxes this hard program into an ordinary linear program that can be solved efficiently. The result is almost model-agnostic: it works for any message-passing GNN, and it buys huge gains in certified performance at very little computational cost.
