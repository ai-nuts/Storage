# Problem

Core claim: Galaxy kinematics modeling is the computational bottleneck in joint gravitational lensing + kinematics modeling, because the physics code (JAM) must be recalled for every likelihood evaluation inside an MCMC.

Supporting detail: Kinematic constraints are required to break lensing mass-sheet degeneracies and recover a precise Hubble constant, but existing joint frameworks remain too expensive to explore both parameter spaces simultaneously.

Narration: Gravitational lensing measures the Hubble constant by comparing time delays between multiple images of a distant source to a model of the lens galaxy's mass. But lensing degeneracies allow many different mass distributions to reproduce the same image, so independent kinematic constraints are needed to break them. The trouble is speed. Modeling galaxy kinematics with a physics code like JAM is slow, and it must be recomputed for every single likelihood evaluation inside a Markov Chain Monte Carlo sampling. This makes jointly exploring the full lensing and kinematics parameter space computationally prohibitive, forcing modelers to cut corners by fitting the two components separately.
