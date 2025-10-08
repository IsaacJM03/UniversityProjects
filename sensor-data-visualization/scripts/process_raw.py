from pathlib import Path
import pandas as pd
import json
import sys
import re
import pytz  # Add this import

BASE = Path(__file__).resolve().parent.parent
RAW_CSV = BASE / "data" / "raw" / "sensor_data.csv"
OUT_DIR = BASE / "data" / "processed"
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_CSV = OUT_DIR / "sensor_data.csv"

# Set timezone to EAT (East Africa Time)
EAT = pytz.timezone('Africa/Nairobi')
UTC = pytz.timezone('UTC')

if not RAW_CSV.exists():
    print(f"Raw file not found: {RAW_CSV}")
    sys.exit(1)

# Read raw file as text and parse manually since JSON contains commas
data_rows = []
with open(RAW_CSV, 'r') as f:
    for line_num, line in enumerate(f, 1):
        line = line.strip()
        if not line:
            continue
        
        # Use regex to split: timestamp, 4 numbers, then everything else as JSON
        # Pattern: timestamp, num, num, num, num, {json...}
        pattern = r'^([^,]+),\s*([^,]+),\s*([^,]+),\s*([^,]+),\s*([^,]+),\s*(.+)$'
        match = re.match(pattern, line)
        
        if match:
            timestamp, battery, humidity, motion, temp, json_part = match.groups()
            data_rows.append({
                'received_at': timestamp.strip(),
                'battery_voltage': battery.strip(),
                'humidity': humidity.strip(), 
                'motion_counts': motion.strip(),
                'temperature': temp.strip(),
                '_raw_payload': json_part.strip()
            })
        else:
            print(f"Could not parse line {line_num}: {line[:50]}...")

if not data_rows:
    print("No valid data rows found")
    sys.exit(1)

df = pd.DataFrame(data_rows)

# Clean and convert numeric columns
for c in ["battery_voltage", "humidity", "motion_counts", "temperature"]:
    df[c] = pd.to_numeric(df[c], errors="coerce")

# Parse timestamp and convert to EAT
def process_timestamps(df):
    """Convert timestamps from UTC to EAT"""
    df["timestamp"] = pd.to_datetime(df["received_at"], errors="coerce")
    
    # Handle timezone conversion
    if not df["timestamp"].empty:
        # Check if timestamps are timezone-naive (assume UTC) or timezone-aware
        if df["timestamp"].dt.tz is None:
            print("Converting timezone-naive timestamps (assuming UTC) to EAT...")
            # Assume UTC and convert to EAT
            df["timestamp"] = df["timestamp"].dt.tz_localize(UTC).dt.tz_convert(EAT)
        else:
            print("Converting timezone-aware timestamps to EAT...")
            # Convert existing timezone to EAT
            df["timestamp"] = df["timestamp"].dt.tz_convert(EAT)
        
        # Remove timezone info for CSV storage (but keep EAT time)
        df["timestamp"] = df["timestamp"].dt.tz_localize(None)
        
        print(f"Timestamps converted to EAT. Sample: {df['timestamp'].iloc[0]}")
    
    return df

# Process timestamps
df = process_timestamps(df)
df = df.sort_values("timestamp", na_position="last").reset_index(drop=True)

# Extract motion_state from raw payload JSON
def get_motion_state(raw):
    try:
        if pd.isna(raw) or raw == "":
            return None
        
        raw_str = str(raw).strip()
        # Remove outer quotes if present and unescape
        if raw_str.startswith('"') and raw_str.endswith('"'):
            raw_str = raw_str[1:-1]
        raw_str = raw_str.replace('""', '"')
        
        j = json.loads(raw_str)
        return j.get("Exti_pin_level")
    except Exception as e:
        print(f"JSON parse error: {e} for: {raw[:50]}...")
        return None

df["motion_state"] = df["_raw_payload"].apply(get_motion_state)

# Remove duplicates
df = df.drop_duplicates(subset=["received_at", "temperature", "humidity"], keep="first")

# Filter out rows with null sensor values
df = df.dropna(subset=["temperature", "humidity"], how="all")

# Add EAT timezone info column for reference
df["timezone"] = "EAT"

# Select final columns
out_cols = ["timestamp", "received_at", "temperature", "humidity", "motion_counts", "motion_state", "battery_voltage", "timezone"]
df_clean = df[out_cols].copy()

# Save processed data
df_clean.to_csv(OUT_CSV, index=False)
print(f"✅ Processed {len(df_clean)} records to {OUT_CSV}")
if len(df_clean) > 0:
    print(f"📅 Date range (EAT): {df_clean['timestamp'].min()} to {df_clean['timestamp'].max()}")
    print(f"🏃 Motion states: {df_clean['motion_state'].value_counts().to_dict()}")
    print(f"📊 Sample data (EAT times):\n{df_clean.head(3)}")
    
    # Show timezone conversion info
    latest_time = df_clean['timestamp'].max()
    print(f"🕐 Latest reading: {latest_time} (EAT)")
    
    # Calculate data freshness
    import datetime
    now_eat = datetime.datetime.now(EAT).replace(tzinfo=None)
    if pd.notna(latest_time):
        time_diff = now_eat - latest_time
        minutes_ago = time_diff.total_seconds() / 60
        print(f"⏰ Data freshness: {minutes_ago:.1f} minutes ago")