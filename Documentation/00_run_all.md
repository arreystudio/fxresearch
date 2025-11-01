# 00_run_all.md

Purpose:
- Orchestrate execution of all analysis steps in order.

Why this method:
- Guarantees a reproducible pipeline that can be run end-to-end with a single command.

Process:
- Imports each numbered module and calls its `main()`.
- Ensures output folders exist before running.

Outputs:
- Progress printed to console.

How to run:
- From terminal: `python /Volumes/Rey/roa/Code/00_run_all.py`