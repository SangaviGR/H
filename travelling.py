import itertools
from lo import distances,data
'''
def calculate_path_distance(path, distances):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distances[path[i]][path[i + 1]]
    
    return total_distance

def tsp_bruteforce(distances, start, end):
    #'n0', 'n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 'n8', 'n9', 'n10', 'n11', 'n12', 'n13', 'n14', 'n15', 'n16', 'n17', 'n18', 'n19', 'r0']
    locations = list(distances.keys())  
    
    locations.remove(start)
    
   # locations.remove(end)

    all_paths = list(itertools.permutations(locations))

    print(all_paths)
    print("\n")
    all_paths = [[start] + list(path) + [end] for path in all_paths]

    min_distance = float('inf')
    best_path = None

    for path in all_paths:
        distance = calculate_path_distance(path, distances)
        if distance < min_distance:
            min_distance = distance
            best_path = path

    return {"path": best_path}




start_point = "r0"
end_point = "r0"

# Solve TSP using brute-force
solution = tsp_bruteforce(distances, start_point, end_point)

# Output the result in the requested format
output = {"v0": solution}
print(output)
'''

def calculate_total_distance(distances, tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        current_city = tour[i]
        next_city = tour[i + 1]
        total_distance += distances[current_city][next_city]
    
    return total_distance

def nearest_neighbor(distances, start_point):
    unvisited_cities = set(distances.keys())
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



start_point = "r0"

# Solve TSP using nearest neighbor algorithm
solution = nearest_neighbor(distances, start_point)

# Output the result
print("TSP Solution:", solution)


# Calculate the total distance of the TSP solution
total_distance = calculate_total_distance(distances, solution)

# Output the total distance
print("Total Distance of TSP Solution:", total_distance)
#  ==========================

