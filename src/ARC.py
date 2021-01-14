'''
module takes kUIindex and returns Aggregate Revenue Contribution for 1-itemset.
'''

def get_arc(data):
    arc = {}
    for itemset in data.keys():
        for item in itemset:
            if item not in arc:
                arc[item] = (data[itemset][0] * data[itemset][1]) / len(itemset)
            arc[item] += (data[itemset][0] * data[itemset][1]) / len(itemset)
    return arc