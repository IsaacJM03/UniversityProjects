import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from sklearn.ensemble import IsolationForest, RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import warnings
import time
from datetime import datetime
warnings.filterwarnings('ignore')

# Page config
st.set_page_config(
    page_title="Smart IoT Sensor Dashboard",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

def load_and_process_data():
    """Load and preprocess sensor data"""
    try:
        # Try processed data first
        df = pd.read_csv('./data/processed/sensor_data.csv')
    except:
        # Fallback to raw data processing
        import subprocess
        subprocess.run(['python3', 'scripts/process_raw.py'])
        df = pd.read_csv('./data/processed/sensor_data.csv')
    
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['hour'] = df['timestamp'].dt.hour
    df['day_of_week'] = df['timestamp'].dt.day_name()
    df['is_weekend'] = df['timestamp'].dt.weekday >= 5
    
    return df

def create_ml_features(df):
    """Create features for ML models"""
    # Time-based features
    df['hour_sin'] = np.sin(2 * np.pi * df['hour'] / 24)
    df['hour_cos'] = np.cos(2 * np.pi * df['hour'] / 24)
    df['is_active'] = (df['motion_state'] == 'Activity').astype(int)
    
    # Rolling averages for trend detection
    df['temp_rolling_mean'] = df['temperature'].rolling(window=10, min_periods=1).mean()
    df['humidity_rolling_mean'] = df['humidity'].rolling(window=10, min_periods=1).mean()
    
    # Environmental comfort score
    df['comfort_score'] = calculate_comfort_score(df['temperature'], df['humidity'])
    
    return df

def calculate_comfort_score(temp, humidity):
    """Calculate environmental comfort score (0-100)"""
    # Optimal ranges: 20-24°C temperature, 40-60% humidity
    temp_score = 100 - abs(temp - 22) * 10  # Penalty for deviation from 22°C
    humidity_score = 100 - abs(humidity - 50) * 2  # Penalty for deviation from 50%
    
    temp_score = np.clip(temp_score, 0, 100)
    humidity_score = np.clip(humidity_score, 0, 100)
    
    return (temp_score + humidity_score) / 2

def detect_anomalies(df):
    """Detect anomalies using Isolation Forest"""
    features = ['temperature', 'humidity', 'motion_counts', 'battery_voltage']
    X = df[features].fillna(df[features].mean())
    
    if len(X) < 10:
        df['is_anomaly'] = False
        return df
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    iso_forest = IsolationForest(contamination=0.1, random_state=42)
    anomalies = iso_forest.fit_predict(X_scaled)
    
    df['is_anomaly'] = (anomalies == -1)
    return df

def predict_occupancy(df):
    """Predict room occupancy patterns"""
    # Simple ML model based on motion and environmental data
    features = ['hour_sin', 'hour_cos', 'temperature', 'humidity', 'motion_counts']
    X = df[features].fillna(df[features].mean())
    
    # Use motion state as ground truth for training
    y = df['is_active'].fillna(0)
    
    if len(X) < 10:
        df['occupancy_probability'] = 0.5
        return df, None, 0.0
    
    model = RandomForestClassifier(n_estimators=50, random_state=42)
    
    # Split data for validation
    split_idx = max(1, int(len(X) * 0.8))
    X_train, X_test = X[:split_idx], X[split_idx:]
    y_train, y_test = y[:split_idx], y[split_idx:]
    
    model.fit(X_train, y_train)
    
    # Predict occupancy probability
    occupancy_prob = model.predict_proba(X)[:, 1]
    df['occupancy_probability'] = occupancy_prob
    
    accuracy = model.score(X_test, y_test) if len(X_test) > 0 else 0.0
    
    return df, model, accuracy

def setup_auto_refresh():
    """Setup auto-refresh functionality"""
    st.sidebar.markdown("---")
    st.sidebar.subheader("🔄 Live Updates")
    
    # Initialize session state for auto-refresh settings
    if 'auto_refresh_enabled' not in st.session_state:
        st.session_state.auto_refresh_enabled = True
    if 'refresh_interval' not in st.session_state:
        st.session_state.refresh_interval = 10
    
    # Auto-refresh controls
    auto_refresh = st.sidebar.checkbox(
        "Enable Auto-Refresh", 
        value=st.session_state.auto_refresh_enabled,
        help="Automatically refresh the dashboard with new data"
    )
    
    refresh_interval = st.sidebar.selectbox(
        "Refresh Interval", 
        [5, 10, 15, 30, 60], 
        index=[5, 10, 15, 30, 60].index(st.session_state.refresh_interval),
        format_func=lambda x: f"{x} seconds",
        help="How often to refresh the dashboard"
    )
    
    # Update session state
    st.session_state.auto_refresh_enabled = auto_refresh
    st.session_state.refresh_interval = refresh_interval
    
    # Manual refresh button
    col1, col2 = st.sidebar.columns(2)
    with col1:
        if st.button("🔄 Refresh", type="primary", help="Refresh data now"):
            st.cache_data.clear()
            st.rerun()
    
    with col2:
        if st.button("🗑️ Clear Cache", help="Clear all cached data"):
            st.cache_data.clear()
            st.success("Cache cleared!")
    
    # Show auto-refresh status
    if auto_refresh:
        st.sidebar.success(f"✅ Auto-refresh: ON ({refresh_interval}s)")
        
        # JavaScript-based auto-refresh with better implementation
        refresh_script = f"""
        <script>
            setTimeout(function(){{
                window.location.reload(true);
            }}, {refresh_interval * 1000});
        </script>
        """
        st.sidebar.markdown(refresh_script, unsafe_allow_html=True)
        
        # Optional: Show countdown (commented out to avoid performance issues)
        # countdown_placeholder = st.sidebar.empty()
        # for i in range(refresh_interval, 0, -1):
        #     countdown_placeholder.write(f"⏱️ Refreshing in: {i}s")
        #     time.sleep(1)
        
    else:
        st.sidebar.info("❌ Auto-refresh: OFF")
    
    return auto_refresh, refresh_interval

def main():
    st.title("🏠 Smart IoT Sensor Dashboard")
    st.markdown("Real-time analytics with machine learning insights")
    
    # Setup auto-refresh
    auto_refresh, refresh_interval = setup_auto_refresh()
    
    # Show dashboard status header
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        last_update = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if auto_refresh:
            st.markdown(f"**📡 Last Updated:** {last_update}")
            st.markdown(f"🔄 **Auto-refresh:** Enabled ({refresh_interval}s intervals)")
        else:
            st.markdown(f"**📡 Last Updated:** {last_update}")
            st.markdown("⏸️ **Auto-refresh:** Disabled (Manual mode)")
    
    with col2:
        # Live status indicator
        if auto_refresh:
            st.markdown("🟢 **LIVE**")
        else:
            st.markdown("🔴 **MANUAL**")
    
    with col3:
        # Data source info
        st.markdown("📊 **Source:** Processed CSV")
    
    # Load data
    with st.spinner("Loading sensor data..."):
        try:
            df = load_and_process_data()
            
            if len(df) == 0:
                st.error("No data found. Please ensure data collection is running.")
                st.info("Make sure you have data in `data/processed/sensor_data.csv`")
                return
                
            df = create_ml_features(df)
            df = detect_anomalies(df)
            df, occupancy_model, ml_accuracy = predict_occupancy(df)
            
            st.success(f"✅ Loaded {len(df):,} records successfully!")
            
        except Exception as e:
            st.error(f"Error loading data: {str(e)}")
            st.info("Please ensure data files exist in data/processed/sensor_data.csv")
            return
    
    # Show data freshness with improved messaging
    latest_record = df['timestamp'].max()
    time_since_last = pd.Timestamp.now() - latest_record
    total_seconds = time_since_last.total_seconds()
    
    # Create a more detailed freshness indicator
    if total_seconds < 60:  # Less than 1 minute
        st.success(f"🟢 **Data is live!** Last sensor reading: {int(total_seconds)}s ago")
    elif total_seconds < 300:  # Less than 5 minutes
        minutes_ago = int(total_seconds // 60)
        st.success(f"🟢 **Data is fresh!** Last sensor reading: {minutes_ago}m ago")
    elif total_seconds < 1800:  # Less than 30 minutes
        minutes_ago = int(total_seconds // 60)
        st.warning(f"🟡 **Data is recent.** Last sensor reading: {minutes_ago}m ago")
    elif total_seconds < 3600:  # Less than 1 hour
        minutes_ago = int(total_seconds // 60)
        st.warning(f"🟡 **Data is aging.** Last sensor reading: {minutes_ago}m ago")
    else:
        hours_ago = total_seconds // 3600
        if hours_ago < 24:
            st.error(f"🔴 **Data is stale!** Last sensor reading: {hours_ago:.0f}h ago")
        else:
            days_ago = hours_ago // 24
            st.error(f"🔴 **Data is very stale!** Last sensor reading: {days_ago:.0f}d ago")
    
    # Show collection info
    st.info(f"📊 **Dataset:** {len(df):,} total records from {df['timestamp'].min().strftime('%Y-%m-%d')} to {df['timestamp'].max().strftime('%Y-%m-%d')}")
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        avg_temp = df['temperature'].mean()
        st.metric("Avg Temperature", f"{avg_temp:.1f}°C")
    
    with col2:
        avg_humidity = df['humidity'].mean()
        st.metric("Avg Humidity", f"{avg_humidity:.1f}%")
    
    with col3:
        activity_rate = df['is_active'].mean() * 100
        st.metric("Activity Rate", f"{activity_rate:.1f}%")
    
    with col4:
        avg_comfort = df['comfort_score'].mean()
        st.metric("Comfort Score", f"{avg_comfort:.0f}/100")
    
    # Live status
    if len(df) > 0:
        latest = df.iloc[-1]
        
        st.markdown("### 🔴 Live Status")
        
        status_col1, status_col2, status_col3 = st.columns(3)
        
        with status_col1:
            if latest['is_active']:
                st.success("🏃 MOTION DETECTED")
            else:
                st.info("😴 No Motion")
        
        with status_col2:
            comfort = latest['comfort_score']
            if comfort >= 80:
                st.success(f"😊 Comfortable ({comfort:.0f}%)")
            elif comfort >= 60:
                st.warning(f"😐 Moderate ({comfort:.0f}%)")
            else:
                st.error(f"😣 Uncomfortable ({comfort:.0f}%)")
        
        with status_col3:
            battery = latest['battery_voltage']
            if battery >= 3.2:
                st.success(f"🔋 Battery OK ({battery:.2f}V)")
            elif battery >= 3.0:
                st.warning(f"🪫 Battery Low ({battery:.2f}V)")
            else:
                st.error(f"⚠️ Battery Critical ({battery:.2f}V)")
    
    # Simple visualizations
    st.subheader("📊 Sensor Data Over Time")
    
    # Temperature and humidity plot
    fig = make_subplots(rows=2, cols=1, 
                        subplot_titles=['Temperature & Humidity Over Time'],
                        # , 'Humidity Over Time'],
                        vertical_spacing=0.1)
    
    fig.add_trace(go.Scatter(x=df['timestamp'], y=df['temperature'], 
                            mode='lines', name='Temperature', line_color='red'), row=1, col=1)
    fig.add_trace(go.Scatter(x=df['timestamp'], y=df['humidity'], 
                            mode='lines', name='Humidity', line_color='blue'), row=2, col=1)
    
    fig.update_layout(height=500)
    st.plotly_chart(fig, use_container_width=True)
    
    # Motion activity
    st.subheader("🏃 Motion Activity")
    motion_data = df[df['is_active'] == 1]
    if len(motion_data) > 0:
        fig_motion = px.scatter(motion_data, x='timestamp', y='motion_counts', 
                               title="Motion Events", color_discrete_sequence=['green'])
        st.plotly_chart(fig_motion, use_container_width=True)
    else:
        st.info("No motion detected in the data")
    
    # ML Insights
    st.subheader("🤖 ML Insights")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Occupancy Model Accuracy", f"{ml_accuracy:.1%}")
        
        # Occupancy prediction
        fig_occ = px.line(df, x='timestamp', y='occupancy_probability',
                         title="Predicted Occupancy Probability")
        fig_occ.update_traces(line_color='purple')
        st.plotly_chart(fig_occ, use_container_width=True)
    
    with col2:
        # Anomalies
        anomaly_count = df['is_anomaly'].sum()
        st.metric("Anomalies Detected", anomaly_count)
        
        # Comfort distribution
        fig_comfort = px.histogram(df, x='comfort_score', nbins=20,
                                 title="Environmental Comfort Distribution")
        fig_comfort.update_traces(marker_color='orange')
        st.plotly_chart(fig_comfort, use_container_width=True)
    
    # Recent data table
    st.subheader("📋 Recent Data")
    st.dataframe(df.tail(10))

if __name__ == "__main__":
    main()