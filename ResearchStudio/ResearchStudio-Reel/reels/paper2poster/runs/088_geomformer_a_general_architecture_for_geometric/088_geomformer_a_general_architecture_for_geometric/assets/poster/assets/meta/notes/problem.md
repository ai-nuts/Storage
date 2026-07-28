# Problem

Core claim: Molecular modeling requires networks that respect physical laws, invariance and equivariance to coordinate rotation and translation, yet no general framework learns both invariant and equivariant features well at once.

Supporting detail: Many applications need strong invariant prediction (e.g. energy) and equivariant prediction (e.g. atomic positions/forces) from the same model simultaneously.

Narration: Deep learning has become a powerful tool for molecular science, predicting properties of molecules from their three-dimensional coordinates and simulating how atoms move. But these tasks impose strict physical constraints. A model's prediction must transform correctly when the input coordinate system is rotated or translated, a requirement known as invariance for scalar quantities and equivariance for vector quantities. Existing methods handle these constraints, but most are built on heuristic and costly modules, and few offer a single general framework that learns both invariant and equivariant representations effectively at the same time.
