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
import pytz
import os
from pathlib import Path
warnings.filterwarnings('ignore')

EAT = pytz.timezone('Africa/Nairobi')

st.set_page_config(
    page_title="Smart IoT Sensor Dashboard",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

def load_and_process_data():
    possible_paths = [
        './data/processed/sensor_data.csv',
        'data/processed/sensor_data.csv',
        '../data/processed/sensor_data.csv',
        Path(__file__).parent.parent / 'data' / 'processed' / 'sensor_data.csv'
    ]
    df = None
    data_source = "sample"
    for path in possible_paths:
        try:
            if os.path.exists(str(path)):
                df = pd.read_csv(str(path))
                data_source = "real"
                st.sidebar.success("Real sensor data loaded")
                break
        except Exception as e:
            continue
    if df is None or len(df) == 0:
        st.sidebar.warning("No real data found. Generating sample data for demo.")
        df = create_sample_data()
        data_source = "sample"
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['hour'] = df['timestamp'].dt.hour
    df['day_of_week'] = df['timestamp'].dt.day_name()
    df['is_weekend'] = df['timestamp'].dt.weekday >= 5
    return df

def create_sample_data():
    from datetime import datetime, timedelta
    import numpy as np
    base_time = datetime.now() - timedelta(days=7)
    data = []
    for i in range(200):
        timestamp = base_time + timedelta(minutes=i*50)
        hour = timestamp.hour
        temp_base = 22 + 3 * np.sin((hour - 6) * np.pi / 12)
        temp = temp_base + np.random.normal(0, 1)
        humidity = 60 - (temp - 22) * 2 + np.random.normal(0, 3)
        humidity = max(30, min(80, humidity))
        activity_prob = 0.8 if 6 <= hour <= 22 else 0.2
        motion_counts = np.random.randint(11000, 12000) if np.random.random() < activity_prob else np.random.randint(10800, 11100)
        motion_state = "Activity" if np.random.random() < activity_prob else "No Activity"
        battery = 3.2 - (i / 2000) + np.random.normal(0, 0.02)
        battery = max(2.8, battery)
        data.append({
            'timestamp': timestamp,
            'received_at': timestamp.isoformat(),
            'temperature': round(temp, 2),
            'humidity': round(humidity, 1),
            'motion_counts': motion_counts,
            'motion_state': motion_state,
            'battery_voltage': round(battery, 3),
            'timezone': 'EAT'
        })
    return pd.DataFrame(data)

def create_ml_features(df):
    df['hour_sin'] = np.sin(2 * np.pi * df['hour'] / 24)
    df['hour_cos'] = np.cos(2 * np.pi * df['hour'] / 24)
    df['is_active'] = (df['motion_state'] == 'Activity').astype(int)
    df['temp_rolling_mean'] = df['temperature'].rolling(window=10, min_periods=1).mean()
    df['humidity_rolling_mean'] = df['humidity'].rolling(window=10, min_periods=1).mean()
    df['comfort_score'] = calculate_comfort_score(df['temperature'], df['humidity'])
    return df

def calculate_comfort_score(temp, humidity):
    temp_score = 100 - abs(temp - 22) * 10
    humidity_score = 100 - abs(humidity - 50) * 2
    temp_score = np.clip(temp_score, 0, 100)
    humidity_score = np.clip(humidity_score, 0, 100)
    return (temp_score + humidity_score) / 2

def detect_anomalies(df):
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
    features = ['hour_sin', 'hour_cos', 'temperature', 'humidity', 'motion_counts']
    X = df[features].fillna(df[features].mean())
    y = df['is_active'].fillna(0)
    if len(X) < 10:
        df['occupancy_probability'] = 0.5
        return df, None, 0.0
    model = RandomForestClassifier(n_estimators=50, random_state=42)
    split_idx = max(1, int(len(X) * 0.8))
    X_train, X_test = X[:split_idx], X[split_idx:]
    y_train, y_test = y[:split_idx], y[split_idx:]
    model.fit(X_train, y_train)
    occupancy_prob = model.predict_proba(X)[:, 1]
    df['occupancy_probability'] = occupancy_prob
    accuracy = model.score(X_test, y_test) if len(X_test) > 0 else 0.0
    return df, model, accuracy

def setup_auto_refresh():
    st.sidebar.markdown("---")
    st.sidebar.subheader("Live Updates")
    if 'auto_refresh_enabled' not in st.session_state:
        st.session_state.auto_refresh_enabled = True
    if 'refresh_interval' not in st.session_state:
        st.session_state.refresh_interval = 10
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
    st.session_state.auto_refresh_enabled = auto_refresh
    st.session_state.refresh_interval = refresh_interval
    col1, col2 = st.sidebar.columns(2)
    with col1:
        if st.button("Refresh", type="primary", help="Refresh data now"):
            st.cache_data.clear()
            st.rerun()
    with col2:
        if st.button("Clear Cache", help="Clear all cached data"):
            st.cache_data.clear()
            st.success("Cache cleared!")
    if auto_refresh:
        st.sidebar.success(f"Auto-refresh: ON ({refresh_interval}s)")
        refresh_script = f"""
        <script>
            setTimeout(function(){{
                window.location.reload(true);
            }}, {refresh_interval * 1000});
        </script>
        """
        st.sidebar.markdown(refresh_script, unsafe_allow_html=True)
    else:
        st.sidebar.info("Auto-refresh: OFF")
    return auto_refresh, refresh_interval

def analyze_occupancy_patterns(df):
    patterns = {}
    hourly_activity = df.groupby('hour')['is_active'].agg(['mean', 'count']).reset_index()
    hourly_activity.columns = ['hour', 'activity_rate', 'readings_count']
    peak_hours = hourly_activity.nlargest(3, 'activity_rate')
    quiet_hours = hourly_activity.nsmallest(3, 'activity_rate')
    patterns['peak_hours'] = peak_hours['hour'].tolist()
    patterns['quiet_hours'] = quiet_hours['hour'].tolist()
    patterns['hourly_data'] = hourly_activity
    weekly_activity = df.groupby('day_of_week')['is_active'].mean().reset_index()
    patterns['weekly_data'] = weekly_activity
    motion_stats = df[df['is_active'] == 1]['motion_counts'].describe()
    patterns['motion_intensity'] = {
        'low_threshold': motion_stats['25%'],
        'high_threshold': motion_stats['75%'],
        'avg_motion': motion_stats['mean']
    }
    return patterns

def analyze_environmental_comfort(df):
    comfort_analysis = {}
    df['temp_comfort'] = df['temperature'].apply(lambda x: 
        'Optimal' if 20 <= x <= 24 else
        'Acceptable' if 18 <= x <= 26 else
        'Uncomfortable'
    )
    df['humidity_comfort'] = df['humidity'].apply(lambda x:
        'Optimal' if 40 <= x <= 60 else
        'Acceptable' if 30 <= x <= 70 else
        'Poor'
    )
    temp_comfort_dist = df['temp_comfort'].value_counts(normalize=True) * 100
    humidity_comfort_dist = df['humidity_comfort'].value_counts(normalize=True) * 100
    comfort_analysis['temperature_comfort'] = temp_comfort_dist.to_dict()
    comfort_analysis['humidity_comfort'] = humidity_comfort_dist.to_dict()
    occupied_data = df[df['is_active'] == 1]
    empty_data = df[df['is_active'] == 0]
    if len(occupied_data) > 0 and len(empty_data) > 0:
        comfort_analysis['occupied_avg_temp'] = occupied_data['temperature'].mean()
        comfort_analysis['empty_avg_temp'] = empty_data['temperature'].mean()
        comfort_analysis['temp_efficiency'] = abs(comfort_analysis['occupied_avg_temp'] - comfort_analysis['empty_avg_temp'])
    uncomfortable_periods = df[
        (df['temp_comfort'] == 'Uncomfortable') | 
        (df['humidity_comfort'] == 'Poor')
    ]
    comfort_analysis['uncomfortable_percentage'] = (len(uncomfortable_periods) / len(df)) * 100
    return comfort_analysis

def predict_next_readings(df):
    predictions = {}
    if len(df) >= 10:
        recent_data = df.tail(20)
        temp_trend = np.polyfit(range(len(recent_data)), recent_data['temperature'], 1)[0]
        next_temp = recent_data['temperature'].iloc[-1] + temp_trend
        humidity_trend = np.polyfit(range(len(recent_data)), recent_data['humidity'], 1)[0]
        next_humidity = recent_data['humidity'].iloc[-1] + humidity_trend
        current_hour = recent_data['hour'].iloc[-1]
        next_hour = (current_hour + 1) % 24
        historical_activity = df[df['hour'] == next_hour]['is_active'].mean() if len(df[df['hour'] == next_hour]) > 0 else 0.5
        predictions = {
            'next_temperature': round(next_temp, 1),
            'temp_trend': 'Rising' if temp_trend > 0.1 else 'Falling' if temp_trend < -0.1 else 'Stable',
            'next_humidity': round(next_humidity, 1),
            'humidity_trend': 'Rising' if humidity_trend > 0.5 else 'Falling' if humidity_trend < -0.5 else 'Stable',
            'next_hour_activity_prob': round(historical_activity * 100, 1)
        }
    return predictions

def detect_behavioral_insights(df):
    insights = {}
    if len(df) >= 50:
        morning_activity = df[(df['hour'] >= 6) & (df['hour'] <= 10)]['is_active'].mean()
        afternoon_activity = df[(df['hour'] >= 12) & (df['hour'] <= 17)]['is_active'].mean()
        evening_activity = df[(df['hour'] >= 18) & (df['hour'] <= 22)]['is_active'].mean()
        night_activity = df[(df['hour'] >= 23) | (df['hour'] <= 5)]['is_active'].mean()
        activity_periods = {
            'Morning (6-10 AM)': morning_activity,
            'Afternoon (12-5 PM)': afternoon_activity,
            'Evening (6-10 PM)': evening_activity,
            'Night (11 PM-5 AM)': night_activity
        }
        most_active_period = max(activity_periods, key=activity_periods.get)
        insights['activity_periods'] = activity_periods
        insights['most_active_period'] = most_active_period
        daily_patterns = df.groupby([df['timestamp'].dt.date, 'hour'])['is_active'].mean()
        routine_consistency = daily_patterns.groupby('hour').std().mean()
        insights['routine_consistency'] = 'High' if routine_consistency < 0.3 else 'Medium' if routine_consistency < 0.5 else 'Low'
        comfortable_temps = df[df['is_active'] == 1]['temperature']
        if len(comfortable_temps) > 0:
            insights['preferred_temp_range'] = {
                'min': comfortable_temps.quantile(0.25),
                'max': comfortable_temps.quantile(0.75),
                'avg': comfortable_temps.mean()
            }
    return insights

def generate_smart_recommendations(df, patterns, comfort_analysis, predictions, behavioral_insights):
    recommendations = []
    if 'temp_efficiency' in comfort_analysis and comfort_analysis['temp_efficiency'] > 2:
        recommendations.append({
            'type': 'Energy',
            'priority': 'High',
            'title': 'Temperature Optimization',
            'description': f"Temperature varies by {comfort_analysis['temp_efficiency']:.1f}°C between occupied/empty periods. Consider smart thermostat scheduling.",
            'action': 'Install programmable thermostat'
        })
    if comfort_analysis.get('uncomfortable_percentage', 0) > 20:
        recommendations.append({
            'type': 'Comfort',
            'priority': 'Medium',
            'title': 'Environmental Comfort',
            'description': f"{comfort_analysis['uncomfortable_percentage']:.1f}% of time spent in uncomfortable conditions.",
            'action': 'Adjust HVAC settings or add humidifier/dehumidifier'
        })
    if behavioral_insights.get('routine_consistency') == 'High' and patterns.get('peak_hours'):
        peak_hours_str = ', '.join([f"{h}:00" for h in patterns['peak_hours'][:2]])
        recommendations.append({
            'type': 'Automation',
            'priority': 'Medium',
            'title': 'Smart Automation',
            'description': f"Consistent activity detected during {peak_hours_str}. Perfect for automated lighting/HVAC.",
            'action': 'Set up automated schedules for peak activity hours'
        })
    latest_battery = df['battery_voltage'].iloc[-1]
    if latest_battery < 3.1:
        recommendations.append({
            'type': 'Maintenance',
            'priority': 'High',
            'title': 'Battery Replacement',
            'description': f"Battery voltage at {latest_battery:.2f}V. Replace soon to avoid data loss.",
            'action': 'Replace sensor battery'
        })
    if predictions.get('temp_trend') == 'Rising' and predictions.get('next_temperature', 0) > 26:
        recommendations.append({
            'type': 'Comfort',
            'priority': 'Medium',
            'title': 'Temperature Alert',
            'description': f"Temperature trending upward. Predicted to reach {predictions['next_temperature']}°C.",
            'action': 'Consider pre-cooling or ventilation'
        })
    return recommendations

def main():
    st.title("Smart IoT Sensor Dashboard")
    st.markdown("Real-time analytics with machine learning insights")
    st.sidebar.markdown("---")
    st.sidebar.subheader("Deployment Info")
    st.sidebar.info("Version: 1.0.0")
    is_cloud = os.getenv('STREAMLIT_SHARING_MODE', False) or 'streamlit.app' in os.getenv('HOSTNAME', '')
    if is_cloud:
        st.sidebar.success("Running on Streamlit Cloud")
    else:
        st.sidebar.info("Running Locally")
    auto_refresh, refresh_interval = setup_auto_refresh()
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        eat_now = datetime.now(EAT)
        last_update = eat_now.strftime("%Y-%m-%d %H:%M:%S EAT")
        if auto_refresh:
            st.markdown(f"Last Updated: {last_update}")
            st.markdown(f"Auto-refresh: Enabled ({refresh_interval}s intervals)")
        else:
            st.markdown(f"Last Updated: {last_update}")
            st.markdown("Auto-refresh: Disabled (Manual mode)")
    with col2:
        if auto_refresh:
            st.markdown("LIVE")
        else:
            st.markdown("MANUAL")
    with col3:
        st.markdown("Source: Processed CSV")
    st.markdown("---")
    with st.spinner("Loading sensor data..."):
        try:
            df = load_and_process_data()
            if len(df) == 0:
                st.error("No data found. Please ensure data collection is running.")
                st.info("Make sure you have data in data/processed/sensor_data.csv")
                return
            df = create_ml_features(df)
            df = detect_anomalies(df)
            df, occupancy_model, ml_accuracy = predict_occupancy(df)
            st.success(f"Loaded {len(df):,} records successfully!")
        except Exception as e:
            st.error(f"Error loading data: {str(e)}")
            st.info("Please ensure data files exist in data/processed/sensor_data.csv")
            return
    latest_record = df['timestamp'].max()
    eat_now_naive = datetime.now(EAT).replace(tzinfo=None)
    time_since_last = eat_now_naive - latest_record
    total_seconds = time_since_last.total_seconds()
    if total_seconds < 60:
        st.success(f"Data is live! Last sensor reading: {int(total_seconds)}s ago (EAT)")
    elif total_seconds < 300:
        minutes_ago = int(total_seconds // 60)
        st.success(f"Data is fresh! Last sensor reading: {minutes_ago}m ago (EAT)")
    elif total_seconds < 1800:
        minutes_ago = int(total_seconds // 60)
        st.warning(f"Data is recent. Last sensor reading: {minutes_ago}m ago (EAT)")
    elif total_seconds < 3600:
        minutes_ago = int(total_seconds // 60)
        st.warning(f"Data is aging. Last sensor reading: {minutes_ago}m ago (EAT)")
    else:
        hours_ago = total_seconds // 3600
        if hours_ago < 24:
            st.error(f"Data is stale! Last sensor reading: {hours_ago:.0f}h ago (EAT)")
        else:
            days_ago = hours_ago // 24
            st.error(f"Data is very stale! Last sensor reading: {days_ago:.0f}d ago (EAT)")
    eat_now_display = datetime.now(EAT).strftime("%Y-%m-%d %H:%M:%S EAT")
    st.info(f"Current time (EAT): {eat_now_display}")
    min_time = df['timestamp'].min()
    max_time = df['timestamp'].max()
    st.info(f"Dataset: {len(df):,} total records from {min_time.strftime('%Y-%m-%d %H:%M EAT')} to {max_time.strftime('%Y-%m-%d %H:%M EAT')}")
    st.markdown("---")
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("Key Metrics")
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
    st.markdown("<br><br>", unsafe_allow_html=True)
    if len(df) > 0:
        latest = df.iloc[-1]
        st.subheader("Live Status")
        status_col1, status_col2, status_col3 = st.columns(3)
        with status_col1:
            if latest['is_active']:
                st.success("MOTION DETECTED")
            else:
                st.info("No Motion")
        with status_col2:
            comfort = latest['comfort_score']
            if comfort >= 80:
                st.success(f"Comfortable ({comfort:.0f}%)")
            elif comfort >= 60:
                st.warning(f"Moderate ({comfort:.0f}%)")
            else:
                st.error(f"Uncomfortable ({comfort:.0f}%)")
        with status_col3:
            battery = latest['battery_voltage']
            if battery >= 3.2:
                st.success(f"Battery OK ({battery:.2f}V)")
            elif battery >= 3.0:
                st.warning(f"Battery Low ({battery:.2f}V)")
            else:
                st.error(f"Battery Critical ({battery:.2f}V)")
    st.markdown("---")
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("Sensor Data Over Time")
    fig = make_subplots(rows=2, cols=1, 
                        subplot_titles=['Temperature Over Time', 'Humidity Over Time'],
                        vertical_spacing=0.15)
    fig.add_trace(go.Scatter(x=df['timestamp'], y=df['temperature'], 
                            mode='lines', name='Temperature', line_color='red'), row=1, col=1)
    fig.add_trace(go.Scatter(x=df['timestamp'], y=df['humidity'], 
                            mode='lines', name='Humidity', line_color='blue'), row=2, col=1)
    fig.update_layout(height=600)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.subheader("Motion Activity")
    motion_data = df[df['is_active'] == 1]
    if len(motion_data) > 0:
        fig_motion = px.scatter(motion_data, x='timestamp', y='motion_counts', 
                               title="Motion Events Over Time", 
                               color_discrete_sequence=['green'])
        fig_motion.update_layout(height=400)
        st.plotly_chart(fig_motion, use_container_width=True)
    else:
        st.info("No motion detected in the data")
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("Smart Analytics & Insights")
    with st.spinner("Analyzing patterns and generating insights..."):
        patterns = analyze_occupancy_patterns(df)
        comfort_analysis = analyze_environmental_comfort(df)
        predictions = predict_next_readings(df)
        behavioral_insights = detect_behavioral_insights(df)
        recommendations = generate_smart_recommendations(df, patterns, comfort_analysis, predictions, behavioral_insights)
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Occupancy Patterns", 
        "Environmental Analysis", 
        "Predictions", 
        "Behavioral Insights",
        "Smart Recommendations"
    ])
    with tab1:
        st.subheader("Daily Activity Patterns")
        col1, col2 = st.columns(2)
        with col1:
            if patterns.get('peak_hours'):
                peak_hours_str = ', '.join([f"{h}:00" for h in patterns['peak_hours']])
                st.success(f"Most Active Hours: {peak_hours_str}")
            if patterns.get('quiet_hours'):
                quiet_hours_str = ', '.join([f"{h}:00" for h in patterns['quiet_hours']])
                st.info(f"Quietest Hours: {quiet_hours_str}")
            total_active_time = df['is_active'].sum()
            total_readings = len(df)
            activity_percentage = (total_active_time / total_readings) * 100
            st.metric("Overall Activity Rate", f"{activity_percentage:.1f}%")
            if 'motion_intensity' in patterns:
                motion_stats = patterns['motion_intensity']
                avg_motion = motion_stats.get('avg_motion', 0)
                st.metric("Average Motion Intensity", f"{avg_motion:.0f} counts")
        with col2:
            if 'hourly_data' in patterns:
                fig_hourly = px.bar(patterns['hourly_data'], x='hour', y='activity_rate',
                                   title="Activity Rate by Hour of Day",
                                   color='activity_rate', color_continuous_scale='Viridis')
                fig_hourly.update_layout(height=350)
                st.plotly_chart(fig_hourly, use_container_width=True)
        if 'weekly_data' in patterns and len(patterns['weekly_data']) > 1:
            st.subheader("Weekly Activity Patterns")
            fig_weekly = px.bar(patterns['weekly_data'], x='day_of_week', y='is_active',
                               title="Activity Rate by Day of Week",
                               color='is_active', color_continuous_scale='Blues')
            fig_weekly.update_layout(height=300)
            st.plotly_chart(fig_weekly, use_container_width=True)
    with tab2:
        st.subheader("Environmental Comfort Analysis")
        col1, col2 = st.columns(2)
        with col1:
            if 'temperature_comfort' in comfort_analysis:
                temp_comfort = comfort_analysis['temperature_comfort']
                fig_temp = px.pie(
                    values=list(temp_comfort.values()),
                    names=list(temp_comfort.keys()),
                    title="Temperature Comfort Distribution",
                    color_discrete_map={
                        'Optimal': '#00CC96',
                        'Acceptable': '#FFA15A', 
                        'Uncomfortable': '#EF553B'
                    }
                )
                st.plotly_chart(fig_temp, use_container_width=True)
            if 'temp_efficiency' in comfort_analysis:
                efficiency_score = max(0, 100 - comfort_analysis['temp_efficiency'] * 10)
                st.metric("Temperature Efficiency Score", f"{efficiency_score:.0f}/100")
                if 'occupied_avg_temp' in comfort_analysis and 'empty_avg_temp' in comfort_analysis:
                    st.info(f"Occupied: {comfort_analysis['occupied_avg_temp']:.1f}°C | Empty: {comfort_analysis['empty_avg_temp']:.1f}°C")
        with col2:
            if 'humidity_comfort' in comfort_analysis:
                humidity_comfort = comfort_analysis['humidity_comfort']
                fig_humidity = px.pie(
                    values=list(humidity_comfort.values()),
                    names=list(humidity_comfort.keys()),
                    title="Humidity Comfort Distribution",
                    color_discrete_map={
                        'Optimal': '#00CC96',
                        'Acceptable': '#FFA15A',
                        'Poor': '#EF553B'
                    }
                )
                st.plotly_chart(fig_humidity, use_container_width=True)
            if 'uncomfortable_percentage' in comfort_analysis:
                uncomfortable_pct = comfort_analysis['uncomfortable_percentage']
                if uncomfortable_pct < 10:
                    st.success(f"Comfort Level: Excellent ({uncomfortable_pct:.1f}% uncomfortable)")
                elif uncomfortable_pct < 25:
                    st.warning(f"Comfort Level: Good ({uncomfortable_pct:.1f}% uncomfortable)")
                else:
                    st.error(f"Comfort Level: Poor ({uncomfortable_pct:.1f}% uncomfortable)")
        st.subheader("Environmental Comfort Over Time")
        fig_comfort_timeline = go.Figure()
        fig_comfort_timeline.add_trace(go.Scatter(
            x=df['timestamp'], 
            y=df['comfort_score'],
            mode='lines',
            name='Comfort Score',
            line=dict(color='green', width=2),
            fill='tonexty'
        ))
        fig_comfort_timeline.add_hline(y=80, line_dash="dash", line_color="green", 
                                      annotation_text="Excellent Comfort")
        fig_comfort_timeline.add_hline(y=60, line_dash="dash", line_color="orange", 
                                      annotation_text="Good Comfort")
        fig_comfort_timeline.update_layout(
            title="Environmental Comfort Score Over Time",
            xaxis_title="Time",
            yaxis_title="Comfort Score (0-100)",
            height=400
        )
        st.plotly_chart(fig_comfort_timeline, use_container_width=True)
    with tab3:
        st.subheader("Smart Predictions")
        if predictions:
            col1, col2, col3 = st.columns(3)
            with col1:
                trend_delta = predictions['temp_trend']
                trend_color = "normal" if trend_delta == "Stable" else "inverse" if trend_delta == "Falling" else "normal"
                st.metric(
                    "Next Hour Temperature", 
                    f"{predictions['next_temperature']}°C",
                    delta=f"{predictions['temp_trend']}",
                    delta_color=trend_color
                )
            with col2:
                humidity_trend_delta = predictions['humidity_trend']
                humidity_color = "normal" if humidity_trend_delta == "Stable" else "inverse" if humidity_trend_delta == "Falling" else "normal"
                st.metric(
                    "Next Hour Humidity", 
                    f"{predictions['next_humidity']}%",
                    delta=f"{predictions['humidity_trend']}",
                    delta_color=humidity_color
                )
            with col3:
                st.metric(
                    "Activity Probability", 
                    f"{predictions['next_hour_activity_prob']}%",
                    help="Likelihood of activity in the next hour based on historical patterns"
                )
        st.subheader("Recent Trends Analysis")
        recent_data = df.tail(50)
        fig_trends = make_subplots(
            rows=3, cols=1,
            subplot_titles=['Temperature Trend', 'Humidity Trend', 'Activity Pattern'],
            vertical_spacing=0.08,
            specs=[[{"secondary_y": False}], [{"secondary_y": False}], [{"secondary_y": False}]]
        )
        fig_trends.add_trace(
            go.Scatter(x=recent_data['timestamp'], y=recent_data['temperature'],
                      mode='lines+markers', name='Temperature', line_color='red', marker_size=4),
            row=1, col=1
        )
        if len(recent_data) > 5:
            z = np.polyfit(range(len(recent_data)), recent_data['temperature'], 1)
            trend_line = np.poly1d(z)(range(len(recent_data)))
            fig_trends.add_trace(
                go.Scatter(x=recent_data['timestamp'], y=trend_line,
                          mode='lines', name='Temp Trend', line=dict(dash='dash', color='red')),
                row=1, col=1
            )
        fig_trends.add_trace(
            go.Scatter(x=recent_data['timestamp'], y=recent_data['humidity'],
                      mode='lines+markers', name='Humidity', line_color='blue', marker_size=4),
            row=2, col=1
        )
        fig_trends.add_trace(
            go.Scatter(x=recent_data['timestamp'], y=recent_data['is_active'],
                      mode='markers', name='Activity', marker=dict(color='green', size=8)),
            row=3, col=1
        )
        fig_trends.update_layout(height=600, showlegend=False)
        st.plotly_chart(fig_trends, use_container_width=True)
    with tab4:
        st.subheader("Behavioral Insights")
        if behavioral_insights:
            col1, col2 = st.columns(2)
            with col1:
                if 'most_active_period' in behavioral_insights:
                    st.success(f"Most Active Period: {behavioral_insights['most_active_period']}")
                if 'routine_consistency' in behavioral_insights:
                    consistency = behavioral_insights['routine_consistency']
                    if consistency == 'High':
                        st.success(f"Routine Consistency: {consistency} - Very predictable schedule")
                    elif consistency == 'Medium':
                        st.warning(f"Routine Consistency: {consistency} - Somewhat predictable schedule")
                    else:
                        st.info(f"Routine Consistency: {consistency} - Variable schedule")
                if 'preferred_temp_range' in behavioral_insights:
                    temp_prefs = behavioral_insights['preferred_temp_range']
                    st.info(f"Preferred Temperature Range: {temp_prefs['min']:.1f}°C - {temp_prefs['max']:.1f}°C")
                    st.info(f"Average Preferred Temp: {temp_prefs['avg']:.1f}°C")
            with col2:
                if 'activity_periods' in behavioral_insights:
                    periods_data = []
                    for period, rate in behavioral_insights['activity_periods'].items():
                        periods_data.append({'Period': period, 'Activity Rate': rate * 100})
                    periods_df = pd.DataFrame(periods_data)
                    fig_periods = px.bar(periods_df, x='Period', y='Activity Rate',
                                       title="Activity Rate by Time Period",
                                       color='Activity Rate', color_continuous_scale='Viridis')
                    fig_periods.update_layout(height=350)
                    st.plotly_chart(fig_periods, use_container_width=True)
        else:
            st.info("Need more data to generate behavioral insights. Keep collecting data!")
    with tab5:
        st.subheader("Smart Recommendations")
        if recommendations:
            for i, rec in enumerate(recommendations):
                with st.expander(f"{rec['priority']} Priority: {rec['title']}", expanded=(rec['priority'] == 'High')):
                    if rec['priority'] == 'High':
                        st.error(f"{rec['title']}")
                    elif rec['priority'] == 'Medium':
                        st.warning(f"{rec['title']}")
                    else:
                        st.info(f"{rec['title']}")
                    col1, col2 = st.columns([2, 1])
                    with col1:
                        st.write(f"Issue: {rec['description']}")
                        st.write(f"Recommended Action: {rec['action']}")
                    with col2:
                        st.write(f"Category: {rec['type']}")
                        st.write(f"Priority: {rec['priority']}")
        else:
            st.success("Everything looks optimal! No immediate recommendations.")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.info("Data Quality\nSensor readings are consistent")
            with col2:
                battery_level = df['battery_voltage'].iloc[-1]
                if battery_level >= 3.1:
                    st.info(f"Battery Health\nGood at {battery_level:.2f}V")
            with col3:
                comfort_avg = df['comfort_score'].mean()
                if comfort_avg >= 70:
                    st.info(f"Comfort Level\nGood at {comfort_avg:.0f}/100")
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("Recent Data")
    st.dataframe(df.tail(10), use_container_width=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
