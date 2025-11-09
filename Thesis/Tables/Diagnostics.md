## Diagnostics: Validity and Reliability

This page consolidates the key diagnostic checks referenced in the thesis to support validity and reliability claims.

### Multicollinearity (VIF)

Source: `../Output/tables/07_vif.csv`

| Variable | VIF |
|---|---|
| ERVol12Q | 1.6472 |
| Hedge | 2.2121 |
| DER | 2.5848 |
| lnTA | 1.2542 |
| CR | 1.3782 |

Interpretation: All VIF values are below 3, comfortably under common thresholds (5–10), indicating low multicollinearity among regressors.

### Heteroskedasticity (Breusch–Pagan, ROA)

Source: `../Output/tables/03_breusch_pagan_roa.csv`

| LM_stat | LM_pvalue | F_stat | F_pvalue |
|---:|---:|---:|---:|
| 1.5363 | 0.6739 | 0.4861 | 0.6936 |

Interpretation: The Breusch–Pagan test does not indicate heteroskedasticity for ROA (p-values ≈ 0.67–0.69). HAC-robust standard errors are nevertheless applied across models for robustness.

### Autocorrelation (ACF/PACF and Dynamic Terms)

Figures: `../Output/figures/03_acf_ROA.svg`, `../Output/figures/03_pacf_ROA.svg`, `../Output/figures/03_acf_NetIncome.svg`, `../Output/figures/03_pacf_NetIncome.svg`, `../Output/figures/03_acf_CFV12Q.svg`, `../Output/figures/03_pacf_CFV12Q.svg`

Dynamic model summaries: `../Output/models/07_roa_dynamic_summary.txt`, `../Output/models/07_netincome_dynamic_summary.txt`, `../Output/models/07_cfv12q_dynamic_summary.txt`

Key notes:
- ROA: `ROA_lag1` is negative and statistically significant; Durbin–Watson ≈ 1.91, suggesting residual autocorrelation is mitigated with the lag term and HAC SEs.
- Net Income: `NetIncome_lag1` is negative and significant; Durbin–Watson ≈ 1.92.
- CFV12Q: Strong persistence (`CFV12Q_lag1` ≈ 0.869, p < 0.001); Durbin–Watson ≈ 2.02 indicates residuals close to white noise once dynamics are included.

Overall: Diagnostics support model validity and reliability. Multicollinearity is low, heteroskedasticity is not detected for ROA, and autocorrelation is addressed using appropriate dynamic specifications and HAC-robust standard errors.