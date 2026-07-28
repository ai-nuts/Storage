# Headline Numbers

Core claim: - 500x speedup over CGAL on a MaxCut instance with over 2 billion decision variables. - >100x convergence speedup from warm-starting versus cold-starting USBS. - 10 / 10 MaxCut instances solved by USBS (in ≤28 hours) vs. only 3 / 10 by CGAL (within 72 hours).

Supporting detail: - Scales to SDPs with over 10¹³ decision variables (333SP MaxCut, n≈3.7M). - QAP relaxation solved at n=198 (1.5 billion decision variables) via r=n sketching.

Narration: To summarize the numbers that matter most: a five-hundred-times speedup over the previous state of the art on a problem with more than two billion decision variables; more than a one-hundred-times convergence speedup just from warm-starting; ten out of ten MaxCut instances solved by USBS in twenty-eight hours or less, versus only three out of ten for CGAL even given seventy-two hours. USBS scales to problems with over ten-to-the-thirteenth decision variables and solves quadratic-assignment relaxations with one point five billion variables.
