from lo import distances,data
import random

def nearest_neighbor(distances, start_point, cities):
    unvisited_cities = set(cities)
    unvisited_cities.remove(start_point)

    current_city = start_point
    tour = [current_city]
    
    while unvisited_cities:
        nearest_city = min(unvisited_cities, key=lambda city: distances[current_city][city])
        tour.append(nearest_city)
        current_city = nearest_city
        unvisited_cities.remove(nearest_city)

    tour.append(start_point)
    return tour


def generate_multiple_paths(distances, start_point, num_paths):
    paths = []
    cities = list(distances.keys())

    for _ in range(num_paths):
        random.shuffle(cities)
        path = nearest_neighbor(distances, start_point, cities)
        total_distance = calculate_total_distance(distances, path)
        paths.append((path, total_distance))

    return paths

def calculate_total_distance(distances, tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        current_city = tour[i]
        next_city = tour[i + 1]
        total_distance += distances[current_city][next_city]
    
    return total_distance

def two_opt(tour, distances):
    best_tour = tour
    improve = True

    while improve:
        improve = False
        for i in range(1, len(tour) - 1):
            for j in range(i + 1, len(tour)):
                if j - i == 1:
                    continue  # No point in considering adjacent edges
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if calculate_total_distance(distances, new_tour) < calculate_total_distance(distances, best_tour):
                    best_tour = new_tour
                    improve = True

        tour = best_tour

    return best_tour

# Example usage:
start_point = "r0"
num_paths = 5

# Generate multiple paths
paths = generate_multiple_paths(distances, start_point, num_paths)

# Optimize each path using 2-opt
optimized_paths = []
for path, total_distance in paths:
    optimized_path = two_opt(path, distances)
    optimized_distance = calculate_total_distance(distances, optimized_path)
    optimized_paths.append((optimized_path, optimized_distance))

# Print and compare the optimized paths
for i, (opt_path, opt_distance) in enumerate(optimized_paths):
    print(f"Optimized Path {i + 1}: {opt_path}")
    print(f"Optimized Total Distance: {opt_distance}\n")
