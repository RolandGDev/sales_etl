import logging
from extract import extract
from load import load
from transform import transform

# log config
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler("./logs/pipeline.log"),
                              logging.StreamHandler()]
                           )
logger = logging.getLogger(__name__)

#orquestrador
def pipeline():
    logger.info("Starting pipeline")

    #1. extract
    df = extract('data/raw/orders.csv')
    logger.info(f"{len(df)} rows extracted")

    #2. transform
    df = transform(df)
    logger.info(f"{len(df)} rows transformed")

    #3. load
    load(df)
    logger.info(f"{len(df)} rows loaded")

if __name__ == "__main__":
    pipeline()