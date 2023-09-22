import sys
from wasteDetection.logger import logging
from wasteDetection.exception import AppException
from wasteDetection.components.data_ingestion import DataIngestion

from wasteDetection.entity.config_entity import DataIngestionConfig
from wasteDetection.entity.artifacts_entity import DataIngestionArtifact



class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        
    
    def start_data_ingestion(self):
        try:
            logging.info("Entered start_data_ingestion_method of Train class")
            logging.info("Getting the data from url")
            
            data_ingestion = DataIngestion(
                data_ingestion_config = self.data_ingestion_config
            )
            
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got the data from URL")
            logging.info("Exited the start_data_ingestion_method of Train Class")
            
            return data_ingestion_artifact
            
        except Exception as e:
            raise AppException(e, sys)
        
        
    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            
        except Exception as e:
            raise AppException(e, sys)