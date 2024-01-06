from lo import distances
import random


def generate_multiple_paths(distances, start_point, num_paths):
    cities = list(distances.keys())
   
    
    for i in range(50):
        random.shuffle(cities)
        total_distance = calculate_total_distance(distances, cities)
        
        print(f"Path {total_distance}\n")
    

def calculate_total_distance(distances, tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        current_city = tour[i]
        next_city = tour[i + 1]
        total_distance += distances[current_city][next_city]
    
    return total_distance


start_point = "r0"
num_paths = 150

# Generate multiple paths
paths = generate_multiple_paths(distances, start_point, num_paths)
