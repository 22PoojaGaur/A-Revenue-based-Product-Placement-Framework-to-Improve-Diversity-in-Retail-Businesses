'''
Given number of slots, type of slots and zipf factor
Returns a 2d array of slots.
'''
import random

# NOTE: not using zipf right now.
def get_slots(num_slots, type_slots, zipf):
    '''
    Args -
        num_slots: Dictionary containing number of slots
            for each slot type
        type_slots: number of type of slots
        zipf: zipf factor [NOT USED YET]
    '''
    slots = []
    for i in range(0, type_slots):
        slots.append([])
        for _ in range(0, num_slots[i]):
            slots[i].append(0)
    
    return slots
