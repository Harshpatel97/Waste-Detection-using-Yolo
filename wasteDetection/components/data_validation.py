import os
import sys
import shutil

from wasteDetection.logger import logging
from wasteDetection.exception import AppException
from wasteDetection.entity.config_entity import DataValidationConfig
from wasteDetection.entity.artifacts_entity import (DataValidationArtifact, DataIngestionArtifact)



class DataValidation:
    def __init__(self,
                 data_ingestion_artifact: DataIngestionArtifact,
                 data_validation_config:DataValidationConfig):
        
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
        except Exception as e:
            raise AppException(e, sys)
        
    def validate_all_files_exist(self):
        
        try:
            validation_status = False
            all_files = os.listdir(self.data_ingestion_artifact.feature_store_path)
            
            for files in all_files:
                if files not in self.data_validation_config.required_files_list:
                    validation_status = False
                    os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)
                    with open(self.data_validation_config.validation_status_file_dir, 'w') as f:
                        f.write(f"Validation Status: {validation_status}")
                        
                else:
                    validation_status = True
                    os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)
                    with open(self.data_validation_config.validation_status_file_dir, 'w')as f:
                        f.write(f"Validation Status: {validation_status}")
            
            return validation_status
            
        except Exception as e:
            raise AppException(e, sys)
        
    
    def initiate_data_validation(self):
        logging.info("Entered initate_data_validation method from DataValidation class")
        try:
            status = self.validate_all_files_exist()
            data_validation_artifact = DataValidationArtifact(validation_status=status)
            
            logging.info("Exited the intiate_data_validation method from DataValidation class")
            logging.info(f"Data Validation artifact: {data_validation_artifact}")
            
            if status:
                shutil.copy(self.data_ingestion_artifact.data_zip_file_path, os.getcwd())
                
            return data_validation_artifact
            
        except Exception as e:
            raise AppException(e, sys)