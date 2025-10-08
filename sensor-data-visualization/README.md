# Smart IoT Sensor Data Visualization Dashboard

## Overview
A comprehensive real-time IoT sensor monitoring system that collects environmental data via MQTT, processes it with machine learning analytics, and presents insights through an interactive Streamlit dashboard. This project provides smart home automation insights, environmental comfort analysis, and predictive analytics for IoT sensor networks.

## 🌟 Key Features
- **Real-time Data Collection** - MQTT-based sensor data ingestion with EAT timezone support
- **Smart Analytics** - ML-powered occupancy prediction, anomaly detection, and behavioral insights
- **Interactive Dashboard** - Live Streamlit web interface with auto-refresh capabilities
- **Environmental Intelligence** - Comfort scoring, energy efficiency analysis, and optimization recommendations
- **Predictive Insights** - Next-hour forecasting and trend analysis
- **Automated Processing** - File watching and real-time data processing pipeline

## 🏗️ Project Structure
```
sensor-data-visualization/
├── src/
│   ├── collector.py          # MQTT data collector with EAT timezone handling
│   ├── dashboard.py          # Main Streamlit dashboard with smart analytics
│   ├── ml_models.py          # Machine learning models for predictions
│   ├── live_processor.py     # File watcher for real-time data processing
│   ├── config.py             # Configuration settings and MQTT credentials
│   └── utils/
│       └── __init__.py       # Utility functions
├── data/
│   ├── raw/
│   │   └── sensor_data.csv   # Raw MQTT sensor data
│   ├── processed/
│   │   └── sensor_data.csv   # Processed data with ML features
│   └── logs/                 # System logs
├── models/                   # Saved ML models
├── scripts/
│   ├── process_raw.py        # Data processing with timezone conversion
│   ├── start_collector.sh    # Data collector launcher
│   ├── run_dashboard.sh      # Dashboard launcher
│   └── start_live_system.sh  # Complete system launcher
├── notebooks/
│   └── analysis.ipynb        # Data analysis and exploration
├── requirements.txt          # Python dependencies
├── .gitignore               # Git ignore rules
└── README.md                # This documentation
```

## 📊 Dashboard Features

### 🏠 Occupancy Patterns
- Peak activity hours identification
- Weekly routine analysis
- Motion intensity insights
- Activity timeline visualization

### 🌡️ Environmental Analysis
- Temperature/humidity comfort zones
- Energy efficiency scoring
- Environmental preferences detection
- Comfort timeline with thresholds

### 🔮 Smart Predictions
- Next-hour temperature/humidity forecasts
- Activity probability predictions
- Trend analysis with visual indicators
- Multi-parameter trend visualization

### 🧠 Behavioral Insights
- Daily routine consistency scoring
- Preferred environmental conditions
- Activity period breakdowns
- Schedule predictability analysis

### 💡 Smart Recommendations
- Energy optimization suggestions
- Comfort improvement actions
- Automation opportunities
- Maintenance alerts and reminders

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.8+
- MQTT broker access
- Streamlit
- Required sensor hardware

### 1. Clone Repository
```bash
git clone <repository-url>
cd sensor-data-visualization
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure MQTT Settings
Edit `src/config.py` with your MQTT broker details:
```python
BROKER_URL = "your-mqtt-broker.com"
BROKER_PORT = 1883
USERNAME = "your-username"
PASSWORD = "your-password"
DEVICE_ID = "your-device-id"
```

### 4. Create Data Directories
```bash
mkdir -p data/{raw,processed,logs}
mkdir -p models
```

## 🚀 Usage

### Option 1: Complete Live System (Recommended)
Start all components with real-time processing:
```bash
chmod +x scripts/start_live_system.sh
./scripts/start_live_system.sh
```

### Option 2: Individual Components

#### Start Data Collector
```bash
python3 src/collector.py
```

#### Process Raw Data
```bash
python3 scripts/process_raw.py
```

#### Launch Dashboard
```bash
streamlit run src/dashboard.py --server.port 8501
```

#### Start Live File Processor
```bash
python3 src/live_processor.py
```

### Option 3: Quick Dashboard Launch
```bash
chmod +x scripts/run_dashboard.sh
./scripts/run_dashboard.sh
```

## 📱 Dashboard Access
Once running, access the dashboard at:
- **URL**: http://localhost:8501
- **Features**: Auto-refresh, live updates, interactive analytics
- **Controls**: Sidebar for refresh settings and manual controls

## 🛠️ Configuration Options

### Auto-Refresh Settings
- **Enable/Disable**: Checkbox in sidebar
- **Intervals**: 5, 10, 15, 30, 60 seconds
- **Manual Refresh**: Instant data reload
- **Cache Control**: Clear cached data

### Data Processing
- **Timezone**: Automatic EAT (East Africa Time) conversion
- **Real-time**: File watching for instant processing
- **ML Features**: Automated feature engineering
- **Anomaly Detection**: Isolation Forest algorithm

## 📈 Data Flow

```
Sensor → MQTT → collector.py → raw CSV → live_processor.py → 
process_raw.py → processed CSV → dashboard.py → Web Interface
```

## 🔧 Troubleshooting

### Common Issues
1. **"Data is stale" message**: Check collector is running and MQTT connection
2. **Dashboard not refreshing**: Enable auto-refresh in sidebar
3. **No data found**: Ensure `data/processed/sensor_data.csv` exists
4. **Port already in use**: Kill existing processes or use different port

### Log Files
Check logs in `data/logs/` for detailed error information:
- `collector.log` - Data collection issues
- `processor.log` - Data processing errors

### Manual Data Processing
If automatic processing fails:
```bash
python3 scripts/process_raw.py
```

## 🤖 Machine Learning Features

### Anomaly Detection
- **Algorithm**: Isolation Forest
- **Features**: Temperature, humidity, motion, battery
- **Threshold**: 10% contamination rate

### Occupancy Prediction
- **Algorithm**: Random Forest Classifier
- **Features**: Time patterns, environmental conditions
- **Output**: Probability scores and activity forecasts

### Environmental Analysis
- **Comfort Scoring**: Temperature/humidity optimization
- **Efficiency Analysis**: Energy usage patterns
- **Behavioral Insights**: Routine detection and preferences

## 📊 Supported Sensor Data

### Required Fields
- `timestamp` - Reading time (converted to EAT)
- `temperature` - Temperature in Celsius
- `humidity` - Relative humidity percentage
- `motion_counts` - Motion sensor readings
- `motion_state` - Activity/No Activity
- `battery_voltage` - Sensor battery level

### Data Formats
- **Input**: MQTT JSON payloads
- **Storage**: CSV files with timezone handling
- **Processing**: Pandas DataFrames with ML features

## 🔮 Future Enhancements
- [ ] Multi-sensor support
- [ ] Mobile-responsive design
- [ ] Email/SMS alerts
- [ ] Historical data export
- [ ] Advanced ML models
- [ ] Integration with smart home platforms

## 🤝 Contributing
1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments
- Streamlit for the excellent dashboard framework
- Plotly for interactive visualizations
- scikit-learn for machine learning capabilities
- MQTT protocol for IoT data transmission

## 📞 Support
For questions or issues:
1. Check troubleshooting section above
2. Review log files in `data/logs/`
3. Open an issue on GitHub
4. Check dashboard status indicators for system health

---
**Dashboard URL**: http://localhost:8501  
**Live System**: Auto-refreshing with real-time insights  
**Last Updated**: October 2024