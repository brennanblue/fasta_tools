#!/usr/bin/env python

# Command line script to calculate base frequency from a .fasta file

import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("base")
args = parser.parse_args()


a_count = float(0)
c_count = float(0)
g_count = float(0)
t_count = float(0)
n = float(0)

with open(args.base,'r') as fasta:
    for line in fasta:
        if line.startswith(">"):
            # Header line, skip it
            continue
        for base in line.strip():
            if base == "A":
                a_count += 1
		n += 1
            elif base == "C":
                c_count += 1
		n += 1
            elif base == "G":
                g_count += 1
		n += 1
	    elif base == "T":
                t_count += 1
		n += 1
	    else:
	    	n += 1

total_count = a_count + c_count + g_count + t_count
valid_rate = (total_count / n) * 100
# validity_msg ='%d' % (valid_rate)

# print ("percent of nucleotides valid: %s: " % validity_msg) 

a_perc = (a_count / total_count) * 100
c_perc = (c_count / total_count) * 100
g_perc = (g_count / total_count) * 100
t_perc = (t_count / total_count) * 100


print("Base counts for file %s:" % args.base)
print("Total Nucleotides Found: %d" % total_count)
print("Percent Nucleotides Valid: %d%%  ( %d / %d )" % (valid_rate, total_count, n)) 
print("A: %d Percentage: %d%%" % (a_count, a_perc))
print("C: %d Percentage: %d%%" % (c_count, c_perc))
print("G: %d Percentage: %d%%" % (g_count, g_perc))
print("T: %d Percentage: %d%%" % (t_count, t_perc))
