import pathlib
from pathlib import Path

base_dir = Path(__file__).resolve().parent

try:
    
    csv_file = base_dir/"weather.csv"
    print("find found .. 😀🍓")
    
except FileNotFoundError as e:
    print(f"Location Error {e}")