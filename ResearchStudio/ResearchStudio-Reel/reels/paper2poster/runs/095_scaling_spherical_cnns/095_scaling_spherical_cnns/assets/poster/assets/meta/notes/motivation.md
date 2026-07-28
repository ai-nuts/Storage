# Motivation

Core claim: Molecular property prediction and weather forecasting are naturally spherical and rotation-related, so rotation-equivariant spherical CNNs should excel, but only if they can scale to datasets like QM9 (134K molecules) and high-resolution ERA5 weather grids.

Supporting detail: These fields were dominated by equivariant graph neural networks and transformers; prior spherical CNNs were limited to tiny benchmarks like QM7 (7,165 molecules).

Narration: Two scientific problems motivate this work: predicting molecular properties and forecasting the weather. Both are intrinsically spherical and tied to rotations. A molecule's properties don't change when you rotate it in space, and the Earth's atmosphere is naturally a signal on a sphere. Rotation-equivariant spherical CNNs should be a perfect match. But the standard benchmarks are large. QM9 has one hundred thirty four thousand molecules, over eighteen times bigger than the tiny QM7 set earlier spherical CNNs could handle, and weather grids demand high spatial resolution. To compete, these models had to scale.
