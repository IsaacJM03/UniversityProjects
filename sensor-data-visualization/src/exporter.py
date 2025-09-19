import pandas as pd
import os
import json

def export_to_csv(json_file_path, csv_file_path):
    if not os.path.exists(json_file_path):
        print(f"Error: The file {json_file_path} does not exist.")
        return

    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    # Assuming the JSON data is a list of records
    df = pd.DataFrame(data)

    # Export to CSV
    df.to_csv(csv_file_path, index=False)
    print(f"Data exported to {csv_file_path} successfully.")

if __name__ == "__main__":
    json_file_path = "../data/raw/message_history.json"  # Path to the JSON file
    csv_file_path = "../data/processed/sensor_data.csv"  # Path to save the CSV file
    export_to_csv(json_file_path, csv_file_path)