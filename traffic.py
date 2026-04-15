import math

def distance(car1, car2):
    return math.sqrt((car1["x"] - car2["x"])**2 + (car1["y"] - car2["y"])**2)

def analyze_traffic(cars):
    for i in range(len(cars)):
        for j in range(i + 1, len(cars)):
            d = distance(cars[i], cars[j])

            if d < 5:
                print(f"WARNING: Cars {cars[i]['id']} and {cars[j]['id']} are too close!")

    avg_speed = sum(car["speed"] for car in cars) / len(cars)
    print(f"Average speed: {avg_speed}")
