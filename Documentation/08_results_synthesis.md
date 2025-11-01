# 08_results_synthesis.md

Purpose:
- Summarize key effects (FX volatility, hedging, interaction) across models.

Why this method:
- Provides a concise view of the main relationships for decision-making.

Process:
- Read parameter tables from baseline and interaction models.
- Extract estimates and p-values for ERVol12Q, Hedge, ERVol12Q_Hedge.
- Save a combined table and a Markdown summary.

Outputs:
- `08_key_effects.csv` in `Output/tables`.
- `08_results_synthesis.md` in `Output/summaries`.
- Log: `Output/logs/08_synthesis.txt`.

How to run:
- `python /Volumes/Rey/roa/Code/08_results_synthesis.py`