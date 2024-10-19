from flask import Flask, jsonify, request
from SimulationMetrics import SimulationMetrics
from SimulationSettings import SimulationSettings
from MapRenderer import MapRenderer
from PrioritizationEngine import PrioritizationEngine


class WebUIController:
    def __init__(self, simulation_settings, map_renderer, prioritization_engine, simulation_metrics):
        # Initialize the controller with references to core components
        self.simulation_settings = simulation_settings
        self.map_renderer = map_renderer
        self.prioritization_engine = prioritization_engine
        self.simulation_metrics = simulation_metrics
        self.app = Flask(__name__)
        self.configure_routes()

    def configure_routes(self):
        # Configure API routes for the web interface

        @self.app.route('/update-settings', methods=['POST'])
        def update_settings():
            # Receive JSON data from the frontend to update simulation settings
            data = request.json
            if 'traffic_density' in data:
                response = self.simulation_settings.update_traffic_density(data['traffic_density'])
            if 'weather_condition' in data:
                response = self.simulation_settings.update_weather_condition(data['weather_condition'])
            if 'vehicle_priorities' in data:
                response = self.simulation_settings.update_vehicle_priorities(data['vehicle_priorities'])
            return jsonify(response)

        @self.app.route('/get-settings', methods=['GET'])
        def get_settings():
            # Return the current simulation settings
            return jsonify(self.simulation_settings.get_simulation_settings())

        @self.app.route('/get-map', methods=['GET'])
        def get_map():
            # Return the current map state (vehicles, traffic lights, zones)
            self.map_renderer.update_map()  # Update the map
            # In a real system, you'd return the map data here (mocked for now)
            return jsonify({"message": "Map updated", "map": "Simulated map data"})

        @self.app.route('/get-metrics', methods=['GET'])
        def get_metrics():
            # Return the current metrics (air quality, traffic reduction, etc.)
            return jsonify(self.simulation_metrics.get_metrics())

        @self.app.route('/get-prioritized-vehicles', methods=['GET'])
        def get_prioritized_vehicles():
            # Return the current list of prioritized vehicles
            vehicles = self.map_renderer.vehicles  # List of vehicles
            zones = self.map_renderer.zones  # List of zones (e.g., school zones)
            weather_effect = {"speed_factor": 1.0}  # Example weather effect (clear weather)
            prioritized_vehicles = self.prioritization_engine.prioritize_traffic(vehicles, zones, weather_effect)
            return jsonify([{"vehicle_type": vehicle.vehicle_type, "position": vehicle.get_position()} for vehicle in prioritized_vehicles])

    def send_map_updates(self):
        # Logic to send real-time map updates to the web UI
        self.map_renderer.update_map()  # Simulate updating the map
        # In a real application, this would push updates to the frontend via WebSockets, or similar

    def handle_user_input(self):
        # Logic to handle user inputs from the web UI (like adjusting settings)
        pass

    def run(self):
        # Start the Flask app (server)
        self.app.run(debug=True)

# Example of how this would be used with the other components
simulation_settings = SimulationSettings()
map_renderer = MapRenderer()
prioritization_engine = PrioritizationEngine()
simulation_metrics = SimulationMetrics()

web_ui_controller = WebUIController(simulation_settings, map_renderer, prioritization_engine, simulation_metrics)
# To run the Flask server:
# web_ui_controller.run()
