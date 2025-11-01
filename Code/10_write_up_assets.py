"""
10_write_up_assets.py
Produces a consolidated Markdown report linking tables and figures.
"""
import os
import importlib.util, os, sys
_cfg_path = os.path.join(os.path.dirname(__file__), "00_config.py")
_spec = importlib.util.spec_from_file_location("cfg", _cfg_path)
cfg = importlib.util.module_from_spec(_spec)
sys.modules["cfg"] = cfg
_spec.loader.exec_module(cfg)


def main():
    cfg.ensure_dirs()
    md = []
    md.append("# Krakatau Steel FX Risk Study: Outputs Report")
    md.append("")
    md.append("## Tables")
    for fname in sorted(os.listdir(cfg.OUTPUT_SUBDIRS["tables"])):
        md.append(f"- {fname}")
    md.append("")
    md.append("## Figures")
    for fname in sorted(os.listdir(cfg.OUTPUT_SUBDIRS["figures"])):
        md.append(f"- {fname}")
    md.append("")
    md.append("## Models")
    for fname in sorted(os.listdir(cfg.OUTPUT_SUBDIRS["models"])):
        md.append(f"- {fname}")
    md.append("")
    md.append("## Summaries")
    for fname in sorted(os.listdir(cfg.OUTPUT_SUBDIRS["summaries"])):
        md.append(f"- {fname}")

    with open(cfg.output_path("summaries", "10_report.md"), "w") as f:
        f.write("\n".join(md))

    with open(cfg.output_path("logs", "10_write_up.txt"), "w") as f:
        f.write("Write-up assets generated.\n")


if __name__ == "__main__":
    main()