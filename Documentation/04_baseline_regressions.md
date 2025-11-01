# 04_baseline_regressions.md

Purpose:
- Estimate baseline OLS models with HAC robust standard errors.

Why this method:
- HAC (Newey–West) adjusts for autocorrelation/heteroskedasticity in quarterly time series.

Models:
- ROA ~ ERVol12Q + Hedge + DER + lnTA + CR
- NetIncome ~ ERVol12Q + Hedge + DER + lnTA + CR
- CFV12Q ~ ERVol12Q + Hedge + DER + lnTA + CR

Outputs:
- Model summaries (text) in `Output/models`.
- Parameter tables in `Output/tables` (e.g., `04_roa_baseline_params.csv`).
- Log: `Output/logs/04_baseline.txt`.

How to run:
- `python /Volumes/Rey/roa/Code/04_baseline_regressions.py`