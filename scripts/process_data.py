import pandas as pd

def remove_duplicates(input_path, output_path):
    df = pd.read_csv(input_path)
    df_cleaned = df.drop_duplicates()
    df_cleaned.to_csv(output_path, index=False)

if __name__ == "__main__":
    remove_duplicates("data/raw_dataset.csv", "data/processed_dataset.csv")
