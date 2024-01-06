'''import itertools
from l1a import *
def calculate_distance(order, restaurant_distance, neighbourhoods):
    total_distance = 0
    for i in range(len(order)):
        if i == 0:
            total_distance += restaurant_distance[order[i]]
        else:
            total_distance += neighbourhoods[order[i - 1]]["distances"][order[i]]
    return total_distance

def generate_delivery_slots(orders, vehicle_capacity, restaurant_distance, neighbourhoods):
    all_orders_permutations = list(itertools.permutations(orders))
    best_distance = float('inf')
    best_delivery_slots = []

    for order_permutation in all_orders_permutations:
        current_distance = 0
        current_delivery_slots = []
        remaining_capacity = vehicle_capacity

        for order in order_permutation:
            if remaining_capacity >= neighbourhoods[order]["order_quantity"]:
                current_delivery_slots.append(order)
                remaining_capacity -= neighbourhoods[order]["order_quantity"]
            else:
                current_distance += calculate_distance(current_delivery_slots, restaurant_distance, neighbourhoods)
                current_delivery_slots = [order]
                remaining_capacity = vehicle_capacity - neighbourhoods[order]["order_quantity"]

        current_distance += calculate_distance(current_delivery_slots, restaurant_distance, neighbourhoods)

        if current_distance < best_distance:
            best_distance = current_distance
            best_delivery_slots = current_delivery_slots

    return best_delivery_slots, best_distance



best_delivery_slots, best_distance = generate_delivery_slots(orders, vehicle_capacity, restaurant_distance, neighbourhoods)

print("Best Delivery Slots:", best_delivery_slots)
print("Total Distance Traveled:", best_distance)
'''

import json
from l1a import *

def create_delivery_slots(orders, capacity, distances):
    delivery_slots = []
    current_slot = {"orders": [], "total_distance": 0, "total_quantity": 0}

    for order in orders:
        order_quantity = neighbourhoods[order]["order_quantity"]
        order_distance = distances[order]

        if current_slot["total_quantity"] + order_quantity <= capacity:
            current_slot["orders"].append(order)
            current_slot["total_quantity"] += order_quantity
            current_slot["total_distance"] += order_distance
        else:
            delivery_slots.append(current_slot)
            current_slot = {"orders": [order], "total_distance": order_distance, "total_quantity": order_quantity}

    delivery_slots.append(current_slot)
    return delivery_slots

# Use the provided data
with open('level1a.json') as f:
    data = json.load(f)
    

# Create delivery slots
delivery_slots = create_delivery_slots(orders, vehicle_capacity, restaurant_distance)

# Create a dictionary to store the output in the desired format
output_data = {"v0": {}}

# Populate the dictionary with delivery paths
for i, slot in enumerate(delivery_slots, 1):
    path_key = f"path{i}"
    output_data["v0"][path_key] = ["r0"] + slot['orders'] + ["r0"]

# Convert the dictionary to JSON format
output_json = json.dumps(output_data, indent=2)

# Write the JSON data to a file
with open('level1a_output.json', 'w') as json_file:
    json_file.write(output_json)

# Print a confirmation message
print("Output successfully stored in 'level1a_output.json'.")

# Print the result
print("Delivery Slots:")
for i, slot in enumerate(delivery_slots, 1):
    print(f"Slot {i}: {slot['orders']} | Total Distance: {slot['total_distance']} | Total Quantity: {slot['total_quantity']}")

