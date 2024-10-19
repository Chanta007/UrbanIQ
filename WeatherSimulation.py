class WeatherSimulation:
    def __init__(self):
        self.current_weather = "clear"  # Default weather condition
        self.weather_effects = {
            "clear": {"speed_factor": 1.0},
            "rain": {"speed_factor": 0.7},
            "fog": {"speed_factor": 0.5},
            "snow": {"speed_factor": 0.4}
        }

    def set_weather(self, weather_condition):
        if weather_condition in self.weather_effects:
            self.current_weather = weather_condition
            return {"message": f"Weather changed to {weather_condition}"}
        return {"error": "Invalid weather condition"}

    def get_weather(self):
        return {"current_weather": self.current_weather}

    def get_weather_effect(self):
        # Return the effect the current weather has on traffic (e.g., speed reduction)
        return self.weather_effects[self.current_weather]

    def simulate_weather_change(self, new_weather):
        # Simulate a dynamic change in weather over time
        self.set_weather(new_weather)
        return self.get_weather()

# Example Usage:
weather_simulation = WeatherSimulation()

# Set a new weather condition
print(weather_simulation.set_weather("rain"))  # Changes weather to rain

# Get the current weather condition
print(weather_simulation.get_weather())  # Returns the current weather

# Get the effect of current weather on traffic
print(weather_simulation.get_weather_effect())  # Returns the speed reduction factor for the current weather
