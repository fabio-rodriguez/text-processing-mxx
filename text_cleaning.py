import pandas as pd

from utils import * 
from constants import *

def testing():
    path = f"{PATH_TO_DATA}/dark_180.csv"
    df = df_from_csv_file(path)    
    print(df)
    print(df.shape)
    print(df.columns)



if __name__ == "__main__":

    testing()