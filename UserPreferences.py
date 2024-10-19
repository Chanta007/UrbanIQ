import json
import os

class UserPreferences:
    def __init__(self, file_path="user_preferences.json"):
        self.file_path = file_path
        self.preferences = {
            "traffic_density": 1.0,
            "weather_condition": "clear",
            "vehicle_priorities": {
                "emergency_vehicle": 1,
                "electric_vehicle": 2,
                "public_transport": 3,
                "school_zone": 4,
                "normal_vehicle": 5
            },
            "map_settings": {
                "zoom_level": 1.0,
                "view_area": "Emory College Campus"
            }
        }

    def load_preferences(self):
        # Load user preferences from a JSON file
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r') as f:
                    self.preferences = json.load(f)
                return self.preferences
            except Exception as e:
                return {"error": f"Failed to load preferences: {str(e)}"}
        else:
            return {"message": "No preferences file found. Using default preferences."}

    def save_preferences(self):
        # Save user preferences to a JSON file
        try:
            with open(self.file_path, 'w') as f:
                json.dump(self.preferences, f, indent=4)
            return {"message": "Preferences saved successfully"}
        except Exception as e:
            return {"error": f"Failed to save preferences: {str(e)}"}

    def update_preferences(self, new_preferences):
        # Update the user preferences with new settings
        self.preferences.update(new_preferences)
        return self.save_preferences()

    def get_preferences(self):
        # Return the current user preferences
        return self.preferences

# Example Usage:
user_prefs = UserPreferences()

# Load user preferences
print(user_prefs.load_preferences())

# Update user preferences (e.g., changing the traffic density and zoom level)
new_prefs = {
    "traffic_density": 1.5,
    "map_settings": {"zoom_level": 1.2}
}
print(user_prefs.update_preferences(new_prefs))

# Get current preferences
print(user_prefs.get_preferences())

# Save the current preferences
print(user_prefs.save_preferences())
