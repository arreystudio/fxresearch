"""
01_data_preparation.py
Reads raw CSV, validates columns, converts types, and saves cleaned dataset.
"""
import pandas as pd
import numpy as np
import importlib.util, os, sys
_cfg_path = os.path.join(os.path.dirname(__file__), "00_config.py")
_spec = importlib.util.spec_from_file_location("cfg", _cfg_path)
cfg = importlib.util.module_from_spec(_spec)
sys.modules["cfg"] = cfg
_spec.loader.exec_module(cfg)


def main():
    cfg.ensure_dirs()
    df = pd.read_csv(cfg.DATA_FILE)
    # Validate expected columns
    missing = [c for c in cfg.EXPECTED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing expected columns: {missing}")

    # Convert numeric columns
    num_cols = [c for c in cfg.EXPECTED_COLUMNS if c not in ["Quarter"]]
    for c in num_cols:
        df[c] = pd.to_numeric(df[c], errors="coerce")

    # Hedge as int
    df["Hedge"] = df["Hedge"].fillna(0).astype(int)

    # Basic cleaning: drop rows with critical NaNs (ERVol12Q, ROA, NetIncome)
    df_clean = df.dropna(subset=["ROA","NetIncome","ERVol12Q"]).copy()

    # Save cleaned data
    out_csv = cfg.output_path("data", "cleaned.csv")
    df_clean.to_csv(out_csv, index=False)

    # Simple log
    with open(cfg.output_path("logs", "01_data_preparation.txt"), "w") as f:
        f.write(f"Rows raw: {len(df)}\n")
        f.write(f"Rows cleaned: {len(df_clean)}\n")
        f.write("Numeric columns converted; Hedge set to int.\n")


if __name__ == "__main__":
    main()