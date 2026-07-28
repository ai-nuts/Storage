# Problem

Core claim: Sketching-based scalable SDP solvers scale to huge problems but need more iterations as size grows, and their iteration-dependent parameter schedules block effective warm-starting.

Supporting detail: Standard SDP solvers pay a cubic per-iteration cost from projecting onto the semidefinite cone via full eigendecomposition, so practitioners dismiss SDPs as intractable at scale.

Narration: Semidefinite programs can model an enormous range of practical problems, from combinatorial optimization to neural network verification and control. But solving them at scale is hard. The classic approaches require projecting onto the semidefinite cone, which needs a full eigendecomposition that scales cubically with problem size. Recent sketching methods, like CGAL, avoid storing the full matrix and scale much further, but they pay for it: as the problem grows they need more and more iterations, so convergence slows down. Worse, they rely on iteration-dependent parameter schedules that prevent them from reliably reusing a previous solution as a warm start, which is exactly what many real applications need.
