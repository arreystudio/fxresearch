"""
00_run_all.py
Runner that sequentially executes all numbered analysis steps.
"""
import os
import sys
import importlib.util

# Load config dynamically from file because the module name starts with a digit
CODE_DIR = os.path.dirname(__file__)
_cfg_path = os.path.join(CODE_DIR, "00_config.py")
_cfg_spec = importlib.util.spec_from_file_location("cfg", _cfg_path)
cfg = importlib.util.module_from_spec(_cfg_spec)
sys.modules["cfg"] = cfg
_cfg_spec.loader.exec_module(cfg)

# List of step scripts to run by file path (numeric module names cannot be imported normally)
MODULE_FILES = [
    os.path.join(CODE_DIR, "01_data_preparation.py"),
    os.path.join(CODE_DIR, "02_eda.py"),
    os.path.join(CODE_DIR, "03_pre_estimation_checks.py"),
    os.path.join(CODE_DIR, "04_baseline_regressions.py"),
    os.path.join(CODE_DIR, "05_interaction_analysis.py"),
    os.path.join(CODE_DIR, "06_sensitivity_analysis.py"),
    os.path.join(CODE_DIR, "07_diagnostics_refinement.py"),
    os.path.join(CODE_DIR, "08_results_synthesis.py"),
    os.path.join(CODE_DIR, "09_policy_implications.py"),
    os.path.join(CODE_DIR, "10_write_up_assets.py"),
]


def _load_module_from_path(mod_path: str, name_hint: str):
    spec = importlib.util.spec_from_file_location(name_hint, mod_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name_hint] = module
    spec.loader.exec_module(module)
    return module


def main():
    cfg.ensure_dirs()
    for mod_path in MODULE_FILES:
        name_hint = f"step_{os.path.splitext(os.path.basename(mod_path))[0]}"
        print(f"Running {name_hint}...")
        mod = _load_module_from_path(mod_path, name_hint)
        if hasattr(mod, "main"):
            mod.main()
        else:
            print(f"Module {name_hint} has no main(); skipping")


if __name__ == "__main__":
    main()