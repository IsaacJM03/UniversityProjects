# Sensor Data Visualization Project

## Overview
The Sensor Data Visualization project is designed to collect, process, and visualize sensor data from an MQTT broker. This project aims to provide an easy-to-use interface for monitoring environmental conditions through various visualizations.

## Project Structure
```
sensor-data-visualization
├── src
│   ├── mqtt_client.py       # Handles MQTT client setup and connection
│   ├── collector.py          # Collects sensor data and stores it
│   ├── exporter.py           # Exports collected data to CSV format
│   ├── visualizer.py         # Visualizes sensor data using plots and charts
│   ├── config.py             # Contains configuration settings
│   └── utils
│       └── __init__.py      # Utility functions for the project
├── data
│   ├── raw                   # Directory for raw sensor data
│   └── processed             # Directory for processed sensor data
├── notebooks
│   └── analysis.ipynb       # Jupyter notebook for data analysis and visualization
├── scripts
│   ├── start_collector.sh    # Shell script to start data collection
│   └── export_csv.py         # Script to export data to CSV
├── requirements.txt          # Lists project dependencies
├── .gitignore                # Specifies files to ignore in Git
└── README.md                 # Project documentation
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd sensor-data-visualization
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
- To start collecting sensor data, run the following command:
  ```
  ./scripts/start_collector.sh
  ```

- To export the collected data to CSV format, execute:
  ```
  python scripts/export_csv.py
  ```

- For data analysis and visualization, open the Jupyter notebook:
  ```
  jupyter notebook notebooks/analysis.ipynb
  ```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.