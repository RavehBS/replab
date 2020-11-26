import h5py

import numpy as np
import matplotlib.pyplot as plt

import sys, os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--path', type=str, default='')
parser.add_argument('--skip_opens', type=int, default=0)
parser.add_argument('--start', type=int, default=0)

args = parser.parse_args()

src = args.path + '/'

file_ids = [int(file[:-5]) for file in os.listdir(src) if file[-5:] == '.hdf5']
file_ids.sort()
file_ids = [str(i) + '.hdf5' for i in file_ids if i >= args.start]

success_n = 0
failure_n = 0

for file in file_ids:
    with h5py.File(src + file, 'r+') as fl:
        if fl['success'][...] == False :
            failure_n = failure_n + 1
        else :
            success_n = success_n + 1
print('number of success: %s'%success_n)
print('number of failure: %s'%failure_n)
exit()
