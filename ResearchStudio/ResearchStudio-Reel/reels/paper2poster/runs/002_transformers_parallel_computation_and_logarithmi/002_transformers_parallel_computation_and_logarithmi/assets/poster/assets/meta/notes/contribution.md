# Contribution

Core claim: (1) A two-way simulation showing logarithmic-depth transformers and constant-round MPC protocols capture exactly the same algorithmic capabilities. (2) The k-hop induction heads task, on which log-depth transformers succeed but recurrent, state-space, and sub-quadratic-attention models provably fail, confirmed empirically.

Supporting detail: The MPC connection immediately yields log-depth transformers for graph problems such as connectivity, plus conditional near-optimality via a well-known MPC lower-bound conjecture.

Narration: The paper makes two main contributions. First, it establishes a tight correspondence: any R-round MPC protocol can be run by a transformer of depth about R, and conversely any depth-L transformer can be simulated by an O(L)-round MPC protocol. So the algorithmic power of logarithmic-depth transformers is captured, up to constants, by the MPC model. That instantly gives log-depth transformers for classic parallel problems like graph connectivity, and, under a standard conjecture about MPC's limits, shows those constructions are near-optimal. Second, the authors introduce a concrete synthetic task, k-hop induction heads, and prove that transformers solve it with logarithmic depth while several competing architectures cannot do so efficiently. They then train real transformers and watch them obey the very same threshold.
