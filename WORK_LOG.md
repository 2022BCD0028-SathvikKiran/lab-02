Work log - Lab updates

What I changed:
- Ran `Script/train.py` to generate model artifacts and `output/metrics.json`.
- Updated `parse_actions_runs.py` to accept `--file`, search common locations, handle BOM, and write `output/actions_summary.json`.
- Cleaned duplicate metrics entry in `output/metrics.json`.

How to reproduce locally:

1. (Optional) create and activate your Python environment

2. Install requirements:

```powershell
pip install -r requirements.txt
```

3. Run training script:

```powershell
python Script\train.py
```

4. Run parser for GitHub Actions runs (auto-detects `lab2/actions_runs.json`):

```powershell
python parse_actions_runs.py
```

Files of interest:
- output/metrics.json
- output/actions_summary.json
- parse_actions_runs.py
- Script/train.py

Notes:
- `parse_actions_runs.py` also supports `--file` to point to a specific JSON file.
- If you want metrics deduplication in future runs, we can update `Script/train.py` to replace existing experiment entries instead of always appending.
 - `parse_actions_runs.py` also supports `--file` to point to a specific JSON file.
 - `Script/train.py` and `lab2/Script/train.py` now replace existing metrics by `Experiment ID` (idempotent) and standardize the R^2 key to `R^2 Score`.
