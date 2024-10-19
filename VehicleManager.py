from PrioritizationEngine import PrioritizationEngine
from TrafficLightController import TrafficLightController
from Vehicle import Bike
from Vehicle import Car


class VehicleManager:
    def __init__(self, prioritization_engine, traffic_light_controller):
        self.vehicles = []  # List to store all vehicles in the simulation
        self.prioritization_engine = prioritization_engine
        self.traffic_light_controller = traffic_light_controller

    def add_vehicle(self, vehicle):
        # Add a new vehicle to the simulation
        self.vehicles.append(vehicle)
        return {"message": f"{vehicle.vehicle_type} added to the simulation."}

    def remove_vehicle(self, vehicle):
        # Remove a vehicle from the simulation
        if vehicle in self.vehicles:
            self.vehicles.remove(vehicle)
            return {"message": f"{vehicle.vehicle_type} removed from the simulation."}
        return {"error": "Vehicle not found in the simulation."}

    def update_vehicle_positions(self):
        # Update the position of all vehicles based on movement logic
        for vehicle in self.vehicles:
            vehicle.move()
        return {"message": "All vehicle positions updated."}

    def get_vehicle_status(self):
        # Return the current status (position and type) of all vehicles
        status = []
        for vehicle in self.vehicles:
            status.append({
                "vehicle_type": vehicle.vehicle_type,
                "position": vehicle.get_position()
            })
        return status

    def prioritize_vehicles(self):
        # Prioritize vehicles based on current traffic conditions and rules
        zones = []  # Example: Pass zones like school zones (if applicable)
        weather_effect = {"speed_factor": 1.0}  # Example: Normal weather
        prioritized_vehicles = self.prioritization_engine.prioritize_traffic(self.vehicles, zones, weather_effect)
        return prioritized_vehicles


# Initialize PrioritizationEngine and TrafficLightController (already defined)
prioritization_engine = PrioritizationEngine()
traffic_light_controller = TrafficLightController()

# Initialize VehicleManager
vehicle_manager = VehicleManager(prioritization_engine, traffic_light_controller)

# Add vehicles to the simulation
car = Car({"x": 10, "y": 20})
bike = Bike({"x": 15, "y": 25})
print(vehicle_manager.add_vehicle(car))
print(vehicle_manager.add_vehicle(bike))

# Update vehicle positions
print(vehicle_manager.update_vehicle_positions())

# Get the current status of vehicles
print(vehicle_manager.get_vehicle_status())

# Prioritize vehicles
print(vehicle_manager.prioritize_vehicles())

# Remove a vehicle from the simulation
print(vehicle_manager.remove_vehicle(car))
