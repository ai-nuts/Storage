# Problem

Core claim: Graph neural networks have inherently limited expressive power, and the Weisfeiler-Lehman (WL) hierarchy used to measure it has a complex, hard-to-act-on definition and is too coarse to separate current GNNs.

Supporting detail: WL gives no direct guidance for improving a model, so practitioners lack a constructive target for building more powerful architectures.

Narration: Graph networks have bounded expressive power: only some functions of a graph can be represented. The field measures this with the Weisfeiler-Lehman hierarchy of isomorphism tests. But WL is combinatorial, giving no recipe to make a network stronger, and its rungs are so far apart that very different GNNs collapse to the same level. We need a finer, more actionable ruler.
