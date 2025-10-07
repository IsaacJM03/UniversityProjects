#!/bin/bash


echo "🚀 Starting Real-time IoT Dashboard..."

# Process any new raw data
python3 scripts/process_raw.py

# Launch dashboard with auto-reload
streamlit run src/dashboard.py --server.runOnSave true --server.port 8501

echo "Dashboard available at: http://localhost:8501"