from itertools import permutations
from lo import distances

def calculate_total_distance(path, distances):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distances[path[i]][path[i + 1]]
    total_distance += distances[path[-1]][path[0]]  # Return to the starting point
    return total_distance

def find_shortest_path(distances):
    n_neighbourhoods = len(distances)
    all_neighbourhoods = set(range(n_neighbourhoods))

    # Generate all possible permutations of neighborhoods
    all_permutations = permutations(range(1, n_neighbourhoods))

    # Find the permutation with the minimum total distance
    min_distance = float('inf')
    best_path = None

    for permutation in all_permutations:
        path = [0] + list(permutation)
        distance = calculate_total_distance(path, distances)
        if distance < min_distance:
            min_distance = distance
            best_path = path

    return best_path

def main():
    # Input data
    n_neighbourhoods = 20
    neighbourhoods_distances = distances

    # Find the shortest path
    shortest_path = find_shortest_path(neighbourhoods_distances)

    # Output the result
    print("Shortest Path:", shortest_path)

if __name__ == "__main__":
    main()
