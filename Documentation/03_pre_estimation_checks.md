# 03_pre_estimation_checks.md

Purpose:
- Check stationarity (ADF), autocorrelation (ACF/PACF), and heteroskedasticity (Breusch–Pagan).

Why this method:
- Time-series properties affect inference; diagnostics guide specification choices.

Process:
- Run ADF on ROA, NetIncome, ERVol12Q, CFV12Q.
- Produce ACF/PACF plots (12 lags).
- Fit a preliminary OLS (ROA ~ DER + lnTA + CR) and perform Breusch–Pagan.

Outputs:
- Tables: `03_adf_results.csv`, `03_breusch_pagan_roa.csv` in `Output/tables`.
- Figures (SVG): `03_acf_*`, `03_pacf_*` in `Output/figures`.
- Log: `Output/logs/03_checks.txt`.

How to run:
- `python /Volumes/Rey/roa/Code/03_pre_estimation_checks.py`