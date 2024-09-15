from src.logger import logging
from src.exceptions import CustomException
import os
import sys
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
from src.components.model_training import ModelTrainerConfig
from src.components.model_training import ModelTrainer



@dataclass
class DataIngestionConfig:
    TRAIN_DATA_PATH: str = os.path.join("artifacts", "train.csv")
    TEST_DATA_PATH: str = os.path.join("artifacts", "test.csv")
    RAW_DATA_PATH: str = os.path.join("artifacts", "data.csv")


class DataIngestion:
    def __init__(self):
        self.Ingestion_config = DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv("/Users/virtue/Desktop/ml_project/src/notebooks/data/stud.csv")
            logging.info("Dataset read correctly into DataFrame")
            os.makedirs(os.path.dirname(self.Ingestion_config.TRAIN_DATA_PATH), exist_ok=True)
            os.makedirs(os.path.dirname(self.Ingestion_config.TEST_DATA_PATH), exist_ok=True)
            df.to_csv(self.Ingestion_config.RAW_DATA_PATH, index=False, header=True)
            
            logging.info("Train test split Initiating!!")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.Ingestion_config.TRAIN_DATA_PATH, index=False, header=True)
            test_set.to_csv(self.Ingestion_config.TEST_DATA_PATH, index=False, header=True)
            
            logging.info("Ingestion of the data is completed")
            
            return (
                self.Ingestion_config.TRAIN_DATA_PATH,
                self.Ingestion_config.TEST_DATA_PATH
            )

        except Exception as e:
            raise CustomException(e, sys)


if __name__=="__main__":
    obj=DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data,test_data)
    
    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))














































































