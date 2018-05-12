# -*- coding: utf-8 -*-
import csv
import os
import argparse

inp_path = './inputs/'
outp_path = './outputs/'

parser = argparse.ArgumentParser()
parser.add_argument('-i', action='store', dest='inp_file', help='takes on a filename')
parser.add_argument('-o', action='store', dest='outp_file', help='takes on an output')
parser.add_argument('-c', action='store', dest='cnt', type=int, help='takes on a count')
args = parser.parse_args()

if not args.inp_file:
    print 'Not enough arguments given. Try "python myalbums.py -h to get syntax"'
    quit()

if os.path.isfile(os.path.join(inp_path, args.inp_file)):
    print 'Input file exists! Beginning to divide files!'
else:
    print "Input file does not exist, or you've misspelled it!"
    quit()


def file_div(y,x,r):
    z = 0
    with open(os.path.join(outp_path, '%s_%s.csv' % (args.outp_file, r)), 'w') as w_file:
        ascsv_outp = csv.writer(w_file)

        for row in x:
            if x.line_num and z < y - 1:
                ascsv_outp.writerow(row)
                z += 1
            elif not x.line_num:
                return False
            else:
                ascsv_outp.writerow(row)
                return True




with open(os.path.join(inp_path, args.inp_file), 'r') as r_file:
    ascsv_inp = csv.reader(r_file)
    x = 1
    go_on = True
    while go_on is True:
        go_on = file_div(args.cnt, ascsv_inp, x)
        x += 1
