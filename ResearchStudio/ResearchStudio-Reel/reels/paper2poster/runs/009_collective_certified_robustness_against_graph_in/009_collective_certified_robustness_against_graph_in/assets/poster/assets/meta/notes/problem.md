# Problem

Core claim: Graph neural networks are vulnerable to graph injection attacks, where an adversary inserts malicious nodes. Existing certificates verify each node independently (sample-wise), yielding hopelessly pessimistic, near-zero certified performance.

Supporting detail: Sample-wise certification unrealistically assumes the attacker can craft a fresh perturbed graph per target node; real attackers produce one graph to disrupt all targets at once.

Narration: Graph neural networks are the workhorses of graph learning, but they can be broken by a graph injection attack that slips a handful of malicious nodes into the graph. To trust these models we want certified robustness, a mathematical guarantee that predictions stay stable under attack. The trouble is that every existing certificate for injection attacks works node by node, certifying each target in isolation. That sample-wise view is far too pessimistic, and in practice it certifies almost nothing once the attacker gets a modest budget.
