from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, vehicle_type, position):
        self.vehicle_type = vehicle_type
        self.position = position  # Position as a dictionary with x and y coordinates

    @abstractmethod
    def move(self):
        # Abstract method to be implemented by subclasses
        pass

    def get_position(self):
        return self.position

    def set_destination(self, destination):
        self.destination = destination

class Ambulance(Vehicle):
    def __init__(self, position):
        super().__init__('Ambulance', position)

    def move(self):
        self.position['x'] += 2

class Car(Vehicle):
    def __init__(self, position):
        super().__init__('Car', position)

    def move(self):
        # Logic for moving a car (simple example of moving along x-axis)
        self.position['x'] += 1

class ElectricVehicle(Vehicle):
    def __init__(self, position):
        super().__init__('Electric Vehicle', position)

    def move(self):
        # Logic for moving an electric vehicle (EV)
        self.position['x'] += 1.5  # EVs might move faster in this example

class Lorry(Vehicle):
    def __init__(self, position):
        super().__init__('Lorry', position)

    def move(self):
        # Logic for moving a lorry (slower movement, for example)
        self.position['x'] += 0.5

class Bike(Vehicle):
    def __init__(self, position):
        super().__init__('Bike', position)

    def move(self):
        # Logic for moving a bike (potentially avoiding certain areas)
        self.position['y'] += 1  # Moving along y-axis in this example

class Pedestrian(Vehicle):
    def __init__(self, position):
        super().__init__('Pedestrian', position)

    def move(self):
        # Logic for pedestrian movement (slower and more random)
        self.position['x'] += 0.2
        self.position['y'] += 0.2

class PublicTransport(Vehicle):
    def __init__(self, position):
        super().__init__('Public Transport', position)

    def move(self):
        # Logic for moving a public transport vehicle
        self.position['x'] += 1  # Public transport moves at a standard speed


# Example of creating different types of vehicles:
car = Car({'x': 0, 'y': 0})
ev = ElectricVehicle({'x': 0, 'y': 0})
lorry = Lorry({'x': 0, 'y': 0})
bike = Bike({'x': 0, 'y': 0})
pedestrian = Pedestrian({'x': 0, 'y': 0})

# Example usage:
for vehicle in [car, ev, lorry, bike, pedestrian]:
    vehicle.move()
    print(f"{vehicle.vehicle_type} moved to position {vehicle.get_position()}")
