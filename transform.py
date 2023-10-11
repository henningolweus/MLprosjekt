import os
import pandas as pd

def parquet_to_csv(directory):
    """Convert all parquet files in the specified directory to CSV format."""
    
    # Create the 'data_csv' folder if it doesn't exist
    csv_folder = os.path.join(directory, 'data_csv')
    if not os.path.exists(csv_folder):
        os.makedirs(csv_folder)

    # Loop through A, B, C folders
    for subfolder in ['A', 'B', 'C']:
        subfolder_path = os.path.join(directory, subfolder)
        
        # Create corresponding subfolder in 'data_csv'
        csv_subfolder_path = os.path.join(csv_folder, subfolder)
        if not os.path.exists(csv_subfolder_path):
            os.makedirs(csv_subfolder_path)
        
        for root, _, files in os.walk(subfolder_path):
            for file in files:
                if file.endswith(".parquet"):
                    # Construct the full file path
                    parquet_file_path = os.path.join(root, file)
                    
                    # Name and path for the CSV file in the 'data_csv' subfolder
                    csv_file_name = os.path.splitext(file)[0] + ".csv"
                    csv_file_path = os.path.join(csv_subfolder_path, csv_file_name)
                    
                    # Read the parquet file and save as CSV
                    df = pd.read_parquet(parquet_file_path)
                    df.to_csv(csv_file_path, index=False)
                    print(f"Converted {parquet_file_path} to {csv_file_path}")

if __name__ == "__main__":
    directory = os.getcwd()  # Get the current directory
    parquet_to_csv(directory)
