'''
Given arc, kui index, data dictionary, dranks, slots
Runs DPRIP algorithm and returns slots.
'''
import globals
import random
import copy

TOTAL_SLOTS = 0
TOTAL_REVENUE = 0
DRANK_MEAN = 0
TOTAL_PLACED = 0

IDX = 0
TOP_REVENUE = {}


def calculate_diversification(itemsets):
    ''' Calculates diversification of itemsets using Parul's approach'''
    assert type(itemsets) == list

    unique_items = set()

    for itemset in itemsets:
        for item in itemset:
            unique_items.add(item)

    return len(unique_items) / len(itemsets)


# takes advantage of the fact that everything is passed
# by reference in python. So
# even though this function does not return anything,
# it still changes both slots and top_kui_per_slot_rev
# arrays
def insert_one_itemset(slots, top_kui_per_slot_rev, top_kui_ptrs, kui_idx, CAS, stype, method=None):
    global TOTAL_SLOTS, TOTAL_REVENUE, DRANK_MEAN, TOTAL_PLACED

    found = False

    while not found:
        top = [None,0]
        for idx, val in enumerate(top_kui_per_slot_rev):
            # ignoring single itemsets
            if idx == 0 or idx == 1:
                continue
            if val > top[1]:
                top = [idx, val]

        if top[0] is None:
            print ('NOT ENOUGH ITEMSETS')
            return
    
        top_kui_node = kui_idx[top[0]][top_kui_ptrs[top[0]]]
        all_slots = list()
        for slot_type in range (0, globals.NUM_TYPE_SLOTS):
            all_slots.extend(slots[slot_type])
        placed = [node[0] for node in all_slots]
        
        if top_kui_node[0] not in placed:
            node = kui_idx[top[0]][top_kui_ptrs[top[0]]]
            price = node[2]
            if method == 'DR':
                price = node[2]
                
            slots[stype].append((
                node[0],
                price, 
                node[-1]))

            DRANK_MEAN += kui_idx[top[0]][top_kui_ptrs[top[0]]][-1]
            TOTAL_PLACED += 1
            factor = 1
            TOTAL_REVENUE += (kui_idx[top[0]][top_kui_ptrs[top[0]]][-2] * 1.0) * factor
            CAS[stype] -= len(kui_idx[top[0]][top_kui_ptrs[top[0]]][0])
        
            found = True
        else:
            pass

        top_kui_ptrs[top[0]] += 1

        # if all itemsets of certain sized already placed
        if top_kui_ptrs[top[0]] >= len(kui_idx[top[0]]):
            top_kui_per_slot_rev[top[0]] = -1
        else:
            if method == 'D':
                top_kui_per_slot_rev[top[0]] = kui_idx[top[0]][top_kui_ptrs[top[0]]][-1]/float(top[0])
            else:
                top_kui_per_slot_rev[top[0]] = kui_idx[top[0]][top_kui_ptrs[top[0]]][-2]/float(top[0])
        
        if found:
            break
    return


# This placement scheme will place itemsets based on the per_slot_revenue
# contribution
def _DPRIP(deta_dict, kui_idx, dranks, slot_sizes, method):
    global TOTAL_SLOTS, TOTAL_REVENUE, DRANK_MEAN, TOTAL_PLACED

    slots = []
    slot_types = len(slot_sizes)
    for i in range(0, slot_types):
        TOTAL_SLOTS += len(slot_sizes[i])
        slots.append([])
    CAS = []
    for stype in range(0, slot_types):
        CAS.append(len(slot_sizes[stype]))
    top_kui_ptrs = [0]*(len(kui_idx.keys())+1)
    top_kui_per_slot_rev = [0]*(len(kui_idx.keys())+1)
    for i in kui_idx.keys():
        try:
            if method == 'D':
                top_kui_per_slot_rev[i] = (kui_idx[i][top_kui_ptrs[i]][-1])/float(i)
            else:
                top_kui_per_slot_rev[i] = (kui_idx[i][top_kui_ptrs[i]][-2])/float(i)
        except:
            top_kui_per_slot_rev[i] = -1
    for stype in range(0, slot_types):
        while CAS[stype] > 0:
            insert_one_itemset(
                slots, top_kui_per_slot_rev,
                top_kui_ptrs, kui_idx, CAS, stype, method)
    
    print ('TOTAL REVENUE TRAINING ')
    print (TOTAL_REVENUE)
    print ('DRANK MEAN')
    print (DRANK_MEAN/float(TOTAL_PLACED))
    # print ('PATTERNS PLACED (TRAIN)')
    # print (TOTAL_PATTERNS)
    print ('SLOTS TOTAL')
    print (TOTAL_SLOTS)


    print ("TOTAL REVENUE")
    import pprint
    pprint.pprint(TOP_REVENUE, width=1)
    
    return (slots, TOTAL_SLOTS, TOTAL_REVENUE,
                DRANK_MEAN/float(TOTAL_PLACED))


def _RHDPRIP(data_dict, kui_R, kui_H, dranks, slot_sizes):
    global TOTAL_SLOTS, TOTAL_REVENUE, DRANK_MEAN, TOTAL_PLACED

    slots = [] # final slots 2d list
    CAS = [] # currently available slots
    slot_types = len(slot_sizes)

    for stype in range(0, slot_types):
        TOTAL_SLOTS += len(slot_sizes[stype])
        slots.append([])
        CAS.append(len(slot_sizes[stype]))

    # store pointers to next candidate of each itemset length
    top_kuir_ptrs = [0] * (len(kui_R.keys()) + 1)
    top_kuir_per_slot_revenue = [0] * (len(kui_R.keys()) + 1)
    for i in kui_R.keys():
        try:
            top_kuir_per_slot_revenue[i] = kui_R[i][0][-2]
        except:
            top_kuir_per_slot_revenue[i] = -1

    top_kuih_ptrs = [0] * (len(kui_H.keys()) + 1)
    top_kuih_per_slot_revenue = [0] * (len(kui_H.keys()) + 1)
    for i in kui_H.keys():
        try:
            top_kuih_per_slot_revenue[i] = kui_H[i][0][-2]
        except:
            top_kuih_per_slot_revenue[i] = -1
    pick_r_or_h = list(['R']*int(globals.R_RATIO * 10))
    pick_r_or_h.extend(['H']*int(globals.H_RATIO * 10))
    random.shuffle(pick_r_or_h)
    kui_to_pick_ptr = 0

    for stype in range(0, slot_types):
        while CAS[stype] > 0:
            if pick_r_or_h[kui_to_pick_ptr] == 'R':
                insert_one_itemset(
                    slots, top_kuir_per_slot_revenue,
                    top_kuir_ptrs, kui_R, CAS, stype)
            elif pick_r_or_h[kui_to_pick_ptr] == 'H':
                insert_one_itemset(
                    slots, top_kuih_per_slot_revenue,
                    top_kuih_ptrs, kui_H, CAS, stype)
            kui_to_pick_ptr = (kui_to_pick_ptr + 1)%10

    print ('TOTAL REVENUE TRAINING ')
    print (TOTAL_REVENUE)
    print ('DRANK MEAN')
    print (DRANK_MEAN/float(TOTAL_PLACED))
    print ('SLOTS TOTAL')
    print (TOTAL_SLOTS)

    return (slots, TOTAL_SLOTS, TOTAL_REVENUE,
                DRANK_MEAN/float(TOTAL_PLACED))


def _DIVERSIFICATION(data_dict, kui_idx, slot_sizes, method):
    TOTAL_SLOTS = 0
    TOTAL_REVENUE = 0
    slots = []
    #kUI = copy.deepcopy(kui_idx)
    kUI = {}

    A = 0.2

    # NRl - a*NRl
    NRl = 0

    for i in kui_idx.keys():
        if i not in kUI:
            kUI[i] = []

        for j in kui_idx[i]:
            # appending NR at the end, has to remove it later
            kUI[i].append((j[0], j[2], j[-1], j[-2]))

    for slot_size in slot_sizes:
        lbd = len(slot_size)

        selected_list = []
        max_div = -1

        NRl = 0

        # fill 30% by 4 itemsets, 30% by 3 itemsets, 40% by 2 itemsets
        num_4 = int(((lbd * 30) / 100) / 4) # because each itemset would take 4 space
        num_3 = int(((lbd * 30) / 100) / 3) # because each itemset would take 3 space
        num_2 = int(((lbd * 40) / 100) / 2) # because each itemset would take 2 space

        for i in range (0, num_2):
            NRl += kui_idx[2][i][-2]

        for i in range (0, num_3):
            NRl += kui_idx[3][i][-2]

        for i in range (0, num_4):
            NRl += kui_idx[4][i][-2]

        for i in range(0, 100):
            # suffle and get diversification and keep with max diversification
            # lbd = 2*num_2 + 3*num_3 + 4*num_4
            short_list = list()
            short_list.extend(random.choices(kUI[2][:2*lbd], k=num_2))
            short_list.extend(random.choices(kUI[3][:2*lbd], k=num_3))
            short_list.extend(random.choices(kUI[4][:2*lbd], k=num_4))
            
            #print (short_list)
            current_div = calculate_diversification(short_list)

            sum_revenue = 0
            for idx, i in enumerate(short_list):
                sum_revenue += i[-1]
                short_list[idx] = short_list[idx][:-1]
            
            # DIV METHOD
            if current_div > max_div and method == 'DIV':
                max_div = current_div
                selected_list = short_list

            # HRD METHOD
            if current_div > max_div and sum_revenue >= NRl - A*NRl and method == 'HRD':
                max_div = current_div
                selected_list = short_list

        slots.append(selected_list)

        print ('selected list ') 
        print (selected_list)

        # remove the items that have been placed
        for item in selected_list:
            print ( '\n\n\n\ PRINT \n\n')
            print ( item)
            try:
                kUI[len(item[0])].remove(item)
            except:
                pass
            TOTAL_SLOTS += len(item[0])
            TOTAL_REVENUE += item[1]
        
    print ('Number of Shelves ' + str(len(slots)))
    print (str(len(slots[0])))
    print (str(len(slots[1])))
    print (str(len(slots[2])))
    
    return (slots, TOTAL_SLOTS, TOTAL_REVENUE, 0)


def DPRIP(data_dict, kui_idx, dranks, slot_sizes, method='R'):
    if method == 'RH' or method == 'RDR':
        return _RHDPRIP(data_dict, kui_idx['R'], kui_idx['DR'], dranks, slot_sizes)
    elif method == 'DIV' or method == 'HRD':
        return _DIVERSIFICATION(data_dict, kui_idx, slot_sizes, method)
    else:
        return _DPRIP(data_dict, kui_idx, dranks, slot_sizes, method)
