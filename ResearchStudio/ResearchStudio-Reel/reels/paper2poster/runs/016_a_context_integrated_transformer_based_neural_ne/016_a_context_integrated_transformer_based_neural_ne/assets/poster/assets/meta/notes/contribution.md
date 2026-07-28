# Contribution

Core claim: The paper (1) formalizes contextual auction design as a learning problem with a sample-complexity generalization bound, and (2) proposes CITransNet, a context-integrated transformer that is permutation-equivariant over bids and contexts yet can represent asymmetric mechanisms whose parameter count is independent of auction scale.

Supporting detail: Because the parameter count does not depend on the number of bidders or items, CITransNet can be trained at one scale and evaluated at another, an ability the authors call out-of-setting generalization.

Narration: The paper makes two contributions. It extends the RegretNet framework to the contextual setting and proves a sample-complexity bound. And it introduces CITransNet, permutation-equivariant over bids and contexts, not restricted to symmetric auctions, with a parameter count independent of auction scale.
