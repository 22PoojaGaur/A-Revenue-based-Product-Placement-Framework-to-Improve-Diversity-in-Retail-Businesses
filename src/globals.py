TRAIN_SPLIT = 0.8
TEST_SPLIT = 1 - TRAIN_SPLIT
SUPPORT_THRESHOLD = 0.002


PRICE_BRACKETS = [
    (0.01, 0.16), (0.17, 0.33), (0.34, 0.50), (0.51, 0.67),
    (0.68, 0.84), (0.85, 1)]
METHOD = 'R'
# This will change the placement scheme to
# place slot with higher per_slot_drank
# in case of D and remain same in case of others


# below are specifically for RH (similar to HC-HCHD) method.
R_RATIO = 0.4
H_RATIO = 0.6

K_FOR_KUI_IDX = 4
KUI_DRIP_DRANK_THRESHOLD = 0 # note that change is made on '>' threshold
KUI_DRIP_REVENUE_THRESHOLD = 0 # comparison made on '>'
LAMBDA = 10000
NUM_TYPE_SLOTS = 1
# NUM_SLOTS is a dictionary to give num slots in each slot type
# so number of keys in NUM_SLOTS is equal to NUM_TYPE_SLOTS

# Rho - this is to try new revenue metric of - nr + (rho*d*nr)
RHO = 0

# slots for each size
NUM_SLOTS = {
    0: 600, 1: 250, 2: 150}