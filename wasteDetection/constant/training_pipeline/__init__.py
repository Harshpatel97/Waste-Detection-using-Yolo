ARTIFACTS_DIR: str = 'artifacts'

""" Data Ingestion 
"""

DATA_INGESTION_DIR_NAME: str = 'data_ingestion'

DATA_INGESTION_FEATURE_STORE_DIR: str = 'feature_store'

DATA_DOWNLOAD_URL: str = "https://drive.google.com/file/d/1ECfl3dtYyfivY8kYPq7RHUBTjC-2vf61/view?usp=share_link"


""" Data Validation
"""

DATA_VALIDATION_DIR_NAME:str = 'data_validation'

DATA_VALIDATION_STATUS_FILE: str = 'status.txt'

DATA_VALIDATION_ALL_REQUIRED_FILES:str = ["train", "valid", 'data.yaml']


""" Model Trainer
"""

MODEL_TRAINER_DIR_NAME:str = 'model_trainer'

MODEL_TRAINER_PRETRAINED_WEIGHT_NAME:str = 'yolov5s.pt'

MODEL_TRAINER_NO_EPOCHS: int= 1

MODEL_TRAINER_BATCH_SIZE: int = 16