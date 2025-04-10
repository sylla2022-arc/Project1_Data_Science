import os
from pathlib import Path
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from src.Project1_Data_Science.utils.common import save_json
from src.Project1_Data_Science.entity.config_entity import ModelEvaluationConfig
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import pandas as pd
import numpy as np
import joblib



class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, actual, y_pred):
        rmse = np.sqrt(mean_squared_error(actual, y_pred))
        mae = mean_absolute_error(actual, y_pred)
        r2 = r2_score(actual, y_pred)
        return rmse, mae, r2

    # define model evluation method
    def log_into_mlflow(self):
        # Load test dataset
        test_data = pd.read_csv(self.config.test_data_path)
        # Load model
        model = joblib.load(self.config.model_path)

        # Extract features and target variable
        X_test = test_data.drop(columns=[self.config.TARGET_COLUMN])
        y_test = test_data[[self.config.TARGET_COLUMN]]

        # set mlflow tracking uri
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_uri_type_score = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            # Predict using the model
            y_pred = model.predict(X_test)

            # Calculate metrics
            (rmse, mae, r2) = self.eval_metrics(y_test, y_pred)
            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(path= Path(self.config.metric_file_name), data=scores)

            # Log metrics to MLflow
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("r2", r2)
            mlflow.log_metric("mae", mae)

            if tracking_uri_type_score != "file":
                # registry the model
                #There are other way ton use model registry, which depends on the use case
                
                # 1. Register the model
                mlflow.sklearn.log_model(model, 'model',registered_model_name ="ElasticNetModel")

            else :
                # 2. Log the model
                mlflow.sklearn.log_model(model, "model")


