# 01_data_preparation.md

Purpose:
- Read the raw CSV, validate columns, convert data types, and save a cleaned dataset.

Why this method:
- Clean inputs prevent downstream errors and ensure consistent numeric processing.

Process:
- Read `/Volumes/Rey/roa/EViews Test.csv`.
- Validate expected columns (Quarter, ROA, NetIncome, CFV12Q, ERVol12Q, DER, lnTA, CR, Hedge, ERVolM3M, ERVolM12M).
- Convert numeric variables and set Hedge as integer.
- Drop rows with missing key fields (ROA, NetIncome, ERVol12Q).
- Save cleaned dataset.

Outputs:
- Cleaned CSV: `Output/data/cleaned.csv`.
- Log: `Output/logs/01_data_preparation.txt`.

How to run:
- `python /Volumes/Rey/roa/Code/01_data_preparation.py`