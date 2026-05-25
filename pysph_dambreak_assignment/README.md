# PySPH Dam-break Experiment

This project reproduces and modifies the Dam-break experiment from the PySPH paper. This project reproduces and modifies the Dam-break experiment from the PySPH paper using AI Coding Tools.

## Files

- `dam_break_baseline.py`: baseline Dam-break simulation
- `dam_break_dx_modified.py`: modified experiment with smaller particle spacing
- `dam_break_gravity_modified.py`: modified experiment with stronger gravity
- `run_baseline.sh`: run baseline experiment
- `run_experiments.sh`: run all experiments
- `PROMPTS.md`: AI Coding Tools prompt log

## Environment Setup

```bash
conda create -n pysph-exp python=3.10
conda activate pysph-exp
pip install -r requirements.txt
```

## Run Baseline

```bash
python dam_break_baseline.py
```

## Run All Experiments

```bash
bash run_experiments.sh
```

## Visualization

After execution, PySPH creates output directories such as:

- `dam_break_baseline_output`
- `dam_break_dx_modified_output`
- `dam_break_gravity_modified_output`

Example:

```bash
pysph view dam_break_baseline_output
```

If the viewer does not work, the simulation is still successful as long as output files are created.