# Dataset / Benchmark

Core claim: Synthetic sparse precision matrices (Scikit-learn generator) with d=15 for the toy study and d=30 with n∈{15,25,35,45} for edge recovery, averaged over 10 ground-truth matrices. Real data is a colorectal-cancer cohort with 7 clinical variables and 312 gene-expression measurements from 260 patients.

Supporting detail: After dropping the p53 mutation status variable and incomplete records, n=190 fully measured patients remain, with s=6 clinical variables and t=312 genes; only the Ω₁₁ and Ω₁₂ query sub-blocks are modeled.

Narration: Experiments use two data types. First, synthetic sparse precision matrices from Scikit-learn: a small fifteen-by-fifteen case to visualize posteriors, and a thirty-dimensional setting with fifteen to forty-five samples for edge recovery, averaged over ten ground-truth matrices. Second, a real colorectal-cancer dataset with six clinical variables and three hundred twelve gene-expression measurements across one hundred ninety patients, inferring only the relevant sub-blocks of the precision matrix.
