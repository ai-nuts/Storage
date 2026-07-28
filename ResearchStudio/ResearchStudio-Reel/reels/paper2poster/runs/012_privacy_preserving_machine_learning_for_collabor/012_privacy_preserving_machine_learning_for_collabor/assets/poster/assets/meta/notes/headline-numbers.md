# Headline Numbers

Core claim: - < 10pp performance drop when replacing raw features with shared latent embeddings - 5%–11% representation (reconstruction) error across the three datasets - House Pricing test R²: 90.29% baseline → 89.33% with two individual autoencoders - Buzz test R²: 96.19% baseline → 94.03% with the non-naive shared autoencoder (Scenario 3)

Supporting detail: Encoding quality: shared autoencoders correctly estimate 96%–98% of observations per feature (≤5% MAPE); MNIST test accuracy 92% baseline → 91% (Scenario 3).

Narration: A few numbers capture the impact. Across all use cases, replacing raw features with shared latent representations dropped downstream performance by less than ten percentage points, while the reconstruction error of the autoencoder ranged from five to eleven percent. On House Pricing, test R-squared fell only from ninety point two nine percent at baseline to eighty-nine point three three percent with two individual autoencoders. On Buzz in Social Media, the non-naive shared autoencoder reached ninety-four percent R-squared against a ninety-six percent baseline. And the shared autoencoders correctly estimated between ninety-six and ninety-eight percent of observations per feature, confirming that the embeddings retain the core structure of the data.
