# Motivation

Core claim: Most prior geometric networks are designed heuristically with costly, specialized modules that either scale poorly or lack expressive power, so a general and flexible design principle is needed.

Supporting detail: Equivariant operations are often limited in number because of the equivariance constraint, leading to complex architectures that are hard to scale and reuse.

Narration: The trouble with existing geometric models is that they are largely built by hand. Designers craft specialized equivariant modules that are either expensive to scale or so constrained that they sacrifice expressive power, and the resulting architectures grow complex just to guarantee the physical constraints. More importantly, real applications increasingly demand a single model that performs both invariant and equivariant prediction with strong accuracy. There is a clear need for a general, flexible framework built on well-understood, standard components rather than one-off heuristic modules.
