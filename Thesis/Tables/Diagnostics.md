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

### Heteroskedasticity (Breusch–Pagan, ROA, NetIncome, CFV12Q)

Sources: `../Output/tables/03_breusch_pagan_roa.csv`, `../Output/tables/03_breusch_pagan_netincome.csv`, `../Output/tables/03_breusch_pagan_cfv12q.csv`

| DepVar | LM_stat | LM_pvalue | F_stat | F_pvalue |
|---|---:|---:|---:|---:|
| ROA | 1.5363 | 0.6739 | 0.4861 | 0.6936 |
| NetIncome | 1.5210 | 0.6774 | 0.4811 | 0.6971 |
| CFV12Q | 0.6005 | 0.8963 | 0.1864 | 0.9051 |

Interpretation: Breusch–Pagan tidak mengindikasikan heteroskedastisitas untuk ketiga dependent variables (p-values tinggi). SE HAC tetap digunakan lintas model sebagai ketahanan.

### Autocorrelation (ACF/PACF and Dynamic Terms)

Figures: `../Output/figures/03_acf_ROA.svg`, `../Output/figures/03_pacf_ROA.svg`, `../Output/figures/03_acf_NetIncome.svg`, `../Output/figures/03_pacf_NetIncome.svg`, `../Output/figures/03_acf_CFV12Q.svg`, `../Output/figures/03_pacf_CFV12Q.svg`

Dynamic model summaries: `../Output/models/07_roa_dynamic_summary.txt`, `../Output/models/07_netincome_dynamic_summary.txt`, `../Output/models/07_cfv12q_dynamic_summary.txt`

Key notes:
- ROA: `ROA_lag1` is negative and statistically significant; Durbin–Watson ≈ 1.91, suggesting residual autocorrelation is mitigated with the lag term and HAC SEs.
- Net Income: `NetIncome_lag1` is negative and significant; Durbin–Watson ≈ 1.92.
- CFV12Q: Strong persistence (`CFV12Q_lag1` ≈ 0.869, p < 0.001); Durbin–Watson ≈ 2.02 indicates residuals close to white noise once dynamics are included.

Overall: Diagnostics support model validity and reliability. Multicollinearity is low, heteroskedasticity is not detected for ROA, and autocorrelation is addressed using appropriate dynamic specifications and HAC-robust standard errors.

### Stationarity (ADF) — Including Controls

Source: `../Output/tables/03_adf_results.csv`

| Variable | ADF stat | p-value | lags | nobs |
|---|---:|---:|---:|---:|
| ROA | -7.468 | 5.16e-11 | 0 | 49 |
| NetIncome | -7.291 | 1.42e-10 | 0 | 49 |
| ERVol12Q | -2.896 | 0.0458 | 1 | 48 |
| CFV12Q | -1.344 | 0.6089 | 0 | 49 |
| DER | -2.379 | 0.1477 | 0 | 49 |
| lnTA | -2.044 | 0.2677 | 0 | 49 |
| CR | -1.837 | 0.3622 | 1 | 48 |

Interpretation: ROA dan NetIncome stasioner; ERVol12Q borderline stasioner pada 5%. CFV12Q non‑stasioner (I(1)); kontrol DER, lnTA, dan CR tidak stasioner di level pada taraf 5%—praktik umum adalah tetap digunakan sebagai kontrol level jika residual model berperilaku baik (lihat BG dan DW). Alternatifnya, gunakan transformasi (differencing/log) bila diperlukan oleh interpretasi.

### Stationarity (ADF) — First Differences

Source: `../Output/tables/03_adf_results_diff.csv`

| Variable | ADF stat | p-value | lags | nobs |
|---|---:|---:|---:|---:|
| D_CFV12Q | -5.643 | 0.0000010 | 0 | 48 |
| D_DER | -5.785 | 0.0000005 | 2 | 46 |
| D_lnTA | -7.251 | 0.00000000018 | 0 | 48 |
| D_CR | -7.459 | 0.000000000054 | 1 | 47 |

Interpretation: Keempat variabel yang non‑stasioner di level menjadi stasioner setelah didifference (p-value < 0.05). Ini memenuhi syarat re‑estimasi OLS dengan versi differenced sesuai instruksi.

### Residual Autocorrelation (Breusch–Godfrey on Dynamics)

Sources: `../Output/tables/07_breusch_godfrey_roa.csv`, `../Output/tables/07_breusch_godfrey_netincome.csv`, `../Output/tables/07_breusch_godfrey_cfv12q.csv`

| Model | LM stat | LM p-value | F stat | F p-value | nlags |
|---|---:|---:|---:|---:|---:|
| ROA | 4.036 | 0.4011 | 0.8528 | 0.5009 | 4 |
| NetIncome | 3.767 | 0.4384 | 0.7913 | 0.5382 | 4 |
| CFV12Q | 0.0640 | 0.9995 | 0.0124 | 0.9997 | 4 |

Residual ACF/PACF figures: `../Output/figures/07_resid_acf_ROA.svg`, `../Output/figures/07_resid_pacf_ROA.svg`, `../Output/figures/07_resid_acf_NetIncome.svg`, `../Output/figures/07_resid_pacf_NetIncome.svg`, `../Output/figures/07_resid_acf_CFV12Q.svg`, `../Output/figures/07_resid_pacf_CFV12Q.svg`.

Interpretation: Tidak ada autokorelasi residual yang terdeteksi (p-values > 0.40 untuk ROA/NetIncome; ~1.00 untuk CFV12Q) pada hingga 4 lag. Hal ini konsisten dengan DW ~ 1.91–2.02 dan penggunaan lag dependen di model dinamis.

### Heteroskedasticity (Breusch–Pagan on Re-run OLS, Differenced Specs)

Sources: `../Output/tables/04_breusch_pagan_roa_baseline_diff.csv`, `../Output/tables/04_breusch_pagan_netincome_baseline_diff.csv`, `../Output/tables/04_breusch_pagan_cfv_baseline_diff.csv`

| Model (OLS diff) | LM_stat | LM_p-value | F_stat | F_p-value |
|---|---:|---:|---:|---:|
| ROA | 19.7002 | 0.00142 | 5.7824 | 0.00036 |
| NetIncome | 19.0467 | 0.00188 | 5.4685 | 0.00056 |
| ΔCFV12Q | 5.9489 | 0.31122 | 1.1884 | 0.33078 |

Interpretation: Pada spesifikasi OLS dengan kontrol differenced (dan ΔCFV sebagai dep untuk CFV), BP mengindikasikan heteroskedastisitas untuk ROA dan NetIncome, namun tidak untuk ΔCFV12Q. Standar error HAC/Newey–West telah digunakan dalam estimasi OLS untuk robustifikasi terhadap heteroskedastisitas dan autokorelasi ringan.

### Robustness: ΔCFV12Q Model (First Difference)

Sources: `../Output/models/07_cfv12q_diff_summary.txt`, `../Output/tables/07_breusch_godfrey_cfv12q_diff.csv`

Key results (OLS with HAC SEs, dep: `DCFV12Q`):
- `R-squared` ≈ 0.240; `Adj. R-squared` ≈ 0.128; `F` p ≈ 0.0835
- `Hedge` negatif dan signifikan (p ≈ 0.003); `DER` negatif, signifikan (p ≈ 0.041); `lnTA` negatif, signifikan (p ≈ 0.015)
- `DCFV12Q_lag1` tidak signifikan; DW ≈ 1.93
- BG test (nlags=4): `LM_pvalue` ≈ 0.917; `F_pvalue` ≈ 0.943 → tidak ada autokorelasi residual

Residual ACF/PACF figures: `../Output/figures/07_resid_acf_DCFV12Q.svg`, `../Output/figures/07_resid_pacf_DCFV12Q.svg`

Interpretation: Model differencing menurunkan risiko spurious regression untuk CFV. Hasil menunjukkan hubungan robust pada beberapa kontrol dan tidak ada autokorelasi residual, mendukung validitas spesifikasi dalam bentuk differenced sebagai cek ketahanan.

### Cointegration (Engle–Granger)

Source: `../Output/tables/07_cointegration_cfv12q.csv`

- Engle–Granger ADF pada residual: `stat` ≈ -3.367; `p` ≈ 0.00077; lags=4
- Residual ACF/PACF figures: `../Output/figures/07_eg_resid_acf_CFV12Q.svg`, `../Output/figures/07_eg_resid_pacf_CFV12Q.svg`

Interpretation: Penolakan H0 unit root pada residual menunjukkan kointegrasi antara `CFV12Q` dan gabungan prediktor (`ERVol12Q`, `DER`, `lnTA`, `CR`, `Hedge`). Ini membenarkan estimasi di level (tanpa differencing) selama dinamika dan SE robust digunakan, serta residual lolos uji BG/DW.