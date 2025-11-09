"""
07_diagnostics_refinement.py
VIF, quarter fixed effects, and simple dynamic (lagged dependent) specs.
"""
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from statsmodels.stats.diagnostic import acorr_breusch_godfrey
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.stats.outliers_influence import variance_inflation_factor
import importlib.util, os, sys
_cfg_path = os.path.join(os.path.dirname(__file__), "00_config.py")
_spec = importlib.util.spec_from_file_location("cfg", _cfg_path)
cfg = importlib.util.module_from_spec(_spec)
sys.modules["cfg"] = cfg
_spec.loader.exec_module(cfg)


def compute_vif(df, cols):
    X = df[cols].dropna()
    X = sm.add_constant(X)
    vif = []
    for i in range(1, X.shape[1]):  # skip constant index 0
        vif.append({"variable": X.columns[i], "VIF": variance_inflation_factor(X.values, i)})
    return pd.DataFrame(vif)


def run_fe(df, dep):
    dummies = pd.get_dummies(df["Quarter"], prefix="Q", drop_first=True)
    base_X = df[["ERVol12Q","Hedge","DER","lnTA","CR"]].apply(pd.to_numeric, errors="coerce")
    X = pd.concat([base_X, dummies], axis=1)
    y = pd.to_numeric(df[dep], errors="coerce")
    data = pd.concat([y.rename(dep), X], axis=1).dropna()
    y_clean = data[dep].astype(float)
    X_clean = sm.add_constant(data.drop(columns=[dep]).astype(float))
    model = sm.OLS(y_clean, X_clean, missing="drop").fit(cov_type="HAC", cov_kwds={"maxlags": 4})
    with open(cfg.output_path("models", f"07_{dep.lower()}_fe_summary.txt"), "w") as f:
        f.write(model.summary().as_text())


def run_dynamic(df, dep):
    df = df.copy()
    df[f"{dep}_lag1"] = pd.to_numeric(df[dep], errors="coerce").shift(1)
    indeps = ["ERVol12Q","Hedge","DER","lnTA","CR", f"{dep}_lag1"]
    X = df[indeps].apply(pd.to_numeric, errors="coerce")
    y = pd.to_numeric(df[dep], errors="coerce")
    data = pd.concat([y.rename(dep), X], axis=1).dropna()
    y_clean = data[dep].astype(float)
    X_clean = sm.add_constant(data[indeps].astype(float))
    model = sm.OLS(y_clean, X_clean, missing="drop").fit(cov_type="HAC", cov_kwds={"maxlags": 4})
    with open(cfg.output_path("models", f"07_{dep.lower()}_dynamic_summary.txt"), "w") as f:
        f.write(model.summary().as_text())

    # Breusch–Godfrey test for residual autocorrelation (up to 4 lags)
    bg_stat = acorr_breusch_godfrey(model, nlags=4)
    bg_df = pd.DataFrame({
        "LM_stat": [bg_stat[0]],
        "LM_pvalue": [bg_stat[1]],
        "F_stat": [bg_stat[2]],
        "F_pvalue": [bg_stat[3]],
        "nlags": [4],
    })
    bg_df.to_csv(cfg.output_path("tables", f"07_breusch_godfrey_{dep.lower()}.csv"), index=False)

    # Residual ACF/PACF plots
    resid = model.resid
    fig1 = plot_acf(resid, lags=12)
    fig1.savefig(cfg.output_path("figures", f"07_resid_acf_{dep}.svg"), format="svg")
    plt.close(fig1)
    fig2 = plot_pacf(resid, lags=12)
    fig2.savefig(cfg.output_path("figures", f"07_resid_pacf_{dep}.svg"), format="svg")
    plt.close(fig2)


def run_dynamic_diff_cfv(df):
    # First difference of CFV12Q
    df = df.copy()
    df["DCFV12Q"] = pd.to_numeric(df["CFV12Q"], errors="coerce").diff()
    df["DCFV12Q_lag1"] = df["DCFV12Q"].shift(1)
    indeps = ["ERVol12Q","Hedge","DER","lnTA","CR","DCFV12Q_lag1"]
    X = df[indeps].apply(pd.to_numeric, errors="coerce")
    y = pd.to_numeric(df["DCFV12Q"], errors="coerce")
    data = pd.concat([y.rename("DCFV12Q"), X], axis=1).dropna()
    y_clean = data["DCFV12Q"].astype(float)
    X_clean = sm.add_constant(data[indeps].astype(float))
    model = sm.OLS(y_clean, X_clean, missing="drop").fit(cov_type="HAC", cov_kwds={"maxlags": 4})
    with open(cfg.output_path("models", "07_cfv12q_diff_summary.txt"), "w") as f:
        f.write(model.summary().as_text())

    # BG residual autocorrelation for differenced model
    bg_stat = acorr_breusch_godfrey(model, nlags=4)
    bg_df = pd.DataFrame({
        "LM_stat": [bg_stat[0]],
        "LM_pvalue": [bg_stat[1]],
        "F_stat": [bg_stat[2]],
        "F_pvalue": [bg_stat[3]],
        "nlags": [4],
    })
    bg_df.to_csv(cfg.output_path("tables", "07_breusch_godfrey_cfv12q_diff.csv"), index=False)

    # Residual ACF/PACF plots for differenced model
    resid = model.resid
    fig1 = plot_acf(resid, lags=12)
    fig1.savefig(cfg.output_path("figures", "07_resid_acf_DCFV12Q.svg"), format="svg")
    plt.close(fig1)
    fig2 = plot_pacf(resid, lags=12)
    fig2.savefig(cfg.output_path("figures", "07_resid_pacf_DCFV12Q.svg"), format="svg")
    plt.close(fig2)


def run_engle_granger_cfv(df):
    # Engle–Granger residual-based cointegration test: CFV12Q ~ ERVol12Q + DER + lnTA + CR (+ Hedge)
    base_cols = ["ERVol12Q","DER","lnTA","CR","Hedge"]
    y = pd.to_numeric(df["CFV12Q"], errors="coerce")
    X = df[base_cols].apply(pd.to_numeric, errors="coerce")
    data = pd.concat([y.rename("CFV12Q"), X], axis=1).dropna()
    y_clean = data["CFV12Q"].astype(float)
    X_clean = sm.add_constant(data[base_cols].astype(float))
    ols = sm.OLS(y_clean, X_clean, missing="drop").fit()

    resid = ols.resid
    from statsmodels.tsa.stattools import adfuller
    adf_res = adfuller(resid, autolag="AIC", regression="n")
    eg_df = pd.DataFrame({
        "eg_adf_stat": [adf_res[0]],
        "eg_p_value": [adf_res[1]],
        "eg_lags": [adf_res[2]],
        "eg_nobs": [adf_res[3]],
    })
    eg_df.to_csv(cfg.output_path("tables", "07_cointegration_cfv12q.csv"), index=False)

    # Save OLS summary for reference
    with open(cfg.output_path("models", "07_cfv12q_eg_ols_summary.txt"), "w") as f:
        f.write(ols.summary().as_text())

    # Residual ACF/PACF for EG residuals
    fig1 = plot_acf(resid, lags=12)
    fig1.savefig(cfg.output_path("figures", "07_eg_resid_acf_CFV12Q.svg"), format="svg")
    plt.close(fig1)
    fig2 = plot_pacf(resid, lags=12)
    fig2.savefig(cfg.output_path("figures", "07_eg_resid_pacf_CFV12Q.svg"), format="svg")
    plt.close(fig2)


def main():
    cfg.ensure_dirs()
    df = pd.read_csv(cfg.output_path("data", "cleaned.csv"))

    # VIF for baseline regressors
    vif_df = compute_vif(df, ["ERVol12Q","Hedge","DER","lnTA","CR"])
    vif_df.to_csv(cfg.output_path("tables", "07_vif.csv"), index=False)

    # Fixed effects and dynamics
    for dep in ["ROA","NetIncome","CFV12Q"]:
        run_fe(df, dep)
        run_dynamic(df, dep)

    # Robustness: differenced CFV and Engle–Granger cointegration
    run_dynamic_diff_cfv(df)
    run_engle_granger_cfv(df)

    with open(cfg.output_path("logs", "07_diagnostics.txt"), "w") as f:
        f.write("Diagnostics and refinement completed.\n")


if __name__ == "__main__":
    main()