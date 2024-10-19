class SimulationSettings:
    def __init__(self):
        # Default settings for the simulation
        self.traffic_density = 1.0  # 1.0 is normal density, >1.0 is higher traffic, <1.0 is lower traffic
        self.weather_condition = "clear"  # Current weather condition
        self.vehicle_priorities = {
            "emergency_vehicle": 1,
            "electric_vehicle": 2,
            "public_transport": 3,
            "school_zone": 4,
            "normal_vehicle": 5
        }

    def update_traffic_density(self, density):
        # Update the traffic density in the simulation
        if 0 <= density <= 2:
            self.traffic_density = density
            return {"message": f"Traffic density updated to {density}"}
        else:
            return {"error": "Invalid traffic density. Must be between 0 and 2."}

    def update_weather_condition(self, weather_condition):
        # Update the weather condition in the simulation
        valid_conditions = ["clear", "rain", "fog", "snow"]
        if weather_condition in valid_conditions:
            self.weather_condition = weather_condition
            return {"message": f"Weather condition updated to {weather_condition}"}
        else:
            return {"error": f"Invalid weather condition. Valid options are {valid_conditions}"}

    def update_vehicle_priorities(self, new_priorities):
        # Update vehicle prioritization rules
        valid_vehicle_types = {"emergency_vehicle", "electric_vehicle", "public_transport", "school_zone", "normal_vehicle"}
        if all(key in valid_vehicle_types for key in new_priorities):
            self.vehicle_priorities.update(new_priorities)
            return {"message": "Vehicle priorities updated", "priorities": self.vehicle_priorities}
        else:
            return {"error": "Invalid vehicle types in priorities"}

    def get_simulation_settings(self):
        # Return the current settings for traffic, weather, and priorities
        return {
            "traffic_density": self.traffic_density,
            "weather_condition": self.weather_condition,
            "vehicle_priorities": self.vehicle_priorities
        }

# Example Usage:
simulation_settings = SimulationSettings()

# Update traffic density
print(simulation_settings.update_traffic_density(1.5))  # Increases traffic density

# Update weather condition
print(simulation_settings.update_weather_condition("rain"))  # Changes weather to rain

# Update vehicle priorities (e.g., making electric vehicles higher priority)
new_priorities = {"electric_vehicle": 1, "public_transport": 2}
print(simulation_settings.update_vehicle_priorities(new_priorities))

# Get current simulation settings
print(simulation_settings.get_simulation_settings())
