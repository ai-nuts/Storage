# Contribution

Core claim: GeoMFormer, a Transformer-based architecture with two streams (invariant and equivariant) bridged by cross-attention, that learns both representation types; the paper shows many prior architectures are special instances of it.

Supporting detail: Built entirely from standard Transformer modules, and validated with new state-of-the-art results across invariant and equivariant molecular benchmarks plus comprehensive ablations.

Narration: The paper makes three main contributions. First, it introduces GeoMFormer, a novel Transformer-based molecular model that maintains two separate streams, one for invariant and one for equivariant representations, using only standard Transformer building blocks. Second, it designs cross-attention modules that bridge these two streams, letting each draw on contextual information from the other to enhance geometric modeling. Third, it shows that this framework is general enough that many previously proposed architectures can be viewed as special instantiations of GeoMFormer, and it backs the design with strong empirical results across a diverse set of molecular tasks.
