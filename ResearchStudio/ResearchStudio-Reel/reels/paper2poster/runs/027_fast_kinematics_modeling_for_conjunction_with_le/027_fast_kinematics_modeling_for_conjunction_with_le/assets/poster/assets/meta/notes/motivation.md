# Motivation

Core claim: Spatially resolved kinematics from telescopes like JWST are now available, but the axisymmetric physics code (JAM) needed to model them self-consistently with elliptical lens mass models is far too slow for joint likelihood sampling.

Supporting detail: Prior joint-modeling frameworks either fit lens and kinematics separately, were built for galaxy-structure research rather than H0, or expanded JAM but remained computationally expensive.

Narration: Recently, spatially resolved kinematics of lensing galaxies became available through instruments like the James Webb Space Telescope. Traditional spherical Jeans models are too simplistic for this richer data, and they lack self-consistency with the elliptical mass models used in lensing. The natural next step is axisymmetric modeling with software such as JAM, but JAM is expensive. Existing frameworks that combine it with lens modeling either fit the two separately or remain far too slow for full joint parameter exploration. The key insight of this work is that JAM's slow physics can be emulated by a neural network, keeping the physics of the overall model while removing the computational bottleneck.
