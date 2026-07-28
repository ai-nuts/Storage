# Problem

Core claim: Machine learning on Sentinel-1 SAR ocean imagery is bottlenecked by sparse expert labels, and prior classifiers used biased, single-label datasets that misrepresent the true image population.

Supporting detail: Labeling SAR vignettes requires trained experts, so datasets beyond a few thousand images are infeasible, limiting supervised deep learning for atmospheric phenomena detection.

Narration: The European Space Agency's Sentinel-1 radar satellites image the global ocean at unprecedented scale, capturing waves, turbulence, fronts, and biological slicks. Computer vision can process these images, but machine learning has been held back by a lack of labeled data, since only trained experts can annotate radar vignettes. Earlier work also relied on a biased dataset that picked only exemplary images and forced a single label per image, even though multiple phenomena usually coexist. The result was a training set that did not reflect the real distribution of ocean conditions.
