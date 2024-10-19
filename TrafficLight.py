class TrafficLight:
    def __init__(self, location, initial_state="red"):
        self.location = location  # Intersection location or coordinates
        self.state = initial_state  # Initial state of the traffic light ("red", "green", or "yellow")
        self.timer = 0  # Timer to control how long the light stays in a given state
        self.cycle_duration = {
            "green": 10,  # Duration for green light in seconds
            "yellow": 3,  # Duration for yellow light
            "red": 7      # Duration for red light
        }

    def change_light_status(self):
        if self.state == "green":
            self.state = "yellow"
        elif self.state == "yellow":
            self.state = "red"
        elif self.state == "red":
            self.state = "green"
        self.timer = 0  # Reset timer when the light changes

    def update_light(self, time_elapsed):
        # Update the traffic light based on the time elapsed
        self.timer += time_elapsed
        if self.timer >= self.cycle_duration[self.state]:
            self.change_light_status()

    def get_light_status(self):
        return {"location": self.location, "state": self.state}

# Example Usage:
traffic_light = TrafficLight(location={"x": 50, "y": 50})

# Simulating time passing and updating the light status
for second in range(30):
    traffic_light.update_light(1)
    print(f"At second {second + 1}, light is {traffic_light.get_light_status()['state']}")
