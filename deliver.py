import itertools
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