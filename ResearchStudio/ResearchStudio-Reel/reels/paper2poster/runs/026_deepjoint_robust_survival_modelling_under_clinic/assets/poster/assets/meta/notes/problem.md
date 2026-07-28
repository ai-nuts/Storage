# Problem

Core claim: Clinical data are sampled through an informative process, when, which, and how often tests are ordered, yet survival models treat this "clinical presence" as noise, hurting accuracy and transportability.

Supporting detail: Because observation practices vary across sites and time, models fit to one observation regime break when deployed under a shifted one.

Narration: Observational medical data arise from the interaction between patients and the healthcare system. When a clinician orders a test, its timing and its existence carry information about the patient. Most models ignore this, assuming sampling is non-informative. Ignoring clinical presence yields sub-optimal, non-transportable models; modelling it explicitly is the fix.
