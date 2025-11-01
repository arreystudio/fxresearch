"""
00_config.py
Central configuration for paths, directories, and shared helpers.
"""
import os
from dataclasses import dataclass

BASE_DIR = "/Volumes/Rey/roa"
DATA_FILE = os.path.join(BASE_DIR, "EViews Test.csv")
CODE_DIR = os.path.join(BASE_DIR, "Code")
DOC_DIR = os.path.join(BASE_DIR, "Documentation")
OUTPUT_DIR = os.path.join(BASE_DIR, "Output")

OUTPUT_SUBDIRS = {
    "data": os.path.join(OUTPUT_DIR, "data"),
    "figures": os.path.join(OUTPUT_DIR, "figures"),
    "tables": os.path.join(OUTPUT_DIR, "tables"),
    "models": os.path.join(OUTPUT_DIR, "models"),
    "logs": os.path.join(OUTPUT_DIR, "logs"),
    "summaries": os.path.join(OUTPUT_DIR, "summaries"),
}

EXPECTED_COLUMNS = [
    "Quarter","ROA","NetIncome","CFV12Q","ERVol12Q","DER","lnTA","CR","Hedge","ERVolM3M","ERVolM12M"
]


def ensure_dirs():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for p in OUTPUT_SUBDIRS.values():
        os.makedirs(p, exist_ok=True)


def output_path(kind: str, filename: str) -> str:
    assert kind in OUTPUT_SUBDIRS, f"Unknown output kind: {kind}"
    return os.path.join(OUTPUT_SUBDIRS[kind], filename)


@dataclass
class ModelSpec:
    dep: str
    indeps: list
    cov_type: str = "HAC"
    hac_lags: int = 4  # quarterly data heuristic


BASELINE_SPECS = [
    ModelSpec(dep="ROA", indeps=["ERVol12Q","Hedge","DER","lnTA","CR"]),
    ModelSpec(dep="NetIncome", indeps=["ERVol12Q","Hedge","DER","lnTA","CR"]),
    ModelSpec(dep="CFV12Q", indeps=["ERVol12Q","Hedge","DER","lnTA","CR"]),
]