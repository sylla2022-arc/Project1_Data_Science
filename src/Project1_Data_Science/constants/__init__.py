from pathlib import Path

# Récupère le chemin du dossier racine du projet
ROOT_DIR = Path(__file__).resolve().parents[3]  # ← car tu es dans src/Project1_Data_Science/constants/

CONFIG_FILE_PATH = ROOT_DIR / "config" / "config.yaml"
PARAMS_FILE_PATH = ROOT_DIR / "params.yaml"
SCHEMA_FILE_PATH = ROOT_DIR / "schema.yaml"
