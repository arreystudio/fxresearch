# 06_sensitivity_analysis.md

Purpose:
- Test robustness to alternative volatility windows, scaling choices, winsorization, and subperiod splits.

Why this method:
- Confirms that findings are not artifacts of specification choices.

Process:
- Re-estimate models using ERVolM3M and ERVolM12M.
- Scale NetIncome by exp(lnTA) (proxy for total assets).
- Winsorize ROA and NetIncome at 1% tails.
- Split sample into pre-2020Q1 and post-2020Q1.

Outputs:
- Model summaries and parameter tables prefixed `06_` in `Output/models` and `Output/tables`.
- Log: `Output/logs/06_sensitivity.txt`.

How to run:
- `python /Volumes/Rey/roa/Code/06_sensitivity_analysis.py`