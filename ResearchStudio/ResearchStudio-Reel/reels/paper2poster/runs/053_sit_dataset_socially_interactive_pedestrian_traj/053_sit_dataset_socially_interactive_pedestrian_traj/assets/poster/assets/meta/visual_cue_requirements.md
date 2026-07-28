# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_social_navigation_robots_move_safely`

- Preferred role: `content`
- Cue keywords: `social, navigation, robots, move, safely, through, crowds, means, perceiving, predicting`
- Narration: Social navigation robots have to move safely through crowds, and that means perceiving and predicting the paths of the people around them.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c1_social_navigation_robots_move_safely" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords social, navigation, robots, move, safely, through in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_introduces_sit_dataset_short_sociall`

- Preferred role: `method`
- Cue keywords: `introduces, sit, dataset, short, socially, interactive, pedestrian, trajectory`
- Narration: This paper introduces the SiT dataset, short for Socially Interactive Pedestrian Trajectory.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c2_introduces_sit_dataset_short_sociall" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords introduces, sit, dataset, short, socially, interactive in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_unlike_earlier_trajectory_datasets_c`

- Preferred role: `figure`
- Cue keywords: `unlike, earlier, trajectory, datasets, captured, fixed, rooftop, cameras, cars, driving`
- Narration: Unlike earlier trajectory datasets captured from fixed rooftop cameras or from cars driving on separate roads, SiT was recorded by a mobile robot navigating densely populated indoor and outdoor spaces in downtown Seoul, capturing genuine human-robot interaction up close.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s01_c3_unlike_earlier_trajectory_datasets_c" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords unlike, earlier, trajectory, datasets, captured, fixed in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_ships_synchronized_lidar_camera_imu`

- Preferred role: `result`
- Cue keywords: `ships, synchronized, lidar, camera, imu, rtk, 2, 3, annotations, semantic`
- Narration: It ships synchronized LiDAR, camera, IMU, and RTK data with 2D and 3D annotations, semantic maps, and a full benchmark spanning 3D detection, tracking, trajectory prediction, and end-to-end motion forecasting.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s01_c4_ships_synchronized_lidar_camera_imu" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ships, synchronized, lidar, camera, imu, rtk in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_robot_navigate_safely_among_people`

- Preferred role: `method`
- Cue keywords: `robot, navigate, safely, among, people, needs, perceive, nearby, pedestrians, individual`
- Narration: For a robot to navigate safely among people, it needs to perceive nearby pedestrians as individual entities in three-dimensional space and predict where they will move next.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c1_robot_navigate_safely_among_people" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords robot, navigate, safely, among, people, needs in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_problem_datasets_used_train_these`

- Preferred role: `content`
- Cue keywords: `problem, datasets, used, train, these, models, don, reflect, robot, real`
- Narration: The problem is that the datasets used to train these models don't reflect the robot's real situation.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c2_problem_datasets_used_train_these" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords problem, datasets, used, train, these, models in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_popular_pedestrian_datasets_like_eth`

- Preferred role: `method`
- Cue keywords: `popular, pedestrian, datasets, like, eth, ucy, sdd, captured, fixed, cameras`
- Narration: Popular pedestrian datasets like ETH, UCY, and SDD were captured by fixed cameras mounted high on rooftops or drones, so they never see human-robot interaction.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c3_popular_pedestrian_datasets_like_eth" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords popular, pedestrian, datasets, like, eth, ucy in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_large_autonomous_driving_datasets_pr`

- Preferred role: `method`
- Cue keywords: `large, autonomous-driving, datasets, provide, rich, sensor, but, vehicle, pedestrians, usually`
- Narration: Large autonomous-driving datasets do provide rich sensor data, but there the vehicle and the pedestrians usually travel on separate roads and rarely come into close contact. Neither setting matches a robot weaving through a crowded hallway or crosswalk.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c4_large_autonomous_driving_datasets_pr" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords large, autonomous-driving, datasets, provide, rich, sensor in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_studies_human_robot_interaction_show`

- Preferred role: `method`
- Cue keywords: `studies, human-robot, interaction, show, robot, motion, changes, how, nearby, people`
- Narration: Studies of human-robot interaction show that a robot's motion changes how nearby people walk, and these effects are strongest when the robot and pedestrians share the same space at close distance.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c1_studies_human_robot_interaction_show" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords studies, human-robot, interaction, show, robot, motion in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_study_need_collected_while_robot`

- Preferred role: `content`
- Cue keywords: `study, need, collected, while, robot, actually, moves, through, crowds, not`
- Narration: To study and model that, we need data collected while a robot actually moves through crowds, not from a camera bolted to a building.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_study_need_collected_while_robot" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords study, need, collected, while, robot, actually in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_earlier_robot_datasets_came_close`

- Preferred role: `method`
- Cue keywords: `earlier, robot, datasets, came, close, but, had, gap, stcrowd, kept`
- Narration: Earlier robot datasets came close but each had a gap: STCrowd kept its sensors at a fixed position, so scenes barely varied, and JRDB did not organize its data into trajectories and did not fully synchronize its multiple sensors in time, which limits sensor fusion.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c3_earlier_robot_datasets_came_close" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords earlier, robot, datasets, came, close, but in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_sit_designed_specifically_fill_these`

- Preferred role: `content`
- Cue keywords: `sit, designed, specifically, fill, these, gaps`
- Narration: SiT is designed specifically to fill these gaps.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c4_sit_designed_specifically_fill_these" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords sit, designed, specifically, fill, these, gaps in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_sit_dataset_makes_several_contributi`

- Preferred role: `method`
- Cue keywords: `sit, dataset, makes, several, contributions, provides, large-scale, real-world, pedestrian, trajectories`
- Narration: The SiT dataset makes several contributions. It provides large-scale real-world pedestrian trajectories gathered as a robot navigated densely populated indoor and outdoor environments, from building interiors and campuses to crosswalks and public walkways.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c1_sit_dataset_makes_several_contributi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords sit, dataset, makes, several, contributions, provides in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_lets_researchers_build_prediction_mo`

- Preferred role: `content`
- Cue keywords: `lets, researchers, build, prediction, models, rich, context, including, appearance, features`
- Narration: It lets researchers build prediction models using rich context, including appearance features, the robot's ego-motion, and semantic map data.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c2_lets_researchers_build_prediction_mo" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords lets, researchers, build, prediction, models, rich in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_achieves_precise_time_synchronizatio`

- Preferred role: `method`
- Cue keywords: `achieves, precise, time, synchronization, between, all, sensor, modalities, centralized, triggering`
- Narration: It achieves precise time synchronization between all sensor modalities using a centralized triggering method, which makes sensor fusion practical. It supplies multi-layered semantic maps for both indoor and outdoor scenes.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c3_achieves_precise_time_synchronizatio" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords achieves, precise, time, synchronization, between, all in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_offers_curated_benchmark_covering_3`

- Preferred role: `result`
- Cue keywords: `offers, curated, benchmark, covering, 3, detection, 3, multi-object, tracking, trajectory`
- Narration: And it offers a curated benchmark covering 3D detection, 3D multi-object tracking, trajectory prediction, and an end-to-end task from perception to motion forecasting, with everything released publicly.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s04_c4_offers_curated_benchmark_covering_3" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords offers, curated, benchmark, covering, 3, detection in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_captured_clearpath_husky_unmanned_gr`

- Preferred role: `content`
- Cue keywords: `captured, clearpath, husky, unmanned, ground, vehicle, remotely, operated, through, downtown`
- Narration: The data was captured with a Clearpath Husky unmanned ground vehicle, remotely operated through downtown Seoul. The robot carried two sixteen-channel Velodyne LiDARs, five Basler cameras arranged to cover a full 360 degrees, two inertial measurement units, and real-time kinematic positioning.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c1_captured_clearpath_husky_unmanned_gr" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords captured, clearpath, husky, unmanned, ground, vehicle in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_fuse_camera_lidar_reliably_pulse_per`

- Preferred role: `content`
- Cue keywords: `fuse, camera, lidar, reliably, pulse-per-second, signal, generator, triggers, all, sensors`
- Narration: To fuse camera and LiDAR reliably, a pulse-per-second signal generator triggers all the sensors so their data is accurately aligned in time.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c2_fuse_camera_lidar_reliably_pulse_per" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords fuse, camera, lidar, reliably, pulse-per-second, signal in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_robot_own_pose_recovered_rtk`

- Preferred role: `method`
- Cue keywords: `robot, own, pose, recovered, rtk, outdoors, lidar-inertial, slam, algorithm, indoors`
- Narration: The robot's own pose is recovered from RTK outdoors and from a LiDAR-inertial SLAM algorithm indoors, which is needed to compensate for the robot's ego-motion when forming pedestrian trajectories and to align the semantic maps.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c3_robot_own_pose_recovered_rtk" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords robot, own, pose, recovered, rtk, outdoors in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_those_maps_twelve_layer_hierarchical`

- Preferred role: `method`
- Cue keywords: `those, maps, twelve-layer, hierarchical, structure, built, point, clouds, segmented, hand`
- Narration: Those maps use a twelve-layer hierarchical structure built from point clouds and segmented by hand. Expert annotators labeled 3D cuboids at five hertz, which were interpolated up to ten hertz, and 2D boxes were generated from the 3D cuboids that share object IDs. For privacy, all faces and license plates are blurred.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_those_maps_twelve_layer_hierarchical" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords those, maps, twelve-layer, hierarchical, structure, built in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_total_sit_contains_60_scenes`

- Preferred role: `content`
- Cue keywords: `total, sit, contains, 60, scenes, which, amounts, about, sixty, thousand`
- Narration: In total, SiT contains 60 scenes, which amounts to about sixty thousand images and twelve thousand point cloud frames, carrying roughly four hundred and seventy thousand two-dimensional annotations and three hundred and twenty thousand three-dimensional annotations.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c1_total_sit_contains_60_scenes" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords total, sit, contains, 60, scenes, which in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_clip_twenty_seconds_sequential_sampl`

- Preferred role: `result`
- Cue keywords: `clip, twenty, seconds, sequential, sampled, ten, hertz, producing, nine, seconds`
- Narration: Each clip is twenty seconds of sequential data sampled at ten hertz, producing nine seconds of trajectory represented as pose vectors. On top of this data, the paper defines four benchmarks.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c2_clip_twenty_seconds_sequential_sampl" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords clip, twenty, seconds, sequential, sampled, ten in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_three_d_pedestrian_detection_scored`

- Preferred role: `method`
- Cue keywords: `three-d, pedestrian, detection, scored, average, precision, based, center, distance, thresholds`
- Narration: Three-D pedestrian detection is scored with average precision based on center distance at thresholds of a quarter, a half, one, and two meters. Three-D tracking uses standard multi-object tracking metrics.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_three_d_pedestrian_detection_scored" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords three-d, pedestrian, detection, scored, average, precision in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_trajectory_prediction_takes_two_seco`

- Preferred role: `method`
- Cue keywords: `trajectory, prediction, takes, two, seconds, past, motion, predicts, seven, seconds`
- Narration: Trajectory prediction takes two seconds of past motion and predicts seven seconds ahead, scored with average and final displacement error over the best of K candidate trajectories. And an end-to-end task runs from raw sensors all the way to future bounding boxes and trajectories.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c4_trajectory_prediction_takes_two_seco" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords trajectory, prediction, takes, two, seconds, past in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_analysis_confirms_sit_captures_exact`

- Preferred role: `figure`
- Cue keywords: `analysis, confirms, sit, captures, exactly, interactions, set, out`
- Narration: The data analysis confirms that SiT captures exactly the interactions it set out to.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s07_c1_analysis_confirms_sit_captures_exact" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords analysis, confirms, sit, captures, exactly, interactions in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_when_you_plot_where_pedestrians`

- Preferred role: `method`
- Cue keywords: `when, you, plot, where, pedestrians, appear, relative, robot, they, cluster`
- Narration: When you plot where pedestrians appear relative to the robot, they cluster close in, from all directions, whereas in Waymo Open and nuScenes pedestrians tend to sit off to the side on separate paths.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c2_when_you_plot_where_pedestrians" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords when, you, plot, where, pedestrians, appear in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_counting_instances_satisfy_both_spac`

- Preferred role: `content`
- Cue keywords: `counting, instances, satisfy, both, space-sharing, condition, within-two-meter, proximity, condition, sit`
- Narration: Counting instances that satisfy both a space-sharing condition and a within-two-meter proximity condition, SiT has dramatically more than the three autonomous-driving datasets, which means driving data underrepresents the human-robot interaction that social navigation robots must handle.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c3_counting_instances_satisfy_both_spac" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords counting, instances, satisfy, both, space-sharing, condition in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_benchmark_itself_standout_finding_su`

- Preferred role: `result`
- Cue keywords: `benchmark, itself, standout, finding, supplying, semantic, map, improves, trajectory, prediction`
- Narration: On the benchmark itself, the standout finding is that supplying the semantic map improves trajectory prediction: the best model, NSP-SFM with the map, reaches an ADE-twenty of about 0.52 and an FDE-twenty of about 0.93, clearly better than the same model without the map.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c4_benchmark_itself_standout_finding_su" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords benchmark, itself, standout, finding, supplying, semantic in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_most_informative_comparison_turning`

- Preferred role: `figure`
- Cue keywords: `most, informative, comparison, turning, semantic, map, off, trajectory, prediction`
- Narration: The most informative comparison in the paper is turning the semantic map on and off for trajectory prediction.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s08_c1_most_informative_comparison_turning" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords most, informative, comparison, turning, semantic, map in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_y_net_adding_map_lowers_ade_twenty`

- Preferred role: `content`
- Cue keywords: `y-net, adding, map, lowers, ade-twenty, about, 0.84, down, 0.68, fde-twenty`
- Narration: For Y-Net, adding the map lowers the ADE-twenty from about 0.84 down to 0.68 and the FDE-twenty from about 1.88 to 1.55.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c2_y_net_adding_map_lowers_ade_twenty" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords y-net, adding, map, lowers, ade-twenty, about in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_nsp_sfm_map_brings_ade_twenty_about`

- Preferred role: `content`
- Cue keywords: `nsp-sfm, map, brings, ade-twenty, about, 0.63, 0.52, fde-twenty, about, 1.09`
- Narration: For NSP-SFM, the map brings ADE-twenty from about 0.63 to 0.52 and FDE-twenty from about 1.09 to 0.93. In both cases the map helps, confirming the value of the scene context that SiT provides.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c3_nsp_sfm_map_brings_ade_twenty_about" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords nsp-sfm, map, brings, ade-twenty, about, 0.63 in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_detection_side_models_fuse_camera`

- Preferred role: `method`
- Cue keywords: `detection, side, models, fuse, camera, lidar, outperform, single-sensor, models, voxel-based`
- Narration: On the detection side, models that fuse camera and LiDAR outperform single-sensor models, and voxel-based backbones outperform pillar-based ones, with TransFusion using a voxel backbone giving the best detection score.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c4_detection_side_models_fuse_camera" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords detection, side, models, fuse, camera, lidar in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_numbers_worth_remembering`

- Preferred role: `content`
- Cue keywords: `numbers, worth, remembering`
- Narration: Here are the numbers worth remembering.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c1_numbers_worth_remembering" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords numbers, worth, remembering in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_sit_sixty_scenes_about_sixty`

- Preferred role: `content`
- Cue keywords: `sit, sixty, scenes, about, sixty, thousand, images, twelve, thousand, point`
- Narration: SiT has sixty scenes, about sixty thousand images and twelve thousand point cloud frames, with roughly four hundred and seventy thousand two-dimensional and three hundred and twenty thousand three-dimensional annotations.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c2_sit_sixty_scenes_about_sixty" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords sit, sixty, scenes, about, sixty, thousand in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_trajectory_benchmark_best_semantic_m`

- Preferred role: `result`
- Cue keywords: `trajectory, benchmark, best, semantic, map, reaches, ade-twenty, about, 0.52, fde-twenty`
- Narration: On the trajectory benchmark, the best model with the semantic map reaches an ADE-twenty of about 0.52 and an FDE-twenty of about 0.93.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c3_trajectory_benchmark_best_semantic_m" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords trajectory, benchmark, best, semantic, map, reaches in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_detection_best_camera_plus_lidar_fus`

- Preferred role: `result`
- Cue keywords: `detection, best, camera-plus-lidar, fusion, reaches, mean, average, precision, about, 0.53`
- Narration: On detection, the best camera-plus-LiDAR fusion model reaches a mean average precision of about 0.53. And on tracking, the CenterPoint tracker leads with an sAMOTA around 0.61.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c4_detection_best_camera_plus_lidar_fus" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords detection, best, camera-plus-lidar, fusion, reaches, mean in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_takeaway_simple`

- Preferred role: `takeaway`
- Cue keywords: `takeaway, simple`
- Narration: The takeaway is simple.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s10_c1_takeaway_simple" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, simple in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_you_want_build_robots_move`

- Preferred role: `method`
- Cue keywords: `you, want, build, robots, move, safely, gracefully, among, people, you`
- Narration: If you want to build robots that move safely and gracefully among people, you need training data that shows the robot up close in the crowd, with all its sensors aligned in time and with the surrounding scene captured as a map.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c2_you_want_build_robots_move" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords you, want, build, robots, move, safely in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_sit_first_dataset_deliver_combinatio`

- Preferred role: `result`
- Cue keywords: `sit, first, dataset, deliver, combination, together, benchmark, spans, detection, tracking`
- Narration: SiT is the first dataset to deliver that combination, together with a benchmark that spans detection, tracking, prediction, and end-to-end forecasting, and it is all publicly released so the community can build on it.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s10_c3_sit_first_dataset_deliver_combinatio" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords sit, first, dataset, deliver, combination, together in title/desc so the matcher can verify semantic overlap.
