import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from agents.traffic_light_agent import TrafficLightAgent
from agents.vehicle_agent import VehicleAgent
import random
import time

def simulate_rush_hour():
    # 初始化多个路口
    intersections = {
        "A": TrafficLightAgent("A"),
        "B": TrafficLightAgent("B"),
        "C": TrafficLightAgent("C")
    }

    # 模拟交通数据
    for i, agent in intersections.items():
        traffic_data = {
            "north": random.randint(10, 30),
            "south": random.randint(10, 30),
            "east": random.randint(10, 30),
            "west": random.randint(10, 30)
        }
        agent.receive_traffic_data(traffic_data)
        agent.update_signal()

    print("\n🚗 模拟多个车辆进入系统...\n")

    # 初始化多个车辆
    vehicles = [
        VehicleAgent("V1", "X", "Z"),
        VehicleAgent("V2", "Y", "W"),
        VehicleAgent("V3", "Z", "A"),
        VehicleAgent("V4", "B", "C"),
    ]

    # 模拟车辆发送状态 & 接收系统反馈
    for v in vehicles:
        status = v.send_status()
        # 模拟随机路况返回 reroute 建议
        if random.choice([True, False]):
            reroute = random.choice(["B", "C", "D"])
            v.receive_signal({"reroute": reroute})
        else:
            v.receive_signal({})  # 无需 reroute

        print(f"✅ {v} 目前路径：{v.route}")
        print("———")

if __name__ == "__main__":
    simulate_rush_hour()
