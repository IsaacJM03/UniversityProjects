#!/bin/bash

echo "🚀 Starting Live IoT System..."
echo "================================"

# Function to cleanup on exit
cleanup() {
    echo ""
    echo "🛑 Shutting down all processes..."
    
    # Kill processes by name
    pkill -f "collector.py" && echo "   ✓ Collector stopped"
    pkill -f "live_processor.py" && echo "   ✓ Live processor stopped"  
    pkill -f "streamlit run" && echo "   ✓ Dashboard stopped"
    
    echo "✅ All processes stopped cleanly"
    exit 0
}

# Trap SIGINT and SIGTERM
trap cleanup SIGINT SIGTERM

# Create log directory
mkdir -p data/logs

# Check if required files exist
if [ ! -f "src/collector.py" ]; then
    echo "❌ collector.py not found!"
    exit 1
fi

if [ ! -f "src/live_processor.py" ]; then
    echo "❌ live_processor.py not found!"
    exit 1
fi

if [ ! -f "src/dashboard.py" ]; then
    echo "❌ dashboard.py not found!"
    exit 1
fi

# Start collector in background
echo "📡 Starting data collector..."
python3 src/collector.py > data/logs/collector.log 2>&1 &
COLLECTOR_PID=$!

if ps -p $COLLECTOR_PID > /dev/null; then
    echo "   ✅ Collector started (PID: $COLLECTOR_PID)"
else
    echo "   ❌ Failed to start collector"
    exit 1
fi

# Wait a bit for collector to initialize
sleep 3

# Start live processor in background
echo "🔄 Starting live data processor..."
python3 src/live_processor.py > data/logs/processor.log 2>&1 &
PROCESSOR_PID=$!

if ps -p $PROCESSOR_PID > /dev/null; then
    echo "   ✅ Live processor started (PID: $PROCESSOR_PID)"
else
    echo "   ❌ Failed to start live processor"
    cleanup
    exit 1
fi

# Wait a bit for processor to initialize
sleep 2

# Process any existing data first
echo "📊 Processing existing data..."
python3 scripts/process_raw.py

# Start dashboard
echo "🌐 Starting dashboard..."
streamlit run src/dashboard.py --server.port 8501 --server.address localhost > data/logs/dashboard.log 2>&1 &
DASHBOARD_PID=$!

# Wait for dashboard to start
sleep 5

if ps -p $DASHBOARD_PID > /dev/null; then
    echo "   ✅ Dashboard started (PID: $DASHBOARD_PID)"
else
    echo "   ❌ Failed to start dashboard"
    cleanup
    exit 1
fi

echo ""
echo "🎉 All systems running successfully!"
echo "================================"
echo "📊 Dashboard:      http://localhost:8501"
echo "📡 Collector PID:  $COLLECTOR_PID"
echo "🔄 Processor PID:  $PROCESSOR_PID"
echo "🌐 Dashboard PID:  $DASHBOARD_PID"
echo ""
echo "📝 Log files:"
echo "   • Collector:    data/logs/collector.log"
echo "   • Processor:    data/logs/processor.log" 
echo "   • Dashboard:    data/logs/dashboard.log"
echo ""
echo "💡 The system will automatically:"
echo "   • Collect sensor data every few seconds"
echo "   • Process new data as it arrives"
echo "   • Update the dashboard in real-time"
echo ""
echo "Press Ctrl+C to stop all services"
echo "================================"

# Keep script running and monitor processes
while true; do
    # Check if all processes are still running
    if ! ps -p $COLLECTOR_PID > /dev/null; then
        echo "⚠️  Collector process died, restarting..."
        python3 src/collector.py > data/logs/collector.log 2>&1 &
        COLLECTOR_PID=$!
    fi
    
    if ! ps -p $PROCESSOR_PID > /dev/null; then
        echo "⚠️  Processor process died, restarting..."
        python3 src/live_processor.py > data/logs/processor.log 2>&1 &
        PROCESSOR_PID=$!
    fi
    
    if ! ps -p $DASHBOARD_PID > /dev/null; then
        echo "⚠️  Dashboard process died, restarting..."
        streamlit run src/dashboard.py --server.port 8501 --server.address localhost > data/logs/dashboard.log 2>&1 &
        DASHBOARD_PID=$!
    fi
    
    sleep 10
done