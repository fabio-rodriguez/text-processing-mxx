import pandas as pd

def df_from_csv_file(path_to_file, index_col=0):
    return pd.read_csv(path_to_file, index_col=index_col)