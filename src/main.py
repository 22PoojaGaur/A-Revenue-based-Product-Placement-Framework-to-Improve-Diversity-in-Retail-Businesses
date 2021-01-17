import argparse
import mock_data
import itertools
from data_parser import parse_data
from data_parser import parse_ch_dict
from calculate_drank import get_dranks
from kui_index import get_kui_index
from ARC import get_arc
from slots import get_slots
from PRIP import PRIP
from DPRIP import DPRIP
from evaluate import evaluate_new
import globals

import _pickle as pkl
import time
import os
from os import path
from random import random

# Adding argument parser.
parser = argparse.ArgumentParser()
parser.add_argument('--data', '-d', help='add path to data file')
parser.add_argument(
    '--with_ch_path', '-ch_path', help='run the experiment with diversity', default=None)

args = parser.parse_args()

# Global variables.
DATA_FNAME = args.data
CH_FNAME = args.with_ch_path

def get_data():
    assert CH_FNAME is not None
    assert DATA_FNAME is not None
    if path.isfile('dataset.pkl') and path.isfile('test.pkl'):
        train = pkl.load(open('dataset.pkl', 'rb'))
        test = pkl.load(open('test.pkl', 'rb'))
#       shorten the train dataset
#       train_2 = {}
#       for (k, v) in train.items():
#           if len(k) > 1:
#               train_2[k] = v   
#       import itertools
#       train = dict(itertools.islice(train_2.items(), 500))
    else:
        (train, test) = parse_data(DATA_FNAME)
        pkl.dump(train_data_dict, open('dataset.pkl', 'wb'))
        pkl.dump(test_transactions, open('test.pkl', 'wb'))
    ch_dict = parse_ch_dict(CH_FNAME)
    dranks = get_dranks(train.keys(), ch_dict)
    return (train, test, ch_dict, dranks)


if __name__ == '__main__':

    # Get globals in variables
    num_slots = globals.NUM_SLOTS
    type_slots = globals.NUM_TYPE_SLOTS
    zipf = globals.ZIPF
    method = globals.METHOD

    # processing data
    data_dict = {}
    ch_dict = {}
    dranks = {}
    
    (train_data, test_transaction, ch_dict, dranks) = get_data()
    if method == 'RH':
        kui_R = get_kui_index(train_data, dranks=dranks, method='R')
        kui_H = get_kui_index(train_data, dranks=dranks, method='H')
        kui_idx = {
            'R': kui_R,
            'H': kui_H
        }
    elif method == 'RDR':
        kui_R = get_kui_index(train_data, dranks=dranks, method='R')
        kui_DR = get_kui_index(train_data, dranks=dranks, method='DR')
        kui_idx = {
            'R': kui_R,
            'DR': kui_DR
        }
    else:
        kui_idx = get_kui_index(train_data, dranks=dranks, method=method)
     
    # for (k, v) in kui_idx.items():
    #     print ("Length level %d", k)
    #     l = 0
    #     for node in v:
    #         l += len(node[0])
    #     print (l)
   
    start = time.time()
    # get empty slots
    slots = get_slots(num_slots, type_slots, zipf)
    (slots, num_slots, tr_train, dr_train) = DPRIP(
        train_data, kui_idx, dranks, slots, method)
    end = time.time()

    time = end - start

    for level in range(0, len(slots)):
        #print ("slot level %d", level)
        l = 0
        for node in slots[level]:
            l += len(node[0])
        #print (l)

    (tr_test, dr_test, place_test, num_total_test, diversification) = evaluate_new(slots, test_transaction)

    output = open('prip_slots_%d.pkl' % type_slots, 'wb')
    pkl.dump(slots, output)
    output.close()

    # Automating the write of graph essential files

    # for stype in range(0, len(slots)):
    #     print ("TOP 10 slots of stype - ", stype)
    #     print (slots[stype][0:10])
    # list of each metric would be stored in pkl files
    pkl_prefix = 'results/' + method + '_'
    metrics = {
        'num_slots': num_slots,
        'total_revenue_train': tr_train,
        'drank_mean_train': dr_train,
        'num_placed_test': place_test,
        'num_total_test': num_total_test,
        'total_revenue_test': tr_test,
        'drank_mean_test': dr_test,
        'train_time': time,
        'diversification': diversification
    }

    for metric in metrics.keys():
        fname = pkl_prefix + metric + '.pkl'

        if path.isfile(fname):
            data = pkl.load(open(fname, 'rb'))
            os.remove(fname)
        else:
            data = []

        data.append(metrics[metric])

        pkl.dump(data, open(fname, 'wb'))
