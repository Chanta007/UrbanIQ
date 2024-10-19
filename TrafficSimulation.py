import random

class TrafficSimulation:
    def __init__(self, vehicle_manager, traffic_light_controller, route_planner):
        self.vehicle_manager = vehicle_manager
        self.traffic_light_controller = traffic_light_controller
        self.route_planner = route_planner
        self.vehicles = []  # List to store active vehicles in the simulation
        self.zones = []  # List to store active vzonesehicles in the simulation
        self.is_running = False

    def start_simulation(self, duration=30):
        if not self.is_running:
            self.is_running = True
            self.vehicles = self.generate_initial_vehicles()
            return {"message": f"Traffic simulation started for {duration} seconds with {len(self.vehicles)} vehicles."}
        return {"message": "Simulation is already running."}

    def pause_simulation(self):
        if self.is_running:
            self.is_running = False
            return {"message": "Traffic simulation paused."}
        return {"message": "No simulation is running to pause."}

    def stop_simulation(self):
        if self.is_running:
            self.is_running = False
            self.vehicles.clear()  # Clear all vehicles
            return {"message": "Traffic simulation stopped and reset."}
        return {"message": "No simulation is running to stop."}

    def generate_initial_vehicles(self, count=20):
        # Generate an initial set of vehicles (e.g., cars, lorries, bikes)
        vehicles = []
        for _ in range(count):
            vehicle_type = random.choice(['Car', 'Lorry', 'Bike'])
            vehicle = {"type": vehicle_type, "position": self.random_position()}
            vehicles.append(vehicle)
        return vehicles

    def random_position(self):
        # Generates a random position (for now, represented as x, y coordinates)
        return {"x": random.randint(0, 100), "y": random.randint(0, 100)}

    def get_traffic_status(self):
        if self.is_running:
            return {"message": "Simulation is running.", "vehicles": self.vehicles}
        return {"message": "Simulation is not running."}

# Example Usage:
# vehicle_manager, traffic_light_controller, route_planner are passed from the main app

# Example Usage:
# traffic_simulation = TrafficSimulation()
# print(traffic_simulation.start_simulation())
# print(traffic_simulation.get_traffic_status())
# print(traffic_simulation.pause_simulation())
# print(traffic_simulation.stop_simulation())
