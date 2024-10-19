from Vehicle import Car, Bike, Lorry  # Import your vehicle classes here
from TrafficLight import TrafficLight

class MapRenderer:
    def __init__(self, area_name="Emory College Campus"):
        self.area_name = area_name
        self.map_width = 100  # Example map size (width)
        self.map_height = 100  # Example map size (height)
        self.vehicles = []
        self.traffic_lights = []
        self.zones = []  # Stores special zones like schools, parks

    def draw_map(self):
        # Simulate drawing a base map (could integrate with a map library later)
        print(f"Drawing map for area: {self.area_name}")
        print(f"Map size: {self.map_width}x{self.map_height}")
        # Example output showing map elements
        for zone in self.zones:
            print(f"Zone: {zone['type']} at {zone['location']}")

    def add_vehicle(self, vehicle):
        # Adds a vehicle to the map for rendering
        self.vehicles.append(vehicle)

    def render_vehicles(self):
        # Render each vehicle by showing its type and position
        print("Rendering vehicles:")
        for vehicle in self.vehicles:
            print(f"Vehicle: {vehicle.vehicle_type} at position {vehicle.get_position()}")

    def add_traffic_light(self, traffic_light):
        # Adds a traffic light to the map for rendering
        self.traffic_lights.append(traffic_light)

    def render_traffic_lights(self):
        # Render each traffic light with its location and current state
        print("Rendering traffic lights:")
        for light in self.traffic_lights:
            print(f"Traffic Light at {light.location} is {light.state}")

    def add_zone(self, zone_type, location):
        # Adds a special zone to the map (e.g., school, park)
        zone = {"type": zone_type, "location": location}
        self.zones.append(zone)

    def update_map(self):
        # Simulates updating the map with vehicles and traffic lights
        self.draw_map()
        self.render_vehicles()
        self.render_traffic_lights()

# Example Usage:
map_renderer = MapRenderer()

# Adding vehicles to the map
map_renderer.add_vehicle(Car({'x': 10, 'y': 20}))
map_renderer.add_vehicle(Bike({'x': 15, 'y': 30}))
map_renderer.add_vehicle(Lorry({'x': 50, 'y': 50}))

# Adding a traffic light to the map
traffic_light = TrafficLight(location={"x": 50, "y": 50}, initial_state="red")
map_renderer.add_traffic_light(traffic_light)

# Adding zones to the map
map_renderer.add_zone("School Zone", {"x": 20, "y": 30})
map_renderer.add_zone("Park", {"x": 10, "y": 50})

# Updating the map
map_renderer.update_map()
