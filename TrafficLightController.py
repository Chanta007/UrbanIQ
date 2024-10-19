from TrafficLight import TrafficLight

class TrafficLightController:
    def __init__(self):
        self.traffic_lights = []  # List to store all traffic lights

    def add_traffic_light(self, traffic_light):
        # Add a new traffic light to the system
        self.traffic_lights.append(traffic_light)
        return {"message": "Traffic light added successfully."}

    def update_traffic_lights(self, time_elapsed):
        # Update the state of each traffic light based on the elapsed time
        for light in self.traffic_lights:
            light.update_light(time_elapsed)
        return {"message": "All traffic lights updated."}

    def get_traffic_light_status(self):
        # Return the current status of all traffic lights
        status = []
        for light in self.traffic_lights:
            status.append(light.get_light_status())
        return status

    def change_traffic_light_priority(self, light_location, priority):
        # Give priority to specific traffic lights (e.g., for emergency vehicles)
        for light in self.traffic_lights:
            if light.location == light_location:
                if priority == "green":
                    light.state = "green"  # Set the traffic light to green
                elif priority == "red":
                    light.state = "red"    # Set the traffic light to red
                return {"message": f"Traffic light at {light_location} set to {priority}."}
        return {"error": "Traffic light not found."}

# Example Usage
traffic_light_controller = TrafficLightController()

# Add traffic lights to the controller
traffic_light_controller.add_traffic_light(TrafficLight({"x": 10, "y": 20}))
traffic_light_controller.add_traffic_light(TrafficLight({"x": 30, "y": 40}))

# Simulate updating the traffic lights after 5 seconds
print(traffic_light_controller.update_traffic_lights(5))

# Get the current status of all traffic lights
print(traffic_light_controller.get_traffic_light_status())

# Change priority of a traffic light to green for an emergency vehicle
print(traffic_light_controller.change_traffic_light_priority({"x": 10, "y": 20}, "green"))
