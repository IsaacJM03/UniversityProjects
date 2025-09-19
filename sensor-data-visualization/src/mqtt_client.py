import paho.mqtt.client as mqtt
import time
from config import BROKER_URL, BROKER_PORT, USERNAME, PASSWORD, DEVICE_ID
import collector

# MQTT Client setup
client = mqtt.Client()
client.username_pw_set(USERNAME, PASSWORD)

# Callback: When connected to broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker!")
        topic = f"v3/{USERNAME}/devices/{DEVICE_ID}/up"
        client.subscribe(topic)
        print(f"Subscribed to {topic}")
    else:
        print(f"Failed to connect, return code {rc}")
        time.sleep(5 * 60)  # Retry delay if needed

# Use the collector's on_message to keep parsing consistent
client.on_connect = on_connect
client.on_message = collector.on_message

# Connect to broker and start loop
def start_mqtt_client():
    client.connect(BROKER_URL, BROKER_PORT, 60)
    try:
        client.loop_forever()
    except KeyboardInterrupt:
        print("MQTT client stopped by user.")

if __name__ == "__main__":
    start_mqtt_client()