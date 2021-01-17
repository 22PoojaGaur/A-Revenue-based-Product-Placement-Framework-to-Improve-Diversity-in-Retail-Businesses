'''
This file implements IMS Apriori.
'''
# test transaction set
transactions = [
    [1],
    [1, 2, 3],
    [1, 2],
    [2, 4],
    [2, 4, 3, 1],
    [1, 2, 5, 6],
    [5, 6],
    [3,4,6],
    [5],
    [1,2,3,4,5,6]
]

def generate_one_itemsets(transactions):
    '''Give itemset of size one'''
    one_itemsets = set()
    supports = {}

    for transaction in transactions:
        for item in transaction:
            one_itemsets.add((item,))

            if (item,) not in supports.keys():
                supports[(item,)] = 0
            supports[(item,)] += 1

    return one_itemsets, supports


def calculate_mis(transactions, supports, SD, LS):
    trans_size = len(transactions)
    mis = {}
    for item in supports.keys():
        mis[item] = max((float(supports[item]) / trans_size) - SD, LS)
        mis[item[0]] = max((float(supports[item]) / trans_size) - SD, LS)

    return mis


def candidate_gen(candidates, one_itemsets):
    new_candidates = set()
    for itemset in candidates:
        for item in one_itemsets:
            if item[0] not in itemset:
                new_candidates.add(
                    tuple(set(itemset) | set(item)))

    return list(new_candidates)

def get_subset(candidates, transaction):
    common = []
    for candidate in candidates:
        if set(candidate).issubset(set(transaction)):
            common.append(candidate)
    return common


def find_patterns(transactions, SD=0.5, LS=0.01):
    C1, S = generate_one_itemsets(transactions)
    mis = calculate_mis(transactions, S, SD, LS)
    data_size = len(transactions)

    patterns = {}
    L = []
    L.append(
        [itemset for itemset in C1 if S[itemset] >= mis[itemset]])
    # sorting based on mis
    L[0] = sorted(L[0], key=lambda x: mis[x], reverse=True)
    patterns.update({k:S[k] for k in L[0]})
    k = 1
    while len(L[k-1]) > 0:
        L.append([])
        C = candidate_gen(L[k-1], C1)
        CT = []
        counts = {}
        for transaction in transactions:
            Ct = get_subset(C, transaction)
            CT.extend(Ct)
            for candidate in Ct:
                if candidate not in counts:
                    counts[candidate] = 0
                counts[candidate] += 1
        print ('len mis ')
        print (len(mis))
        print(mis)
        for itemset in CT:
            misi = min([mis[i] for i in itemset])
            if float(counts[itemset])/data_size >= misi:
                L[k].append(itemset)
        # L[k] = [
        #     itemset for itemset in CT if float(counts[itemset]) / data_size >= min([mis[i] for i in itemset])]
        patterns.update(
            {itemset:counts[itemset] for itemset in L[k]})
        k += 1
        # print (C)

    # print (C1)
    # print (S)
    # print (mis)
    # print (L)
    # print (patterns)
    return patterns

if __name__ == '__main__':
    find_patterns(transactions)