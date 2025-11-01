"""
08_results_synthesis.py
Aggregates key coefficients from outputs into summary tables and Markdown.
"""
import os
import pandas as pd
import importlib.util, os, sys
_cfg_path = os.path.join(os.path.dirname(__file__), "00_config.py")
_spec = importlib.util.spec_from_file_location("cfg", _cfg_path)
cfg = importlib.util.module_from_spec(_spec)
sys.modules["cfg"] = cfg
_spec.loader.exec_module(cfg)

KEY_TABLES = {
    "baseline_roa": "04_roa_baseline_params.csv",
    "baseline_netincome": "04_netincome_baseline_params.csv",
    "baseline_cfv": "04_cfv_baseline_params.csv",
    "interaction_roa": "05_roa_interaction_params.csv",
    "interaction_netincome": "05_netincome_interaction_params.csv",
    "interaction_cfv": "05_cfv_interaction_params.csv",
}


def main():
    cfg.ensure_dirs()
    rows = []
    for label, fname in KEY_TABLES.items():
        path = cfg.output_path("tables", fname)
        if os.path.exists(path):
            df = pd.read_csv(path, index_col=0)
            for var in df.index:
                if var in ["ERVol12Q","Hedge","ERVol12Q_Hedge"]:
                    rows.append({
                        "model": label,
                        "variable": var,
                        "estimate": df.loc[var, "estimate"],
                        "std_err": df.loc[var, "std_err"],
                        "p_value": df.loc[var, "p_value"],
                    })
    out_df = pd.DataFrame(rows)
    out_df.to_csv(cfg.output_path("tables", "08_key_effects.csv"), index=False)

    md = ["# Results Synthesis", "", "Key effects (ERVol, Hedge, Interaction):", ""]
    for _, r in out_df.iterrows():
        md.append(f"- {r['model']} | {r['variable']}: est={r['estimate']:.4g}, p={r['p_value']:.3g}")

    # Append structural break tests
    break_path = cfg.output_path("tables", "06_break_tests.csv")
    if os.path.exists(break_path):
        md += ["", "Structural Break Tests (CUSUM and Chow at 2020Q1):", ""]
        bt = pd.read_csv(break_path)
        for _, r in bt.iterrows():
            if r["test"].startswith("CUSUM"):
                md.append(
                    f"- {r['dep']} | {r['test']}: stat={r['statistic']:.4g}, p={r['p_value']:.3g}; crit(1/5/10%)=({r['crit_1']:.4g},{r['crit_5']:.4g},{r['crit_10']:.4g})"
                )
            else:
                md.append(
                    f"- {r['dep']} | {r['test']}: F={r['statistic']:.4g}, p={r['p_value']:.3g} (df1={int(r['df1'])}, df2={int(r['df2'])})"
                )

    with open(cfg.output_path("summaries", "08_results_synthesis.md"), "w") as f:
        f.write("\n".join(md))

    with open(cfg.output_path("logs", "08_synthesis.txt"), "w") as f:
        f.write("Synthesis completed.\n")


if __name__ == "__main__":
    main()