# 07_diagnostics_refinement.md

Purpose:
- Evaluate multicollinearity (VIF), add quarter fixed effects, and test simple dynamics with lagged dependent variables.

Why this method:
- Improves model reliability if diagnostics indicate issues.

Process:
- Compute VIF for baseline regressors.
- Add quarter dummies to control seasonality.
- Include lagged dependent variable as a simple dynamic term.

Outputs:
- `07_vif.csv` in `Output/tables`.
- Model summaries (text) in `Output/models`.
- Log: `Output/logs/07_diagnostics.txt`.

How to run:
- `python /Volumes/Rey/roa/Code/07_diagnostics_refinement.py`