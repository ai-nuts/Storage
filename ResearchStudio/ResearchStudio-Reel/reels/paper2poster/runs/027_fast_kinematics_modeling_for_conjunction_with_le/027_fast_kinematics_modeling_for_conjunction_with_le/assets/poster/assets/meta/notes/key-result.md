# Key Result

Core claim: Once trained, SKiNN generates a vrms image in about 50 ms on a GPU, roughly 300× faster than JAM, while achieving relative error within ±1% for almost all pixels inside the scientifically important innermost two-arcsecond region.

Supporting detail: Across the 500 test images, the median absolute error averaged over an entire image is about 0.47% and the 90th percentile about 1.1%, both well below the typical ≳2% systematic uncertainty in velocity measurements.

Narration: Once trained, SKiNN produces a velocity image from an input parameter vector in about fifty milliseconds on a single GPU, which is roughly three hundred times faster than JAM. Accuracy is assessed on the five hundred held-out test images by computing the relative error at each pixel. While some outer regions can show errors of a few percent, the important innermost region, where real data actually constrains the model, is matched to within plus or minus one percent for almost all pixels. Averaged over entire images, the median absolute error is about 0.47 percent and the ninetieth percentile is about 1.1 percent. Both are comfortably below the typical two-percent-or-greater systematic uncertainty in real velocity measurements.
