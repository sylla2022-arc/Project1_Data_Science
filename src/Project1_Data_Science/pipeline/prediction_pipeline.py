import joblib
import pandas as pd
import numpy as np
from pathlib import Path

class PredictionPipeline:
    def __init__(self):
        # Charger le modèle au moment de l’instanciation
        self.model = joblib.load(Path('artifacts/model_trainer/model.joblib'))

    def predict(self, data):
        data = np.array(data).reshape(1, -1)  # force la forme (1, n_features)
        prediction = self.model.predict(data)
        return prediction
