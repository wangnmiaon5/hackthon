class VehicleAgent:
    def __init__(self, vehicle_id, current_location, destination):
        self.vehicle_id = vehicle_id
        self.current_location = current_location
        self.destination = destination
        self.route = [current_location]  # Stores the path taken

    def send_status(self):
        # Simulate sending data to infrastructure
        return {
            "vehicle_id": self.vehicle_id,
            "location": self.current_location,
            "destination": self.destination
        }

    def receive_signal(self, signal_data):
        # Act on V2I feedback
        print(f"[{self.vehicle_id}] Received signal data: {signal_data}")
        if signal_data.get("reroute"):
            self.route.append(signal_data["reroute"])
            self.current_location = signal_data["reroute"]
        else:
            self.route.append("continue")

    def __str__(self):
        return f"Vehicle {self.vehicle_id} at {self.current_location} heading to {self.destination}"
