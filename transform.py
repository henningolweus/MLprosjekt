import os
import pandas as pd

def parquet_to_csv(directory):
    """Convert all parquet files in the specified directory to CSV format."""
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".parquet"):
                # Construct the full file path
                parquet_file_path = os.path.join(root, file)
                csv_file_path = os.path.splitext(parquet_file_path)[0] + ".csv"
                
                # Read the parquet file and save as CSV
                df = pd.read_parquet(parquet_file_path)
                df.to_csv(csv_file_path, index=False)
                print(f"Converted {parquet_file_path} to {csv_file_path}")

if __name__ == "__main__":
    directory = os.getcwd()  # Get the current directory
    parquet_to_csv(directory)
