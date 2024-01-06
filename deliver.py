
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
