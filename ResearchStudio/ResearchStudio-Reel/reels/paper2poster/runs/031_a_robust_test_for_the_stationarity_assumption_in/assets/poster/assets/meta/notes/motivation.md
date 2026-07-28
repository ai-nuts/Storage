# Motivation

Core claim: Non-stationarity is pervasive in mobile health, traffic signal control, and robotics — e.g. waning intervention effects in the Intern Health Study — where ignoring drift sends inopportune prompts and erodes long-term reward.

Supporting detail: Existing stationarity tests either need known MDP models (Hadoux et al.), rely on linear approximation that fails in high dimensions (Padakandla et al.; Li et al.), or learn a policy per time step and waste samples when the process is piecewise homogeneous.

Narration: Why does this matter now? Consider the Intern Health Study, a year-long mobile-health trial that nudges first-year physicians toward healthier habits through push notifications. The effect of those nudges wanes over time, a textbook case of non-stationarity. Similar drift shows up in traffic signal control, where flow patterns swing between peak and off-peak hours. Ignoring these shifts leads to policies that send prompts at the wrong moments and erode long-term reward. Prior stationarity tests either demand knowledge of the true model, or fall back on linear approximations that collapse in high dimensions, leaving a real gap for modern applications.
