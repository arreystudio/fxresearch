"""
07_diagnostics_refinement.py
VIF, quarter fixed effects, and simple dynamic (lagged dependent) specs.
"""
import pandas as pd
import statsmodels.api as sm
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

    with open(cfg.output_path("logs", "07_diagnostics.txt"), "w") as f:
        f.write("Diagnostics and refinement completed.\n")


if __name__ == "__main__":
    main()