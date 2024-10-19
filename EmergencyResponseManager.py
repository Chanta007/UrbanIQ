from  PrioritizationEngine import PrioritizationEngine
from Vehicle import Ambulance

class EmergencyResponseManager:
    def __init__(self, prioritization_engine):
        self.active_emergencies = []
        self.prioritization_engine = prioritization_engine

    def register_emergency_vehicle(self, vehicle, emergency_type):
        # Register a new emergency vehicle and give it top priority
        if vehicle not in self.active_emergencies:
            self.active_emergencies.append({
                "vehicle": vehicle,
                "emergency_type": emergency_type
            })
            # Update prioritization to ensure the vehicle gets top priority
            self.prioritization_engine.set_prioritization_rules({
                vehicle.vehicle_type.lower(): 0  # Assign highest priority (0) for this emergency vehicle
            })
            return {
                "message": f"{emergency_type} emergency vehicle registered for {vehicle.vehicle_type}.",
                "vehicle": vehicle.vehicle_type,
                "priority": 0
            }
        return {"error": "Emergency vehicle already registered."}

    def remove_emergency_vehicle(self, vehicle):
        # Remove an emergency vehicle from active emergencies and reset priorities
        for emergency in self.active_emergencies:
            if emergency["vehicle"] == vehicle:
                self.active_emergencies.remove(emergency)
                self.reset_prioritization()
                return {"message": f"Emergency vehicle {vehicle.vehicle_type} removed."}
        return {"error": "Vehicle not found in active emergencies."}

    def reset_prioritization(self):
        # Reset the prioritization back to default values
        self.prioritization_engine.set_prioritization_rules({
            "emergency_vehicle": 1,
            "electric_vehicle": 2,
            "public_transport": 3,
            "school_zone": 4,
            "normal_vehicle": 5
        })

    def get_active_emergencies(self):
        # Return the list of active emergencies
        return [{
            "vehicle_type": emergency["vehicle"].vehicle_type,
            "emergency_type": emergency["emergency_type"]
        } for emergency in self.active_emergencies]



# Example PrioritizationEngine (already defined in earlier steps)
prioritization_engine = PrioritizationEngine()

# Initialize EmergencyResponseManager
emergency_manager = EmergencyResponseManager(prioritization_engine)

# Register an emergency vehicle
ambulance = Ambulance({"x": 10, "y": 20})
print(emergency_manager.register_emergency_vehicle(ambulance, "medical"))

# Get active emergencies
print(emergency_manager.get_active_emergencies())

# Remove the emergency vehicle
print(emergency_manager.remove_emergency_vehicle(ambulance))

# Get active emergencies after removal
print(emergency_manager.get_active_emergencies())
