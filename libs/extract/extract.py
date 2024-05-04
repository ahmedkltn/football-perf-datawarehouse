from loguru import logger
import pandas as pd

def csv_into_df(file_path) -> pd.DataFrame:  
    logger.debug(f"Transforming {file_path} into csv")
    return pd.read_csv(file_path)


def extractor(file_path : str) :
    logger.debug(f"Starting EXTRACT process for csv file : {file_path}")
    df = csv_into_df(file_path)