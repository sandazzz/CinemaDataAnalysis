#filter_columns.py
import pandas as pd

def filter_csv_columns(file_path, columns, sep=",", encoding="utf-8"):
    df = pd.read_csv(file_path, sep=sep, encoding=encoding)
    missing_columns = [col for col in columns if col not in df.columns]
    
    if missing_columns:
        print(f"Colonnes manquantes : {missing_columns}")
        return pd.DataFrame()
    
    return df[columns]
