# Takeaway

Core claim: Framing HD map construction as detection-then-polyline-generation lets a single end-to-end network predict clean, directional vector maps straight from onboard sensors, beating rasterize-and-post-process pipelines by double-digit mAP.

Supporting detail: Polylines are a versatile primitive: the same model extends to centerline prediction with no structural changes, and its outputs measurably help downstream motion forecasting.

Narration: The takeaway: HD mapping needs no rasterize-then-vectorize detour. Treating mapping as detection plus autoregressive polyline generation, VectorMapNet produces directional vector maps directly from sensors, beats rasterized pipelines by double digits, and even extends to centerlines with no architectural change.
