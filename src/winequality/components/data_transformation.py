import os
from src import logger
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Normalizer
import pandas as pd
from winequality.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    ## Note: You can add different data transformation techniques such as Scaler, PCA and all
    #You can perform all kinds of EDA in ML cycle here before passing this data to the model

    # I am only adding train_test_spliting cz this data is already cleaned up


    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)
        Q1 = data['quality'].quantile(0.25)
        Q3 = data['quality'].quantile(0.75)
        IQR = Q3 - Q1


        lower_bound = Q1 - 1.5 *IQR
        upper_bound = Q3 + 1.5 *IQR

        data = data[(data['quality'] >= lower_bound) & (data['quality'] <= upper_bound)]

        features = data.drop(['quality'], axis=1)

        normalizer =  Normalizer().fit(features)
        norm =  normalizer.transform(features)

        # Split the data into training and test sets. (0.75, 0.25) split.
        target = data['quality']


        X_train, X_test, y_train, y_test = train_test_split(norm, target, test_size=0.25, random_state=42)


        X_train = pd.DataFrame(X_train)
        X_test = pd.DataFrame(X_test)
        y_train = pd.DataFrame(y_train)
        y_test = pd.DataFrame(y_test)
        X_test.columns = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
            'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
            'pH', 'sulphates', 'alcohol']

        X_train.columns = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
            'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
            'pH', 'sulphates', 'alcohol']
        y_train.columns = ['quality']
        y_test.columns = ['quality']


        y_train.to_csv(os.path.join(self.config.root_dir, "y_train.csv"),index = False)
        X_train.to_csv(os.path.join(self.config.root_dir, "X_train.csv"),index = False)
        y_test.to_csv(os.path.join(self.config.root_dir, "y_test.csv"),index = False)
        X_test.to_csv(os.path.join(self.config.root_dir, "X_test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(y_train.shape)
        logger.info(X_train.shape)
        logger.info(y_test.shape)
        logger.info(X_test.shape)

        print(y_train.shape)
        print(X_train.shape)
        print(y_test.shape)
        print(X_test.shape)
        
