from MapRenderer import MapRenderer
from TrafficLightController import TrafficLightController
from Vehicle import Car


class RoutePlanner:
    def __init__(self, map_renderer, traffic_light_controller):
        self.map_renderer = map_renderer  # Reference to the map for route planning
        self.traffic_light_controller = traffic_light_controller  # Reference to traffic lights

    def calculate_route(self, vehicle, destination):
        # Basic route calculation (can be enhanced with real map data and algorithms like A*)
        vehicle_position = vehicle.get_position()
        route = []
        
        # Simple straight-line path (this is a placeholder; can be replaced with advanced routing)
        if vehicle_position['x'] < destination['x']:
            route.append("move right")
        elif vehicle_position['x'] > destination['x']:
            route.append("move left")
        
        if vehicle_position['y'] < destination['y']:
            route.append("move up")
        elif vehicle_position['y'] > destination['y']:
            route.append("move down")

        return {
            "vehicle_type": vehicle.vehicle_type,
            "current_position": vehicle_position,
            "destination": destination,
            "route": route
        }

    def reroute_due_to_traffic_light(self, vehicle):
        # If the traffic light at the vehicle's position is red, reroute the vehicle
        vehicle_position = vehicle.get_position()
        for light in self.traffic_light_controller.traffic_lights:
            if light.location == vehicle_position and light.state == "red":
                # Simple rerouting example (could be expanded to a full reroute algorithm)
                return {"message": f"Rerouting {vehicle.vehicle_type} due to red light at {vehicle_position}."}
        return {"message": f"No reroute needed for {vehicle.vehicle_type} at {vehicle_position}."}

    def optimize_route_for_priority(self, vehicle, destination, prioritized_vehicles):
        # Adjust the route to give priority to certain vehicles
        if vehicle in prioritized_vehicles:
            return self.calculate_priority_route(vehicle, destination)
        return self.calculate_route(vehicle, destination)

    def calculate_priority_route(self, vehicle, destination):
        # Prioritized vehicles take the most direct route, ignoring normal traffic constraints
        # (For simplicity, this method currently just calculates a straight-line route)
        return self.calculate_route(vehicle, destination)


# Initialize MapRenderer and TrafficLightController (already defined)
map_renderer = MapRenderer()
traffic_light_controller = TrafficLightController()

# Initialize RoutePlanner
route_planner = RoutePlanner(map_renderer, traffic_light_controller)

# Add a car and calculate its route
car = Car({"x": 10, "y": 20})
destination = {"x": 30, "y": 40}
print(route_planner.calculate_route(car, destination))

# Simulate rerouting due to a red traffic light
print(route_planner.reroute_due_to_traffic_light(car))

# Optimize the route for a high-priority vehicle
prioritized_vehicles = [car]  # Example: Car is high-priority
print(route_planner.optimize_route_for_priority(car, destination, prioritized_vehicles))
