import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor, IsolationForest, RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, classification_report, accuracy_score
from sklearn.preprocessing import StandardScaler
import joblib
import os
from pathlib import Path

class IoTPredictor:
    def __init__(self):
        self.temp_model = None
        self.occupancy_model = None
        self.anomaly_detector = None
        self.scaler = StandardScaler()
        
        # Create models directory
        self.models_dir = Path(__file__).parent.parent / "models"
        self.models_dir.mkdir(parents=True, exist_ok=True)
    
    def train_temperature_predictor(self, df):
        """Predict future temperature based on time and humidity"""
        features = ['hour', 'humidity', 'motion_counts']
        X = df[features].fillna(df[features].mean())
        y = df['temperature']
        
        if len(X) < 10:  # Need minimum data
            return 0.0
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        self.temp_model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.temp_model.fit(X_train, y_train)
        
        score = self.temp_model.score(X_test, y_test) if len(X_test) > 0 else 0.0
        return score
    
    def train_occupancy_predictor(self, df):
        """Train occupancy prediction model"""
        features = ['hour', 'temperature', 'humidity', 'motion_counts']
        X = df[features].fillna(df[features].mean())
        y = (df['motion_state'] == 'Activity').astype(int)
        
        if len(X) < 10:
            return 0.0
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        self.occupancy_model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.occupancy_model.fit(X_train, y_train)
        
        score = self.occupancy_model.score(X_test, y_test) if len(X_test) > 0 else 0.0
        return score
    
    def train_anomaly_detector(self, df):
        """Train anomaly detection model"""
        features = ['temperature', 'humidity', 'motion_counts', 'battery_voltage']
        X = df[features].fillna(df[features].mean())
        
        if len(X) < 20:
            return 0.0
        
        X_scaled = self.scaler.fit_transform(X)
        
        self.anomaly_detector = IsolationForest(contamination=0.1, random_state=42)
        self.anomaly_detector.fit(X_scaled)
        
        return 1.0  # Always returns success for unsupervised
    
    def predict_next_hour_temperature(self, hour, humidity, motion_counts):
        """Predict temperature for next hour"""
        if self.temp_model:
            return self.temp_model.predict([[hour, humidity, motion_counts]])[0]
        return None
    
    def predict_occupancy(self, hour, temperature, humidity, motion_counts):
        """Predict occupancy probability"""
        if self.occupancy_model:
            prob = self.occupancy_model.predict_proba([[hour, temperature, humidity, motion_counts]])
            return prob[0][1]  # Probability of occupancy
        return None
    
    def detect_anomaly(self, temperature, humidity, motion_counts, battery_voltage):
        """Detect if current readings are anomalous"""
        if self.anomaly_detector:
            X = [[temperature, humidity, motion_counts, battery_voltage]]
            X_scaled = self.scaler.transform(X)
            return self.anomaly_detector.predict(X_scaled)[0] == -1
        return False
    
    def save_models(self, path=None):
        """Save trained models"""
        if path is None:
            path = self.models_dir
        else:
            path = Path(path)
        
        path.mkdir(parents=True, exist_ok=True)
        
        try:
            if self.temp_model:
                joblib.dump(self.temp_model, path / "temperature_model.pkl")
                print(f"Temperature model saved to {path / 'temperature_model.pkl'}")
            
            if self.occupancy_model:
                joblib.dump(self.occupancy_model, path / "occupancy_model.pkl")
                print(f"Occupancy model saved to {path / 'occupancy_model.pkl'}")
            
            if self.anomaly_detector:
                joblib.dump(self.anomaly_detector, path / "anomaly_detector.pkl")
                joblib.dump(self.scaler, path / "scaler.pkl")
                print(f"Anomaly detector saved to {path / 'anomaly_detector.pkl'}")
                
        except Exception as e:
            print(f"Error saving models: {e}")
    
    def load_models(self, path=None):
        """Load pre-trained models"""
        if path is None:
            path = self.models_dir
        else:
            path = Path(path)
        
        try:
            temp_path = path / "temperature_model.pkl"
            if temp_path.exists():
                self.temp_model = joblib.load(temp_path)
                print("Temperature model loaded")
            
            occ_path = path / "occupancy_model.pkl"
            if occ_path.exists():
                self.occupancy_model = joblib.load(occ_path)
                print("Occupancy model loaded")
            
            anom_path = path / "anomaly_detector.pkl"
            scaler_path = path / "scaler.pkl"
            if anom_path.exists() and scaler_path.exists():
                self.anomaly_detector = joblib.load(anom_path)
                self.scaler = joblib.load(scaler_path)
                print("Anomaly detector loaded")
                
        except Exception as e:
            print(f"Error loading models: {e}")
    
    def train_all_models(self, df):
        """Train all models at once"""
        results = {}
        
        print("Training temperature predictor...")
        results['temperature_score'] = self.train_temperature_predictor(df)
        
        print("Training occupancy predictor...")
        results['occupancy_score'] = self.train_occupancy_predictor(df)
        
        print("Training anomaly detector...")
        results['anomaly_score'] = self.train_anomaly_detector(df)
        
        print("Saving models...")
        self.save_models()
        
        return results

# Example usage function
def train_models_from_data(csv_path):
    """Train models from CSV data"""
    try:
        df = pd.read_csv(csv_path)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df['hour'] = df['timestamp'].dt.hour
        
        predictor = IoTPredictor()
        results = predictor.train_all_models(df)
        
        print("\nTraining Results:")
        for model, score in results.items():
            print(f"{model}: {score:.3f}")
        
        return predictor, results
        
    except Exception as e:
        print(f"Error training models: {e}")
        return None, {}

if __name__ == "__main__":
    # Train models if run directly
    csv_path = "./data/processed/sensor_data.csv"
    if os.path.exists(csv_path):
        predictor, results = train_models_from_data(csv_path)
    else:
        print(f"Data file not found: {csv_path}")