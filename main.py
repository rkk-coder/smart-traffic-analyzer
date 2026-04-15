from traffic import analyze_traffic
import json

with open("data.json") as f:
    cars = json.load(f)

analyze_traffic(cars)
