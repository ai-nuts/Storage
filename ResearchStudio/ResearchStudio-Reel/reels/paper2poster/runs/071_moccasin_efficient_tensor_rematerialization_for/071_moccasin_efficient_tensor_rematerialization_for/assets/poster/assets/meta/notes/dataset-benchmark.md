# Dataset / Benchmark

Core claim: Evaluated on random layered graphs G1–G4 spanning 100 to 1000 nodes (up to 5875 edges), on synthetic and real-world compute graphs, with memory budgets set to 80% and 90% of the peak memory of the initial rematerialization-free schedule.

Supporting detail: A real-world graph with n = 442 nodes and m = 1247 edges is used for the headline solve-time comparison; experiments run on a 16-core workstation with 32 GB RAM.

Narration: The evaluation uses a range of compute graphs. The main scaling study is on four random layered graphs, G1 through G4, whose sizes grow from one hundred nodes and a couple hundred edges up to one thousand nodes and nearly six thousand edges. There is also a real-world compute graph with four hundred forty-two nodes and over twelve hundred edges used for the headline comparison. For every graph the memory budget is set to eighty and ninety percent of the peak memory of the initial schedule without rematerialization, so the solver is forced to actually recompute tensors. All experiments run on a sixteen-core workstation with thirty-two gigabytes of RAM.
