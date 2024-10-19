class RiskAssessmentEngine:
    def __init__(self):
        self.weather_risk = 0.0  # Risk due to weather conditions
        self.traffic_density_risk = 0.0  # Risk due to traffic density (congestion)
        self.accident_risk = 0.0  # Risk of accidents based on vehicle behavior
        self.overall_risk_score = 0.0  # Composite risk score

    def assess_weather_risk(self, weather_condition):
        # Assess the risk based on the current weather condition
        if weather_condition == "clear":
            self.weather_risk = 0  # No risk in clear weather
        elif weather_condition == "rain":
            self.weather_risk = 30  # Moderate risk due to rain
        elif weather_condition == "fog":
            self.weather_risk = 50  # High risk due to reduced visibility
        elif weather_condition == "snow":
            self.weather_risk = 70  # Very high risk due to snow/ice
        else:
            self.weather_risk = 10  # Default risk for unknown conditions

        return {"message": f"Weather risk assessed: {self.weather_risk}"}

    def assess_traffic_density_risk(self, traffic_density):
        # Assess the risk based on traffic density (0 to 2.0 scale)
        if traffic_density < 0.5:
            self.traffic_density_risk = 10  # Low risk (light traffic)
        elif traffic_density < 1.0:
            self.traffic_density_risk = 30  # Moderate risk
        elif traffic_density < 1.5:
            self.traffic_density_risk = 50  # High risk (heavy traffic)
        else:
            self.traffic_density_risk = 70  # Very high risk (severe congestion)

        return {"message": f"Traffic density risk assessed: {self.traffic_density_risk}"}

    def assess_accident_risk(self, vehicle_behavior):
        # Assess the risk of accidents based on vehicle behavior (e.g., speeding, erratic movement)
        if vehicle_behavior == "normal":
            self.accident_risk = 10  # Low risk
        elif vehicle_behavior == "speeding":
            self.accident_risk = 50  # High risk due to speeding
        elif vehicle_behavior == "erratic":
            self.accident_risk = 70  # Very high risk due to dangerous driving
        else:
            self.accident_risk = 20  # Default risk for unknown behavior

        return {"message": f"Accident risk assessed: {self.accident_risk}"}

    def calculate_overall_risk(self):
        # Combine the different risk factors to calculate an overall risk score
        self.overall_risk_score = (self.weather_risk * 0.3) + (self.traffic_density_risk * 0.4) + (self.accident_risk * 0.3)
        return {"overall_risk_score": self.overall_risk_score}

    def get_risk_report(self):
        # Return a report summarizing the risk factors and overall score
        return {
            "weather_risk": self.weather_risk,
            "traffic_density_risk": self.traffic_density_risk,
            "accident_risk": self.accident_risk,
            "overall_risk_score": self.overall_risk_score
        }

# Example Usage
risk_engine = RiskAssessmentEngine()

# Assess weather risk (e.g., rain)
print(risk_engine.assess_weather_risk("rain"))

# Assess traffic density risk (e.g., moderate traffic density)
print(risk_engine.assess_traffic_density_risk(1.2))

# Assess accident risk (e.g., speeding vehicles)
print(risk_engine.assess_accident_risk("speeding"))

# Calculate the overall risk score based on the assessed factors
print(risk_engine.calculate_overall_risk())

# Get a report summarizing the risk factors and overall risk score
print(risk_engine.get_risk_report())
