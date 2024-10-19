import json
import os

class DataStore:
    def __init__(self, file_path="simulation_data.json"):
        self.file_path = file_path

    def save_simulation_data(self, data):
        # Save simulation data to a JSON file
        try:
            with open(self.file_path, 'w') as f:
                json.dump(data, f, indent=4)
            return {"message": "Simulation data saved successfully"}
        except Exception as e:
            return {"error": f"Failed to save data: {str(e)}"}

    def load_simulation_data(self):
        # Load simulation data from a JSON file
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r') as f:
                    data = json.load(f)
                return data
            except Exception as e:
                return {"error": f"Failed to load data: {str(e)}"}
        else:
            return {"error": "No saved data found"}

    def delete_simulation_data(self):
        # Delete the simulation data file
        if os.path.exists(self.file_path):
            try:
                os.remove(self.file_path)
                return {"message": "Simulation data deleted successfully"}
            except Exception as e:
                return {"error": f"Failed to delete data: {str(e)}"}
        else:
            return {"error": "No data file to delete"}

    def save_metric_history(self, metrics):
        # Save the metrics history to a file
        history_file = "metrics_history.json"
        try:
            if os.path.exists(history_file):
                with open(history_file, 'r') as f:
                    history = json.load(f)
            else:
                history = []

            history.append(metrics)
            with open(history_file, 'w') as f:
                json.dump(history, f, indent=4)
            return {"message": "Metrics history saved successfully"}
        except Exception as e:
            return {"error": f"Failed to save metrics history: {str(e)}"}

    def load_metric_history(self):
        # Load the metrics history from a file
        history_file = "metrics_history.json"
        if os.path.exists(history_file):
            try:
                with open(history_file, 'r') as f:
                    history = json.load(f)
                return history
            except Exception as e:
                return {"error": f"Failed to load metrics history: {str(e)}"}
        else:
            return {"error": "No metrics history found"}

# Example Usage
data_store = DataStore()

# Save example simulation data
simulation_data = {
    "vehicles": [{"vehicle_type": "Car", "position": {"x": 10, "y": 20}}],
    "traffic_lights": [{"location": {"x": 50, "y": 50}, "state": "red"}],
    "zones": [{"type": "School Zone", "location": {"x": 20, "y": 30}}]
}
print(data_store.save_simulation_data(simulation_data))

# Load saved simulation data
print(data_store.load_simulation_data())

# Save example metrics history
metrics_data = {
    "air_quality_improvement": 10.5,
    "traffic_reduction": 20.0,
    "livability_score": 85.0,
    "noise_reduction": 15.0
}
print(data_store.save_metric_history(metrics_data))

# Load metrics history
print(data_store.load_metric_history())

# Delete simulation data
print(data_store.delete_simulation_data())
