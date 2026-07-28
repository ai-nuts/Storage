# Method

Core claim: CITransNet embeds bidder-contexts and item-contexts, assembles them with the bidding profile into a per-bidder-item representation, and passes it through one or more transformer-based interaction layers that model mutual influence across bidders and items, then an output layer emits the allocation and payment.

Supporting detail: Each interaction layer combines a global average, a transformer applied along each column, and a transformer applied along each row, keeping the mechanism permutation-equivariant; IR is guaranteed by architecture and DSIC is enforced as a regret constraint trained via the augmented-Lagrangian method of RegretNet.

Narration: CITransNet takes three inputs: the bidding profile, bidder-contexts, and item-contexts. It embeds contexts with bids into a representation per bidder-item pair, then passes it through transformer interaction layers that mix a global average with row and column transformers, staying permutation-equivariant. A final layer outputs allocations and payments, with zero-regret enforced during training.
