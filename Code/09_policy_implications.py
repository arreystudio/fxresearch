"""
09_policy_implications.py
Derives high-level policy and managerial implications from baseline signs and significance.
"""
import pandas as pd
import importlib.util, os, sys
_cfg_path = os.path.join(os.path.dirname(__file__), "00_config.py")
_spec = importlib.util.spec_from_file_location("cfg", _cfg_path)
cfg = importlib.util.module_from_spec(_spec)
sys.modules["cfg"] = cfg
_spec.loader.exec_module(cfg)

THRESH = 0.05


def interpret_row(row):
    sign = "positive" if row["estimate"] > 0 else "negative"
    signif = row["p_value"] < THRESH
    return sign, signif


def main():
    cfg.ensure_dirs()
    synth = pd.read_csv(cfg.output_path("tables", "08_key_effects.csv"))

    lines = ["# Policy and Managerial Implications", ""]
    for model in sorted(synth["model"].unique()):
        sub = synth[synth["model"] == model]
        lines.append(f"## {model}")
        for _, r in sub.iterrows():
            sign, signif = interpret_row(r)
            msg = f"- {r['variable']}: {sign} effect; " + ("statistically significant." if signif else "not statistically significant.")
            lines.append(msg)
        lines.append("")

    with open(cfg.output_path("summaries", "09_policy_implications.md"), "w") as f:
        f.write("\n".join(lines))

    with open(cfg.output_path("logs", "09_policy.txt"), "w") as f:
        f.write("Policy implications drafted from key effects.\n")


if __name__ == "__main__":
    main()