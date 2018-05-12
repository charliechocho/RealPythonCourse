import argparse
import csv
import os

my_path = './inputs/'


parser = argparse.ArgumentParser()
parser.add_argument('-i', action='store', dest='inp_file', help='takes on a filename')
parser.add_argument('-o', action='store', dest='outp_file', help='takes on an output')
parser.add_argument('-c', action='store', dest='cnt', type=int, help='takes on a count')
args = parser.parse_args()

if os.path.isfile(os.path.join(my_path, args.inp_file)):
    print args.inp_file, '\n', args.outp_file, '\n', args.cnt
else:
    print 'File does not exist!'
