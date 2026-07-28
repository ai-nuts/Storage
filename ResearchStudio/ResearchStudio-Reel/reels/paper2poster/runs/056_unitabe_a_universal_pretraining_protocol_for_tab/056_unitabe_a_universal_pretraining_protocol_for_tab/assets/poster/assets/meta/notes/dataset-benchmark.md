# Dataset / Benchmark

Core claim: The authors curated a 7TB tabular pretraining corpus from Kaggle spanning 303 domains, 283K tables, and roughly 13 billion examples (averaging 28.7 numerical, 0.4 categorical, and 7.7 textual columns per table). Evaluation uses 12 held-out Kaggle tasks (6 classification, 6 regression) plus 7 standard public tabular benchmarks.

Supporting detail: The top domains include Investing (71K tables, 1B examples), Time Series (65K), Finance (52K), Economics (47K), and Games (32K); the Kaggle evaluation tasks were explicitly excluded from pretraining to avoid leakage.

Narration: To pretrain at scale, the team assembled a massive tabular dataset from Kaggle: about seven terabytes spanning three hundred and three domains, two hundred eighty-three thousand tables, and roughly thirteen billion examples. On average each table has about twenty-nine numerical columns and eight textual ones, with investing, finance, and economics among the largest domains. For evaluation, they hold out twelve Kaggle tasks, six classification and six regression, never seen in pretraining, plus seven widely used public benchmarks to compare against established methods.
