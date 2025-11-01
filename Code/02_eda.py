"""
02_eda.py
Generates summary statistics, correlation matrix, and time-series plots.
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import importlib.util, os, sys
_cfg_path = os.path.join(os.path.dirname(__file__), "00_config.py")
_spec = importlib.util.spec_from_file_location("cfg", _cfg_path)
cfg = importlib.util.module_from_spec(_spec)
sys.modules["cfg"] = cfg
_spec.loader.exec_module(cfg)

sns.set(style="whitegrid")

PLOT_VARS = ["ROA","NetIncome","ERVol12Q","CFV12Q","Hedge"]


def _line_plot(df, col):
    fig, ax = plt.subplots(figsize=(10,4))
    ax.plot(df["Quarter"], df[col], marker="o", linewidth=1)
    ax.set_title(f"Time Series: {col}")
    ax.set_xlabel("Quarter")
    ax.set_ylabel(col)
    plt.xticks(rotation=90)
    fig.tight_layout()
    fig.savefig(cfg.output_path("figures", f"02_eda_{col}.svg"), format="svg")
    plt.close(fig)


def main():
    cfg.ensure_dirs()
    df = pd.read_csv(cfg.output_path("data", "cleaned.csv"))

    # Summary stats
    desc = df.describe(include="all")
    desc.to_csv(cfg.output_path("tables", "02_summary_stats.csv"))

    # Correlation matrix (numeric only)
    corr = df.select_dtypes(include="number").corr()
    corr.to_csv(cfg.output_path("tables", "02_correlations.csv"))

    # Heatmap
    fig, ax = plt.subplots(figsize=(8,6))
    sns.heatmap(corr, cmap="coolwarm", ax=ax)
    ax.set_title("Correlation Matrix")
    fig.tight_layout()
    fig.savefig(cfg.output_path("figures", "02_corr_heatmap.svg"), format="svg")
    plt.close(fig)

    # Line plots
    for col in PLOT_VARS:
        _line_plot(df, col)

    with open(cfg.output_path("logs", "02_eda.txt"), "w") as f:
        f.write("EDA completed: summary, correlations, and plots saved.\n")


if __name__ == "__main__":
    main()