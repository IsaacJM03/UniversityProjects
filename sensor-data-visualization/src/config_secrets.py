import os

# MQTT Broker Configuration
BROKER_URL = "eu1.cloud.thethings.network"
BROKER_PORT = 1883
USERNAME = "bd-test-app2@ttn"
PASSWORD = "NNSXS.NGFSXX4UXDX55XRIDQZS6LPR4OJXKIIGSZS56CQ.6O4WUAUHFUAHSTEYRWJX6DDO7TL2IBLC7EV2LS4EHWZOOEPCEUOA"
DEVICE_ID = "lht65n-01-temp-humidity-sensor"

# API Configuration
API_KEY = "NNSXS.NGFSXX4UXDX55XRIDQZS6LPR4OJXKIIGSZS56CQ.6O4WUAUHFUAHSTEYRWJX6DDO7TL2IBLC7EV2LS4EHWZOOEPCEUOA"
APP_ID = "group-h-eve-application"

# Data Storage Paths
RAW_DATA_PATH = os.path.join("data", "raw")
PROCESSED_DATA_PATH = os.path.join("data", "processed")

# Historical Data Fetching Parameters
HISTORICAL_DATA_LAST = "12h"  # Fetch messages from the last 12 hours
