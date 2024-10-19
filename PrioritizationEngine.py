
from Vehicle import Vehicle, Car, Bike, Lorry, ElectricVehicle, PublicTransport  # Import your vehicle classes here
from TrafficLight import TrafficLight


class PrioritizationEngine:
    def __init__(self):
        # Default prioritization rules
        self.default_prioritization_rules = {
            "emergency_vehicle": 1,   # Highest priority
            "electric_vehicle": 2,
            "public_transport": 3,
            "school_zone": 4,
            "normal_vehicle": 5       # Lowest priority
        }
        self.prioritization_rules = self.default_prioritization_rules.copy()

    def set_prioritization_rules(self, new_rules):
        # Update prioritization rules with new values
        self.prioritization_rules.update(new_rules)

    def reset_prioritization(self):
        # Reset prioritization rules to default values
        self.prioritization_rules = self.default_prioritization_rules.copy()
        return {"message": "Prioritization rules reset to default."}

    def prioritize_traffic(self, vehicles, zones, weather_effect):
        # Prioritize vehicles based on current conditions (weather, zones, etc.)
        prioritized_vehicles = sorted(
            vehicles, 
            key=lambda vehicle: self.calculate_priority(vehicle, zones, weather_effect)
        )
        return prioritized_vehicles

    def calculate_priority(self, vehicle, zones, weather_effect):
        # Adjust priority based on the vehicle type and zones they are in
        base_priority = self.prioritization_rules.get(vehicle.vehicle_type.lower(), 5)

        # Example adjustments:
        # Increase priority for vehicles in or near school zones
        for zone in zones:
            if zone['type'] == 'School Zone' and self.is_vehicle_in_zone(vehicle, zone):
                base_priority -= 1  # Boost priority in school zones (lower number is higher priority)

        # Adjust for weather conditions (reduce speed, increase importance of EVs during pollution)
        if weather_effect['speed_factor'] < 1.0 and vehicle.vehicle_type == 'Electric Vehicle':
            base_priority -= 1  # Boost priority for EVs in poor weather

        return base_priority

    def is_vehicle_in_zone(self, vehicle, zone):
        # Simple check to see if a vehicle is in a zone (could be more complex in a real system)
        vehicle_position = vehicle.get_position()
        zone_position = zone['location']
        return abs(vehicle_position['x'] - zone_position['x']) < 10 and abs(vehicle_position['y'] - zone_position['y']) < 10

# Example Usage:
prioritization_engine = PrioritizationEngine()

# Sample vehicles (already defined Car, ElectricVehicle, PublicTransport)
car = Car({'x': 20, 'y': 20})
ev = ElectricVehicle({'x': 15, 'y': 25})
bus = PublicTransport({'x': 30, 'y': 40})

# Sample zones (e.g., school zones)
zones = [{"type": "School Zone", "location": {"x": 20, "y": 20}}]

# Sample weather effect (from the WeatherSimulation class)
weather_effect = {"speed_factor": 0.8}  # Poor weather slowing down vehicles

# Prioritize traffic based on current conditions
vehicles = [car, ev, bus]
prioritized_vehicles = prioritization_engine.prioritize_traffic(vehicles, zones, weather_effect)

# Print prioritized vehicles
for vehicle in prioritized_vehicles:
    print(f"{vehicle.vehicle_type} at position {vehicle.get_position()} has priority.")

# Reset prioritization
print(prioritization_engine.reset_prioritization())
