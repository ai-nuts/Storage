# Motivation

Core claim: An enormous, growing volume of unlabeled time series is collected from IoT sensors and wearables; a pre-training method that explicitly emphasizes temporal correlation modeling could unlock this data for downstream forecasting and classification.

Supporting detail: Prior work treats each subseries in isolation and overlooks the chronological relationship between temporally distanced observations, leaving the time-dependent structure of the data unused.

Narration: The timing could not be better for a method that gets this right. Every day the world's sensors, wearables, and industrial systems pour out staggering volumes of unlabeled time series through the Internet of Things. That data is a gold mine, but only if we can learn from it without hand labeling. The key insight motivating TimeSiam is that time series carry a special kind of information prior methods throw away: the correlation between what happened in the past and what is happening now. Instead of treating each window in isolation, why not build a pre-training task that explicitly asks the model to relate distant moments in time to each other.
