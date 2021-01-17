'''
module takes kUIindex and returns Aggregate Revenue Contribution for 1-itemset.
'''

def get_arc(data):
    '''
    Args -
        data: dictionary {(itemset,) -> (sup_count, price)}
    '''
    arc = {}
    for itemset in data.keys():
        for item in itemset:
            if item not in arc:
                arc[item] = (data[itemset][0] * data[itemset][1]) / len(itemset)
            arc[item] += (data[itemset][0] * data[itemset][1]) / len(itemset)

    arc = {k:v for k,v in sorted(arc.items(), key=lambda x: x[1], reverse=True)}
    return arc