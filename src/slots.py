'''
Given number of slots, type of slots and zipf factor
Returns a 2d array of slots.
'''
import random

# NOTE: not using zipf right now.
def get_slots(num_slots, type_slots, zipf):
    slots = []
    premiumness_idx = {}
    start = 0.01
    for i in range(1, type_slots+1):
        premiumness_idx[i-1] = (start, start+(1/(type_slots)))
        slots.append([])
        for _ in range(0, int(num_slots/type_slots)):
            slots[i-1].append(0)
    else:
        rem = num_slots - type_slots*int(num_slots/type_slots)
        for k in range(0, rem):
            slots[-1].append(0)
    
    return slots
