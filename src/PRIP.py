'''
Given arc, kui index, data dictionary, slots
Runs PRIP algorithm and returns slots.
'''

def PRIP(data_dict, kui_idx, arc, slot_sizes):
    print(slot_sizes)
    s_type = 0
    item_placed = 0
    slot_type_arr = []
    CAS = []

    num_slots = len(slot_sizes)
    total_slots = 0
    slots = []
    for i in range(0, num_slots):
        CAS.append(len(slot_sizes[i]))
        total_slots += len(slot_sizes[i])
        slots.append([])
    
    # placing 1 itemsets
    Y = []
    for i in range(0, num_slots):
        Y.append(int((len(slot_sizes[i])/float(total_slots))*len(arc.keys())))
    else:
        Y[num_slots-1] += len(arc.keys()) - sum(Y)

    # Adjusting CAS
    for i in range(0, num_slots):
        CAS[i] -= Y[i]

    print (Y)
    # sorting ARC by value
    arc_sorted = {k: v for k, v in sorted(arc.items(), key=lambda item: item[1])}

    for (item, price) in arc_sorted.items():
        placed = False
        while not placed:
            if Y[s_type] != 0:
                slots[s_type].append((item,))
                item_placed += 1
                Y[s_type] -= 1
                placed = True
            if(Y[s_type] == 0):
                s_type += 1
            if s_type == num_slots:
                break

    print ('SLOTS')
    print (slots)

    # Scan kUI Index to fill remaining slots
    h = []
    for i in range(0, len(kui_idx.keys())+1):
        h.append(0)
    for stype in range(0, num_slots):
        for lv in range(2, len(kui_idx.keys())+1):
            if CAS[stype] <= 0 or h[lv] >= len(kui_idx[lv]):
                continue
            # if there is not enough space to place itemset
            if CAS[stype] < lv:
                placed = False
                while not placed:
                    lv -= 1
                    if lv <= 1:
                        break
                    if CAS[stype] >= lv:
                        if h[lv] >= len(kui_idx[lv]):
                            continue
                        print('lv h[lv]')
                        print(lv)
                        print(h[lv])
                        itemset = kui_idx[lv][h[lv]][0]
                        slots[stype].append(itemset)
                        h[lv] += 1
                        CAS[stype] = CAS[stype] - lv
                        placed = True
                        break
            else:
                if h[lv] >= len(kui_idx[lv]):
                    continue
                itemset = kui_idx[lv][h[lv]][0]
                slots[stype].append(itemset)
                h[lv] += 1
                CAS[stype] = CAS[stype] - lv

    return slots