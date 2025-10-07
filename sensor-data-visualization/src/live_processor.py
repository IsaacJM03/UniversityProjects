import time
import subprocess
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import pandas as pd
from datetime import datetime
import sys
import os

class CSVFileHandler(FileSystemEventHandler):
    def __init__(self, raw_csv_path, process_script_path):
        self.raw_csv_path = Path(raw_csv_path)
        self.process_script_path = Path(process_script_path)
        self.last_processed_size = 0
        self.processing = False
        
        # Get initial file size
        if self.raw_csv_path.exists():
            self.last_processed_size = self.raw_csv_path.stat().st_size
            print(f"📏 Initial file size: {self.last_processed_size} bytes")
    
    def on_modified(self, event):
        if event.is_directory or self.processing:
            return
            
        # Check if it's our target CSV file
        if Path(event.src_path) == self.raw_csv_path:
            try:
                current_size = self.raw_csv_path.stat().st_size
                
                # Only process if file has grown (new data added)
                if current_size > self.last_processed_size:
                    print(f"\n📈 New data detected at {datetime.now().strftime('%H:%M:%S')}!")
                    print(f"   File size: {self.last_processed_size} → {current_size} bytes")
                    self.process_new_data()
                    self.last_processed_size = current_size
            except FileNotFoundError:
                # File might be temporarily unavailable during write
                pass
    
    def process_new_data(self):
        """Process the raw data whenever new data is added"""
        if self.processing:
            return
            
        self.processing = True
        try:
            print("🔄 Processing new sensor data...")
            
            # Run the process_raw.py script
            result = subprocess.run([
                sys.executable, str(self.process_script_path)
            ], capture_output=True, text=True, cwd=self.process_script_path.parent.parent)
            
            if result.returncode == 0:
                print("✅ Data processed successfully!")
                if result.stdout.strip():
                    print(f"   Output: {result.stdout.strip()}")
            else:
                print(f"❌ Processing failed!")
                if result.stderr.strip():
                    print(f"   Error: {result.stderr.strip()}")
                
        except Exception as e:
            print(f"⚠️ Error processing data: {e}")
        finally:
            self.processing = False

def start_live_processor():
    """Start the live data processor"""
    
    # Paths
    base_dir = Path(__file__).parent.parent
    raw_csv = base_dir / "data" / "raw" / "sensor_data.csv"
    process_script = base_dir / "scripts" / "process_raw.py"
    
    # Validate paths
    if not process_script.exists():
        print(f"❌ Process script not found: {process_script}")
        return
    
    # Create directories if they don't exist
    raw_csv.parent.mkdir(parents=True, exist_ok=True)
    
    # Create empty CSV if it doesn't exist
    if not raw_csv.exists():
        raw_csv.touch()
        print(f"📄 Created empty CSV file: {raw_csv}")
    
    print("🚀 Live Data Processor Starting...")
    print(f"👁️  Watching: {raw_csv}")
    print(f"🔧 Processor: {process_script}")
    print("=" * 50)
    
    # Set up file watcher
    event_handler = CSVFileHandler(raw_csv, process_script)
    observer = Observer()
    observer.schedule(event_handler, str(raw_csv.parent), recursive=False)
    
    # Start watching
    observer.start()
    print("✅ Live processor started! Press Ctrl+C to stop.")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n🛑 Live processor stopped.")
    
    observer.join()

if __name__ == "__main__":
    start_live_processor()