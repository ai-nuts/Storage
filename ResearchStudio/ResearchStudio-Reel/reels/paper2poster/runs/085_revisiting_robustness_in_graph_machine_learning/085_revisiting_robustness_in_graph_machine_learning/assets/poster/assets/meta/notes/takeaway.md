# Takeaway

Core claim: Much of what looks like graph neural network robustness is actually over-robustness, staying fixed after a node's semantics have already changed, and injecting the training graph's label structure via label propagation reduces it while helping accuracy and true robustness.

Supporting detail: With a semantics-aware notion of robustness, inductively classifying a newly added node has no robustness-accuracy tradeoff, reframing how graph adversarial robustness should be measured.

Narration: The one-line takeaway is that graph neural networks are not simply fragile, they are over-robust: a large part of their measured robustness is stubborn robustness that persists after the node's true meaning has already changed, which conventional evaluations wrongly credit as good behaviour. Bringing the training graph's label structure into inference through label propagation reduces this over-robustness while improving accuracy and real adversarial robustness. And with a semantics-aware definition, classifying a newly added node carries no robustness-accuracy tradeoff at all, changing how robustness in graph machine learning ought to be measured.
