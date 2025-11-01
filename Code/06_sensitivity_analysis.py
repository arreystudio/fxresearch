"""
06_sensitivity_analysis.py
Alternative volatility windows, scaling, winsorization, and subperiod splits.
"""
import pandas as pd
import numpy as np
import statsmodels.api as sm
import importlib.util, os, sys
from statsmodels.stats.diagnostic import breaks_cusumolsresid
import scipy.stats as sps
_cfg_path = os.path.join(os.path.dirname(__file__), "00_config.py")
_spec = importlib.util.spec_from_file_location("cfg", _cfg_path)
cfg = importlib.util.module_from_spec(_spec)
sys.modules["cfg"] = cfg
_spec.loader.exec_module(cfg)


def _winsorize(series, lower=0.01, upper=0.99):
    ql, qu = series.quantile(lower), series.quantile(upper)
    return series.clip(ql, qu)


def _crit_values_array(crit):
    vals = []
    try:
        for c in crit:
            if isinstance(c, (list, tuple)):
                # pick the last numeric element if present
                picked = None
                for x in reversed(c):
                    if isinstance(x, (int, float, np.floating)):
                        picked = float(x)
                        break
                vals.append(picked if picked is not None else np.nan)
            elif isinstance(c, (int, float, np.floating)):
                vals.append(float(c))
            else:
                vals.append(np.nan)
    except Exception:
        return [np.nan, np.nan, np.nan]
    if len(vals) < 3:
        vals = vals + [np.nan] * (3 - len(vals))
    return vals[:3]


def run_spec(df, name: str, dep: str, indeps: list):
    y = pd.to_numeric(df[dep], errors="coerce")
    X = df[indeps].apply(pd.to_numeric, errors="coerce")
    data = pd.concat([y.rename(dep), X], axis=1).dropna()
    y_clean = data[dep].astype(float)
    X_clean = sm.add_constant(data[indeps].astype(float))
    model = sm.OLS(y_clean, X_clean, missing="drop").fit(cov_type="HAC", cov_kwds={"maxlags": 4})
    with open(cfg.output_path("models", f"06_{name}_summary.txt"), "w") as f:
        f.write(model.summary().as_text())
    params = model.params.to_frame("estimate")
    params["std_err"] = model.bse
    params["p_value"] = model.pvalues
    params.to_csv(cfg.output_path("tables", f"06_{name}_params.csv"))


def run_break_tests(df, dep: str, indeps: list, break_q: str = "2020Q1"):
    # Ensure numeric types and consistent sample
    y = pd.to_numeric(df[dep], errors="coerce")
    X = df[indeps].apply(pd.to_numeric, errors="coerce")
    data = pd.concat([y.rename(dep), X], axis=1).dropna()
    y_clean = data[dep].astype(float)
    X_clean = sm.add_constant(data[indeps].astype(float))

    # Fit pooled OLS
    pooled = sm.OLS(y_clean, X_clean).fit()

    # CUSUM test on OLS residuals
    sup_b, pval, crit = breaks_cusumolsresid(pooled.resid, ddof=X_clean.shape[1])
    c1, c5, c10 = _crit_values_array(crit)
    results = [
        {
            "dep": dep,
            "test": "CUSUM",
            "statistic": float(sup_b),
            "p_value": float(pval),
            "crit_1": c1,
            "crit_5": c5,
            "crit_10": c10,
        }
    ]

    # Chow test at a known breakpoint (e.g., 2020Q1)
    # restrict to common non-missing index
    idx = data.index
    pre_idx = [i for i in idx if df.loc[i, "Quarter"] < break_q]
    post_idx = [i for i in idx if df.loc[i, "Quarter"] >= break_q]

    if len(pre_idx) > X_clean.shape[1] and len(post_idx) > X_clean.shape[1]:
        y1, X1 = y_clean.loc[pre_idx], X_clean.loc[pre_idx]
        y2, X2 = y_clean.loc[post_idx], X_clean.loc[post_idx]
        m1 = sm.OLS(y1, X1).fit()
        m2 = sm.OLS(y2, X2).fit()
        SSR1 = float(np.sum(m1.resid**2))
        SSR2 = float(np.sum(m2.resid**2))
        SSRp = float(np.sum(pooled.resid**2))
        k = X_clean.shape[1]
        n1 = len(y1)
        n2 = len(y2)
        # Chow F-statistic
        num = (SSRp - (SSR1 + SSR2)) / k
        den = (SSR1 + SSR2) / (n1 + n2 - 2 * k)
        F_stat = float(num / den) if den > 0 else np.nan
        df1 = k
        df2 = n1 + n2 - 2 * k
        p_chow = float(sps.f.sf(F_stat, df1, df2)) if np.isfinite(F_stat) and df2 > 0 else np.nan
        results.append({
            "dep": dep,
            "test": f"Chow({break_q})",
            "statistic": F_stat,
            "p_value": p_chow,
            "df1": df1,
            "df2": df2,
        })

    return results


def main():
    cfg.ensure_dirs()
    df = pd.read_csv(cfg.output_path("data", "cleaned.csv"))

    # Alternative volatility windows
    for dep in ["ROA","NetIncome","CFV12Q"]:
        run_spec(df, f"{dep.lower()}_ervolm3m", dep, ["ERVolM3M","Hedge","DER","lnTA","CR"]) 
        run_spec(df, f"{dep.lower()}_ervolm12m", dep, ["ERVolM12M","Hedge","DER","lnTA","CR"]) 

    # Scaling NetIncome by Total Assets proxy: exp(lnTA)
    df["TA"] = np.exp(df["lnTA"])  # rough proxy
    df["NetIncome_TA"] = df["NetIncome"] / df["TA"]
    run_spec(df, "netincome_over_ta", "NetIncome_TA", ["ERVol12Q","Hedge","DER","lnTA","CR"]) 

    # Winsorization of ROA and NetIncome
    df_w = df.copy()
    df_w["ROA_w"] = _winsorize(df_w["ROA"]) 
    df_w["NetIncome_w"] = _winsorize(df_w["NetIncome"]) 
    run_spec(df_w, "roa_winsor", "ROA_w", ["ERVol12Q","Hedge","DER","lnTA","CR"]) 
    run_spec(df_w, "netincome_winsor", "NetIncome_w", ["ERVol12Q","Hedge","DER","lnTA","CR"]) 

    # Subperiod splits: pre-2020Q1 vs post-2020Q1
    pre_df = df[df["Quarter"] < "2020Q1"]
    post_df = df[df["Quarter"] >= "2020Q1"]
    for subname, subdf in [("pre2020", pre_df),("post2020", post_df)]:
        run_spec(subdf, f"roa_{subname}", "ROA", ["ERVol12Q","Hedge","DER","lnTA","CR"]) 
        run_spec(subdf, f"netincome_{subname}", "NetIncome", ["ERVol12Q","Hedge","DER","lnTA","CR"]) 
        run_spec(subdf, f"cfv_{subname}", "CFV12Q", ["ERVol12Q","Hedge","DER","lnTA","CR"]) 

    # Structural break tests (CUSUM and Chow at 2020Q1)
    break_rows = []
    for dep in ["ROA", "NetIncome", "CFV12Q"]:
        break_rows += run_break_tests(df, dep, ["ERVol12Q","Hedge","DER","lnTA","CR"], break_q="2020Q1")
    pd.DataFrame(break_rows).to_csv(cfg.output_path("tables", "06_break_tests.csv"), index=False)

    # Regime dummy (post-2020Q1) and interaction specifications
    df["Post2020"] = (df["Quarter"] >= "2020Q1").astype(int)
    # Interactions
    df["ERVol12Q_Post2020"] = pd.to_numeric(df["ERVol12Q"], errors="coerce") * df["Post2020"].astype(float)
    df["Hedge_Post2020"] = pd.to_numeric(df["Hedge"], errors="coerce") * df["Post2020"].astype(float)
    # Regime-augmented main effects
    for dep in ["ROA","NetIncome","CFV12Q"]:
        run_spec(df, f"{dep.lower()}_regime", dep, ["ERVol12Q","Hedge","DER","lnTA","CR","Post2020"]) 
    # Regime interactions
    for dep in ["ROA","NetIncome","CFV12Q"]:
        run_spec(df, f"{dep.lower()}_regime_interactions", dep, [
            "ERVol12Q","Hedge","DER","lnTA","CR","Post2020","ERVol12Q_Post2020","Hedge_Post2020"
        ])

    with open(cfg.output_path("logs", "06_sensitivity.txt"), "w") as f:
        f.write("Sensitivity analyses and structural break tests completed.\nRegime-dummy models (post-2020) estimated with interactions.\n")


if __name__ == "__main__":
    main()