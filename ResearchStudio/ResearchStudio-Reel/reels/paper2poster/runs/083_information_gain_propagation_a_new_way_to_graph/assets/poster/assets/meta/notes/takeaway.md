# Takeaway

Core claim: Ask a cheaper yes/no question and pick nodes whose information gain propagates farthest, and graph active learning gets both more accurate and much cheaper to label.

Supporting detail: Relaxed queries plus propagation-aware selection is a general recipe that plugs into any GNN.

Narration: The takeaway is simple. Ask a cheap binary yes-or-no question, and select nodes whose information gain propagates farthest across the graph. IGP makes graph active learning both more accurate and far cheaper to label, and works with any graph neural network.
