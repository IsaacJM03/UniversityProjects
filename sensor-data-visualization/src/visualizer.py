import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def load_data(file_path):
    return pd.read_csv(file_path)

def visualize_temperature(data):
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=data, x='timestamp', y='temperature', marker='o')
    plt.title('Temperature Over Time')
    plt.xlabel('Time')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def visualize_humidity(data):
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=data, x='timestamp', y='humidity', marker='o', color='orange')
    plt.title('Humidity Over Time')
    plt.xlabel('Time')
    plt.ylabel('Humidity (%)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def visualize_motion(data):
    plt.figure(figsize=(12, 6))
    sns.barplot(data=data, x='timestamp', y='motion_counts', color='green')
    plt.title('Motion Counts Over Time')
    plt.xlabel('Time')
    plt.ylabel('Motion Counts')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    data_dir = '../data/processed'
    file_name = 'sensor_data.csv'  # Adjust the file name as necessary
    file_path = os.path.join(data_dir, file_name)

    if os.path.exists(file_path):
        data = load_data(file_path)
        visualize_temperature(data)
        visualize_humidity(data)
        visualize_motion(data)
    else:
        print(f"Data file {file_path} does not exist.")

if __name__ == "__main__":
    main()