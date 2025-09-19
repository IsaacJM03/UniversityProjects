import paho.mqtt.client as mqtt
import json
import pandas as pd
import os
import time
from datetime import datetime
from pathlib import Path

# Configuration
from config import BROKER_URL, BROKER_PORT, USERNAME, PASSWORD, DEVICE_ID, RAW_DATA_PATH

# Data storage
data_storage = []

# Resolve project-rooted output dir and CSV path
BASE_DIR = Path(__file__).resolve().parent.parent  # repo root
OUTPUT_DIR = BASE_DIR.joinpath(RAW_DATA_PATH)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
CSV_PATH = OUTPUT_DIR.joinpath("sensor_data.csv")

def _extract_payload_dict(raw_payload_str):
    """
    Return a dict containing decoded payload fields if possible.
    Handles common TTN v3 shapes: top-level decoded_payload or uplink_message.decoded_payload,
    and payload_fields. Falls back to top-level JSON.
    """
    try:
        j = json.loads(raw_payload_str)
    except Exception:
        return {}
    # TTN v3 common places for decoded data
    uplink = j.get("uplink_message") or {}
    decoded = uplink.get("decoded_payload") or uplink.get("payload_fields") or j.get("decoded_payload") or j.get("payload_fields")
    if isinstance(decoded, dict):
        return decoded
    # fallback: some messages put fields at top-level
    if isinstance(j, dict):
        return j
    return {}

def _pick_one(d, candidates):
    for k in candidates:
        if k in d:
            return d[k]
    return None

# Callback: When a message is received
def on_message(client, userdata, msg):
    try:
        payload_dict = _extract_payload_dict(msg.payload.decode())
        sensor_data = {
            "received_at": datetime.utcnow().isoformat(),
            # try multiple possible key names for robustness
            "battery_voltage": _pick_one(payload_dict, ["field1", "battery", "bat", "battery_voltage"]),
            "humidity": _pick_one(payload_dict, ["field3", "humidity", "hum"]),
            "motion_counts": _pick_one(payload_dict, ["field4", "motion_counts", "motion"]),
            "temperature": _pick_one(payload_dict, ["field5", "temperature", "temp"]),
            "_raw_payload": json.dumps(payload_dict, ensure_ascii=False)  # store as JSON string for CSV
        }
        data_storage.append(sensor_data)

        # Append to rolling CSV so data is visible immediately
        df = pd.DataFrame([sensor_data])
        write_header = not CSV_PATH.exists()
        df.to_csv(CSV_PATH, mode='a', header=write_header, index=False)
        print(f"Collected: {sensor_data['received_at']} temp={sensor_data['temperature']} hum={sensor_data['humidity']}")
    except Exception as e:
        print("Error processing message:", e)

# Set up MQTT client
def start_collector():
    client = mqtt.Client()
    client.username_pw_set(USERNAME, PASSWORD)
    client.on_message = on_message

    client.connect(BROKER_URL, BROKER_PORT, 60)
    client.subscribe(f"v3/{USERNAME}/devices/{DEVICE_ID}/up")

    try:
        # run forever; KeyboardInterrupt triggers graceful stop
        client.loop_forever()
    except KeyboardInterrupt:
        print("Stopping collector, saving snapshot...")
        # also save a timestamped snapshot in RAW_DATA_PATH
        save_data_to_csv()

# Save collected data to CSV
def save_data_to_csv():
    if data_storage:
        df = pd.DataFrame(data_storage)
        # ensure output dir exists (already created at module import, but safe)
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        csv_file_path = OUTPUT_DIR.joinpath(f"sensor_data_{timestamp}.csv")
        df.to_csv(csv_file_path, index=False)
        print(f"Data saved to {csv_file_path}")
    else:
        print("No data collected; nothing to save.")

if __name__ == "__main__":
    start_collector()