# Appendices

### A. Artifacts and Outputs
- Pre-estimation checks: ../Output/tables/03_adf_results.csv; ACF/PACF figures in ../Output/figures/03_*.
- Baseline and interaction models: ../Output/tables/04_* and ../Output/tables/05_*; summaries in ../Output/models/04_* and ../Output/models/05_*.
- Sensitivity analyses: ../Output/tables/06_* (alt windows, scaling, winsorization, subperiods, regime models); summaries in ../Output/models/06_*.
- Diagnostics: ../Output/tables/07_vif.csv; FE/Dynamic summaries in ../Output/models/07_*.
- Structural break tests: ../Output/tables/06_break_tests.csv.
- Synthesis and policy: ../Output/summaries/08_results_synthesis.md; ../Output/summaries/09_policy_implications.md.

### B. Methods Details
- OLS with HAC-robust standard errors; moderation via interaction terms.
- Regime analysis: Post2020 dummy and interaction specifications.
- Structural stability: CUSUM test and Chow break test around 2020Q1.
- Data integrity: numeric coercion, NA handling, reproducible scripts in Code/.

### C. Variable Definitions (Study-Specific)
- FXVol (ERVol12Q): 12-quarter moving volatility of IDR/USD.
- CFV12Q: 12-quarter moving volatility of operating cash flows.
- Hedge: observed hedging activity indicator(s).
- DER, Total Assets, Current Ratio: firm characteristics as moderators.