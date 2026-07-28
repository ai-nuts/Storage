# Ablation Study

Core claim: Under Jacobian regularisation the eigenfeatures of the kernel-regression solution show accuracy and robustness moving together — high test accuracy implies robustness (Figure 4). Standard training shows little to no such correlation (Figure 5), and no highly-accurate-but-fragile eigenfeatures appear, unlike the finite-NTK finding of Tsilivis & Kempe (2022).

Supporting detail: The smallest eigenvalue (Assumption 4.4) is far smaller for the JNTK than the NTK and needs deeper networks to become positive — depth ≥11 for GeLU versus ≥6 for erf activation (Figure 6).

Narration: The most striking finding comes from analysing the kernel-regression solution. With Jacobian regularisation, the eigenfeatures that are more accurate are also more robust; accuracy and robustness move together. Standard training shows almost no such link, and it never produces the accurate-but-fragile features seen in earlier finite-NTK work. So the regulariser isn't just trading a little accuracy for robustness; it aligns the two. A separate check on the key full-rank assumption shows it is fragile: the JNTK's smallest eigenvalue is far below the NTK's and only becomes positive for deeper networks, depth eleven for GeLU but just six for the erf activation.
