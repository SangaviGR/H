# Python program to read json file

import json
import numpy as np 
# Opening JSON file
f = open('level0.json')

# returns JSON object as 
# a dictionary
data = json.load(f)

# Iterating through the json
# list
flat=[]
for i in data['neighbourhoods']:
	flat.append(data['neighbourhoods'][i])
      
distances=[]	
for i in flat:
    distances.append(i['distances'])	
    print("\n")


a = np.array(distances)

# Extract distances from the data
distances = {key: value["distances"] for key, value in data["neighbourhoods"].items()}
distances.update({key: value["neighbourhood_distance"] for key, value in data["restaurants"].items()})

print(distances)


# Extract distances from the data
distances = {}

# Extract distances from neighbourhoods
for n_key, n_value in data["neighbourhoods"].items():
    distances[n_key] = {r_key: n_value["distances"][0] for r_key in data["restaurants"].keys()}
    distances[n_key].update({n_key_2: distance for n_key_2, distance in zip(data["neighbourhoods"].keys(), n_value["distances"])})

# Extract distances from restaurants
for r_key, r_value in data["restaurants"].items():
    distances[r_key] = {n_key: distance for n_key, distance in zip(data["neighbourhoods"].keys(), r_value["neighbourhood_distance"])}

print("\n")
print(distances['r0'])

# Closing file
f.close()
