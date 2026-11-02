# Python Programming

Python practice, automation scripts, machine-learning case studies, and deep-learning experiments.

## Repository layout

- `Python_Fundamentals/` — Python language fundamentals and OOP exercises.
- `Automation/` — automation scripts and related examples.
- `Machine_Learning/Code/` — machine-learning algorithms, visualizations, and case-study code.
- `Machine_Learning/Datasets/` — selected smaller datasets used by the examples.
- `Deep_Learning/` — ANN, CNN, TensorFlow, and RNN experiments.

## Datasets intentionally not included

The original archive contained very large CSV datasets (`Fake.csv` and `True.csv`, each over 50 MB).
They are excluded from this Git repository to keep cloning and downloads manageable. Obtain them from
their original source or place local copies in `Machine_Learning/Datasets/` when running the related
case study. Check the source and license of each dataset before redistributing it.

Generated model files, virtual environments, compiled Python files, caches, logs, nested archives,
and certificate bundles are not included.

## Setup

Use a virtual environment and install the dependencies required by the particular script or case study.
Not every script uses the same packages; see imports in the relevant file before installing dependencies.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

## Notes

These are learning and project files collected from multiple exercises. Some scripts may require local
datasets, specific package versions, command-line arguments, or paths to be adjusted before execution.
