#!/bin/bash

# Start the MQTT data collector
python3.12 ../src/collector.py &

# Optionally, you can add a command to log the output
# For example, redirecting output to a log file
python3.12 ../src/collector.py >> ../data/logs/collector.log 2>&1 &

echo "Data collector started."