"""
05_interaction_analysis.py
Adds ERVol12Q × Hedge interaction to baseline models.
"""
import pandas as pd
import statsmodels.api as sm
import importlib.util, os, sys
_cfg_path = os.path.join(os.path.dirname(__file__), "00_config.py")
_spec = importlib.util.spec_from_file_location("cfg", _cfg_path)
cfg = importlib.util.module_from_spec(_spec)
sys.modules["cfg"] = cfg
_spec.loader.exec_module(cfg)


def run_interaction(df, spec_name: str, dep: str):
    df = df.copy()
    df["ERVol12Q_Hedge"] = pd.to_numeric(df["ERVol12Q"], errors="coerce") * pd.to_numeric(df["Hedge"], errors="coerce")
    indeps = ["ERVol12Q","Hedge","ERVol12Q_Hedge","DER","lnTA","CR"]
    y = pd.to_numeric(df[dep], errors="coerce")
    X = df[indeps].apply(pd.to_numeric, errors="coerce")
    data = pd.concat([y.rename(dep), X], axis=1).dropna()
    y_clean = data[dep].astype(float)
    X_clean = sm.add_constant(data[indeps].astype(float))
    model = sm.OLS(y_clean, X_clean, missing="drop").fit(cov_type="HAC", cov_kwds={"maxlags": 4})
    with open(cfg.output_path("models", f"05_{spec_name}_summary.txt"), "w") as f:
        f.write(model.summary().as_text())
    params = model.params.to_frame("estimate")
    params["std_err"] = model.bse
    params["p_value"] = model.pvalues
    params.to_csv(cfg.output_path("tables", f"05_{spec_name}_params.csv"))


def main():
    cfg.ensure_dirs()
    df = pd.read_csv(cfg.output_path("data", "cleaned.csv"))
    for dep, name in [("ROA","roa_interaction"),("NetIncome","netincome_interaction"),("CFV12Q","cfv_interaction")]:
        run_interaction(df, name, dep)
    with open(cfg.output_path("logs", "05_interaction.txt"), "w") as f:
        f.write("Interaction models estimated.\n")


if __name__ == "__main__":
    main()