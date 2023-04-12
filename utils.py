import pandas as pd

def read_df_from_csv_file(path_to_file, index_col=0):
    return pd.read_csv(path_to_file, index_col=index_col)

def save_df_to_csv(df, output_path, index=False):
    df.to_csv(output_path,index=index)
    
def update_df_value(df, row, column, value):
    df.at[row,column]=value
