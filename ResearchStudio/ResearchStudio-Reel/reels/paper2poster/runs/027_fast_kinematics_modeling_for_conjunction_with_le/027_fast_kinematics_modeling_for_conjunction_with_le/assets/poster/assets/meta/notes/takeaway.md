# Takeaway

Core claim: A neural network can emulate slow physics-based galaxy kinematics (JAM) at ~300× speed and sub-percent accuracy, making joint lensing + spatially-resolved-kinematics modeling feasible for precise Hubble-constant measurements.

Supporting detail: The strategy of replacing an expensive-but-calculable model component with a trained neural network while keeping the rest of the physics is broadly transferable to other modeling domains.

Narration: The takeaway is simple. By training a neural network to emulate the slow kinematics physics of JAM, SKiNN achieves roughly a three-hundred-fold speedup at sub-percent accuracy in the region that matters. This removes the main computational bottleneck and makes it feasible to jointly model gravitational lensing together with spatially resolved kinematics, which corrects for the largest source of uncertainty in measuring the Hubble constant. More broadly, the strategy of swapping an expensive but calculable model piece for a trained neural network, while keeping the surrounding physics intact, likely transfers to many other scientific modeling problems.
