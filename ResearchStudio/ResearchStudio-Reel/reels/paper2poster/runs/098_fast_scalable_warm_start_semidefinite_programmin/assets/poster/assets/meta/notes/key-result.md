# Key Result

Core claim: Against CGAL with sketching, the previous state-of-the-art scalable solver, USBS reaches an accurate solution on all ten MaxCut instances within 28 hours while CGAL fails on 7 of 10 within 72 hours, and it delivers a 500x speedup on an instance with over 2 billion decision variables.

Supporting detail: On QAP and entity-resolution tasks USBS consistently reaches lower relative gaps and cumulative solve times, and the performance gap over CGAL widens as problem size grows; USBS also leverages warm starts far more reliably than CGAL.

Narration: The results are striking. On MaxCut, USBS reaches an accurate solution on all ten instances in twenty-eight hours or less, even without a warm start, while the previous state-of-the-art solver, CGAL, fails to reach an accurate solution on seven of the ten instances within seventy-two hours. On an instance with over two billion decision variables, USBS is five hundred times faster than CGAL. On the quadratic assignment and entity-resolution tasks, USBS reaches better relative gaps and lower cumulative solve times, and the gap in its favor grows as the problems get larger. Across all three settings, USBS reliably takes advantage of warm starts, whereas CGAL often cannot.
