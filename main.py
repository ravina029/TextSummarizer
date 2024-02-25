from textsummarizer.pipeline.stage_01_dataingestion import DataIngestionTrainingPipeline
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