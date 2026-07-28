# Key Result

Core claim: On LM-O the prediction sets attain their target coverage (empirical coverage near 90% at ε=0.1), the worst-case error bounds are always correct whenever PURSE contains the groundtruth pose, and the average pose matches or beats strong baselines on the 2D-projection success metric.

Supporting detail: In the coverage-vs-bound plots, points covered by PURSE (blue circles) never cross the y=x diagonal, confirming the bounds upper-bound the true error as guaranteed with probability 1−ε.

Narration: The results confirm the theory on three fronts. First, coverage is valid: at a ninety percent target, empirical coverage across objects sits right around ninety percent and tightens as the calibration set grows. Second, the bounds are correct: in scatter plots of certified bound versus actual error, every case where PURSE covers the true pose stays below the diagonal, so the bound is never violated when the guarantee holds. Third, the average pose is accurate, beating prior methods on the two-dimensional projection metric with groundtruth boxes and staying comparable with Faster-RCNN detections.
