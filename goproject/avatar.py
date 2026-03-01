import numpy as np            
import pandas as pd              
import seaborn as sns               
import matplotlib.pyplot as plt  
from pathlib import Path 
import os              

# file location 
try: 
    
    parent_folder = Path(__file__).resolve().parent
    fileName = parent_folder/"mydrone_Data.csv"
    print(fileName)
    
except FileNotFoundError as e:
    print(f"File Note Found {e}")