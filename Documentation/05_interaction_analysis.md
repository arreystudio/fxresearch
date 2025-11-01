# 05_interaction_analysis.md

Purpose:
- Assess whether hedging moderates the effect of FX volatility.

Why this method:
- Interaction term ERVol × Hedge identifies mitigation effects.

Models:
- Add `ERVol12Q_Hedge` to ROA, NetIncome, CFV12Q specifications.

Outputs:
- Model summaries (text) in `Output/models`.
- Parameter tables in `Output/tables` (e.g., `05_roa_interaction_params.csv`).
- Log: `Output/logs/05_interaction.txt`.

How to run:
- `python /Volumes/Rey/roa/Code/05_interaction_analysis.py`