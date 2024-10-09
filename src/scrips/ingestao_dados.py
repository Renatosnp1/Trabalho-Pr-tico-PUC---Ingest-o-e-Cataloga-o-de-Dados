import pandas as pd

def ingestao_csv_para_parquet(input_path, output_path):
    df = pd.read_csv(input_path)
    df.to_parquet(output_path, index=False)
