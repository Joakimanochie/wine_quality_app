import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from winequality.utils.common import save_json
from urllib.parse import urlparse
import numpy as np
import joblib
from winequality.entity.config_entity import ModelEvaluationConfig
from pathlib import Path


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self,actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2

    
    def save_results(self):

        test_x = pd.read_csv(self.config.X_test_data_path)
        test_y = pd.read_csv(self.config.y_test_data_path)
        model = joblib.load(self.config.model_path)


        
        predicted_qualities = model.predict(test_x)

        (rmse, mae, r2) = self.eval_metrics(test_y, predicted_qualities)
        
        # Saving metrics as local
        scores = {"rmse": rmse, "mae": mae, "r2": r2}
        save_json(path=Path(self.config.metric_file_name), data=scores)
