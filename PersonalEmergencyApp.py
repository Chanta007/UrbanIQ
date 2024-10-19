from PrioritizationEngine import PrioritizationEngine

class PersonalEmergencyApp:
    def __init__(self, prioritization_engine):
        self.emergency_active = False
        self.emergency_type = None
        self.emergency_vehicle = None
        self.prioritization_engine = prioritization_engine

    def declare_emergency(self, emergency_type, vehicle):
        # Declare a personal emergency and register the vehicle for priority routing
        if not self.emergency_active:
            self.emergency_active = True
            self.emergency_type = emergency_type
            self.emergency_vehicle = vehicle
            self.prioritization_engine.set_prioritization_rules({
                vehicle.vehicle_type.lower(): 0  # Assign highest priority (0) for this vehicle
            })
            return {
                "message": f"{emergency_type} emergency declared for {vehicle.vehicle_type}."
            }
        return {"error": "Emergency already active. Cannot declare another emergency."}

    def end_emergency(self):
        # End the active emergency and reset the prioritization
        if self.emergency_active:
            self.emergency_active = False
            self.emergency_type = None
            self.emergency_vehicle = None
            # Reset the prioritization engine to default values
            self.prioritization_engine.set_prioritization_rules({
                "emergency_vehicle": 1,
                "electric_vehicle": 2,
                "public_transport": 3,
                "school_zone": 4,
                "normal_vehicle": 5
            })
            return {"message": "Emergency ended, priorities reset."}
        return {"error": "No active emergency to end."}

    def get_emergency_status(self):
        # Return the status of the current emergency
        if self.emergency_active:
            return {
                "emergency_type": self.emergency_type,
                "emergency_vehicle": self.emergency_vehicle.vehicle_type,
                "priority": 0  # Always highest priority during emergency
            }
        return {"message": "No active emergency."}

# Example Usage
from abc import ABC, abstractmethod

# Mock Vehicle class (You can replace this with your actual Vehicle class)
class Vehicle(ABC):
    def __init__(self, vehicle_type, position):
        self.vehicle_type = vehicle_type
        self.position = position

    def get_position(self):
        return self.position

    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    def __init__(self, position):
        super().__init__('Car', position)

    def move(self):
        self.position['x'] += 1

# Example PrioritizationEngine (already defined in earlier steps)
prioritization_engine = PrioritizationEngine()

# Initialize PersonalEmergencyApp
emergency_app = PersonalEmergencyApp(prioritization_engine)

# Declare a personal emergency for a Car
car = Car({"x": 10, "y": 20})
print(emergency_app.declare_emergency("medical", car))

# Get emergency status
print(emergency_app.get_emergency_status())

# End the emergency
print(emergency_app.end_emergency())

# Get emergency status after ending
print(emergency_app.get_emergency_status())
