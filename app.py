from flask import Flask, jsonify, request, render_template
from VehicleManager import VehicleManager
from WeatherSimulation import WeatherSimulation
from TrafficSimulation import TrafficSimulation
from TrafficLightController import TrafficLightController
from RoutePlanner import RoutePlanner
from MapRenderer import MapRenderer
from PrioritizationEngine import PrioritizationEngine
from Vehicle import Ambulance

class App:
    def __init__(self):
        self.app = Flask(__name__)

        # Initialize backend components
        self.weather_simulation = WeatherSimulation()
        self.prioritization_engine = PrioritizationEngine()
        self.traffic_light_controller = TrafficLightController()
        self.map_renderer = MapRenderer()
        self.route_planner = RoutePlanner(self.map_renderer, self.traffic_light_controller)
        self.vehicle_manager = VehicleManager(self.prioritization_engine, self.traffic_light_controller)
        self.traffic_simulation = TrafficSimulation(self.vehicle_manager, self.traffic_light_controller, self.route_planner)

        self.configure_routes()

    def configure_routes(self):
        @self.app.route('/')
        def home():
            # Render index.html from the /templates directory
            return render_template('index.html')

        # Start traffic simulation
        @self.app.route('/simulate/traffic', methods=['POST'])
        def simulate_traffic():
            duration = request.json.get("duration", 30)  # Duration in seconds (default: 30)
            result = self.traffic_simulation.start_simulation(duration)
            return jsonify(result)

        # Trigger a weather change simulation
        @self.app.route('/simulate/weather', methods=['POST'])
        def simulate_weather():
            weather_change = self.weather_simulation.simulate_weather_change()
            return jsonify(weather_change)

        # Render the current state of the map
        @self.app.route('/map/render', methods=['GET'])
        def render_map():
            # Generate a map with vehicles, traffic lights, and zones
            rendered_map = {
                "vehicles": [
                    {
                        "type": vehicle['type'],
                        "position": vehicle['position']
                    }
                    for vehicle in self.traffic_simulation.vehicles
                ],
                "traffic_lights": [
                    {
                        "location": light['location'],
                        "state": light['state']
                    }
                    for light in self.traffic_simulation.traffic_light_controller.traffic_lights
                ],
                "zones": self.traffic_simulation.zones
            }
            return jsonify(rendered_map)


        # Prioritize traffic based on current conditions
        @self.app.route('/prioritize', methods=['POST'])
        def prioritize():
            prioritized_vehicles = self.prioritization_engine.prioritize_traffic(
                self.vehicle_manager.vehicles, [], self.weather_simulation.get_weather_effect())
            return jsonify({"prioritized_vehicles": [v.vehicle_type for v in prioritized_vehicles]})

        # Register an emergency vehicle (ambulance)
        @self.app.route('/emergency_vehicle', methods=['POST'])
        def register_emergency_vehicle():
            vehicle_type = request.json.get("vehicle_type", "ambulance")
            position = request.json.get("position", {"x": 0, "y": 0})
            destination = request.json.get("destination", {"x": 10, "y": 10})

            # Register vehicle and set destination
            if vehicle_type == "ambulance":
                vehicle = Ambulance(position)
            else:
                return jsonify({"error": "Invalid vehicle type"}), 400

            self.vehicle_manager.add_vehicle(vehicle)
            vehicle.set_destination(destination)
            return jsonify({"message": f"{vehicle_type} registered", "position": vehicle.get_position()})

        # Stop the simulation
        @self.app.route('/simulation/stop', methods=['POST'])
        def stop_simulation():
            result = self.traffic_simulation.stop_simulation()
            return jsonify(result)

    def run(self):
        # Start the Flask app
        self.app.run(debug=True)


# To run the app:
if __name__ == '__main__':
    app = App()
    app.run()
