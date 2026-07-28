# Key Result

Core claim: All three theoretical bounds hold empirically: memorization vs. curvature shows a strong linear trend on CIFAR100 and ImageNet, and stronger privacy (smaller epsilon) produces measurably lower curvature and memorization, matching the predicted best-fit curves.

Supporting detail: The linear memorization-curvature relationship is especially pronounced on ImageNet; as the DP budget epsilon increases, memorization of the top-500 most-memorized examples rises as predicted, staying below the Theorem 5.4 bound.

Narration: Every prediction holds. Memorization plotted against input loss curvature shows a strong linear trend on CIFAR100 and ImageNet, especially clean on ImageNet. Stronger privacy drives curvature down along the predicted curve, and for the most-memorized examples, memorization rises with the privacy budget while staying under the theoretical bound.
