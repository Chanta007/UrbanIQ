from RoutePlanner import RoutePlanner
from TrafficLightController import TrafficLightController
from PrioritizationEngine import PrioritizationEngine
from Vehicle import Ambulance

class EmergencyVehicleCoordinator:
    def __init__(self, route_planner, traffic_light_controller, prioritization_engine):
        self.route_planner = route_planner
        self.traffic_light_controller = traffic_light_controller
        self.prioritization_engine = prioritization_engine
        self.active_emergency_vehicles = []

    def register_emergency_vehicle(self, vehicle, destination):
        # Register the emergency vehicle and assign a route
        vehicle.set_destination(destination)  # Set the destination
        self.active_emergency_vehicles.append(vehicle)
        route = self.route_planner.calculate_priority_route(vehicle, destination)
        self.prioritize_vehicle(vehicle)
        self.control_traffic_lights(vehicle)
        return {
            "message": f"Emergency vehicle {vehicle.vehicle_type} registered and routed.",
            "route": route
        }

    def prioritize_vehicle(self, vehicle):
        # Give the emergency vehicle the highest priority
        self.prioritization_engine.set_prioritization_rules({
            vehicle.vehicle_type.lower(): 0  # Highest priority
        })
        return {"message": f"{vehicle.vehicle_type} given highest priority."}

    def control_traffic_lights(self, vehicle):
        # Control traffic lights to ensure green lights for emergency vehicles
        vehicle_position = vehicle.get_position()
        for light in self.traffic_light_controller.traffic_lights:
            if light.location == vehicle_position:
                self.traffic_light_controller.change_traffic_light_priority(light.location, "green")
        return {"message": f"Traffic lights adjusted for {vehicle.vehicle_type}."}

    def update_emergency_vehicle_routes(self):
        # Continuously update the routes of all emergency vehicles
        for vehicle in self.active_emergency_vehicles:
            if hasattr(vehicle, 'destination'):
                route = self.route_planner.calculate_priority_route(vehicle, vehicle.destination)
                self.control_traffic_lights(vehicle)
            else:
                return {"error": f"{vehicle.vehicle_type} does not have a destination set."}
        return {"message": "Emergency vehicle routes updated."}

    def remove_emergency_vehicle(self, vehicle):
        # Remove an emergency vehicle after its task is complete
        if vehicle in self.active_emergency_vehicles:
            self.active_emergency_vehicles.remove(vehicle)
            self.prioritization_engine.reset_prioritization()
            return {"message": f"Emergency vehicle {vehicle.vehicle_type} removed."}
        return {"error": "Emergency vehicle not found."}

    def get_active_emergency_vehicles(self):
        # Return a list of all active emergency vehicles
        return [{"vehicle_type": vehicle.vehicle_type, "position": vehicle.get_position()} for vehicle in self.active_emergency_vehicles]


# Example Usage
from VehicleManager import VehicleManager
from MapRenderer import MapRenderer
from PrioritizationEngine import PrioritizationEngine
from TrafficLightController import TrafficLightController

# Initialize dependencies
route_planner = RoutePlanner(MapRenderer(), TrafficLightController())
traffic_light_controller = TrafficLightController()
prioritization_engine = PrioritizationEngine()

# Initialize EmergencyVehicleCoordinator
ev_coordinator = EmergencyVehicleCoordinator(route_planner, traffic_light_controller, prioritization_engine)

# Add a sample emergency vehicle (ambulance) and set its route
ambulance = Ambulance({"x": 10, "y": 20})
destination = {"x": 50, "y": 60}
print(ev_coordinator.register_emergency_vehicle(ambulance, destination))

# Update emergency vehicle routes
print(ev_coordinator.update_emergency_vehicle_routes())

# Get active emergency vehicles
print(ev_coordinator.get_active_emergency_vehicles())

# Remove the emergency vehicle after its task
print(ev_coordinator.remove_emergency_vehicle(ambulance))
