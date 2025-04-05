from agents.traffic_light_agent import TrafficLightAgent
from agents.vehicle_agent import VehicleAgent

def main():
    # Initialize traffic light and vehicle agents
    traffic_agent = TrafficLightAgent("intersection-1")
    vehicle_agent = VehicleAgent(vehicle_id="V123", current_location="A", destination="D")

    # Simulated traffic data sent to traffic light
    traffic_data = {
        "north": 18,
        "south": 7,
        "east": 22,
        "west": 11
    }

    # Traffic light agent receives and processes the data
    traffic_agent.receive_traffic_data(traffic_data)
    traffic_agent.update_signal()

    # Vehicle sends its current status
    status = vehicle_agent.send_status()

    # Simulated V2I feedback from system (e.g., rerouting due to congestion)
    signal_to_vehicle = {
        "reroute": "B"  # System instructs vehicle to reroute through point B
    }

    # Vehicle processes the reroute instruction
    vehicle_agent.receive_signal(signal_to_vehicle)

    # Final output
    print(f"\nFinal vehicle state: {vehicle_agent}")
    print(f"Route taken: {vehicle_agent.route}")

if __name__ == "__main__":
    main()
