import argparse
import mock_data
from data_parser import parse_data
from kui_index import get_kui_index
from ARC import get_arc
from slots import get_slots
from PRIP import PRIP

import _pickle as pkl
import time
from os import path

DEBUG_MODE = False

# Adding argument parser.
parser = argparse.ArgumentParser()
parser.add_argument('--data', '-d', help='add path to data file')

args = parser.parse_args()

# Global variables.
DATA_FNAME = args.data

if __name__ == '__main__':
    if DEBUG_MODE:
        data_dict = mock_data.DATA_DICT
    elif path.isfile('../data/retail_data_dict.pkl'):
        data_dict = pkl.load(open('../data/retail_data_dict.pkl', 'rb'))
    else:
        data_dict = parse_data(DATA_FNAME)
    print ('Data dictionary formed...')

    print ('storing data dict for retail.txt in pickled dictionary')
    pkl.dump(data_dict, open('../data/retail_data_dict.pkl', 'wb'))

    if DEBUG_MODE:
        kUI_idx = mock_data.KUI_IDX
        arc = mock_data.ARC
    else:
        kUI_idx = get_kui_index(data_dict)
    print('Done kUI Index and ARC...')

    num_slots = sum([len(k) for k in data_dict.keys()])
    type_slots = 24
    zipf = 0.7

    start = time.time()
    slots = get_slots(num_slots, type_slots, zipf)
    arc = get_arc(data_dict)
    slots = PRIP(data_dict, kUI_idx, arc, slots)
    end = time.time()

    print ('TIME -> ')
    print (end - start)

    output = open('prip_slots_24.pkl', 'wb')
    pkl.dump(slots, output)
    output.close()

    #print('KUI INDEX->')
    #print(kUI_idx)
    #print('ARC->')
    #print(arc)
    # print('slots->')
    # print(slots)
