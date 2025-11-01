# 02_eda.md

Purpose:
- Explore the data via summary statistics, correlations, and line plots.

Why this method:
- Understand distributions, relationships, and trends before modeling.

Process:
- Compute summary stats and correlation matrix.
- Plot time series for ROA, NetIncome, ERVol12Q, CFV12Q, Hedge.
- Save a correlation heatmap.

Outputs:
- Tables: `02_summary_stats.csv`, `02_correlations.csv` in `Output/tables`.
- Figures (SVG): line plots per variable and `02_corr_heatmap.svg` in `Output/figures`.
- Log: `Output/logs/02_eda.txt`.

How to run:
- `python /Volumes/Rey/roa/Code/02_eda.py`