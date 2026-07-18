import time
import random
import json
from datetime import datetime

class PrecisionSoilMonitor:
    def __init__(self, threshold_moisture=35.0):
        # Moisture percentage below which alert triggers
        self.threshold_moisture = threshold_moisture
        print("[System Initialized] Precision Soil Monitoring Engine Active.\n")

    def read_sensor_data(self):
        """Simulates real-time IoT sensor telemetry data."""
        return {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "moisture_percentage": round(random.uniform(15.0, 60.0), 2),
            "temperature_celsius": round(random.uniform(22.0, 40.0), 2),
            "nitrogen_level_mg_kg": round(random.uniform(10.0, 50.0), 2)
        }

    def evaluate_resource_need(self, telemetry):
        """AI rule-engine classifying irrigation urgency based on data points."""
        moisture = telemetry["moisture_percentage"]
        temp = telemetry["temperature_celsius"]
        
        if moisture < self.threshold_moisture and temp > 30.0:
            return "CRITICAL: Severe Water Scarcity Detected. Deploy Irrigation Immediately."
        elif moisture < self.threshold_moisture:
            return "WARNING: Low Soil Moisture. Schedule Irrigation."
        else:
            return "OPTIMAL: Resource Levels Satisfactory."

    def run_session(self, cycles=5):
        """Runs the telemetry loop and logs findings."""
        session_logs = []
        for i in range(1, cycles + 1):
            print(f"--- Fetching Telemetry Cycle {i}/{cycles} ---")
            data = self.read_sensor_data()
            status = self.evaluate_resource_need(data)
            
            log_entry = {
                "telemetry": data,
                "status_assessment": status
            }
            session_logs.append(log_entry)
            
            print(f"Timestamp: {data['timestamp']}")
            print(f"Moisture: {data['moisture_percentage']}% | Temp: {data['temperature_celsius']}°C")
            print(f"Assessment: {status}\n")
            time.sleep(1) # Simulates delay between sensor readings
            
        self.save_report(session_logs)

    def save_report(self, logs):
        """Saves session execution logs to a structured JSON file."""
        filename = "soil_health_report.json"
        with open(filename, "w") as f:
            json.dump(logs, f, indent=4)
        print(f"[Data Pipeline] Execution session successfully saved to {filename}")

if __name__ == "__main__":
    # Initialize engine with a standard 35% moisture threshold
    monitor = PrecisionSoilMonitor(threshold_moisture=35.0)
    monitor.run_session(cycles=5)