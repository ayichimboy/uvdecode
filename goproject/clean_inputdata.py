# Import Libraries
                
import pandas as pd                         
from pathlib import Path  
import logging
import numpy as np    

logger = logging.getLogger(__name__)

class CleanMydata():
     
    def __init__(self, input_data):
        self.input_data = input_data
        logger.info("CleanMydata Initialized ...")
        
    def clean_cols(self):
        logger.info("Claning Column Names  ...")
        self.input_data.columns = [col[0] for col in self.input_data.columns.str.lower().str.strip().str.split()]
        self.input_data = self.input_data.iloc[:,1:5]
        return self
    
    def convert_timecol(self):
        logger.info("Convert Column to Date-Time ...")
        self.input_data["date-time"] = pd.to_datetime(self.input_data["date-time"])
        return self
    
    def add_datacol(self):
        logger.info("Create Multiple New Columns ...")
        self.input_data["month"] = self.input_data["date-time"].dt.month
        self.input_data['day'] = self.input_data["date-time"].dt.day
        self.input_data['year'] = self.input_data["date-time"].dt.year
        self.input_data['minute'] = self.input_data["date-time"].dt.minute
        self.input_data['hour'] = self.input_data["date-time"].dt.hour
        self.input_data['second'] = self.input_data["date-time"].dt.second
        return self
        
    def final_results(self):
        return self.convert_timecol().add_datacol()
                   
