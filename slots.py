import json

def create_delivery_slots(neighbourhoods, orders, capacity, distances):
    delivery_slots = []
    current_slot = {"orders": [], "total_distance": 0, "total_quantity": 0}

    for order in orders:
        order_data = neighbourhoods[order]
        order_quantity = order_data["order_quantity"]
        order_distance = order_data["distances"][0]  # Use distance to the restaurant

        if current_slot["total_quantity"] + order_quantity <= capacity:
            current_slot["orders"].append(order)
            current_slot["total_quantity"] += order_quantity
            current_slot["total_distance"] += order_distance
        else:
            delivery_slots.append(current_slot)
            current_slot = {"orders": [order], "total_distance": order_distance, "total_quantity": order_quantity}

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

# Extract relevant data
neighbourhoods = data["neighbourhoods"]
orders = [f"n{i}" for i in range(data["n_neighbourhoods"])]
vehicle_capacity = data["vehicles"]["v0"]["capacity"]
restaurant_distance = data["restaurants"]["r0"]["neighbourhood_distance"]

# Create delivery slots
delivery_slots = create_delivery_slots(neighbourhoods, orders, vehicle_capacity, restaurant_distance)

# Create a dictionary to store the output in the desired format
output_data = {"v0": {f"path{i}": ["r0"] + slot["orders"] + ["r0"] for i, slot in enumerate(delivery_slots, 1)}}

# Save the output to a JSON file
save_to_json(output_data)

# Print the result
print_delivery_slots(delivery_slots)
