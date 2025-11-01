# 00_config.md

Purpose:
- Centralize paths for data, code, documentation, and outputs.
- Provide helper functions to ensure required folders exist.
- Define common model specs and expected columns.

Why this method:
- A single config avoids hard-coded paths scattered across scripts and makes the project portable.

Process:
- Set base directories and expected CSV columns.
- Create Output subfolders (data, figures, tables, models, logs, summaries).
- Provide helper to build output file paths.

Outputs:
- None directly; used by all other scripts.

How to run:
- Imported automatically by every numbered script.