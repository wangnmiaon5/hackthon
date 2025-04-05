class TrafficLightAgent:
    def __init__(self, intersection_id):
        self.intersection_id = intersection_id
        self.state = 'RED'
        self.traffic_data = {}

    def receive_traffic_data(self, data):
        self.traffic_data = data
        print(f"[{self.intersection_id}] Received traffic data: {data}")

    def update_signal(self):
        if not self.traffic_data:
            print("No traffic data to process.")
            return
        max_dir = max(self.traffic_data, key=self.traffic_data.get)
        self.state = f"GREEN-{max_dir.upper()}"
        print(f"[{self.intersection_id}] Updated signal to {self.state}")
