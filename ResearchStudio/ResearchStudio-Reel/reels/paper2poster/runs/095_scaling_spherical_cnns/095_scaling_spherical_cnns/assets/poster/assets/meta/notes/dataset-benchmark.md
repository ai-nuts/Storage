# Dataset / Benchmark

Core claim: QM9 (134,000 molecules, up to 29 atoms, 12 regression targets) for molecular property regression, and WeatherBench / ERA5 reanalysis data for short and medium-range weather forecasting.

Supporting detail: Weather tasks span WeatherBench (Z500, T850, T2M at 3 and 5 days), global extreme temperature forecasting up to 28 days, and iterative high-resolution forecasting following Keisler (2022).

Narration: The experiments span two very different domains. For molecules, the benchmark is QM9, with one hundred thirty four thousand molecules, up to twenty nine atoms each, and twelve regression targets covering energetic, electronic, and thermodynamic properties. For weather, the models are trained on ERA5 reanalysis data through the WeatherBench benchmark, forecasting quantities like geopotential height and temperature at three and five day horizons, plus longer tasks reaching out to twenty eight days and iterative high-resolution forecasting.
