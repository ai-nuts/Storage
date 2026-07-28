# Motivation

Core claim: A robot sharing the same path and space as pedestrians provokes interactive walking behaviors that only appear at close range, so training data must be collected from a moving robot inside real crowds, with fully synchronized multi-modal sensors.

Supporting detail: Prior robot-collected sets fall short: STCrowd used fixed-viewpoint sensors, and JRDB did not arrange data in trajectory form nor fully time-synchronize its sensors.

Narration: Studies of human-robot interaction show that a robot's motion changes how nearby people walk, and these effects are strongest when the robot and pedestrians share the same space at close distance. To study and model that, we need data collected while a robot actually moves through crowds, not from a camera bolted to a building. Earlier robot datasets came close but each had a gap: STCrowd kept its sensors at a fixed position, so scenes barely varied, and JRDB did not organize its data into trajectories and did not fully synchronize its multiple sensors in time, which limits sensor fusion. SiT is designed specifically to fill these gaps.
