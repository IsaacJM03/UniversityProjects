import pandas as pd
import json
import os

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
    json_file_path = "../data/processed/message_history.json"  # Adjust path as necessary
    csv_file_path = "../data/processed/sensor_data.csv"  # Adjust path as necessary
    export_to_csv(json_file_path, csv_file_path)