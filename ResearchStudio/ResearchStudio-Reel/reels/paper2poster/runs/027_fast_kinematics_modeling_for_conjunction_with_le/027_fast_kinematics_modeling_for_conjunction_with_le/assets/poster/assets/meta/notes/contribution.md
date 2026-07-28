# Contribution

Core claim: The paper introduces SKiNN (Stellar Kinematics Neural Network), the first application of neural-network emulation to the kinematic-modeling piece of a gravitational lens modeling framework, delivering roughly 300× speedup with sub-percent accuracy.

Supporting detail: By confining the machine-learning component to emulating JAM only, the approach exploits the speed of neural networks while retaining the physical fidelity of the full model, and demonstrates a strategy generalizable to other fields.

Narration: The core contribution is SKiNN, the Stellar Kinematics Neural Network. It is the first time the strategy of replacing an expensive model component with a neural network has been applied to the kinematic-modeling aspect of gravitational lens modeling. Crucially, SKiNN emulates only the JAM physics calculation rather than being applied directly to observations. This design choice keeps the physics of the overall model intact while exploiting the speed and versatility of neural networks. The result is a roughly 300-fold speedup at sub-percent accuracy, which finally makes joint lensing plus kinematics modeling computationally feasible.
