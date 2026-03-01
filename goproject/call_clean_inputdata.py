
import pandas as pd                         
from pathlib import Path  
import logging
import numpy as np 
from clean_inputdata import CleanMydata

def setup_logging(log_file):
    
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    
def main():
    
    base_dir = Path(__file__).resolve().parent
    log_file = base_dir/"app.log"
    setup_logging(log_file)
    
    logger = logging.getLogger(__name__)
    logger.info("Application started.")

    csv_file = base_dir / "weather.csv"
    
    if not csv_file.exists:
        logger.error(f"{csv_file} not found")
        raise FileNotFoundError(f"{csv_file} not found")
    logger.info("CSV file located ...")
        
    try:
        df = pd.read_csv(csv_file)
        logger.info("CSV loaded successfully.")
    except Exception:
        logger.exception("Failed to load CSV file.")
        raise

    cleaned_df = (
        CleanMydata(df)
        .clean_cols()
        .final_results()
    )

    logger.info("Data cleaning completed.")
    print(cleaned_df.head())
