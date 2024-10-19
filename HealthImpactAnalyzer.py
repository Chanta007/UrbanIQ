import math

class HealthImpactAnalyzer:
    def __init__(self):
        self.pollution_level = 0.0  # Air pollution level (e.g., PM2.5 index)
        self.noise_level = 0.0  # Noise pollution level (in decibels)
        self.health_impact_score = 0.0  # Composite health impact score

    def update_pollution_level(self, pollution_value):
        # Update the pollution level based on simulation data (e.g., vehicle emissions)
        self.pollution_level = pollution_value
        return {"message": f"Pollution level updated to {pollution_value}."}

    def update_noise_level(self, noise_value):
        # Update the noise level based on traffic and environment noise data
        self.noise_level = noise_value
        return {"message": f"Noise level updated to {noise_value} dB."}

    def calculate_health_impact(self):
        # Calculate a health impact score based on pollution and noise levels
        pollution_impact = self.calculate_pollution_impact(self.pollution_level)
        noise_impact = self.calculate_noise_impact(self.noise_level)
        
        # Combine pollution and noise impacts to get a health score (simplified formula)
        self.health_impact_score = (pollution_impact * 0.6) + (noise_impact * 0.4)
        return {
            "health_impact_score": self.health_impact_score,
            "pollution_level": self.pollution_level,
            "noise_level": self.noise_level
        }

    def calculate_pollution_impact(self, pollution_level):
        # Simple model to calculate pollution impact based on the pollution level
        if pollution_level <= 50:
            return 0  # No health impact
        elif pollution_level <= 100:
            return 25  # Minor impact
        elif pollution_level <= 150:
            return 50  # Moderate impact
        elif pollution_level <= 200:
            return 75  # Significant impact
        else:
            return 100  # Severe impact

    def calculate_noise_impact(self, noise_level):
        # Simple model to calculate noise impact based on noise levels
        if noise_level < 55:
            return 0  # Safe noise level
        elif noise_level < 70:
            return 25  # Minor impact
        elif noise_level < 85:
            return 50  # Moderate impact
        elif noise_level < 100:
            return 75  # Significant impact
        else:
            return 100  # Severe impact

    def get_health_impact_report(self):
        # Returns a summary report of the current health impact factors
        return {
            "pollution_level": self.pollution_level,
            "noise_level": self.noise_level,
            "health_impact_score": self.health_impact_score
        }

# Example Usage
health_analyzer = HealthImpactAnalyzer()

# Update pollution and noise levels based on the simulation
print(health_analyzer.update_pollution_level(120))  # Moderate pollution level
print(health_analyzer.update_noise_level(80))  # Significant noise level

# Calculate the overall health impact score
print(health_analyzer.calculate_health_impact())

# Get a summary report of the health impact
print(health_analyzer.get_health_impact_report())
