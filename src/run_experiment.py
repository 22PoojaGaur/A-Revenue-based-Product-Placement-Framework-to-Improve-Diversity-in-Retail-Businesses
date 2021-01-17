
import time
import os
import shutil
import subprocess
from collections import OrderedDict

# Number of slots to use
# NUM_SLOTS = {
#     '70': { 0: 20, 1: 25, 2: 25 },
#     '170': { 0: 50, 1: 60, 2: 60 },
#     '370': { 0: 80, 1: 90, 2: 200 },
#     '600': {0: 150, 1: 250, 2: 200},
#     '900': {0: 250, 1: 250, 2: 400},
#     '1500': {0: 400, 1: 500, 2: 600},
#     '2000': {0: 500, 1: 700, 2: 800},
#     '3000': {0: 800, 1: 1100, 2: 1100},
#     '5000': {0: 1500, 1: 1500, 2: 2000},
#     '8000': {0: 3000, 1: 2500, 2: 2500},
#     '10000': {0: 3000, 1: 3500, 2: 3500}
# }


# NUM_SLOTS = {
#     '1000': {0: 600, 1: 250, 2: 150},
#     '2000': {0: 700, 1: 600, 2: 700},
#     '4000': {0: 1000, 1: 1500, 2: 1500},
#     '8000': {0: 3000, 1: 3000, 2: 2000},
#     '12000': {0: 4500, 1: 4500, 2: 3000},
#     '16000': {0: 5500, 1: 5500, 2: 5000},
#     '20000': {0: 6500, 1: 6500, 2: 7000},
#     '22000': {0: 7000, 1: 7000, 2: 8000},
#     '25000': {0: 8000, 1: 8000, 2: 9000}
# }

NUM_SLOTS = {
    '1000': {0: 1000},
    '2000': {0: 2000},
    '4000': {0: 4000},
    '8000': {0: 8000},
    '12000': {0: 12000},
    '16000': {0: 16000},
    '20000': {0: 20000}
}

NUM_SLOTS = OrderedDict(NUM_SLOTS)

bash_cmd = 'python3 main.py -d ../data/grocery_transactions.txt -ch_path ../data/grocery1_ch.txt'

# create directory to save experiment details
create_experiment_dir = 'with_rdr/'
if not os.path.exists(create_experiment_dir):
    os.mkdir(create_experiment_dir)

shutil.copyfile('globals.py', 'globals_bk.py')

for key in NUM_SLOTS.keys():
    gfile = open('globals.py', 'a')
    num_slots_str = '\nNUM_SLOTS = ' + str(NUM_SLOTS[key])
    gfile.write(num_slots_str)
    gfile.close()

    process = subprocess.Popen(bash_cmd.split())

    stdout, stderr = process.communicate()

if not os.path.exists(create_experiment_dir + 'globals.py'):
    shutil.move('globals.py', create_experiment_dir)

if not os.path.exists(create_experiment_dir + 'results/'):
    os.mkdir(create_experiment_dir + 'results/')

files = os.listdir('results/')

for f in files:
    shutil.move('results/'+f, create_experiment_dir + 'results/')

shutil.move('globals_bk.py', 'globals.py')
