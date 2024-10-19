from TrafficSimulation import TrafficSimulation
from WeatherSimulation import WeatherSimulation
from MapRenderer import MapRenderer
from PrioritizationEngine import PrioritizationEngine
from EmergencyResponseManager import EmergencyResponseManager
from NotificationSystem import NotificationSystem
from Vehicle import Ambulance

class SimulationController:
    def __init__(self, traffic_simulation, weather_simulation, map_renderer, prioritization_engine, emergency_manager, notification_system):
        self.traffic_simulation = traffic_simulation
        self.weather_simulation = weather_simulation
        self.map_renderer = map_renderer
        self.prioritization_engine = prioritization_engine
        self.emergency_manager = emergency_manager
        self.notification_system = notification_system
        self.running = False

    def start_simulation(self):
        if not self.running:
            self.running = True
            self.traffic_simulation.start_simulation()
            self.notification_system.send_notification("Simulation started.", "info")
            return {"message": "Simulation started."}
        return {"error": "Simulation is already running."}

    def pause_simulation(self):
        if self.running:
            self.traffic_simulation.pause_simulation()
            self.running = False
            self.notification_system.send_notification("Simulation paused.", "info")
            return {"message": "Simulation paused."}
        return {"error": "Simulation is not running."}

    def stop_simulation(self):
        if self.running:
            self.traffic_simulation.stop_simulation()
            self.running = False
            self.notification_system.send_notification("Simulation stopped.", "info")
            return {"message": "Simulation stopped and reset."}
        return {"error": "Simulation is not running."}

    def update_weather(self, new_weather):
        response = self.weather_simulation.simulate_weather_change(new_weather)
        self.notification_system.send_notification(f"Weather updated to {new_weather}.", "weather")
        return response

    def handle_emergency(self, vehicle, emergency_type):
        # Register the emergency vehicle in the emergency manager
        response = self.emergency_manager.register_emergency_vehicle(vehicle, emergency_type)
        self.notification_system.send_notification(f"{emergency_type} emergency declared for {vehicle.vehicle_type}.", "emergency")
        return response

    def end_emergency(self, vehicle):
        # Remove the emergency vehicle and reset priorities
        response = self.emergency_manager.remove_emergency_vehicle(vehicle)
        self.notification_system.send_notification(f"Emergency for {vehicle.vehicle_type} has ended.", "info")
        return response

    def update_simulation(self):
        if self.running:
            # Update the traffic, weather, and map in real-time
            self.traffic_simulation.get_traffic_status()  # Update vehicle movements
            self.weather_simulation.get_weather()         # Get current weather conditions
            self.map_renderer.update_map()                # Render map changes
            self.notification_system.send_notification("Simulation updated.", "info")
            return {"message": "Simulation updated."}
        return {"error": "Simulation is not running."}

# Example Usage
traffic_simulation = TrafficSimulation()
weather_simulation = WeatherSimulation()
map_renderer = MapRenderer()
prioritization_engine = PrioritizationEngine()
emergency_manager = EmergencyResponseManager(prioritization_engine)
notification_system = NotificationSystem()

# Initialize SimulationController
simulation_controller = SimulationController(traffic_simulation, weather_simulation, map_renderer, prioritization_engine, emergency_manager, notification_system)

# Start the simulation
print(simulation_controller.start_simulation())

# Update the weather condition to "rain"
print(simulation_controller.update_weather("rain"))

# Handle an emergency for an ambulance
ambulance = Ambulance({"x": 15, "y": 25})
print(simulation_controller.handle_emergency(ambulance, "medical"))

# End the emergency for the ambulance
print(simulation_controller.end_emergency(ambulance))

# Stop the simulation
print(simulation_controller.stop_simulation())
