from textsummarizer.pipeline.stage_01_dataingestion import DataIngestionTrainingPipeline
from textsummarizer.pipeline.stage_02_datavalidation import DataValidationPipeline
from textsummarizer.pipeline.stage_03_datatransformation import DataTransformationPipeline
from textsummarizer.logging import logger


STAGE_NAME="Data ingestion stage"

try:
    logger.info(f">>>>>>> stage{STAGE_NAME} started <<<<<<<<")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\n x=============x")
except Exception as e:
         logger.exception(e)
         raise e




STAGE_NAME="Data validation stage"

try:
    logger.info(f">>>>>>> stage{STAGE_NAME} started <<<<<<<<")
    data_validation=DataValidationPipeline()
    data_validation.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\n x=============x")
except Exception as e:
         logger.exception(e)
         raise e


STAGE_NAME="Data transformation stage"

try:
    logger.info(f">>>>>>> stage{STAGE_NAME} started <<<<<<<<")
    data_transformation=DataTransformationPipeline()
    data_transformation.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\n x=============x")
except Exception as e:
         logger.exception(e)
         raise e