from constants import *
from text_cleaning import *
from utils import * 


def main():
    
    path = f"{PATH_TO_DATA}/dark_180.csv"
    clean_file_descriptions(path)

    path = f"{PATH_TO_DATA}/funny_169.csv"
    clean_file_descriptions(path)

    path = f"{PATH_TO_DATA}/inspirational_191.csv"
    clean_file_descriptions(path)

    path = f"{PATH_TO_DATA}/sad_140.csv"
    clean_file_descriptions(path)


def clean_file_descriptions(path):

    df = read_df_from_csv_file(path)    
    clean_column(df)
    
    output_path = f"{path.split('.')[0]}_clean.csv"
    save_df_to_csv(df, output_path, True)


def clean_column(df, column="description"):
    for i, description in enumerate(df[column]):
        d2 = remove_links_in_text(description)
        d3 = remove_breaklines_in_text(d2)        
        d4 = remove_quotes_in_text(d3)
        update_df_value(df, i, column, d4)
    return df


if __name__ == "__main__":

    main()