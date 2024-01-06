import json

def nearest_neighbor_algorithm(distances, start_point):
    current_point = start_point
    path = [current_point]
    remaining_points = set(range(len(distances)))
    remaining_points.remove(current_point)

    while remaining_points:
        nearest_point = min(remaining_points, key=lambda point: distances[current_point]["distances"][point])
        path.append(nearest_point)
        remaining_points.remove(nearest_point)
        current_point = nearest_point

    path.append(start_point)
    return path

def create_delivery_slots_nearest_neighbor(data):
    # Extract relevant data
    neighbourhoods = data["neighbourhoods"]
    orders = [f"n{i}" for i in range(data["n_neighbourhoods"])]
    vehicle_capacity = data["vehicles"]["v0"]["capacity"]
    restaurant_distance = data["restaurants"]["r0"]["neighbourhood_distance"]

    # Use nearest neighbor algorithm to find an initial path
    initial_path = nearest_neighbor_algorithm(neighbourhoods["n0"], start_point=0)

    # Split the initial path into delivery slots based on capacity
    delivery_slots = []
    current_slot = {"orders": [], "total_distance": 0, "total_quantity": 0}

    for point in initial_path[1:]:
        order_data = neighbourhoods[orders[point]]
        order_quantity = order_data["order_quantity"]
        order_distance = neighbourhoods[initial_path[point-1]]["distances"][point]  # Use distance to the restaurant

        if current_slot["total_quantity"] + order_quantity <= vehicle_capacity:
            current_slot["orders"].append(orders[point])
            current_slot["total_quantity"] += order_quantity
            current_slot["total_distance"] += order_distance
        else:
            delivery_slots.append(current_slot)
            current_slot = {"orders": [orders[point]], "total_distance": order_distance, "total_quantity": order_quantity}

    delivery_slots.append(current_slot)
    return delivery_slots

def save_to_json(output_data, output_file='level1a_output.json'):
    with open(output_file, 'w') as json_file:
        json.dump(output_data, json_file, indent=2)
    print(f"Output successfully stored in '{output_file}'.")

def print_delivery_slots(delivery_slots):
    print("Delivery Slots:")
    for i, slot in enumerate(delivery_slots, 1):
        print(f"Slot {i}: {slot['orders']} | Total Distance: {slot['total_distance']} | Total Quantity: {slot['total_quantity']}")

# Read JSON data
with open('level1a.json') as f:
    data = json.load(f)

# Create delivery slots using nearest neighbor algorithm
delivery_slots_nearest_neighbor = create_delivery_slots_nearest_neighbor(data)

# Create a dictionary to store the output in the desired format
output_data_nearest_neighbor = {"v0": {f"path{i}": ["r0"] + slot["orders"] + ["r0"] for i, slot in enumerate(delivery_slots_nearest_neighbor, 1)}}

# Save the output to a JSON file
save_to_json(output_data_nearest_neighbor)

# Print the result
print_delivery_slots(delivery_slots_nearest_neighbor)
