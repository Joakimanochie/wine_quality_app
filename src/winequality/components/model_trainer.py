import pandas as pd
import os
from winequality import logger
from sklearn.ensemble import AdaBoostRegressor
import joblib
from winequality.entity.config_entity import ModelTrainerConfig



class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config


    
    def train(self):
        train_x = pd.read_csv(self.config.X_train_data_path)
        train_y = pd.read_csv(self.config.y_train_data_path)



        ADA = AdaBoostRegressor(learning_rate=self.config.learning_rate, n_estimators=self.config.n_estimators)
        ADA.fit(train_x, train_y)

        joblib.dump(ADA, os.path.join(self.config.root_dir, self.config.model_name))


