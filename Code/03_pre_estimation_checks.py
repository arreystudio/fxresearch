"""
03_pre_estimation_checks.py
ADF stationarity, ACF/PACF plots, and preliminary Breusch–Pagan test.
"""
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import statsmodels.api as sm
from statsmodels.stats.diagnostic import het_breuschpagan
import importlib.util, os, sys
_cfg_path = os.path.join(os.path.dirname(__file__), "00_config.py")
_spec = importlib.util.spec_from_file_location("cfg", _cfg_path)
cfg = importlib.util.module_from_spec(_spec)
sys.modules["cfg"] = cfg
_spec.loader.exec_module(cfg)

CHECK_VARS = ["ROA","NetIncome","ERVol12Q","CFV12Q"]


def main():
    cfg.ensure_dirs()
    df = pd.read_csv(cfg.output_path("data", "cleaned.csv"))

    # ADF tests
    rows = []
    for col in CHECK_VARS:
        series = df[col].dropna().values
        adf_res = adfuller(series, autolag="AIC")
        rows.append({
            "variable": col,
            "adf_stat": adf_res[0],
            "p_value": adf_res[1],
            "lags": adf_res[2],
            "nobs": adf_res[3],
        })
        # ACF/PACF plots
        fig1 = plot_acf(series, lags=12)
        fig1.savefig(cfg.output_path("figures", f"03_acf_{col}.svg"), format="svg")
        plt.close(fig1)
        fig2 = plot_pacf(series, lags=12)
        fig2.savefig(cfg.output_path("figures", f"03_pacf_{col}.svg"), format="svg")
        plt.close(fig2)

    pd.DataFrame(rows).to_csv(cfg.output_path("tables", "03_adf_results.csv"), index=False)

    # Preliminary OLS for BP test: ROA ~ DER + lnTA + CR
    y = df["ROA"]
    X = df[["DER","lnTA","CR"]]
    X = sm.add_constant(X)
    ols = sm.OLS(y, X, missing="drop").fit()
    bp = het_breuschpagan(ols.resid, ols.model.exog)
    bp_df = pd.DataFrame({
        "LM_stat": [bp[0]],
        "LM_pvalue": [bp[1]],
        "F_stat": [bp[2]],
        "F_pvalue": [bp[3]],
    })
    bp_df.to_csv(cfg.output_path("tables", "03_breusch_pagan_roa.csv"), index=False)

    with open(cfg.output_path("logs", "03_checks.txt"), "w") as f:
        f.write("ADF, ACF/PACF, and BP test completed.\n")


if __name__ == "__main__":
    main()