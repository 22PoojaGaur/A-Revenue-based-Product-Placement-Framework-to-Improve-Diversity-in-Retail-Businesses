'''
Given arc, kui index, data dictionary, slots
Runs PRIP algorithm and returns slots.
'''
import globals

def PRIP(data_dict, kui_idx, arc, slot_sizes):
    '''
    Args -
        data_dict: Dict. {itemset -> (sup_count, price)}
        kui_idx: Dict. {level -> [list of itemset sorted by utility function]}
        slot_sizes: List[List]. Empty slots.
    '''
    ITEMS_PLACED = 0
    TOTAL_REVENUE = 0
    SLOT_WISE_REVENUE = {}

    s_type = 0
    item_placed = 0
    slot_type_arr = []
    CAS = []

    num_type_slots = len(slot_sizes)
    for i in range(0, num_type_slots):
        SLOT_WISE_REVENUE[i] = 0
    total_slots = 0
    slots = []
    for i in range(0, num_type_slots):
        CAS.append(len(slot_sizes[i]))
        total_slots += len(slot_sizes[i])
        slots.append([])
    # placing 1 itemsets
    # Y = []
    # for i in range(0, num_type_slots):
    #     # print (arc.keys())
    #     # print(min(
    #     #         int(globals.ONE_ITEMSET_RATIO * len(slot_sizes[i])),
    #     #         int((len(slot_sizes[i])/float(total_slots))*len(arc.keys()))
    #     #     ))
    #     Y.append(
    #         min(
    #             int(globals.ONE_ITEMSET_RATIO * len(slot_sizes[i])),
    #             int((len(slot_sizes[i])/float(total_slots))*len(arc.keys()))
    #         )
    #     )
    # else:
    #     if Y[num_type_slots - 1] == globals.ONE_ITEMSET_RATIO * len(slot_sizes[num_type_slots - 1]):
    #         pass
    #     else:
    #         Y[num_type_slots-1] += len(arc.keys()) - sum(Y)

    # # Adjusting CAS
    # for i in range(0, num_type_slots):
    #     CAS[i] -= Y[i]

    # #print (Y)

    # revenue_1_itemset = {}
    # for node in kui_idx[1]:
    #     revenue_1_itemset[node[1]] = node[2]

    # for (item, price) in arc.items():
    #     placed = False
    #     if s_type == num_type_slots:
    #         break
    #     while not placed:
    #         if Y[s_type] != 0:
    #             slots[s_type].append(((item,), (price*1.0)/(1+s_type)))
    #             item_placed += 1
    #             ITEMS_PLACED += 1
    #             try:
    #                 TOTAL_REVENUE += (revenue_1_itemset[(item,)] * 1.0)/(1+s_type)
    #             except:
    #                 pass
    #             Y[s_type] -= 1
    #             placed = True
    #         if(Y[s_type] == 0):
    #             s_type += 1
    #         if s_type == num_type_slots:
    #             break


    # Scan kUI Index to fill remaining slots
    h = []
    for i in range(0, len(kui_idx.keys())+1):
        h.append(0)
    stype = 0
    can_place_more = True
    
    while stype < num_type_slots:
        
        for lv in range(2, len(kui_idx.keys())+1):
            #print('.', end='')
            if can_place_more == False:
                break
            # if the slot type is filled
            if CAS[stype] <= 0:
                can_place_more = False
                break
            # if there is not enough space to place itemset
            if CAS[stype] < lv:
                ilv = lv
                placed = False
                while not placed:
                    ilv -= 1
                    if ilv <= 1 or CAS[stype] <= 0:
                        can_place_more = False
                        break
                    if h[ilv] >= len(kui_idx[lv]):
                        ilv -= 1
                        continue
                    if CAS[stype] >= ilv:
                        # if h[lv] >= len(kui_idx[lv]):
                        #     continue
                        # print('lv h[lv]')
                        # print(lv)
                        # print(h[lv])
                        
                        itemset = tuple([kui_idx[ilv][h[ilv]][0], (kui_idx[ilv][h[ilv]][-3]*1.0)/(1+stype)])
                        slots[stype].append(itemset)
                        ITEMS_PLACED += len(itemset)
                        SLOT_WISE_REVENUE[stype] += kui_idx[ilv][h[ilv]][-1]
                        TOTAL_REVENUE += kui_idx[ilv][h[ilv]][2] * (1.0 / (stype+1))
                        h[ilv] += 1
                        CAS[stype] = CAS[stype] - ilv
                        placed = True
                        break
            else:
                if h[lv] >= len(kui_idx[lv]):
                    continue
                itemset = tuple([kui_idx[lv][h[lv]][0], (kui_idx[lv][h[lv]][-3]*1.0)/(1+stype)])
                slots[stype].append(itemset)
                ITEMS_PLACED += len(itemset)
                SLOT_WISE_REVENUE[stype] += kui_idx[lv][h[lv]][-1]
                TOTAL_REVENUE += kui_idx[lv][h[lv]][2] * (1.0/ (stype+1))
                h[lv] += 1
                CAS[stype] = CAS[stype] - lv
        if can_place_more == False:
            print('THE SLOT TYPES COMPLETED SO CONTINUE')
            stype += 1
            can_place_more = True

    # print('ITEMS_PLACED ->')
    # print(ITEMS_PLACED)
    # print('TOTAL ITEMS ->')
    # print(sum([len(k) for k in data_dict.keys()]))
    # print('TOTAL_SLOTS ->')
    # print(total_slots)
    print('TOTAL_REVENUE_TRAINING_PLACEMENT ->')
    print(TOTAL_REVENUE)
    # print ('SLOT WISE REVENUE ->')
    # print (SLOT_WISE_REVENUE)
    return slots