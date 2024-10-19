import os
import logging
from datetime import datetime

class SimulationLogger:
    def __init__(self, log_file="simulation.log"):
        self.log_file = log_file
        self.logger = logging.getLogger("SimulationLogger")
        self.logger.setLevel(logging.INFO)
        
        # Create a file handler to save logs to a file
        file_handler = logging.FileHandler(self.log_file)
        file_handler.setLevel(logging.INFO)
        
        # Create a console handler to output logs to the console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        # Define the log format
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        # Add handlers to the logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def log_event(self, message, level="info"):
        # Log events with different levels (info, warning, error)
        if level == "info":
            self.logger.info(message)
        elif level == "warning":
            self.logger.warning(message)
        elif level == "error":
            self.logger.error(message)

    def log_vehicle_movement(self, vehicle):
        # Log the movement of a vehicle
        position = vehicle.get_position()
        message = f"Vehicle {vehicle.vehicle_type} moved to position {position}."
        self.log_event(message, "info")

    def log_weather_change(self, new_weather):
        # Log a change in weather conditions
        message = f"Weather changed to {new_weather}."
        self.log_event(message, "info")

    def log_traffic_light_change(self, traffic_light):
        # Log changes in traffic light state
        status = traffic_light.get_light_status()
        message = f"Traffic light at {status['location']} changed to {status['state']}."
        self.log_event(message, "info")

    def log_emergency(self, emergency_type, vehicle):
        # Log when an emergency is declared
        message = f"Emergency declared: {emergency_type} for vehicle {vehicle.vehicle_type}."
        self.log_event(message, "warning")

    def clear_log(self):
        # Clear the log file
        if os.path.exists(self.log_file):
            with open(self.log_file, 'w') as log:
                log.write("")
            return {"message": "Log file cleared."}
        return {"error": "Log file does not exist."}

# Example Usage
from VehicleManager import VehicleManager
from WeatherSimulation import WeatherSimulation
from TrafficLight import TrafficLight
from Vehicle import Car

# Initialize the SimulationLogger
simulation_logger = SimulationLogger()

# Log vehicle movement
car = Car({"x": 10, "y": 20})
simulation_logger.log_vehicle_movement(car)

# Log a weather change
simulation_logger.log_weather_change("rain")

# Log a traffic light change
traffic_light = TrafficLight({"x": 30, "y": 40}, "green")
simulation_logger.log_traffic_light_change(traffic_light)

# Log an emergency
simulation_logger.log_emergency("medical", car)

# Clear the log file
print(simulation_logger.clear_log())
