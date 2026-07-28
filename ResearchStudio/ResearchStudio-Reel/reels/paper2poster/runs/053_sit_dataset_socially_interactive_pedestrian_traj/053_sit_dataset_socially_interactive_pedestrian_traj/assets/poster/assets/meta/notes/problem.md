# Problem

Core claim: Social navigation robots must perceive and predict nearby pedestrian trajectories to move safely in shared spaces, but existing trajectory datasets do not capture the close, dynamic human-robot interaction a navigating robot actually experiences.

Supporting detail: Prior datasets are either static top-view camera recordings (ETH, UCY, SDD) or autonomous-driving data (nuScenes, Waymo, Argoverse) where vehicles and pedestrians occupy separate roads.

Narration: For a robot to navigate safely among people, it needs to perceive nearby pedestrians as individual entities in three-dimensional space and predict where they will move next. The problem is that the datasets used to train these models don't reflect the robot's real situation. Popular pedestrian datasets like ETH, UCY, and SDD were captured by fixed cameras mounted high on rooftops or drones, so they never see human-robot interaction. Large autonomous-driving datasets do provide rich sensor data, but there the vehicle and the pedestrians usually travel on separate roads and rarely come into close contact. Neither setting matches a robot weaving through a crowded hallway or crosswalk.
