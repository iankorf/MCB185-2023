# 61kmers.py

# Make a program that reports the kmer counts for a fasta file
# Your program should take 2 arguments:
#    1. The file name
#    2. The size of k

# Hint: use argparse
# Hint: use mcb185.read_fasta()

import argparse
import mcb185

parser = argparse.ArgumentParser(
	description='Count k-mers in a fasta file')
parser.add_argument('fasta', metavar='<fasta file>', type=str,
	help='path to file')
parser.add_argument('size', metavar='<kmer size>', type=int,
	help='small integers')
arg = parser.parse_args()

count = {}
for name, seq in mcb185.read_fasta(arg.fasta):
	for i in range(len(seq) - arg.size +1):
		kmer = seq[i:i+arg.size]
		if kmer not in count: count[kmer] = 0
		count[kmer] += 1

for kmer in sorted(count):
	print(kmer, count[kmer])


"""
python3 60kmers.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz 2
AA 338006
AC 256773
AG 238013
AT 309950
CA 325327
CC 271821
CG 346793
CT 236149
GA 267384
GC 384102
GG 270252
GT 255699
TA 212024
TC 267395
TG 322379
TT 339584
"""
