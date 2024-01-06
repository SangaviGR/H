import json
import numpy as np 
# Opening JSON file
f = open('level1a.json')

# returns JSON object as 
# a dictionary
data = json.load(f)

# Iterating through the json
# list
orders=[]
for i in data['neighbourhoods']:
	orders.append(i)

print(orders)  

# Extract vehicle capacity from the provided JSON data
vehicle_capacity = data["vehicles"]["v0"]["capacity"]

# Example usage
print("Vehicle Capacity:", vehicle_capacity)

# Extract restaurant distances from the provided JSON data
restaurant_distances = data["restaurants"]["r0"]["neighbourhood_distance"]

# Create a dictionary mapping neighbourhoods to their respective distances
restaurant_distance = {f"n{i}": distance for i, distance in enumerate(restaurant_distances)}

# Example usage
print("Restaurant Distance:", restaurant_distance)


# Extract neighbourhoods information from the provided JSON data
neighbourhoods_data = data["neighbourhoods"]

# Create a dictionary mapping neighbourhoods to their respective data
neighbourhoods = {key: {"order_quantity": value["order_quantity"], "distances": value["distances"]} for key, value in neighbourhoods_data.items()}

# Example usage
print("Neighbourhoods:", neighbourhoods)


