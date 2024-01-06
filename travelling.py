import itertools
import random
import json
from lo import distances
def calculate_total_distance(tour, distances):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distances[tour[i]][tour[i + 1]]
    total_distance += distances[tour[-1]][tour[0]]  # Return to the starting point
    return total_distance

def two_opt(tour, distances):
    best_tour = tour
    improvement = True
    while improvement:
        improvement = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1:
                    continue  # Ignore adjacent edges
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if calculate_total_distance(new_tour, distances) < calculate_total_distance(best_tour, distances):
                    best_tour = new_tour
                    improvement = True
        tour = best_tour
    return best_tour

def generate_random_paths(distances, num_paths):
    keys = list(distances.keys())
    keys.remove('r0')  # Exclude 'r0' from midpoints
    random_paths = {}

    for i in range(num_paths):
        random.shuffle(keys)
        random_path = ['r0'] + keys + ['r0']
        random_paths[f"v{i}"] = random_path

    return random_paths

def find_shortest_path(paths, distances):
    shortest_path = None
    shortest_distance = float('inf')

    for path_name, initial_tour in paths.items():
        optimized_tour = two_opt(initial_tour, distances)
        total_distance = calculate_total_distance(optimized_tour, distances)

        if total_distance < shortest_distance:
            shortest_path = {"path": optimized_tour}
            shortest_distance = total_distance

    return shortest_path


# Generate random paths with 'r0' as start and end
num_random_paths = 5  # Adjust as needed
random_paths = generate_random_paths(distances, num_random_paths)

# Print and save the generated random paths
print("Generated Random Paths:")
for path_name, path in random_paths.items():
    print(f"{path_name}: {path}")

print(distances)
# Find the shortest path among the generated random paths
shortest_path_result = find_shortest_path(random_paths, distances)

# Save the result to a JSON file
output_filename = "shortest_random_path_output.json"
with open(output_filename, "w") as output_file:
    json.dump(shortest_path_result, output_file, indent=2)

print(f"Shortest random path saved to {output_filename}")
