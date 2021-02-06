import random
import globals

def calculate_diversification(itemsets):
    ''' Calculates diversification of itemsets using Parul's approach'''
    assert type(itemsets) == list

    unique_items = set()

    for itemset in itemsets:
        for item in itemset:
            unique_items.add(item)

    return len(unique_items) / len(itemsets)


def evaluate_new(slots, test_transactions):
    TOTAL_REVENUE = 0
    NUM_TEST_TRANSACTION = 0 
    NUM_TEST_PATTERN_FOUND = 0
    TEST_DRANK_MEAN = 0

    NUM_2 = 0
    NUM_3 = 0
    NUM_4 = 0

    for transaction in test_transactions:
        itemset = tuple(transaction)
        # print (itemset)
        NUM_TEST_TRANSACTION += 1

        if (len(itemset)) == 2:
            NUM_2 += 1
        if (len(itemset)) == 3:
            NUM_3 += 1
        if (len(itemset)) == 4:
            NUM_4 += 1
        
        all_slots = []
        for stype in range (0, len(slots)):
            for (item, price, drank) in slots[stype]:
                
                if tuple(item) == itemset:
                    prob_value = random.randint(0, 1000)
                    if stype == 2 and prob_value < 600:
                        TOTAL_REVENUE += price
                        NUM_TEST_PATTERN_FOUND += 1
                        TEST_DRANK_MEAN += drank

                    elif stype == 1 and prob_value < 800:
                        TOTAL_REVENUE += price
                        NUM_TEST_PATTERN_FOUND += 1
                        if NUM_TEST_PATTERN_FOUND-1 in CUMULATIVE_PATTERN_REVENUE.keys():
                            CUMULATIVE_PATTERN_REVENUE[NUM_TEST_PATTERN_FOUND] = (
                                CUMULATIVE_PATTERN_REVENUE[NUM_TEST_PATTERN_FOUND-1][0] + price,
                                itemset
                            )
                        else:
                            CUMULATIVE_PATTERN_REVENUE[NUM_TEST_PATTERN_FOUND] = (
                                price,
                                itemset)
                        TEST_DRANK_MEAN += drank

                    elif stype ==0 :
                        TOTAL_REVENUE += price
                        NUM_TEST_PATTERN_FOUND += 1
                        TEST_DRANK_MEAN += drank
                    
                    break

    print ('NUM 2')
    print (NUM_2)
    print ('NUM 3')
    print (NUM_3)
    print ('NUM 4')
    print (NUM_4)

    print('\nTOTAL REVENUE OF TEST PATTERNS PLACED ->\n')
    print('\n\nNUMBER OF TEST  PLACED ->\n')
    print(str(NUM_TEST_PATTERN_FOUND))
    print('\n\nTOTAL NUMBER OF TEST PATTERNS ->\n')
    print(str(NUM_TEST_TRANSACTION))
    print('\n\nMEAN DRANK OF TESTING ->\n')
    drank_mean = 0
    if NUM_TEST_PATTERN_FOUND != 0:
        drank_mean = TEST_DRANK_MEAN / float(NUM_TEST_PATTERN_FOUND)
    #print(str(TEST_DRANK_MEAN/float(NUM_TEST_PATTERN_FOUND)))

    all_transactions = []

    for stype in range(len(slots)):
        for slot in slots[stype]:
            all_transactions.append(slot[0])
    diversification = calculate_diversification(all_transactions)

    return (TOTAL_REVENUE, drank_mean, NUM_TEST_PATTERN_FOUND, NUM_TEST_TRANSACTION, diversification)
