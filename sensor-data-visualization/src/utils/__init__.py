def save_to_csv(data, filename):
    import pandas as pd

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

def load_from_csv(filename):
    import pandas as pd

    return pd.read_csv(filename)

def preprocess_data(data):
    # Implement any necessary preprocessing steps here
    return data

def visualize_data(data):
    import matplotlib.pyplot as plt
    import seaborn as sns

    # Example visualization
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=data, x='timestamp', y='temperature', label='Temperature')
    sns.lineplot(data=data, x='timestamp', y='humidity', label='Humidity')
    plt.title('Temperature and Humidity Over Time')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.legend()
    plt.show()