# Contribution

Core claim: They propose T-RevSNN, altering SNN forward propagation so only key spiking neurons carry temporal information via multi-level temporal-reversible connections, giving O(L) training memory; combined with once-only input encoding and a grouped sub-network organization, inference becomes O(1).

Supporting detail: They redesign the basic SNN block (ConvNeXt-style, BN-free, depth-wise/point-wise convolutions) and add a scaled residual connection to make sparse temporal information interaction effective.

Narration: Their answer is T-RevSNN, a Temporal Reversible architecture for spiking networks. The core idea is to turn off the temporal dynamics of most spiking neurons and keep them on only at a few key positions, where the temporal connections are made reversible. Reversibility means the network can recompute activations during the backward pass instead of storing them, which brings training memory down to order L. On top of that, they encode the input image only once and split both the features and the network into independent sub-networks, so inference cost becomes constant, order one. To make this sparse temporal design actually train well, they also redesign the basic SNN block in a ConvNeXt style and add a scaled residual connection.
