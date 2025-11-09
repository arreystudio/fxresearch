"""
04_baseline_regressions.py
OLS with HAC robust standard errors for three baseline models.
"""
import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.diagnostic import het_breuschpagan
import importlib.util, os, sys
_cfg_path = os.path.join(os.path.dirname(__file__), "00_config.py")
_spec = importlib.util.spec_from_file_location("cfg", _cfg_path)
cfg = importlib.util.module_from_spec(_spec)
sys.modules["cfg"] = cfg
_spec.loader.exec_module(cfg)


def run_model(df, spec_name: str, dep: str, indeps: list):
    y = pd.to_numeric(df[dep], errors="coerce")
    X = df[indeps].apply(pd.to_numeric, errors="coerce")
    data = pd.concat([y.rename(dep), X], axis=1).dropna()
    y_clean = data[dep].astype(float)
    X_clean = sm.add_constant(data[indeps].astype(float))
    model = sm.OLS(y_clean, X_clean, missing="drop").fit(cov_type=cfg.BASELINE_SPECS[0].cov_type, cov_kwds={"maxlags": cfg.BASELINE_SPECS[0].hac_lags})
    # Save summary and params
    with open(cfg.output_path("models", f"04_{spec_name}_summary.txt"), "w") as f:
        f.write(model.summary().as_text())
    params = model.params.to_frame("estimate")
    params["std_err"] = model.bse
    params["p_value"] = model.pvalues
    params.to_csv(cfg.output_path("tables", f"04_{spec_name}_params.csv"))
    # Breusch–Pagan test
    bp = het_breuschpagan(model.resid, model.model.exog)
    bp_df = pd.DataFrame({
        "LM_stat": [bp[0]],
        "LM_pvalue": [bp[1]],
        "F_stat": [bp[2]],
        "F_pvalue": [bp[3]],
    })
    bp_df.to_csv(cfg.output_path("tables", f"04_breusch_pagan_{spec_name}.csv"), index=False)


def main():
    cfg.ensure_dirs()
    df = pd.read_csv(cfg.output_path("data", "cleaned.csv"))

    specs = [
        ("roa_baseline", "ROA", ["ERVol12Q","Hedge","DER","lnTA","CR"]),
        ("netincome_baseline", "NetIncome", ["ERVol12Q","Hedge","DER","lnTA","CR"]),
        ("cfv_baseline", "CFV12Q", ["ERVol12Q","Hedge","DER","lnTA","CR"]),
    ]
    for name, dep, indeps in specs:
        run_model(df, name, dep, indeps)

    # Differenced controls and ΔCFV12Q specification
    df_diff = df.copy()
    for col in ["DER","lnTA","CR","CFV12Q"]:
        df_diff[f"D_{col}"] = pd.to_numeric(df_diff[col], errors="coerce").diff()
    specs_diff = [
        ("roa_baseline_diff", "ROA", ["ERVol12Q","Hedge","D_DER","D_lnTA","D_CR"]),
        ("netincome_baseline_diff", "NetIncome", ["ERVol12Q","Hedge","D_DER","D_lnTA","D_CR"]),
        ("cfv_baseline_diff", "D_CFV12Q", ["ERVol12Q","Hedge","D_DER","D_lnTA","D_CR"]),
    ]
    for name, dep, indeps in specs_diff:
        run_model(df_diff, name, dep, indeps)

    with open(cfg.output_path("logs", "04_baseline.txt"), "w") as f:
        f.write("Baseline regressions (levels + differenced controls/ΔCFV) completed. HAC robust SEs used.\n")


if __name__ == "__main__":
    main()