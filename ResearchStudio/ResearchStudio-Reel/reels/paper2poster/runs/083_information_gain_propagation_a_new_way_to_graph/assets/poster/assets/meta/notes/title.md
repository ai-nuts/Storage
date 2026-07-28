# Title

Graph neural networks need many labeled nodes, and labeling is expensive. This ICLR 2022 paper, Information Gain Propagation, rethinks graph active learning. Instead of asking an oracle for a node's exact class, it asks a cheaper binary question: does this node belong to a given class? That soft label, plus a criterion picking nodes whose information gain propagates farthest, gives higher accuracy at lower cost.
