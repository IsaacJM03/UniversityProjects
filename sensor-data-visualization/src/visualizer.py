import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from matplotlib.dates import DateFormatter, HourLocator, MinuteLocator
import matplotlib.dates as mdates

def load_data(file_path):
    df = pd.read_csv(file_path)
    # Convert timestamp to datetime if not already
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

def visualize_temperature(data):
    plt.figure(figsize=(14, 6))
    plt.plot(data['timestamp'], data['temperature'], marker='o', linewidth=2, markersize=4)
    plt.title('Temperature Over Time', fontsize=16)
    plt.xlabel('Time', fontsize=12)
    plt.ylabel('Temperature (°C)', fontsize=12)
    
    # Format x-axis
    plt.gca().xaxis.set_major_locator(HourLocator(interval=1))  # Every hour
    plt.gca().xaxis.set_minor_locator(MinuteLocator(interval=30))  # Every 30 minutes
    plt.gca().xaxis.set_major_formatter(DateFormatter('%H:%M'))
    
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def visualize_humidity(data):
    plt.figure(figsize=(14, 6))
    plt.plot(data['timestamp'], data['humidity'], marker='o', color='orange', linewidth=2, markersize=4)
    plt.title('Humidity Over Time', fontsize=16)
    plt.xlabel('Time', fontsize=12)
    plt.ylabel('Humidity (%)', fontsize=12)
    
    # Format x-axis
    plt.gca().xaxis.set_major_locator(HourLocator(interval=1))
    plt.gca().xaxis.set_minor_locator(MinuteLocator(interval=30))
    plt.gca().xaxis.set_major_formatter(DateFormatter('%H:%M'))
    
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def visualize_motion(data):
    plt.figure(figsize=(14, 6))
    
    # For motion, use scatter plot instead of bar plot to avoid overcrowding
    plt.scatter(data['timestamp'], data['motion_counts'], color='green', alpha=0.7, s=50)
    plt.title('Motion Counts Over Time', fontsize=16)
    plt.xlabel('Time', fontsize=12)
    plt.ylabel('Motion Counts', fontsize=12)
    
    # Format x-axis
    plt.gca().xaxis.set_major_locator(HourLocator(interval=1))
    plt.gca().xaxis.set_minor_locator(MinuteLocator(interval=30))
    plt.gca().xaxis.set_major_formatter(DateFormatter('%H:%M'))
    
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def visualize_motion_state(data):
    """Visualize motion state as a timeline"""
    if 'motion_state' in data.columns:
        plt.figure(figsize=(14, 4))
        
        # Create binary values for motion state
        motion_binary = data['motion_state'].map({'Activity': 1, 'No Activity': 0}).fillna(0)
        
        plt.fill_between(data['timestamp'], motion_binary, alpha=0.7, color='red', label='Activity Detected')
        plt.title('Motion Activity Timeline', fontsize=16)
        plt.xlabel('Time', fontsize=12)
        plt.ylabel('Activity', fontsize=12)
        plt.yticks([0, 1], ['No Activity', 'Activity'])
        
        # Format x-axis
        plt.gca().xaxis.set_major_locator(HourLocator(interval=1))
        plt.gca().xaxis.set_minor_locator(MinuteLocator(interval=30))
        plt.gca().xaxis.set_major_formatter(DateFormatter('%H:%M'))
        
        plt.xticks(rotation=45)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()

def main():
    data_dir = './data/processed'
    file_name = 'sensor_data.csv'
    file_path = os.path.join(data_dir, file_name)

    if os.path.exists(file_path):
        data = load_data(file_path)
        print(f"Loaded {len(data)} records from {data['timestamp'].min()} to {data['timestamp'].max()}")
        
        visualize_temperature(data)
        visualize_humidity(data)
        visualize_motion(data)
        visualize_motion_state(data)
    else:
        print(f"Data file {file_path} does not exist.")

if __name__ == "__main__":
    main()