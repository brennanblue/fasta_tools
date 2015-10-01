#!/usr/bin/env python

# Command line script to calculate base frequency from a .fasta file

import sys

a_count = float(0)
c_count = float(0)
g_count = float(0)
t_count = float(0)

with open(sys.argv[1], 'r') as fasta:
    for line in fasta:
        if line.startswith(">"):
            # Header line, skip it
            continue
        for base in line.strip():
            if base == "A":
                a_count += 1
            elif base == "C":
                c_count += 1
            elif base == "G":
                g_count += 1
            else:
                t_count += 1
total_count = a_count + c_count + g_count + t_count
a_perc = (a_count / total_count) * 100
c_perc = (c_count / total_count) * 100
g_perc = (g_count / total_count) * 100
t_perc = (t_count / total_count) * 100

print("Base counts for file %s:" % sys.argv[1])
print("Total Nucleotides: %d" % total_count)
print("A: %d percentage: %d%%" % (a_count, a_perc))
print("C: %d percentage: %d%%" % (c_count, c_perc))
print("G: %d Percentage: %d%%" % (g_count, g_perc))
print("T: %d Percentage: %d%%" % (t_count, t_perc))
